from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def home():
        return "<p>Hello, World!</p>"
    @app.route("/mouaad")
    def mouaad():
        return "<h1>Mouaad</h1>"
    return app