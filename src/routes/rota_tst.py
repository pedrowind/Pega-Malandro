from src.utils.utilidades_tst import Action_Tst
from src.utils.utilidades_bo_tst import Action_Bo_Tst
from flask import Blueprint, render_template, request, session

mod_tst = Blueprint('mod_tst', __name__)
act_tst = Action_Tst()
act_bo_tst = Action_Bo_Tst()

@mod_tst.route('/incluir_tst', methods=['GET', 'POST'])
def incluir_tst():
  try:
    usr = session['usuario']
  except:
    return render_template(
      'login.html', 
      msg='Não Burle o Sistema!'
    )

  if request.method == 'POST':
    nme_tst = request.form['nme_tst']
    cpf_tst = request.form['cpf_tst']
    rg_tst = request.form['rg_tst']
    tel_tst = request.form['tel_tst']
    cel_tst = request.form['cel_tst']
    eml_tst = request.form['eml_tst']
    end_tst = request.form['end_tst']
    com_tst = request.form['com_tst']
    set_tst = request.form['set_tst']
    cid_tst = request.form['cid_tst']
    uf_tst = request.form['uf_tst']
    cep_tst = request.form['cep_tst']
    psr_tst = request.form['psr_tst']
    sxo_tst = request.form['sxo_tst']
    rca_tst = request.form['rca_tst']
    dta_nsc_tst = request.form['dta_nsc_tst']
    org_tst = request.form['org_tst']
    nme_pai_tst = request.form['nme_pai_tst']
    nme_mae_tst = request.form['nme_mae_tst']

    retorno_tst = act_tst.incluir_tst(
      nme_tst,
      cpf_tst,
      rg_tst,
      tel_tst,
      cel_tst,
      eml_tst, 
      end_tst,
      com_tst,
      set_tst,
      cid_tst,
      uf_tst,
      cep_tst, 
      psr_tst,
      sxo_tst,
      rca_tst,
      dta_nsc_tst,
      org_tst, 
      nme_pai_tst,
      nme_mae_tst
    )

    return render_template(
      'incluir_bo.html', 
      usr=usr,
      msg='Criado o Testemunha com ID: {0}.'.format(retorno_tst)
    )
  else:
    return render_template(
      'incluir_bo.html',
      usr=usr,
      msg=''
    )
  
@mod_tst.route('/listar_tsts', methods=['GET', 'POST'])
def listar_tsts():
  try:
    session['usuario']
  except:
    return render_template(
      'login.html', 
      msg='Não Burle o Sistema!'
    )

  if request.method == 'POST':
    idt_bo = request.form['idt_bo']
    idt_tst = request.form['idt_tst']
    act_bo_tst.vincular_bo_tst(idt_bo, idt_tst)

    return render_template(
      'listar_tsts.html',
      lista_tsts=[],
      msg='Vinculado a Testemunha com ID: {0} ao BO com ID: {1}.'.format(idt_tst, idt_bo)
    )
  else:
    idt_bo = request.args.get('idt_bo')
    lista_tsts = act_tst.listar_tsts()

    return render_template(
      'listar_tsts.html',
      lista_tsts=lista_tsts,
      msg='',
      idt_bo=idt_bo
    )