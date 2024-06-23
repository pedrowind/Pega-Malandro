from src.server.servidor import SQL
import random
import string

class Action_Login:
  def __init__(self):
    self.mysql = SQL()

  def login(self, usr, pwd):
    cmd = '''
      SELECT *
      FROM tb_usr
      WHERE 
        nme_usr = %s AND
        pwd_usr = SHA(%s) AND
        deleted_at IS NULL;
    '''
    obj = self.mysql.get_object(cmd, [usr, pwd])

    return obj

  def alterar_senha(self, idt_usr, senha_atual, nova_senha, confirmacao_senha_nova):
    cmd = '''
      SELECT COUNT(idt_usr) AS qtd
      FROM tb_usr
      WHERE
        idt_usr = %s AND
        pwd_usr = SHA(%s) AND
        deleted_at IS NULL;
    '''
    num = self.mysql.get_int(cmd, [idt_usr, senha_atual])

    if num == 1:
      if nova_senha == confirmacao_senha_nova:
        cmd = '''
          UPDATE tb_usr
          SET pwd_usr = SHA(%s)
          WHERE
            idt_usr = %s AND
            deleted_at IS NULL;
        '''
        ret = self.mysql.upd_del(cmd, [nova_senha, idt_usr])

        if ret == 1:
          return 'Senha Alterada com Sucesso!'
        else:
          return 'Erro ao Tentar Mudar a Senha!'
      else:
        return 'A Senha Nova e Confirmação Não São Iguais!'
    else:
      return 'A Senha Atual Está Errada!'

  def resetar_senha(self, nme_usr):
    caracteres = string.ascii_letters + string.digits
    senha = ''

    for i in range(8):
      senha += random.choice(caracteres)

    cmd = '''
      UPDATE tb_usr
      SET pwd_usr = SHA(%s)
      WHERE
        nme_usr = %s AND
        deleted_at IS NULL AND
        pfl_usr != 'A' AND
        pfl_usr != 'P';
    '''
    ret = self.mysql.upd_del(cmd, [senha, nme_usr])

    if ret == 1:
      return senha
    else:
      return 0
  
  def incluir_usuario(self, nme_usr, eml_usr, pwd_usr, pfl_usr):
    cmd = '''
      INSERT INTO tb_usr(nme_usr, eml_usr, pwd_usr, pfl_usr)
      VALUES (%s, %s, SHA(%s), %s);
    '''
    ret = self.mysql.insert(cmd, [nme_usr,eml_usr, pwd_usr, pfl_usr])

    if ret > 0:
      return (ret, pwd_usr)
    else:
      return 'Erro ao Tentar Inserir Usuário!'
    
  def cadastrar(self, nme_usr, eml_usr, pwd_usr):
    cmd = '''
      INSERT INTO tb_usr(nme_usr, eml_usr, pwd_usr, pfl_usr)
      VALUES (%s, %s, SHA(%s), 'C');
    '''
    ret = self.mysql.insert(cmd, [nme_usr,eml_usr, pwd_usr])

    if ret > 0:
      return (ret, pwd_usr)
    else:
      return 'Erro ao Tentar Inserir Usuário!'

  def listar_usuarios(self, nme_usr, pfl_usr):
    cmd = '''
      SELECT *
      FROM tb_usr
      WHERE
        nme_usr LIKE CONCAT('%', %s, '%') AND (
          pfl_usr = %s OR
          %s = 'T'
        ) AND
        deleted_at IS NULL
      ORDER BY nme_usr ASC;
    '''
    lista = self.mysql.get_list(cmd, [nme_usr, pfl_usr, pfl_usr])

    return lista

  def get_usuario(self, idt_usr):
    cmd = '''
      SELECT *
      FROM tb_usr
      WHERE
        idt_usr = %s AND
        deleted_at IS NULL;
    '''
    obj = self.mysql.get_object(cmd, [idt_usr])

    return obj

  def alterar_usuario(self, idt_usr, nme_usr, eml_usr, pwd_usr, pfl_usr):
    cmd = '''
      UPDATE tb_usr
      SET
        nme_usr = %s,
        eml_usr = %s,
        pwd_usr = SHA(%s),
        pfl_usr = %s
      WHERE
        idt_usr = %s AND
        deleted_at IS NULL;
    '''
    ret = self.mysql.upd_del(cmd, [nme_usr, eml_usr, pwd_usr, pfl_usr, idt_usr])

    if ret > 0:
      return 'Usuário Alterado com Sucesso!'
    else:
      return 'Nada a Alterar ou Erro ao Tentar Alterar o Usuário!'
    
  def excluir_usuario(self, idt_usr):
    cmd = '''
      UPDATE tb_usr
      SET deleted_at = NOW()
      WHERE
        idt_usr = %s AND
        deleted_at IS NULL;
    '''
    ret = self.mysql.upd_del(cmd, [idt_usr])

    if ret > 0:
      return 'Usuário Deletado com Sucesso!'
    else:
      return 'Nada a Deletar ou Erro ao Tentar Deletar o Usuário!'