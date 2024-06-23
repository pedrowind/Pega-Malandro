from src.utils.utilidades_login import Action_Login
from flask import Blueprint, render_template, request, session

mod_login = Blueprint('mod_login', __name__)
act_login = Action_Login()

@mod_login.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'POST':
    nme_usr = request.form['nme_usr']
    eml_usr = request.form['eml_usr']
    pwd_usr = request.form['pwd_usr']
    confirmar_pwd_usr = request.form['confirmar_pwd_usr']

    if pwd_usr != confirmar_pwd_usr:
      return render_template('cadastro.html', msg='Senhas Diferentes!')
    else:
      retorno = act_login.cadastrar(nme_usr, eml_usr, pwd_usr)

      return render_template('cadastro.html', msg='Criado o Usuário com ID: {0} e Senha: {1}'.format(retorno[0], retorno[1]))
  else:
    return render_template('cadastro.html', msg='')

@mod_login.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    usr = request.form['usuario']
    pwd = request.form['senha']
    obj = act_login.login(usr, pwd)

    if obj is not None:
      session['usuario'] = obj

      return render_template('menu.html')
    else:
      return render_template('login.html', msg='Falha no Login ao Sistema!')
  else:
    return render_template('login.html', msg='')

@mod_login.route('/sair')
def sair():
  session.pop('usuario', None)

  return render_template('login.html', msg='')

@mod_login.route('/resetar_senha', methods=['GET', 'POST'])
def resetar_senha():
  try:
    session['usuario']
  except:
    return render_template('login.html', msg='Não Burle o Sistema!')

  if session['usuario']['pfl_usr'] == 'C':
    return render_template('login.html', msg='Você é um Usuário Comum, Não Pode Fazer Isso!')

  if request.method == 'POST':
    usuario = request.form['usuario']
    senha = act_login.resetar_senha(usuario)

    if senha == 0:
      return render_template('resetar_senha.html', msg='Erro ao Tentar Mudar a Senha!')
    else:
      return render_template('resetar_senha.html', msg='Senha Resetada com Sucesso! Nova Senha: {0}'.format(senha))
  else:
    return render_template('resetar_senha.html', msg='')

@mod_login.route('/alterar_senha', methods=['GET', 'POST'])
def alterar_senha():
  try:
    session['usuario']
  except:
    return render_template('login.html', msg='Não Burle o Sistema!')

  if request.method == 'POST':
    senha_atual = request.form['senha_atual']
    senha_nova = request.form['senha_nova']
    confirmacao_senha_nova = request.form['confirmacao_senha_nova']
    msg = act_login.alterar_senha(session['usuario']['idt_usr'], senha_atual, senha_nova, confirmacao_senha_nova)

    return render_template('alterar_senha.html', msg=msg)
  else:
    return render_template('alterar_senha.html', msg='')

@mod_login.route('/incluir_usuario', methods=['GET', 'POST'])
def incluir_usuario():
  try:
    session['usuario']
  except:
    return render_template('login.html', msg='Não Burle o Sistema!')

  if session['usuario']['pfl_usr'] != 'A':
    return render_template('login.html', msg='Você Não é Administrador!')

  if request.method == 'POST':
    nme_usr = request.form['nme_usr']
    eml_usr = request.form['eml_usr']
    pwd_usr = request.form['pwd_usr']
    pfl_usr = request.form['pfl_usr']
    retorno = act_login.incluir_usuario(nme_usr, eml_usr, pwd_usr, pfl_usr)

    return render_template('incluir_usuario.html', msg='Criado o Usuário com ID: {0} e Senha: {1}'.format(retorno[0], retorno[1]))
  else:
    return render_template('incluir_usuario.html', msg='')
  
@mod_login.route('/listar_usuarios', methods=['GET', 'POST'])
def listar_usuarios():
  try:
    session['usuario']
  except:
    return render_template('login.html', msg='Não Burle o Sistema!')

  if session['usuario']['pfl_usr'] != 'A':
    return render_template('login.html', msg='Você Não é Administrador!')

  if request.method == 'POST':
    nme_usr = request.form['nme_usr']
    pfl_usr = request.form['pfl_usr']
    lista = act_login.listar_usuarios(nme_usr, pfl_usr)

    return render_template('listar_usuarios.html', msg='Retornado(s) {0} Usuário(s).'.format(len(lista)), lista=lista)
  else:
    return render_template('listar_usuarios.html', msg='', lista=[])

@mod_login.route('/alterar_usuario', methods=['GET', 'POST'])
def alterar_usuario():
  try:
    usr = session['usuario']
  except:
    return render_template('login.html', msg='Não Burle o Sistema!')

  if session['usuario']['pfl_usr'] != 'A':
    return render_template('login.html', msg='Você Não é Administrador!')

  if request.method == 'POST':
    idt_usr = request.form['idt_usr']
    nme_usr = request.form['nme_usr']
    eml_usr = request.form['eml_usr']
    pwd_usr = request.form['pwd_usr']
    pfl_usr = request.form['pfl_usr']
    retorno = act_login.alterar_usuario(idt_usr, nme_usr, eml_usr, pwd_usr, pfl_usr)
    usr = act_login.get_usuario(idt_usr)

    return render_template('alterar_usuario.html', msg=retorno, usr=usr)
  else:
    idt_usr = request.args.get('idt_usr')
    usr = act_login.get_usuario(idt_usr)

    return render_template('alterar_usuario.html', msg='', usr=usr)
  
@mod_login.route('/excluir_usuario', methods=['GET', 'POST'])
def excluir_usuario():
  try:
    session['usuario']
  except:
    return render_template('login.html', msg='Não Burle o Sistema!')

  if session['usuario']['pfl_usr'] != 'A':
    return render_template('login.html', msg='Você Não é Administrador!')

  if request.method == 'POST':
    idt_usr = request.form['idt_usr']
    retorno = act_login.excluir_usuario(idt_usr)
    usr = act_login.get_usuario(idt_usr)

    return render_template('excluir_usuario.html', msg=retorno, usr=usr)
  else:
    idt_usr = request.args.get('idt_usr')
    usr = act_login.get_usuario(idt_usr)

    return render_template('excluir_usuario.html', msg='', usr=usr)