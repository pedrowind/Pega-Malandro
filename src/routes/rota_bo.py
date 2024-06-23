from src.utils.utilidades_bo import Action_Bo
from flask import Blueprint, render_template, request, session

mod_bo = Blueprint('mod_bo', __name__)
act_bo = Action_Bo()

@mod_bo.route('/incluir_bo', methods=['GET', 'POST'])
def incluir_bo():
  try:
    usr = session['usuario']
  except:
    return render_template(
      'login.html', 
      msg='Não Burle o Sistema!'
    )

  if request.method == 'POST':
    dta_ini_bo = request.form['dta_ini_bo']
    dta_fim_bo = request.form['dta_fim_bo']
    uf_bo = request.form['uf_bo']
    cid_bo = request.form['cid_bo']
    set_bo = request.form['set_bo']
    qua_bo = request.form['qua_bo']
    com_bo = request.form['com_bo']
    dsc_bo = request.form['dsc_bo']

    retorno_bo = act_bo.incluir_bo(
      dta_ini_bo, dta_fim_bo, uf_bo, cid_bo, set_bo, qua_bo, 
      com_bo, dsc_bo, usr['idt_usr']
    )

    return render_template(
      'incluir_bo.html', 
      usr=usr, 
      msg='Criado o BO com ID: {0}.'.format(retorno_bo)
    )
  else:
    return render_template(
      'incluir_bo.html', 
      usr=usr, 
      msg=''
    )
  
@mod_bo.route('/listar_bos', methods=['GET', 'POST'])
def listar_bos():
  try:
    session['usuario']
  except:
    return render_template(
      'login.html', 
      msg='Não Burle o Sistema!'
    )

  if request.method == 'POST':
    dta_ini_bo = request.form['dta_ini_bo']
    dta_fim_bo = request.form['dta_fim_bo']

    lista = act_bo.listar_bos(
      dta_ini_bo, 
      dta_fim_bo
    )

    return render_template(
      'listar_bos.html', 
      msg='Retornado(s) {0} B.O(s).'.format(len(lista)), 
      lista=lista
    )
  else:
    return render_template(
      'listar_bos.html', 
      msg='', 
      lista=[]
    )
  
@mod_bo.route('/listar_bos_by_usuario', methods=['GET', 'POST'])
def listar_bos_by_usuario():
  try:
    usr = session['usuario']
  except:
    return render_template(
      'login.html', 
      msg='Não Burle o Sistema!'
    )

  if request.method == 'POST':
    lista = act_bo.listar_bos_by_usuario(usr['idt_usr'])

    return render_template(
      'incluir_bo.html',
      usr=usr,
      msg='Retornado(s) {0} B.O(s).'.format(len(lista)),
      lista=lista
    )
  else:
    return render_template(
      'incluir_bo.html',
      usr=usr,
      msg='', 
      lista=[]
    )