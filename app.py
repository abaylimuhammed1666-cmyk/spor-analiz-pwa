from flask import Flask, render_template, request

app = Flask(__name__)

tum_maclar = [
    # Trendyol Süper Lig (20 Maç)
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-05", "saat": "19:00", "mac": "Galatasaray - Fenerbahçe", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-05", "saat": "21:00", "mac": "Beşiktaş - Trabzonspor", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-06", "saat": "17:00", "mac": "Başakşehir - Trabzonspor", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%55", "kg_var": "%60", "alt_ust_6_gol": "%30"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-06", "saat": "20:00", "mac": "Adana Demirspor - Samsunspor", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%40"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-07", "saat": "19:00", "mac": "Antalyaspor - Alanyaspor", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%40", "kg_var": "%45", "alt_ust_6_gol": "%15"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-07", "saat": "21:00", "mac": "Konyaspor - Kayserispor", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-08", "saat": "19:00", "mac": "Gaziantep FK - Hatayspor", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-08", "saat": "21:00", "mac": "Rizespor - Kasımpaşa", "skor_tahmini": "3 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%45"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-09", "saat": "19:00", "mac": "Sivasspor - Eyüpspor", "skor_tahmini": "0 - 1", "iy_1_5_ust": "%35", "kg_var": "%40", "alt_ust_6_gol": "%10"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-09", "saat": "21:00", "mac": "Bodrum FK - Göztepe", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%55", "kg_var": "%65", "alt_ust_6_gol": "%30"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-10", "saat": "19:00", "mac": "Galatasaray - Beşiktaş", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-10", "saat": "21:00", "mac": "Fenerbahçe - Trabzonspor", "skor_tahmini": "3 - 1", "iy_1_5_ust": "%65", "kg_var": "%60", "alt_ust_6_gol": "%30"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-11", "saat": "19:00", "mac": "Başakşehir - Galatasaray", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%60", "kg_var": "%70", "alt_ust_6_gol": "%25"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-11", "saat": "21:00", "mac": "Alanyaspor - Fenerbahçe", "skor_tahmini": "0 - 2", "iy_1_5_ust": "%50", "kg_var": "%45", "alt_ust_6_gol": "%20"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-12", "saat": "19:00", "mac": "Kayserispor - Beşiktaş", "skor_tahmini": "1 - 3", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-12", "saat": "21:00", "mac": "Samsunspor - Göztepe", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%55", "kg_var": "%60", "alt_ust_6_gol": "%25"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-13", "saat": "19:00", "mac": "Eyüpspor - Kasımpaşa", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%45", "kg_var": "%55", "alt_ust_6_gol": "%15"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-13", "saat": "21:00", "mac": "Antalyaspor - Konyaspor", "skor_tahmini": "2 - 0", "iy_1_5_ust": "%50", "kg_var": "%40", "alt_ust_6_gol": "%20"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-14", "saat": "19:00", "mac": "Hatayspor - Gaziantep FK", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%30"},
    {"lig": "Trendyol Süper Lig", "tarih": "2026-10-14", "saat": "21:00", "mac": "Rizespor - Sivasspor", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},

    # Premier Lig (20 Maç)
    {"lig": "Premier Lig", "tarih": "2026-10-05", "saat": "16:00", "mac": "Manchester City - Arsenal", "skor_tahmini": "3 - 2", "iy_1_5_ust": "%80", "kg_var": "%85", "alt_ust_6_gol": "%45"},
    {"lig": "Premier Lig", "tarih": "2026-10-05", "saat": "18:30", "mac": "Liverpool - Manchester United", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%70", "kg_var": "%65", "alt_ust_6_gol": "%30"},
    {"lig": "Premier Lig", "tarih": "2026-10-06", "saat": "16:00", "mac": "Chelsea - Tottenham", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%35"},
    {"lig": "Premier Lig", "tarih": "2026-10-06", "saat": "18:30", "mac": "Newcastle United - Aston Villa", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%55", "kg_var": "%60", "alt_ust_6_gol": "%20"},
    {"lig": "Premier Lig", "tarih": "2026-10-07", "saat": "17:00", "mac": "West Ham - Brighton", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Premier Lig", "tarih": "2026-10-07", "saat": "20:00", "mac": "Crystal Palace - Fulham", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%45", "kg_var": "%40", "alt_ust_6_gol": "%15"},
    {"lig": "Premier Lig", "tarih": "2026-10-08", "saat": "17:00", "mac": "Brentford - Everton", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%30"},
    {"lig": "Premier Lig", "tarih": "2026-10-08", "saat": "20:00", "mac": "Wolves - Bournemouth", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Premier Lig", "tarih": "2026-10-09", "saat": "17:00", "mac": "Nottingham Forest - Leicester City", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%60", "alt_ust_6_gol": "%25"},
    {"lig": "Premier Lig", "tarih": "2026-10-09", "saat": "20:00", "mac": "Southampton - Ipswich Town", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%55", "kg_var": "%70", "alt_ust_6_gol": "%25"},
    {"lig": "Premier Lig", "tarih": "2026-10-10", "saat": "16:00", "mac": "Arsenal - Liverpool", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "Premier Lig", "tarih": "2026-10-10", "saat": "18:30", "mac": "Manchester United - Chelsea", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Premier Lig", "tarih": "2026-10-11", "saat": "16:00", "mac": "Tottenham - Manchester City", "skor_tahmini": "1 - 3", "iy_1_5_ust": "%80", "kg_var": "%85", "alt_ust_6_gol": "%50"},
    {"lig": "Premier Lig", "tarih": "2026-10-11", "saat": "18:30", "mac": "Aston Villa - Newcastle United", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%65", "kg_var": "%65", "alt_ust_6_gol": "%30"},
    {"lig": "Premier Lig", "tarih": "2026-10-12", "saat": "17:00", "mac": "Brighton - West Ham", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},
    {"lig": "Premier Lig", "tarih": "2026-10-12", "saat": "20:00", "mac": "Fulham - Crystal Palace", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%40", "kg_var": "%45", "alt_ust_6_gol": "%15"},
    {"lig": "Premier Lig", "tarih": "2026-10-13", "saat": "17:00", "mac": "Everton - Brentford", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Premier Lig", "tarih": "2026-10-13", "saat": "20:00", "mac": "Bournemouth - Wolves", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Premier Lig", "tarih": "2026-10-14", "saat": "17:00", "mac": "Leicester City - Southampton", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%65", "kg_var": "%70", "alt_ust_6_gol": "%30"},
    {"lig": "Premier Lig", "tarih": "2026-10-14", "saat": "20:00", "mac": "Ipswich Town - Nottingham Forest", "skor_tahmini": "0 - 1", "iy_1_5_ust": "%45", "kg_var": "%40", "alt_ust_6_gol": "%15"},

    # La Liga (20 Maç)
    {"lig": "La Liga", "tarih": "2026-10-05", "saat": "19:00", "mac": "Real Madrid - Barcelona", "skor_tahmini": "3 - 2", "iy_1_5_ust": "%80", "kg_var": "%85", "alt_ust_6_gol": "%45"},
    {"lig": "La Liga", "tarih": "2026-10-05", "saat": "21:30", "mac": "Atletico Madrid - Real Sociedad", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%45", "kg_var": "%40", "alt_ust_6_gol": "%15"},
    {"lig": "La Liga", "tarih": "2026-10-06", "saat": "19:00", "mac": "Athletic Bilbao - Villarreal", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "La Liga", "tarih": "2026-10-06", "saat": "21:30", "mac": "Real Betis - Valencia", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "La Liga", "tarih": "2026-10-07", "saat": "19:00", "mac": "Sevilla - Celta Vigo", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%30"},
    {"lig": "La Liga", "tarih": "2026-10-07", "saat": "21:30", "mac": "Girona - Osasuna", "skor_tahmini": "2 - 0", "iy_1_5_ust": "%55", "kg_var": "%45", "alt_ust_6_gol": "%20"},
    {"lig": "La Liga", "tarih": "2026-10-08", "saat": "19:00", "mac": "Mallorca - Rayo Vallecano", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%45", "kg_var": "%50", "alt_ust_6_gol": "%15"},
    {"lig": "La Liga", "tarih": "2026-10-08", "saat": "21:30", "mac": "Getafe - Alaves", "skor_tahmini": "0 - 1", "iy_1_5_ust": "%35", "kg_var": "%40", "alt_ust_6_gol": "%10"},
    {"lig": "La Liga", "tarih": "2026-10-09", "saat": "19:00", "mac": "Las Palmas - Leganes", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "La Liga", "tarih": "2026-10-09", "saat": "21:30", "mac": "Valladolid - Espanyol", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%55", "kg_var": "%60", "alt_ust_6_gol": "%25"},
    {"lig": "La Liga", "tarih": "2026-10-10", "saat": "19:00", "mac": "Barcelona - Atletico Madrid", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%65", "kg_var": "%70", "alt_ust_6_gol": "%30"},
    {"lig": "La Liga", "tarih": "2026-10-10", "saat": "21:30", "mac": "Real Madrid - Real Betis", "skor_tahmini": "3 - 0", "iy_1_5_ust": "%70", "kg_var": "%40", "alt_ust_6_gol": "%35"},
    {"lig": "La Liga", "tarih": "2026-10-11", "saat": "19:00", "mac": "Real Sociedad - Athletic Bilbao", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "La Liga", "tarih": "2026-10-11", "saat": "21:30", "mac": "Villarreal - Sevilla", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "La Liga", "tarih": "2026-10-12", "saat": "19:00", "mac": "Valencia - Girona", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "La Liga", "tarih": "2026-10-12", "saat": "21:30", "mac": "Celta Vigo - Mallorca", "skor_tahmini": "2 - 0", "iy_1_5_ust": "%55", "kg_var": "%45", "alt_ust_6_gol": "%20"},
    {"lig": "La Liga", "tarih": "2026-10-13", "saat": "19:00", "mac": "Osasuna - Getafe", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%40", "kg_var": "%40", "alt_ust_6_gol": "%15"},
    {"lig": "La Liga", "tarih": "2026-10-13", "saat": "21:30", "mac": "Rayo Vallecano - Las Palmas", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},
    {"lig": "La Liga", "tarih": "2026-10-14", "saat": "19:00", "mac": "Alaves - Valladolid", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "La Liga", "tarih": "2026-10-14", "saat": "21:30", "mac": "Leganes - Espanyol", "skor_tahmini": "0 - 2", "iy_1_5_ust": "%55", "kg_var": "%50", "alt_ust_6_gol": "%25"},

    # Serie A (20 Maç)
    {"lig": "Serie A", "tarih": "2026-10-05", "saat": "18:00", "mac": "Inter - Juventus", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Serie A", "tarih": "2026-10-05", "saat": "21:45", "mac": "AC Milan - Napoli", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%65", "kg_var": "%70", "alt_ust_6_gol": "%30"},
    {"lig": "Serie A", "tarih": "2026-10-06", "saat": "18:00", "mac": "Roma - Lazio", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},
    {"lig": "Serie A", "tarih": "2026-10-06", "saat": "21:45", "mac": "Atalanta - Fiorentina", "skor_tahmini": "3 - 1", "iy_1_5_ust": "%75", "kg_var": "%65", "alt_ust_6_gol": "%40"},
    {"lig": "Serie A", "tarih": "2026-10-07", "saat": "18:30", "mac": "Bologna - Torino", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%40", "kg_var": "%45", "alt_ust_6_gol": "%15"},
    {"lig": "Serie A", "tarih": "2026-10-07", "saat": "21:45", "mac": "Monza - Udinese", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Serie A", "tarih": "2026-10-08", "saat": "18:30", "mac": "Genoa - Verona", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Serie A", "tarih": "2026-10-08", "saat": "21:45", "mac": "Cagliari - Empoli", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%55", "kg_var": "%60", "alt_ust_6_gol": "%20"},
    {"lig": "Serie A", "tarih": "2026-10-09", "saat": "18:30", "mac": "Lecce - Parma", "skor_tahmini": "0 - 0", "iy_1_5_ust": "%30", "kg_var": "%35", "alt_ust_6_gol": "%10"},
    {"lig": "Serie A", "tarih": "2026-10-09", "saat": "21:45", "mac": "Venezia - Como", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},
    {"lig": "Serie A", "tarih": "2026-10-10", "saat": "18:00", "mac": "Juventus - AC Milan", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Serie A", "tarih": "2026-10-10", "saat": "21:45", "mac": "Napoli - Inter", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "Serie A", "tarih": "2026-10-11", "saat": "18:00", "mac": "Lazio - Atalanta", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%65", "kg_var": "%70", "alt_ust_6_gol": "%30"},
    {"lig": "Serie A", "tarih": "2026-10-11", "saat": "21:45", "mac": "Fiorentina - Roma", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Serie A", "tarih": "2026-10-12", "saat": "18:30", "mac": "Torino - Bologna", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%45", "kg_var": "%50", "alt_ust_6_gol": "%15"},
    {"lig": "Serie A", "tarih": "2026-10-12", "saat": "21:45", "mac": "Udinese - Monza", "skor_tahmini": "2 - 0", "iy_1_5_ust": "%55", "kg_var": "%45", "alt_ust_6_gol": "%20"},
    {"lig": "Serie A", "tarih": "2026-10-13", "saat": "18:30", "mac": "Verona - Genoa", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Serie A", "tarih": "2026-10-13", "saat": "21:45", "mac": "Empoli - Cagliari", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Serie A", "tarih": "2026-10-14", "saat": "18:30", "mac": "Parma - Venezia", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Serie A", "tarih": "2026-10-14", "saat": "21:45", "mac": "Como - Lecce", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%40", "kg_var": "%45", "alt_ust_6_gol": "%15"},

    # Bundesliga (20 Maç)
    {"lig": "Bundesliga", "tarih": "2026-10-05", "saat": "16:30", "mac": "Bayern Munich - Bayer Leverkusen", "skor_tahmini": "3 - 2", "iy_1_5_ust": "%80", "kg_var": "%85", "alt_ust_6_gol": "%45"},
    {"lig": "Bundesliga", "tarih": "2026-10-05", "saat": "19:30", "mac": "Borussia Dortmund - RB Leipzig", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "Bundesliga", "tarih": "2026-10-06", "saat": "16:30", "mac": "Stuttgart - Eintracht Frankfurt", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%65", "kg_var": "%70", "alt_ust_6_gol": "%30"},
    {"lig": "Bundesliga", "tarih": "2026-10-06", "saat": "19:30", "mac": "Wolfsburg - Bayer Leverkusen", "skor_tahmini": "1 - 3", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%35"},
    {"lig": "Bundesliga", "tarih": "2026-10-07", "saat": "16:30", "mac": "Union Berlin - Freiburg", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Bundesliga", "tarih": "2026-10-07", "saat": "19:30", "mac": "Werder Bremen - Mainz 05", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%70", "kg_var": "%75", "alt_ust_6_gol": "%30"},
    {"lig": "Bundesliga", "tarih": "2026-10-08", "saat": "16:30", "mac": "Hoffenheim - Augsburg", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Bundesliga", "tarih": "2026-10-08", "saat": "19:30", "mac": "Bochum - St. Pauli", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%45", "kg_var": "%50", "alt_ust_6_gol": "%15"},
    {"lig": "Bundesliga", "tarih": "2026-10-09", "saat": "16:30", "mac": "Heidenheim - Holstein Kiel", "skor_tahmini": "2 - 0", "iy_1_5_ust": "%55", "kg_var": "%45", "alt_ust_6_gol": "%20"},
    {"lig": "Bundesliga", "tarih": "2026-10-09", "saat": "19:30", "mac": "Bayer Leverkusen - Borussia Dortmund", "skor_tahmini": "3 - 2", "iy_1_5_ust": "%80", "kg_var": "%85", "alt_ust_6_gol": "%45"},
    {"lig": "Bundesliga", "tarih": "2026-10-10", "saat": "16:30", "mac": "RB Leipzig - Bayern Munich", "skor_tahmini": "2 - 3", "iy_1_5_ust": "%80", "kg_var": "%85", "alt_ust_6_gol": "%45"},
    {"lig": "Bundesliga", "tarih": "2026-10-10", "saat": "19:30", "mac": "Eintracht Frankfurt - Stuttgart", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "Bundesliga", "tarih": "2026-10-11", "saat": "16:30", "mac": "Freiburg - Wolfsburg", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%50", "kg_var": "%55", "alt_ust_6_gol": "%20"},
    {"lig": "Bundesliga", "tarih": "2026-10-11", "saat": "19:30", "mac": "Mainz 05 - Union Berlin", "skor_tahmini": "1 - 0", "iy_1_5_ust": "%40", "kg_var": "%40", "alt_ust_6_gol": "%15"},
    {"lig": "Bundesliga", "tarih": "2026-10-12", "saat": "16:30", "mac": "Augsburg - Werder Bremen", "skor_tahmini": "2 - 1", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Bundesliga", "tarih": "2026-10-12", "saat": "19:30", "mac": "St. Pauli - Hoffenheim", "skor_tahmini": "1 - 2", "iy_1_5_ust": "%60", "kg_var": "%65", "alt_ust_6_gol": "%25"},
    {"lig": "Bundesliga", "tarih": "2026-10-13", "saat": "16:30", "mac": "Holstein Kiel - Bochum", "skor_tahmini": "1 - 1", "iy_1_5_ust": "%45", "kg_var": "%50", "alt_ust_6_gol": "%15"},
    {"lig": "Bundesliga", "tarih": "2026-10-13", "saat": "19:30", "mac": "Bayer Leverkusen - Heidenheim", "skor_tahmini": "3 - 0", "iy_1_5_ust": "%70", "kg_var": "%40", "alt_ust_6_gol": "%35"},
    {"lig": "Bundesliga", "tarih": "2026-10-14", "saat": "16:30", "mac": "Borussia Dortmund - Stuttgart", "skor_tahmini": "2 - 2", "iy_1_5_ust": "%75", "kg_var": "%80", "alt_ust_6_gol": "%40"},
    {"lig": "Bundesliga", "tarih": "2026-10-14", "saat": "19:30", "mac": "Bayern Munich - Union Berlin", "skor_tahmini": "3 - 0", "iy_1_5_ust": "%70", "kg_var": "%35", "alt_ust_6_gol": "%35"}
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