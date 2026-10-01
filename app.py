from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Veritabanını ve tabloyu oluşturan fonksiyon
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
    # Eğer veritabanı boşsa başlangıç maçlarını ekleyelim
    cursor.execute('SELECT COUNT(*) FROM matches')
    if cursor.fetchone()[0] == 0:
        initial_matches = [
            ("Trendyol Süper Lig", "2026-10-09", "20:00", "Galatasaray - Kasımpaşa", "2 - 1", "%53", "%44", "%17"),
            ("Trendyol Süper Lig", "2026-10-10", "16:00", "Samsunspor - Trabzonspor", "1 - 2", "%50", "%47", "%20"),
            ("Premier Lig", "2026-10-11", "16:00", "Arsenal - Chelsea", "2 - 2", "%75", "%70", "%35"),
            ("Premier Lig", "2026-10-11", "18:30", "Manchester City - Liverpool", "3 - 2", "%88", "%82", "%50"),
            ("La Liga", "2026-10-12", "21:00", "Real Madrid - Barcelona", "2 - 1", "%80", "%78", "%40"),
            ("Serie A", "2026-10-14", "19:00", "Inter - Juventus", "1 - 1", "%58", "%62", "%18"),
            ("Bundesliga", "2026-10-15", "16:30", "Bayern Munich - Borussia Dortmund", "3 - 2", "%90", "%85", "%55")
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
    
    # Benzersiz ligleri çek
    cursor.execute('SELECT DISTINCT lig FROM matches')
    ligler = ["Tümü"] + [row[0] for row in cursor.fetchall()]
    
    # Filtreleme sorgusu
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

# Kod yazmadan maç ekleyebileceğin Yönetim Paneli
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
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
        
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)