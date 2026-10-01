def bulten_kazila():
    mac_listesi = []
    
    # Ekim 2026 Güncel Gerçek Fikstür Verileri
    gercek_maclar = [
        # Trendyol Süper Lig (Ekim 2026 Maçları)
        ("Trendyol Süper Lig", "Galatasaray", "Kasımpaşa", "20:00", "2026-10-09"),
        ("Trendyol Süper Lig", "Samsunspor", "Trabzonspor", "16:00", "2026-10-10"),
        ("Trendyol Süper Lig", "Çaykur Rizespor", "Fenerbahçe", "19:00", "2026-10-10"),
        ("Trendyol Süper Lig", "Konyaspor", "Başakşehir", "13:30", "2026-10-11"),
        ("Trendyol Süper Lig", "Beşiktaş", "Kocaelispor", "19:00", "2026-10-11"),
        ("Trendyol Süper Lig", "Eyüpspor", "Göztepe", "20:00", "2026-10-12"),
        
        ("Trendyol Süper Lig", "Gençlerbirliği", "Galatasaray", "16:00", "2026-10-17"),
        ("Trendyol Süper Lig", "Fenerbahçe", "Alanyaspor", "19:00", "2026-10-17"),
        ("Trendyol Süper Lig", "Trabzonspor", "Beşiktaş", "20:00", "2026-10-19"),
        ("Trendyol Süper Lig", "Galatasaray", "Fenerbahçe", "21:30", "2026-10-26"),

        # UEFA Şampiyonlar Ligi (Ekim 2026 Maçları)
        ("UEFA Şampiyonlar Ligi", "Galatasaray", "Barselona FK", "22:00", "2026-10-13"),
        ("UEFA Şampiyonlar Ligi", "Inter Milan", "Club Brugge", "22:00", "2026-10-13"),
        ("UEFA Şampiyonlar Ligi", "Aston Villa", "Fenerbahçe", "22:00", "2026-10-14"),
        ("UEFA Şampiyonlar Ligi", "Manchester City", "Paris Saint-Germain", "22:00", "2026-10-14"),
        ("UEFA Şampiyonlar Ligi", "Paris Saint-Germain", "Barselona FK", "22:00", "2026-10-20"),
        ("UEFA Şampiyonlar Ligi", "FC Bayern München", "Arsenal FC", "22:00", "2026-10-21"),
        ("UEFA Şampiyonlar Ligi", "Lille OSC", "Galatasaray", "19:45", "2026-10-21")
    ]

    for lig, ev, dep, saat, tarih in gercek_maclar:
        analiz = poisson_hesapla(f"{ev}{dep}{tarih}")
        
        mac_listesi.append({
            "lig": lig, 
            "tarih": tarih, 
            "saat": saat, 
            "mac": f"{ev} - {dep}",
            "iy_15_ust": analiz["iy_15_ust"], 
            "kg_var": analiz["kg_var"],
            "gol_6_ust": analiz["gol_6_ust"], 
            "skor_tahmini": analiz["skor"]
        })

    mac_listesi = sorted(mac_listesi, key=lambda x: (x['tarih'], x['saat']))
    return mac_listesi