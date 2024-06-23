from src.server.servidor import SQL

class Action_Bo_Tst:
  def __init__(self):
    self.mysql = SQL()
  
  def vincular_bo_tst(self, fk_bo, fk_tst):
    cmd = '''
      INSERT INTO tba_bo_tst(
        idt_bo,
        idt_tst
      )
      VALUES (
        %s,
        %s
      );
    '''
    ret = self.mysql.insert(
      cmd,
      [
        fk_bo,
        fk_tst
      ]
    )

    if ret > 0:
      return ret
    else:
      return None