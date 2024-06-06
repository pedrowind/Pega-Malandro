from flask import Flask, render_template
from servidor.repositorio import Repositorio
from crud.usuario import modulo_usuario
from crud.boletim_ocorrencia import modulo_boletim_ocorrencia


aplicacao = Flask(__name__)


@aplicacao.route('/')
def formulario_index():
    return render_template('index.html')


@aplicacao.route('/relatorio_grafico_pizza')
def relatorio_grafico_pizza():
    repositorio = Repositorio()

    comando = '''
        SELECT
            tabela_usuario.nome_usuario,
            COUNT(tabela_boletim_ocorrencia.identificador_boletim_ocorrencia) AS quantidade_boletim_ocorrencias
        FROM tabela_usuario
        JOIN tabela_boletim_ocorrencia ON tabela_usuario.identificador_usuario = tabela_boletim_ocorrencia.codigo_usuario
        GROUP BY tabela_usuario.nome_usuario;
    '''
    dados = repositorio.pegar_lista(comando, [])

    return render_template('relatorio_grafico_pizza.html', dados=dados)


@aplicacao.route('/relatorio_grafico_organograma')
def relatorio_grafico_organograma():
    repositorio = Repositorio()

    comando_usuario = '''
        SELECT *
        FROM tabela_usuario
        ORDER BY nome_usuario;
    '''
    lista_usuarios = repositorio.pegar_lista(comando_usuario, [])

    comando_boletim_ocorrencia = '''
        SELECT 
            identificador_boletim_ocorrencia,
            nome_boletim_ocorrencia
        FROM tabela_boletim_ocorrencia
        WHERE codigo_usuario = %s
        ORDER BY nome_boletim_ocorrencia;
    '''
    for usuario in lista_usuarios:
        usuario['boletim_ocorrencias'] = repositorio.pegar_lista(comando_boletim_ocorrencia, [usuario['identificador_usuario']])

    return render_template('relatorio_grafico_organograma.html', dados=lista_usuarios)


aplicacao.register_blueprint(modulo_usuario)
aplicacao.register_blueprint(modulo_boletim_ocorrencia)


if __name__ == '__main__':
    aplicacao.run()