from src.server.repositorio import Repositorio
import random
import string


class Deposito_Funcoes:
    def __init__(self):
        self.repositorio = Repositorio()

    def login(self, usr, pwd):
        comando = '''
            SELECT *
            FROM tabela_usuario
            WHERE nome_usuario = %s
            AND senha_usuario = SHA(%s);
        '''
        obj = self.repositorio.pegar_dicionario(comando, [usr, pwd])
        return obj

    def alterar_senha(self, identificador_usuario, senha_atual, senha, confirma):
        comando = '''
            SELECT COUNT(identificador_usuario) AS qtd
            FROM tabela_usuario
            WHERE identificador_usuario = %s
            AND senha_usuario = SHA(%s);
        '''
        numero = self.repositorio.pegar_inteiro(comando, [identificador_usuario, senha_atual])

        if numero == 1:
            if senha == confirma:
                comando = '''
                    UPDATE tabela_usuario
                    SET senha_usuario = SHA(%s)
                    WHERE identificador_usuario = %s;
                '''
                retorno = self.repositorio.atualizar_deletar(comando, [senha, identificador_usuario])

                if retorno == 1:
                    return 'Senha Alterada com Sucesso!'
                else:
                    return 'Erro ao Tentar Mudar a Senha!'
            else:
                return 'A Senha Nova e a Confirmação Não São Iguais!'
        else:
            return 'A Senha Atual Está Errada!'


    def resetar_senha(self, nome_usuario):
        caracteres = string.ascii_letters + string.digits

        senha = ''
        for i in range(8):
            senha += random.choice(caracteres)

        comando = '''
            UPDATE tabela_usuario
            SET senha_usuario = SHA(%s)
            WHERE nome_usuario = %s;
        '''
        retorno = self.repositorio.atualizar_deletar(comando, [senha, nome_usuario])
    
        if retorno == 1:
            return senha
        else:
            return 'Erro ao Tentar Mudar a Senha!'
