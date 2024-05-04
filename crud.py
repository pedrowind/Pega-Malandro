from flask import Flask, render_template,request
from sql.banco import SQL

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')


if __name__ == '__main__':
   app.run(debug=1)

@app.route('/inc_form')
def inc_form():
   return render_template('inc_form.html')


@app.route('/inclusao', methods=['POST'])
def inclusao():
   # Pegando os dados do formulário
   nome = request.form['nme_cliente']
   data = request.form['dta_nasc_cliente']
   # Rodando comando SQL
   sql = SQL()
   cmd = 'INSERT INTO tb_cliente(nme_cliente, dta_nasc_cliente) VALUES (%s, %s)'
   idt = sql.insert(cmd, [nome, data])


   return render_template('inclusao.html', idt=idt)


@app.route('/consulta')
def consulta():
   # Rodando comando SQL
   sql = SQL()
   cmd = 'SELECT * FROM tb_cliente ORDER BY nme_cliente'
   lista = sql.get_list(cmd)


   return render_template('consulta.html', lista=lista)
