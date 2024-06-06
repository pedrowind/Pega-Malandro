from flask import Blueprint, render_template, request
from servidor.repositorio import Repositorio


modulo_boletim_ocorrencia = Blueprint('modulo_boletim_ocorrencia', __name__)


@modulo_boletim_ocorrencia.route('/formulario_insercao_boletim_ocorrencia')
def formulario_insercao_boletim_ocorrencia():
    return render_template('formulario_insercao_boletim_ocorrencia.html')


@modulo_boletim_ocorrencia.route('/insercao_boletim_ocorrencia', methods=['POST'])
def insercao_boletim_ocorrencia():
    nome = request.form['nome_boletim_ocorrencia']
    codigo = request.form['codigo_usuario']
    repositorio = Repositorio()

    comando = '''
        INSERT INTO tabela_boletim_ocorrencia(nome_boletim_ocorrencia, codigo_usuario)
        VALUES (%s, %s)
    '''
    identificador = repositorio.inserir(comando, [nome, codigo])

    return render_template('resultado_insercao_boletim_ocorrencia.html', identificador=identificador)


@modulo_boletim_ocorrencia.route('/consulta_boletim_ocorrencia')
def consulta_boletim_ocorrencia():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_boletim_ocorrencia
        ORDER BY nome_boletim_ocorrencia
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('consulta_boletim_ocorrencia.html', lista=lista)


@modulo_boletim_ocorrencia.route('/escolha_atualizacao_boletim_ocorrencia')
def escolha_atualizacao_boletim_ocorrencia():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_boletim_ocorrencia
        ORDER BY nome_boletim_ocorrencia
    '''
    lista = repositorio.pegar_lista(comando, [])

    return render_template('escolha_atualizacao_boletim_ocorrencia.html', lista=lista)


@modulo_boletim_ocorrencia.route('/formulario_atualizacao_boletim_ocorrencia', methods=['GET'])
def formulario_atualizacao_boletim_ocorrencia():
    repositorio = Repositorio()

    comando = '''
        SELECT *
        FROM tabela_boletim_ocorrencia
        WHERE identificador_boletim_ocorrencia = %s
    '''
    dicionario = repositorio.pegar_dicionario(comando, [request.args.get('identificador')])

    return render_template('formulario_atualizacao_boletim_ocorrencia.html',
                           identificador_boletim_ocorrencia=dicionario['identificador_boletim_ocorrencia'],
                           nome_boletim_ocorrencia=dicionario['nome_boletim_ocorrencia'], codigo_usuario=dicionario['codigo_usuario'])


@modulo_boletim_ocorrencia.route('/atualizacao_boletim_ocorrencia', methods=['POST'])
def atualizacao_boletim_ocorrencia():
    identificador = request.form['identificador_boletim_ocorrencia']
    nome = request.form['nome_boletim_ocorrencia']
    codigo = request.form['codigo_usuario']
    repositorio = Repositorio()

    comando = '''
        UPDATE tabela_boletim_ocorrencia
        SET 
            nome_boletim_ocorrencia = %s,
            codigo_usuario = %s
        WHERE identificador_boletim_ocorrencia = %s
    '''
    numero_linhas = repositorio.atualizar_deletar(comando, [nome, codigo, identificador])

    return render_template('resultado_atualizacao_boletim_ocorrencia.html', numero_linhas=numero_linhas)


@modulo_boletim_ocorrencia.route('/delecao_boletim_ocorrencia', methods=['GET'])
def delecao_boletim_ocorrencia():
    repositorio = Repositorio()

    comando = '''
        DELETE FROM tabela_boletim_ocorrencia
        WHERE identificador_boletim_ocorrencia = %s
    '''
    numero_linhas = repositorio.atualizar_deletar(comando, [request.args.get('identificador')])

    return render_template('resultado_delecao_boletim_ocorrencia.html', numero_linhas=numero_linhas)