from flask import Blueprint, render_template, request
from servidor.repositorio import Repositorio


modulo_estado = Blueprint('modulo_estado', __name__)


@modulo_estado.route('/formulario_insercao_estado')
def formulario_insercao_estado():
    return render_template('formulario_insercao_estado.html')


@modulo_estado.route('/insercao_estado', methods=['POST'])
def insercao_estado():
    nome = request.form['nome_estado']
    codigo = request.form['codigo_pais']
    repositorio = Repositorio()

    comando = '''
        INSERT INTO tabela_estado(nome_estado, codigo_pais)
        VALUES (%s, %s)
    '''
    identificador = repositorio.inserir(comando, [nome, codigo])

    return render_template('insercao_estado.html', identificador=identificador)


@modulo_estado.route('/consulta_estado')
def consulta_estado():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_estado
        ORDER BY nome_estado
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('consulta_estado.html', lista=lista)


@modulo_estado.route('/escolha_atualizacao_estado')
def escolha_atualizacao_estado():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_estado
        ORDER BY nome_estado
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('escolha_atualizacao_estado.html', lista=lista)


@modulo_estado.route('/formulario_atualizacao_estado', methods=['GET'])
def formulario_atualizacao_estado():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_estado
        WHERE identificador_estado = %s
    '''
    dicionario = repositorio.pegar_dicionario(comando, [request.args.get('identificador')])

    return render_template('formulario_atualizacao_estado.html',
                           identificador_estado=dicionario['identificador_estado'],
                           nome_estado=dicionario['nome_estado'], codigo_pais=dicionario['codigo_pais'])


@modulo_estado.route('/atualizacao_estado', methods=['POST'])
def atualizacao_estado():
    identificador = request.form['identificador_estado']
    nome = request.form['nome_estado']
    codigo = request.form['codigo_pais']
    repositorio = Repositorio()

    comando = '''
        UPDATE tabela_estado
        SET 
            nome_estado = %s,
            codigo_pais = %s
        WHERE identificador_estado = %s
    '''
    numero_linhas = repositorio.atualizar_deletar(comando, [nome, codigo, identificador])

    return render_template('atualizacao_estado.html', numero_linhas=numero_linhas)


@modulo_estado.route('/delecao_estado', methods=['GET'])
def delecao_estado():
    repositorio = Repositorio()

    comando = '''
        DELETE FROM tabela_estado
        WHERE identificador_estado = %s
    '''
    numero_linhas = repositorio.atualizar_deletar(comando, [request.args.get('identificador')])

    return render_template('delecao_estado.html', numero_linhas=numero_linhas)
