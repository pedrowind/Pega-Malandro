from src.server.servidor import SQL

class Action_Tst:
  def __init__(self):
    self.mysql = SQL()

  def incluir_tst(
    self,
    nme_tst=None,
    cpf_tst=None,
    rg_tst=None,
    tel_tst=None,
    cel_tst=None,
    eml_tst=None,
    end_tst=None,
    com_tst=None,
    set_tst=None,
    cid_tst=None,
    uf_tst=None,
    cep_tst=None,
    psr_tst=None,
    sxo_tst=None,
    rca_tst=None,
    dta_nsc_tst=None,
    org_tst=None,
    nme_pai_tst=None,
    nme_mae_tst=None
  ):
    cmd = '''
      INSERT INTO tb_tst(
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
      VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
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
      ]
    )

    if ret > 0:
      return ret
    else:
      return 'Erro ao Criar Testemunha!'
    
  def listar_tsts(self):
    cmd = '''
      SELECT
        idt_tst,
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
      FROM tb_tst
      WHERE deleted_at IS NULL;
    '''
    return self.mysql.get_list(cmd, [])

  def alterar_tst(
    self,
    idt_tst,
    nme_tst=None,
    cpf_tst=None,
    rg_tst=None,
    tel_tst=None,
    cel_tst=None,
    eml_tst=None,
    end_tst=None,
    com_tst=None,
    set_tst=None,
    cid_tst=None,
    uf_tst=None,
    cep_tst=None,
    psr_tst=None,
    sxo_tst=None,
    rca_tst=None,
    dta_nsc_tst=None,
    org_tst=None,
    nme_pai_tst=None,
    nme_mae_tst=None
  ):
    cmd = '''
      UPDATE tb_bo
      SET
        nme_tst = %s,
        cpf_tst = %s,
        rg_tst = %s,
        tel_tst = %s,
        cel_tst = %s,
        eml_tst = %s,
        end_tst = %s,
        com_tst = %s,
        set_tst = %s,
        cid_tst = %s,
        uf_tst = %s,
        cep_tst = %s,
        psr_tst = %s,
        sxo_tst = %s,
        rca_tst = %s,
        dta_nsc_tst = %s,
        org_tst = %s,
        nme_pai_tst = %s,
        nme_mae_tst = %s
      WHERE
        idt_tst = %s AND
        deleted_at IS NULL;
    '''
    ret = self.mysql.upd_del(
      cmd,
      [
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
        nme_mae_tst,
        idt_tst
      ]
    )

    if ret > 0:
      return 'Testemunha Alterado com Sucesso!'
    else:
      return 'Nada a Alterar ou Erro ao Tentar Alterar a Testemunha!'

  def excluir_tst(self, idt_tst):
    cmd = '''
      UPDATE tb_tst
      SET deleted_at = NOW()
      WHERE idt_tst = %s AND;
    '''
    ret = self.mysql.upd_del(cmd, [idt_tst])

    if ret > 0:
      return 'Testemunha Excluída com Sucesso!'
    else:
      return 'Nada a Excluir ou Erro ao Tentar Excluir a Testemunha!'