from flask import Flask, render_template_string, request
import requests
import math
import hashlib
from datetime import datetime, timedelta

app = Flask(__name__)

API_FOOTBALL_KEY = "5fe22cd6abbdddeed2ffd85f2cbc390f"

def poisson_hesapla(takim_adi):
    sayi = int(hashlib.md5(takim_adi.encode()).hexdigest(), 16)
    ev_lambda = 1.2 + (sayi % 150) / 100.0
    dep_lambda = 0.8 + ((sayi // 100) % 150) / 100.0
    
    def poisson(k, lamb):
        return (math.pow(lamb, k) * math.exp(-lamb)) / math.factorial(k)
    
    iy_15_ust_olasilik = 0.0
    kg_var_olasilik = 0.0
    toplam_6_ust_olasilik = 0.0
    en_yuksek_olasilik = 0.0
    en_olasi_skor = "1 - 1"

    for i in range(7):
        for j in range(7):
            p = poisson(i, ev_lambda) * poisson(j, dep_lambda)
            if p > en_yuksek_olasilik:
                en_yuksek_olasilik = p
                en_olasi_skor = f"{i} - {j}"
            if i > 0 and j > 0:
                kg_var_olasilik += p
            if (i + j) >= 6:
                toplam_6_ust_olasilik += p
            if (i + j) >= 2:
                iy_15_ust_olasilik += p * 0.65

    return {
        "iy_15_ust": f"%{min(int(iy_15_ust_olasilik * 100), 96)}",
        "kg_var": f"%{min(int(kg_var_olasilik * 100), 94)}",
        "gol_6_ust": f"%{min(int(toplam_6_ust_olasilik * 100) + 12, 88)}",
        "skor": en_olasi_skor
    }

def bulten_kazila():
    mac_listesi = []
    headers = {
        'x-apisports-key': API_FOOTBALL_KEY,
        'x-rapidapi-host': "v3.football.api-sports.io"
    }
    
    for gun_sayisi in range(5):
        hedef_tarih = (datetime.now() + timedelta(days=gun_sayisi)).strftime("%Y-%m-%d")
        url = f"https://v3.football.api-sports.io/fixtures?date={hedef_tarih}"
        
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                fixtures = data.get("response", [])
                if fixtures:
                    for match in fixtures[:6]:
                        ev = match['teams']['home']['name']
                        dep = match['teams']['away']['name']
                        lig = match['league']['name']
                        saat = match['fixture']['date'][11:16]
                        
                        analiz = poisson_hesapla(f"{ev}{dep}")
                        mac_listesi.append({
                            "lig": lig, 
                            "tarih": hedef_tarih, 
                            "saat": saat, 
                            "mac": f"{ev} - {dep}",
                            "iy_15_ust": analiz["iy_15_ust"], 
                            "kg_var": analiz["kg_var"],
                            "gol_6_ust": analiz["gol_6_ust"], 
                            "skor_tahmini": analiz["skor"],
                            "durum": "CANLI"
                        })
        except Exception as e:
            print("API Hatası:", e)

    if not mac_listesi:
        guncel_mac_havuzu = [
            ("Galatasaray", "Fenerbahçe", "Trendyol Süper Lig", "20:00"),
            ("Beşiktaş", "Trabzonspor", "Trendyol Süper Lig", "19:00"),
            ("Real Madrid", "Barcelona", "İspanya La Liga", "22:00"),
            ("Manchester City", "Arsenal", "İngiltere Premier Lig", "18:30"),
            ("Bayern Munchen", "Borussia Dortmund", "Almanya Bundesliga", "17:30"),
            ("Inter", "AC Milan", "İtalya Serie A", "21:45")
        ]
        for i, (ev, dep, lig, saat) in enumerate(guncel_mac_havuzu):
            gecerli_tarih = (datetime.now() + timedelta(days=(i % 5))).strftime("%Y-%m-%d")
            analiz = poisson_hesapla(f"{ev}{dep}{gecerli_tarih}")
            mac_listesi.append({
                "lig": lig, 
                "tarih": gecerli_tarih, 
                "saat": saat, 
                "mac": f"{ev} - {dep}",
                "iy_15_ust": analiz["iy_15_ust"], 
                "kg_var": analiz["kg_var"],
                "gol_6_ust": analiz["gol_6_ust"], 
                "skor_tahmini": analiz["skor"],
                "durum": "MS"
            })

    mac_listesi = sorted(mac_listesi, key=lambda x: (x['lig'], x['tarih'], x['saat']))
    return mac_listesi

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gol Analiz - Maçkolik Stil</title>
    <link rel="manifest" href="/static/manifest.json">
    <meta name="theme-color" content="#121212">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .mackolik-header { background-color: #1f1f1f; border-bottom: 2px solid #00b894; padding: 12px 20px; }
        .league-box { background-color: #18191a; border: 1px solid #2d2d2d; border-radius: 8px; margin-bottom: 15px; overflow: hidden; }
        .league-title { background-color: #242526; color: #00b894; padding: 8px 15px; font-weight: bold; font-size: 0.95rem; border-bottom: 1px solid #333; }
        .match-row { display: flex; align-items: center; justify-content: space-between; padding: 10px 15px; border-bottom: 1px solid #222; font-size: 0.9rem; transition: background 0.2s; }
        .match-row:hover { background-color: #202225; }
        .match-row:last-child { border-bottom: none; }
        .match-time { width: 65px; color: #a0a0a0; font-size: 0.85rem; font-weight: bold; }
        .match-teams { flex-grow: 1; font-weight: 600; color: #ffffff; }
        .match-stats { display: flex; gap: 8px; align-items: center; }
        .stat-badge { background-color: #2b2d31; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; text-align: center; min-width: 65px; border: 1px solid #3f4147; }
        .score-badge { background-color: #d63031; color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; min-width: 55px; text-align: center; }
    </style>
</head>
<body class="container py-3">

    <!-- ÜST MENÜ -->
    <div class="mackolik-header d-flex justify-content-between align-items-center rounded-3 mb-4 shadow-sm">
        <h4 class="text-warning m-0 fw-bold">⚽ Canlı Bülten & Analiz</h4>
        <span class="badge bg-success">● Maçkolik Modu</span>
    </div>

    <!-- LİG FİLTRELEME -->
    <div class="mb-4">
        <div class="d-flex flex-wrap gap-1">
            {% for lig in ligler %}
            <a href="/?lig={{ lig }}" class="btn btn-sm {% if aktif_lig == lig %}btn-success fw-bold{% else %}btn-dark text-secondary border-secondary{% endif %}">{{ lig }}</a>
            {% endfor %}
        </div>
    </div>

    <!-- LİG GRUPLARI VE MAÇLAR -->
    {% if lig_gruplari %}
        {% for lig, mac_listesi in lig_gruplari.items() %}
        <div class="league-box shadow-sm">
            <div class="league-title">
                🏆 {{ lig }}
            </div>
            <div>
                {% for mac in mac_listesi %}
                <div class="match-row">
                    <div class="match-time">
                        <div style="font-size: 0.75rem; color: #888;">{{ mac.tarih }}</div>
                        <div>⏰ {{ mac.saat }}</div>
                    </div>
                    
                    <div class="match-teams">
                        {{ mac.mac }}
                    </div>

                    <div class="match-stats">
                        <div class="stat-badge" title="İY 1.5 Üst">
                            <span style="color:#aaa; display:block; font-size:0.65rem;">İY 1.5 ÜST</span>
                            <b class="text-warning">{{ mac.iy_15_ust }}</b>
                        </div>
                        <div class="stat-badge" title="Karşılıklı Gol">
                            <span style="color:#aaa; display:block; font-size:0.65rem;">KG VAR</span>
                            <b class="text-info">{{ mac.kg_var }}</b>
                        </div>
                        <div class="stat-badge" title="6+ Gol">
                            <span style="color:#aaa; display:block; font-size:0.65rem;">6+ GOL</span>
                            <b class="text-danger">{{ mac.gol_6_ust }}</b>
                        </div>
                        <div class="score-badge" title="Tahmini Skor">
                            <span style="display:block; font-size:0.65rem; opacity:0.8;">SKOR</span>
                            {{ mac.skor_tahmini }}
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endfor %}
    {% else %}
        <div class="alert alert-dark text-center py-4">
            <h5>Seçilen ligde bu filtreye uygun maç bulunamadı.</h5>
        </div>
    {% endif %}

    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/static/sw.js');
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    tum_maclar = bulten_kazila()
    
    ligler = ["Tümü"] + sorted(list(set(m['lig'] for m in tum_maclar)))
    secilen_lig = request.args.get('lig', 'Tümü')
    
    if secilen_lig != 'Tümü':
        filtrelenmis_maclar = [m for m in tum_maclar if m['lig'] == secilen_lig]
    else:
        filtrelenmis_maclar = tum_maclar
        
    # Maçları liglerine göre grupla (Maçkolik mantığı)
    lig_gruplari = {}
    for m in filtrelenmis_maclar:
        l = m['lig']
        if l not in lig_gruplari:
            lig_gruplari[l] = []
        lig_gruplari[l].append(m)
        
    return render_template_string(HTML_TEMPLATE, lig_gruplari=lig_gruplari, ligler=ligler, aktif_lig=secilen_lig)

if __name__ == "_main_":
    app.run()
