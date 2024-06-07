from flask import Flask, redirect, url_for
from dotenv import load_dotenv
import os
from src.routes.login import modulo_login
from src.routes.usuario import modulo_usuario
from src.routes.boletim_ocorrencia import modulo_boletim_ocorrencia
from src.routes.relatorio_grafico import modulo_relatorio_grafico


load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")


aplicacao = Flask(__name__)
aplicacao.config["SECRET_KEY"] = SECRET_KEY


@aplicacao.route("/")
def formulario_index():
<<<<<<< HEAD
    return redirect(url_for('modulo_login.login'))
=======
    return render_template("index.html")


@aplicacao.route("/login")
def formulario_login():
    return render_template("login.html")
>>>>>>> 4d49e44963dfa437437e7900a7d79e86433ec06b


aplicacao.register_blueprint(modulo_login)
aplicacao.register_blueprint(modulo_usuario)
aplicacao.register_blueprint(modulo_boletim_ocorrencia)
aplicacao.register_blueprint(modulo_relatorio_grafico)


if __name__ == "__main__":
    aplicacao.run(debug=True)
