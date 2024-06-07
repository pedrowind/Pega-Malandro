from flask import Blueprint, render_template, request, flash, redirect, url_for
from src.server.repositorio import Repositorio


modulo_usuario = Blueprint('modulo_usuario', __name__)


@modulo_usuario.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@modulo_usuario.route('/inserir_usuario', methods=['POST'])
def inserir_usuario():
    repositorio = Repositorio()

    nome = request.form['nome_usuario']
    email = request.form['email_usuario']
    senha = request.form['senha_usuario']
    confirmar_senha = request.form['confirmar_senha_usuario']

    erro = 'Senhas não conferem!'
    if senha != confirmar_senha:
        return erro

    comando = '''
        INSERT INTO tabela_usuario(nome_usuario, email_usuario, senha_usuario, perfil_usuario)
        VALUES (%s, %s, SHA(%s), 'C')
    '''
    repositorio.inserir(comando, [nome, email, senha])

    return render_template('resultado_inserir_usuario.html')


@modulo_usuario.route('/consulta_usuario')
def consulta_usuario():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_usuario
        ORDER BY nome_usuario
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('consulta_usuario.html', lista=lista)


@modulo_usuario.route('/escolha_atualizacao_usuario')
def escolha_atualizacao_usuario():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_usuario
        ORDER BY nome_usuario
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('escolha_atualizacao_usuario.html', lista=lista)


@modulo_usuario.route('/formulario_atualizacao_usuario', methods=['GET'])
def formulario_atualizacao_usuario():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_usuario
        WHERE identificador_usuario = %s
    '''
    dicionario = repositorio.pegar_dicionario(comando, [request.args.get('identificador')])

    return render_template('formulario_atualizacao_usuario.html', identificador_usuario=dicionario['identificador_usuario'],
                           nome_usuario=dicionario['nome_usuario'])


@modulo_usuario.route('/atualizacao_usuario', methods=['POST'])
def atualizacao_usuario():
    identificador = request.form['identificador_usuario']
    nome = request.form['nome_usuario']
    repositorio = Repositorio()

    comando = '''
        UPDATE tabela_usuario
        SET nome_usuario = %s
        WHERE identificador_usuario = %s
    '''
    numero_linhas = repositorio.atualizar_deletar(comando, [nome, identificador])

    return render_template('resultado_atualizacao_usuario.html', numero_linhas=numero_linhas)


@modulo_usuario.route('/delecao_usuario', methods=['GET'])
def delecao_usuario():
    repositorio = Repositorio()

    comando = '''
        DELETE FROM tabela_usuario
        WHERE identificador_usuario = %s
    '''

    try:
        numero_linhas = repositorio.atualizar_deletar(comando, [request.args.get('identificador')])
    except Exception as erro:
        return render_template('erro_relacionamento_usuario_boletim_ocorrencia.html', erro=erro)
    else:
        return render_template('resultado_delecao_usuario.html', numero_linhas=numero_linhas)
