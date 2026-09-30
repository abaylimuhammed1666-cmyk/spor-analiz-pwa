from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Spor Analiz PWA API Calisiyor!"
    })

@app.route('/api/analyze', methods=['GET'])
def get_sample_analysis():
    sample_data = [
        {
            "id": 1,
            "teams": "Barcelona vs Getafe",
            "over35_prob": "%78",
            "btts_both_halves": "%35",
            "risk_level": "Orta"
        },
        {
            "id": 2,
            "teams": "France vs Belgium",
            "over35_prob": "%65",
            "btts_both_halves": "%28",
            "risk_level": "Yuksek"
        }
    ]
    return jsonify({"status": "success", "matches": sample_data})

if _name_ == '_main_':
    app.run(debug=True)