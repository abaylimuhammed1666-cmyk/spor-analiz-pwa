from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Spor Analiz PWA Uygulamasi Calisiyor!"

if __name__ == "_main_":
    app.run()
