from flask import Blueprint, render_template, request
from servidor.repositorio import Repositorio


modulo_pais = Blueprint('modulo_pais', __name__)


@modulo_pais.route('/formulario_insercao_pais')
def formulario_insercao_pais():
    return render_template('formulario_insercao_pais.html')


@modulo_pais.route('/insercao_pais', methods=['POST'])
def insercao_pais():
    nome = request.form['nome_pais']
    repositorio = Repositorio()

    comando = '''
        INSERT INTO tabela_pais(nome_pais)
        VALUES (%s)
    '''
    identificador = repositorio.inserir(comando, [nome])

    return render_template('insercao_pais.html', identificador=identificador)


@modulo_pais.route('/consulta_pais')
def consulta_pais():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_pais
        ORDER BY nome_pais
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('consulta_pais.html', lista=lista)


@modulo_pais.route('/escolha_atualizacao_pais')
def escolha_atualizacao_pais():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_pais
        ORDER BY nome_pais
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('escolha_atualizacao_pais.html', lista=lista)


@modulo_pais.route('/formulario_atualizacao_pais', methods=['GET'])
def formulario_atualizacao_pais():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_pais
        WHERE identificador_pais = %s
    '''
    dicionario = repositorio.pegar_dicionario(comando, [request.args.get('identificador')])

    return render_template('formulario_atualizacao_pais.html', identificador_pais=dicionario['identificador_pais'],
                           nome_pais=dicionario['nome_pais'])


@modulo_pais.route('/atualizacao_pais', methods=['POST'])
def atualizacao_pais():
    identificador = request.form['identificador_pais']
    nome = request.form['nome_pais']
    repositorio = Repositorio()

    comando = '''
        UPDATE tabela_pais
        SET nome_pais = %s
        WHERE identificador_pais = %s
    '''
    numero_linhas = repositorio.atualizar_deletar(comando, [nome, identificador])

    return render_template('atualizacao_pais.html', numero_linhas=numero_linhas)


@modulo_pais.route('/delecao_pais', methods=['GET'])
def delecao_pais():
    repositorio = Repositorio()

    comando = '''
        DELETE FROM tabela_pais
        WHERE identificador_pais = %s
    '''

    try:
        numero_linhas = repositorio.atualizar_deletar(comando, [request.args.get('identificador')])
    except Exception as erro:
        return render_template('erro_relacionamento_pais_estado.html', erro=erro)
    else:
        return render_template('delecao_pais.html', numero_linhas=numero_linhas)
