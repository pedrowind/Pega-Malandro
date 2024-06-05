from flask import Flask, render_template
from servidor.repositorio import Repositorio
from icad.pais import modulo_pais
from icad.estado import modulo_estado


aplicacao = Flask(__name__)


@aplicacao.route('/')
def formulario_index():
    return render_template('index.html')


@aplicacao.route('/relatorio_grafico_pizza')
def relatorio_grafico_pizza():
    repositorio = Repositorio()

    comando = '''
        SELECT
            tabela_pais.nome_pais,
            COUNT(tabela_estado.identificador_estado) AS quantidade_estados
        FROM tabela_pais
        JOIN tabela_estado ON tabela_pais.identificador_pais = tabela_estado.codigo_pais
        GROUP BY tabela_pais.nome_pais;
    '''
    dados = repositorio.pegar_lista(comando, [])

    return render_template('relatorio_grafico_pizza.html', dados=dados)


@aplicacao.route('/relatorio_grafico_organograma')
def relatorio_grafico_organograma():
    repositorio = Repositorio()

    comando_pais = '''
        SELECT *
        FROM tabela_pais
        ORDER BY nome_pais;
    '''
    lista_paises = repositorio.pegar_lista(comando_pais, [])

    comando_estado = '''
        SELECT 
            identificador_estado,
            nome_estado
        FROM tabela_estado
        WHERE codigo_pais = %s
        ORDER BY nome_estado;
    '''
    for pais in lista_paises:
        pais['estados'] = repositorio.pegar_lista(comando_estado, [pais['identificador_pais']])

    return render_template('relatorio_grafico_organograma.html', dados=lista_paises)


aplicacao.register_blueprint(modulo_pais)
aplicacao.register_blueprint(modulo_estado)


if __name__ == '__main__':
    aplicacao.run()
