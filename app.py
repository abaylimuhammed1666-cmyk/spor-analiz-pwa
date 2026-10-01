from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # Bülteni direkt zengin ve dolu bir liste olarak verelim ki her ligden maçlar görünsün
    tum_maclar = [
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-09", "saat": "20:00", "mac": "Galatasaray - Kasımpaşa", "skor_tahmini": "2 - 1", "iy_15_ust": "%53", "kg_var": "%44", "gol_6_ust": "%17"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-10", "saat": "16:00", "mac": "Samsunspor - Trabzonspor", "skor_tahmini": "1 - 2", "iy_15_ust": "%50", "kg_var": "%47", "gol_6_ust": "%20"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-10", "saat": "19:00", "mac": "Çaykur Rizespor - Fenerbahçe", "skor_tahmini": "0 - 2", "iy_15_ust": "%66", "kg_var": "%43", "gol_6_ust": "%17"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-11", "saat": "13:30", "mac": "Konyaspor - Başakşehir", "skor_tahmini": "1 - 1", "iy_15_ust": "%84", "kg_var": "%84", "gol_6_ust": "%44"},
        {"lig": "Premier Lig", "tarih": "2026-10-11", "saat": "16:00", "mac": "Arsenal - Chelsea", "skor_tahmini": "2 - 2", "iy_15_ust": "%75", "kg_var": "%70", "gol_6_ust": "%35"},
        {"lig": "Premier Lig", "tarih": "2026-10-11", "saat": "18:30", "mac": "Manchester City - Liverpool", "skor_tahmini": "3 - 2", "iy_15_ust": "%88", "kg_var": "%82", "gol_6_ust": "%50"},
        {"lig": "La Liga", "tarih": "2026-10-12", "saat": "21:00", "mac": "Real Madrid - Barcelona", "skor_tahmini": "2 - 1", "iy_15_ust": "%80", "kg_var": "%78", "gol_6_ust": "%40"}
    ]

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

if __name__ == "__main__":
    app.run(debug=True)
