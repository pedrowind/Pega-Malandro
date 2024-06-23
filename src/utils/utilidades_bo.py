from src.server.servidor import SQL

class Action_Bo:
  def __init__(self):
    self.mysql = SQL()

  def incluir_bo(
    self, 
    dta_ini_bo, 
    dta_fim_bo, 
    uf_bo, 
    cid_bo, 
    set_bo, 
    qua_bo, 
    com_bo, 
    dsc_bo, 
    fk_bo_usr
  ):
    cmd = '''
      INSERT INTO tb_bo(
        dta_ini_bo, 
        dta_fim_bo, 
        uf_bo, 
        cid_bo, 
        set_bo, 
        qua_bo, 
        com_bo, 
        dsc_bo, 
        idt_usr
      )
      VALUES (
        %s,
        %s, 
        %s, 
        %s, 
        %s, 
        %s, 
        %s, 
        %s, 
        %s
      );
    '''
    ret = self.mysql.insert(
      cmd, 
      [
        dta_ini_bo, 
        dta_fim_bo, 
        uf_bo, 
        cid_bo, 
        set_bo, 
        qua_bo, 
        com_bo, 
        dsc_bo, 
        fk_bo_usr
      ]
    )

    if ret > 0:
      return ret
    else:
      return 'Erro ao Criar B.O!'

  def alterar_bo(
    self, 
    idt_bo, 
    dta_ini_bo=None, 
    dta_fim_bo=None, 
    uf_bo=None, 
    cid_bo=None, 
    set_bo=None, 
    qua_bo=None, 
    com_bo=None, 
    dsc_bo=None, 
    fk_bo_usr=None
  ):
    cmd = '''
      UPDATE tb_bo
      SET
        dta_ini_bo = %s,
        dta_fim_bo = %s,
        uf_bo = %s,
        cid_bo = %s,
        set_bo = %s,
        qua_bo = %s,
        com_bo = %s,
        dsc_bo = %s,
        idt_usr = %s
      WHERE
        idt_bo = %s AND
        deleted_at IS NULL;
    '''
    ret = self.mysql.upd_del(
      cmd, 
      [
        dta_ini_bo, 
        dta_fim_bo, 
        uf_bo, 
        cid_bo, 
        set_bo, 
        qua_bo, 
        com_bo, 
        dsc_bo, 
        fk_bo_usr, 
        idt_bo
      ]
    )

    if ret > 0:
      return 'B.O Alterado com Sucesso!'
    else:
      return 'Nada a Alterar ou Erro ao Tentar Alterar o B.O!'

  def excluir_bo(self, idt_bo):
    cmd = '''
      UPDATE tb_bo
      SET deleted_at = NOW()
      WHERE idt_bo = %s AND;
    '''
    ret = self.mysql.upd_del(
      cmd, 
      [idt_bo]
    )

    if ret > 0:
      return 'B.O Excluído com Sucesso!'
    else:
      return 'Nada a Excluir ou Erro ao Tentar Excluir o B.O!'

  def listar_bos(
    self, 
    dta_ini_bo, 
    dta_fim_bo
  ):
    cmd = '''
      SELECT
        idt_bo,
        dta_ini_bo,
        dta_fim_bo,
        uf_bo,
        cid_bo,
        set_bo,
        qua_bo,
        com_bo,
        dsc_bo,
        idt_usr
      FROM tb_bo
      WHERE
        dta_ini_bo BETWEEN %s AND
        %s AND
        deleted_at IS NULL;
    '''
    return self.mysql.get_list(
      cmd, 
      [
        dta_ini_bo, 
        dta_fim_bo
      ]
    )
  
  def listar_bos_by_usuario(
    self, 
    idt_usr
  ):
    cmd = '''
      SELECT
        idt_bo,
        dta_ini_bo,
        dta_fim_bo,
        uf_bo,
        cid_bo,
        set_bo,
        qua_bo,
        com_bo,
        dsc_bo,
        idt_usr
      FROM tb_bo
      WHERE
        idt_usr = %s AND
        deleted_at IS NULL;
    '''
    return self.mysql.get_list(
      cmd, [idt_usr]
    )