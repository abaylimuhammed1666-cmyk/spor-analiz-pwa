from flask import Flask, render_template, request

app = Flask(__name__)

tum_maclar = [
    # Trendyol Süper Lig
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-02", "saat": "20:00", "mac": "Galatasaray - Fenerbahçe", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-02", "saat": "19:00", "mac": "Beşiktaş - Trabzonspor", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-03", "saat": "16:00", "mac": "Başakşehir - Samsunspor", "skor_tahmini": "2 - 0", "iy_1_5_ust": "%45", "kg_var": "%40", "alt_ust_6_gol": "%15"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-03", "saat": "19:00", "mac": "Göztepe - Antalyaspor", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%55", "kg_var": "%70", "alt_ust_6_gol": "%30"},

    # Premier Lig
    {"lig": "Premier Lig", "tarih": "2026-10-04", "saat": "16:00", "mac": "Arsenal - Chelsea", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},
    {"lig": "Premier Lig", "tarih": "2026-10-04", "saat": "18:30", "mac": "Manchester City - Liverpool", "skor_tahmini": "3 - 2", "iy_1_5_ust": "%80", "kg_var": "%85", "alt_ust_6_gol": "%45"},
    {"lig": "Premier Lig", "tarih": "2026-10-05", "saat": "16:00", "mac": "Manchester United - Tottenham", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%55", "kg_var": "%60", "alt_ust_6_gol": "%20"},
    {"lig": "Premier Lig", "tarih": "2026-10-05", "saat": "18:30", "mac": "Newcastle United - Aston Villa", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%65", "kg_var": "%65", "alt_ust_6_gol": "%30"},

    # La Liga
    {"lig": "La Liga", "tarih": "2026-10-12", "saat": "21:00", "mac": "Real Madrid - Barcelona", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "La Liga", "tarih": "2026-10-13", "saat": "19:30", "mac": "Atletico Madrid - Real Sociedad", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%60", "alt_ust_6_gol": "%15"},
    {"lig": "La Liga", "tarih": "2026-10-13", "saat": "22:00", "mac": "Villarreal - Valencia", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%55", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "La Liga", "tarih": "2026-10-19", "saat": "19:00", "mac": "Barcelona - Athletic Bilbao", "skor_tahmini": "3 - 1", "iy_1_5_ust": "%70", "kg_var": "%50", "alt_ust_6_gol": "%30"},

    # Serie A
    {"lig": "Serie A", "tarih": "2026-10-14", "saat": "19:00", "mac": "Inter - Juventus", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%45", "kg_var": "%55", "alt_ust_6_gol": "%10"},
    {"lig": "Serie A", "tarih": "2026-10-14", "saat": "21:45", "mac": "AC Milan - Napoli", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%60", "alt_ust_6_gol": "%20"},
    {"lig": "Serie A", "tarih": "2026-10-15", "saat": "19:30", "mac": "Roma - Lazio", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%55", "kg_var": "%70", "alt_ust_6_gol": "%25"},
    {"lig": "Serie A", "tarih": "2026-10-20", "saat": "20:00", "mac": "Atalanta - Fiorentina", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%65", "kg_var": "%75", "alt_ust_6_gol": "%35"},

    # Bundesliga
    {"lig": "Bundesliga", "tarih": "2026-10-15", "saat": "16:30", "mac": "Bayern Munich - Borussia Dortmund", "skor_tahmini": "3 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "Bundesliga", "tarih": "2026-10-15", "saat": "19:30", "mac": "RB Leipzig - Bayer Leverkusen", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%70", "alt_ust_6_gol": "%30"},
    {"lig": "Bundesliga", "tarih": "2026-10-21", "saat": "17:30", "mac": "Stuttgart - Eintracht Frankfurt", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%15"}
]

@app.route('/')
def home():
    secilen_lig = request.args.get("lig", "Tümü")
    ligler = ["Tümü"] + sorted(list(set(m["lig"] for m in tum_maclar)))

    if secilen_lig == "Tümü":
        filtrelenmis_maclar = tum_maclar
    else:
        filtrelenmis_maclar = [m for m in tum_maclar if m["lig"] == secilen_lig]

    lig_gruplari = {}
    for m in filtrelenmis_maclar:
         l = m["lig"]
         if l not in lig_gruplari:
             lig_gruplari[l] = []
         lig_gruplari[l].append(m)

    return render_template("index.html", ligler=ligler, secilen_lig=secilen_lig, lig_gruplari=lig_gruplari)

if __name__ == '__main__':
    app.run(debug=True)