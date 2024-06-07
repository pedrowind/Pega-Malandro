from flask import Flask, render_template
from dotenv import load_dotenv
import os
from src.routes.usuario import modulo_usuario
from src.routes.boletim_ocorrencia import modulo_boletim_ocorrencia
from src.routes.relatorio_grafico import modulo_relatorio_grafico

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")


aplicacao = Flask(__name__)
aplicacao.config["SECRET_KEY"] = SECRET_KEY


@aplicacao.route("/")
def formulario_index():
    return render_template("index.html")


@aplicacao.route("/login")
def formulario_login():
    return render_template("login.html")


@aplicacao.route("/cadastrar")
def formulario_cadastrar():
    return render_template("cadastro_usuario.html")


aplicacao.register_blueprint(modulo_usuario)
aplicacao.register_blueprint(modulo_boletim_ocorrencia)
aplicacao.register_blueprint(modulo_relatorio_grafico)


if __name__ == "__main__":
    aplicacao.run(debug=True)
