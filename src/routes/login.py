from flask import Blueprint, render_template, request, session
from utils.deposito_funcoes import Deposito_Funcoes


modulo_login = Blueprint('modulo_login', __name__)
modulo_login.config['SECRET_KEY'] = 'SECRET_KEY_VERY_MUCH_BIG_AND_STRONG'


deposito_funcoes = Deposito_Funcoes()


@modulo_login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        dicionario = deposito_funcoes.login(usuario, senha)
        if dicionario is not None:
            session['usuario'] = dicionario
            return render_template('menu.html')
        else:
            return render_template('login.html', msg='Falha no Login ao Sistema')
    else:
        return render_template('login.html')


@modulo_login.route('/sair')
def sair():
    session.pop('usuario', None)
    return render_template('login.html')


@modulo_login.route('/alterar_senha', methods=['GET', 'POST'])
def alterar_senha():
    try:
        session['usuario']
    except:
        return render_template('login.html', msg='Está Tentando Burlar o Sistema!')

    if request.method == 'POST':
        senha_atual = request.form['senha_atual']
        nova_senha = request.form['nova_senha']
        confirmar_senha = request.form['confirmar_senha']
        msg = deposito_funcoes.alterar_senha(session['usuario']['idt_usuario'], senha_atual, nova_senha, confirmar_senha)

        return render_template('alterar_senha.html', msg=msg)
    else:
        return render_template('alterar_senha.html')


@modulo_login.route('/resetar_senha', methods=['GET', 'POST'])
def resetar_senha():
    try:
        session['usuario']
    except:
        return render_template('login.html', msg='Está Tentando Burlar o Sistema!')

    if session['usuario']['pfl_usuario'] != 'G':
        return render_template('login.html', msg='Está Tentando Burlar o Sistema! Você Não é Gerente!')

    if request.method == 'POST':
        usuario = request.form['usuario']
        deposito_funcoes.resetar_senha(usuario)
        return render_template('resetar_senha.html', msg='Senha Resetada com Sucesso!')
    else:
        return render_template('resetar_senha.html')
