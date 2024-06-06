import mysql.connector


class Repositorio:
    def __init__(self, servidor='localhost', usuario='root', senha='ceub123456', banco_dados='pega_malandro'):
        self.conexao = mysql.connector.connect(host=servidor, user=usuario, password=senha, database=banco_dados)

    def inserir(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        self.conexao.commit()
        identificador = cursor.lastrowid

        cursor.close()
        return identificador

    def atualizar_deletar(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        self.conexao.commit()
        numero_linhas = cursor.rowcount

        cursor.close()
        return numero_linhas

    def pegar_cursor(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        return cursor

    def pegar_inteiro(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        resultado = int(cursor.fetchone()[0])

        cursor.close()
        return resultado

    def pegar_real(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        resultado = float(cursor.fetchone()[0])

        cursor.close()
        return resultado

    def pegar_data(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        data = cursor.fetchone()[0]
        resultado = str(data.day).zfill(2) + "/" + str(data.month).zfill(2) + "/" + str(data.year)

        cursor.close()
        return resultado

    def pegar_horario(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        hora = cursor.fetchone()[0]
        total_segundos = hora.total_seconds()
        horas = int(total_segundos // 3600)
        minutos = int((total_segundos % 3600) // 60)
        segundos = int(total_segundos % 60)
        resultado = f"{horas:02}:{minutos:02}:{segundos:02}"

        cursor.close()
        return resultado

    def pegar_texto(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        resultado = str(cursor.fetchone()[0])

        cursor.close()
        return resultado

    def pegar_dicionario(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)

        dados = cursor.fetchone()
        if dados is None:
            dicionario = None
        else:
            descricao_coluna = cursor.description
            dicionario = {
                coluna[0]: valor for coluna,
                valor in zip(descricao_coluna, dados)
            }

        cursor.close()
        return dicionario

    def pegar_lista(self, comando, parametros):
        cursor = self.conexao.cursor()
        cursor.execute(comando, parametros)
        descricao_coluna = cursor.description

        lista = []
        for registro in cursor:
            dicionario = {
                coluna[0]: valor for coluna,
                valor in zip(descricao_coluna, registro)
            }
            lista.append(dicionario)

        cursor.close()
        return lista
