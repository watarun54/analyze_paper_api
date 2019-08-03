from flask import Flask
from controllers import scrape_paper as scrape

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

app.register_blueprint(scrape.app)

if __name__ == "__main__":
    app.run(debug=True)
