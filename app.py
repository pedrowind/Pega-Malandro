from flask import Flask, render_template
from routes.usuario import modulo_usuario
from routes.boletim_ocorrencia import modulo_boletim_ocorrencia
from routes.relatorio_grafico import modulo_relatorio_grafico


aplicacao = Flask(__name__)


@aplicacao.route('/')
def formulario_index():
    return render_template('index.html')


aplicacao.register_blueprint(modulo_usuario)
aplicacao.register_blueprint(modulo_boletim_ocorrencia)
aplicacao.register_blueprint(modulo_relatorio_grafico)


if __name__ == '__main__':
    aplicacao.run()
