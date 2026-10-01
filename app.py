from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('matches.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lig TEXT,
            tarih TEXT,
            saat TEXT,
            mac TEXT,
            skor_tahmini TEXT,
            iy_15_ust TEXT,
            kg_var TEXT,
            gol_6_ust TEXT
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM matches')
    if cursor.fetchone()[0] == 0:
        initial_matches = [
            # Trendyol Süper Lig
            ("Trendyol Süper Lig", "2026-10-09", "20:00", "Galatasaray - Kasımpaşa", "2 - 1", "%53", "%44", "%17"),
            ("Trendyol Süper Lig", "2026-10-10", "16:00", "Samsunspor - Trabzonspor", "1 - 2", "%50", "%47", "%20"),
            ("Trendyol Süper Lig", "2026-10-10", "19:00", "Çaykur Rizespor - Fenerbahçe", "0 - 2", "%66", "%43", "%17"),
            ("Trendyol Süper Lig", "2026-10-11", "13:30", "Konyaspor - Başakşehir", "1 - 1", "%84", "%84", "%44"),
            ("Trendyol Süper Lig", "2026-10-11", "19:00", "Beşiktaş - Kocaelispor", "1 - 1", "%67", "%63", "%30"),
            ("Trendyol Süper Lig", "2026-10-12", "20:00", "Eyüpspor - Göztepe", "1 - 2", "%58", "%71", "%36"),
            ("Trendyol Süper Lig", "2026-10-17", "16:00", "Gençlerbirliği - Galatasaray", "1 - 2", "%60", "%77", "%40"),
            ("Trendyol Süper Lig", "2026-10-17", "19:00", "Fenerbahçe - Alanyaspor", "3 - 1", "%72", "%55", "%25"),
            ("Trendyol Süper Lig", "2026-10-18", "19:00", "Trabzonspor - Antalyaspor", "2 - 0", "%65", "%40", "%15"),
            ("Trendyol Süper Lig", "2026-10-19", "20:00", "Adana Demirspor - Beşiktaş", "1 - 3", "%78", "%68", "%35"),

            # Premier Lig
            ("Premier Lig", "2026-10-11", "16:00", "Arsenal - Chelsea", "2 - 2", "%75", "%70", "%35"),
            ("Premier Lig", "2026-10-11", "18:30", "Manchester City - Liverpool", "3 - 2", "%88", "%82", "%50"),
            ("Premier Lig", "2026-10-12", "16:00", "Manchester United - Tottenham", "2 - 1", "%68", "%65", "%28"),
            ("Premier Lig", "2026-10-12", "18:30", "Newcastle United - Aston Villa", "1 - 1", "%62", "%60", "%20"),
            ("Premier Lig", "2026-10-18", "16:00", "Liverpool - Everton", "2 - 0", "%70", "%45", "%22"),
            ("Premier Lig", "2026-10-18", "18:30", "Chelsea - Manchester United", "2 - 2", "%76", "%74", "%38"),

            # La Liga
            ("La Liga", "2026-10-12", "21:00", "Real Madrid - Barcelona", "2 - 1", "%80", "%78", "%40"),
            ("La Liga", "2026-10-13", "19:30", "Atletico Madrid - Real Sociedad", "1 - 0", "%52", "%42", "%12"),
            ("La Liga", "2026-10-13", "22:00", "Villarreal - Valencia", "2 - 2", "%74", "%72", "%30"),
            ("La Liga", "2026-10-19", "19:00", "Barcelona - Athletic Bilbao", "3 - 1", "%82", "%60", "%32"),

            # Serie A
            ("Serie A", "2026-10-14", "19:00", "Inter - Juventus", "1 - 1", "%58", "%62", "%18"),
            ("Serie A", "2026-10-14", "21:45", "AC Milan - Napoli", "2 - 1", "%70", "%68", "%25"),
            ("Serie A", "2026-10-15", "21:45", "Roma - Lazio", "1 - 2", "%65", "%70", "%22"),
            ("Serie A", "2026-10-20", "20:00", "Atalanta - Fiorentina", "2 - 2", "%79", "%80", "%35"),

            # Bundesliga
            ("Bundesliga", "2026-10-15", "16:30", "Bayern Munich - Borussia Dortmund", "3 - 2", "%90", "%85", "%55"),
            ("Bundesliga", "2026-10-15", "19:30", "RB Leipzig - Bayer Leverkusen", "2 - 2", "%82", "%81", "%45"),
            ("Bundesliga", "2026-10-21", "17:30", "Stuttgart - Eintracht Frankfurt", "2 - 1", "%75", "%70", "%30")
        ]
        cursor.executemany('''
            INSERT INTO matches (lig, tarih, saat, mac, skor_tahmini, iy_15_ust, kg_var, gol_6_ust)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', initial_matches)
        conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    search_query = request.args.get("q", "")
    secilen_lig = request.args.get("lig", "Tümü")
    
    conn = sqlite3.connect('matches.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT DISTINCT lig FROM matches')
    ligler = ["Tümü"] + [row[0] for row in cursor.fetchall()]
    
    query = 'SELECT * FROM matches WHERE 1=1'
    params = []
    
    if secilen_lig != "Tümü":
        query += ' AND lig = ?'
        params.append(secilen_lig)
        
    if search_query:
        query += ' AND mac LIKE ?'
        params.append(f'%{search_query}%')
        
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    tum_maclar = []
    for r in rows:
        tum_maclar.append({
            "id": r[0], "lig": r[1], "tarih": r[2], "saat": r[3], 
            "mac": r[4], "skor_tahmini": r[5], "iy_15_ust": r[6], 
            "kg_var": r[7], "gol_6_ust": r[8]
        })
        
    lig_gruplari = {}
    for m in tum_maclar:
        l = m["lig"]
        if l not in lig_gruplari:
            lig_gruplari[l] = []
        lig_gruplari[l].append(m)

    return render_template("index.html", ligler=ligler, secilen_lig=secilen_lig, lig_gruplari=lig_gruplari, search_query=search_query)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    hata = None
    if request.method == "POST":
        girilen_sifre = request.form.get("sifre")
        OGRI_SIFRE = "muhammed123" 
        
        if girilen_sifre != OGRI_SIFRE:
            hata = "Hatalı şifre! Sadece yetkili kişi ekleyebilir."
        else:
            lig = request.form.get("lig")
            tarih = request.form.get("tarih")
            saat = request.form.get("saat")
            mac = request.form.get("mac")
            skor_tahmini = request.form.get("skor_tahmini")
            iy_15_ust = request.form.get("iy_15_ust")
            kg_var = request.form.get("kg_var")
            gol_6_ust = request.form.get("gol_6_ust")
            
            conn = sqlite3.connect('matches.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO matches (lig, tarih, saat, mac, skor_tahmini, iy_15_ust, kg_var, gol_6_ust)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (lig, tarih, saat, mac, skor_tahmini, iy_15_ust, kg_var, gol_6_ust))
            conn.commit()
            conn.close()
            return redirect(url_for('home'))
            
    return render_template("admin.html", hata=hata)

if __name__ == "__main__":
    app.run(debug=True)