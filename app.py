from flask import Flask, redirect, url_for
from dotenv import load_dotenv
import os
from src.routes.rota_login import mod_login
from src.routes.rota_bo import mod_bo
from src.routes.rota_tst import mod_tst

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def formulario_index():
    return redirect(url_for("mod_login.login"))


app.register_blueprint(mod_login)
app.register_blueprint(mod_bo)
app.register_blueprint(mod_tst)

if __name__ == "__main__":
    app.run(debug=True)
