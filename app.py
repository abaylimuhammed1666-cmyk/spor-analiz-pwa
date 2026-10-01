from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # Hiçbir şeyi bozmadan, sistemi yormayan zengin ve genişletilmiş maç bülteni
    tum_maclar = [
        # Trendyol Süper Lig
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-09", "saat": "20:00", "mac": "Galatasaray - Kasımpaşa", "skor_tahmini": "2 - 1", "iy_15_ust": "%53", "kg_var": "%44", "gol_6_ust": "%17"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-10", "saat": "16:00", "mac": "Samsunspor - Trabzonspor", "skor_tahmini": "1 - 2", "iy_15_ust": "%50", "kg_var": "%47", "gol_6_ust": "%20"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-10", "saat": "19:00", "mac": "Çaykur Rizespor - Fenerbahçe", "skor_tahmini": "0 - 2", "iy_15_ust": "%66", "kg_var": "%43", "gol_6_ust": "%17"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-11", "saat": "13:30", "mac": "Konyaspor - Başakşehir", "skor_tahmini": "1 - 1", "iy_15_ust": "%84", "kg_var": "%84", "gol_6_ust": "%44"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-11", "saat": "19:00", "mac": "Beşiktaş - Kocaelispor", "skor_tahmini": "1 - 1", "iy_15_ust": "%67", "kg_var": "%63", "gol_6_ust": "%30"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-12", "saat": "20:00", "mac": "Eyüpspor - Göztepe", "skor_tahmini": "1 - 2", "iy_15_ust": "%58", "kg_var": "%71", "gol_6_ust": "%36"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-17", "saat": "16:00", "mac": "Gençlerbirliği - Galatasaray", "skor_tahmini": "1 - 2", "iy_15_ust": "%60", "kg_var": "%77", "gol_6_ust": "%40"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-17", "saat": "19:00", "mac": "Fenerbahçe - Alanyaspor", "skor_tahmini": "3 - 1", "iy_15_ust": "%72", "kg_var": "%55", "gol_6_ust": "%25"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-18", "saat": "19:00", "mac": "Trabzonspor - Antalyaspor", "skor_tahmini": "2 - 0", "iy_15_ust": "%65", "kg_var": "%40", "gol_6_ust": "%15"},
        {"lig": "Trendyol Süper Lig", "tarih": "2026-10-19", "saat": "20:00", "mac": "Adana Demirspor - Beşiktaş", "skor_tahmini": "1 - 3", "iy_15_ust": "%78", "kg_var": "%68", "gol_6_ust": "%35"},

        # Premier Lig
        {"lig": "Premier Lig", "tarih": "2026-10-11", "saat": "16:00", "mac": "Arsenal - Chelsea", "skor_tahmini": "2 - 2", "iy_15_ust": "%75", "kg_var": "%70", "gol_6_ust": "%35"},
        {"lig": "Premier Lig", "tarih": "2026-10-11", "saat": "18:30", "mac": "Manchester City - Liverpool", "skor_tahmini": "3 - 2", "iy_15_ust": "%88", "kg_var": "%82", "gol_6_ust": "%50"},
        {"lig": "Premier Lig", "tarih": "2026-10-12", "saat": "16:00", "mac": "Manchester United - Tottenham", "skor_tahmini": "2 - 1", "iy_15_ust": "%68", "kg_var": "%65", "gol_6_ust": "%28"},
        {"lig": "Premier Lig", "tarih": "2026-10-12", "saat": "18:30", "mac": "Newcastle United - Aston Villa", "skor_tahmini": "1 - 1", "iy_15_ust": "%62", "kg_var": "%60", "gol_6_ust": "%20"},
        {"lig": "Premier Lig", "tarih": "2026-10-18", "saat": "16:00", "mac": "Liverpool - Everton", "skor_tahmini": "2 - 0", "iy_15_ust": "%70", "kg_var": "%45", "gol_6_ust": "%22"},
        {"lig": "Premier Lig", "tarih": "2026-10-18", "saat": "18:30", "mac": "Chelsea - Manchester United", "skor_tahmini": "2 - 2", "iy_15_ust": "%76", "kg_var": "%74", "gol_6_ust": "%38"},

        # La Liga
        {"lig": "La Liga", "tarih": "2026-10-12", "saat": "21:00", "mac": "Real Madrid - Barcelona", "skor_tahmini": "2 - 1", "iy_15_ust": "%80", "kg_var": "%78", "gol_6_ust": "%40"},
        {"lig": "La Liga", "tarih": "2026-10-13", "saat": "19:30", "mac": "Atletico Madrid - Real Sociedad", "skor_tahmini": "1 - 0", "iy_15_ust": "%52", "kg_var": "%42", "gol_6_ust": "%12"},
        {"lig": "La Liga", "tarih": "2026-10-13", "saat": "22:00", "mac": "Villarreal - Valencia", "skor_tahmini": "2 - 2", "iy_15_ust": "%74", "kg_var": "%72", "gol_6_ust": "%30"},
        {"lig": "La Liga", "tarih": "2026-10-19", "saat": "19:00", "mac": "Barcelona - Athletic Bilbao", "skor_tahmini": "3 - 1", "iy_15_ust": "%82", "kg_var": "%60", "gol_6_ust": "%32"},

        # Serie A
        {"lig": "Serie A", "tarih": "2026-10-14", "saat": "19:00", "mac": "Inter - Juventus", "skor_tahmini": "1 - 1", "iy_15_ust": "%58", "kg_var": "%62", "gol_6_ust": "%18"},
        {"lig": "Serie A", "tarih": "2026-10-14", "saat": "21:45", "mac": "AC Milan - Napoli", "skor_tahmini": "2 - 1", "iy_15_ust": "%70", "kg_var": "%68", "gol_6_ust": "%25"},
        {"lig": "Serie A", "tarih": "2026-10-15", "saat": "21:45", "mac": "Roma - Lazio", "skor_tahmini": "1 - 2", "iy_15_ust": "%65", "kg_var": "%70", "gol_6_ust": "%22"},
        {"lig": "Serie A", "tarih": "2026-10-20", "saat": "20:00", "mac": "Atalanta - Fiorentina", "skor_tahmini": "2 - 2", "iy_15_ust": "%79", "kg_var": "%80", "gol_6_ust": "%35"},

        # Bundesliga
        {"lig": "Bundesliga", "tarih": "2026-10-15", "saat": "16:30", "mac": "Bayern Munich - Borussia Dortmund", "skor_tahmini": "3 - 2", "iy_15_ust": "%90", "kg_var": "%85", "gol_6_ust": "%55"},
        {"lig": "Bundesliga", "tarih": "2026-10-15", "saat": "19:30", "mac": "RB Leipzig - Bayer Leverkusen", "skor_tahmini": "2 - 2", "iy_15_ust": "%82", "kg_var": "%81", "gol_6_ust": "%45"},
        {"lig": "Bundesliga", "tarih": "2026-10-21", "saat": "17:30", "mac": "Stuttgart - Eintracht Frankfurt", "skor_tahmini": "2 - 1", "iy_15_ust": "%75", "kg_var": "%70", "gol_6_ust": "%30"}
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