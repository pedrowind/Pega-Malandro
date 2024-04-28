from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route('/bemvindo')
def bemvindo():
  return render_template('bemvindo.html')

@app.route('/hora')
def hora():
   dh = datetime.now()
   saida_dh = dh.isoformat(" ", timespec='seconds')
   hora = dh.hour
   cumprimento = "Bom dia"
   if hora > 11 and hora < 19:
       cumprimento = "Boa tarde"
   elif hora > 18 and hora < 24:
       cumprimento = "Boa noite"

   return render_template('hora.html', data_hora=saida_dh, cumprimento=cumprimento)

@app.route('/tabuada')
def tabuada():
   tab = ""
   for num in range(11):
       tab += "<TR><TD>"
       tab += "7 x " + str(num) + " = " + str(7 * num)
       tab += "</TD></TR>\n"

   return render_template('tabuada.html', tab=tab)

@app.route('/tabpar', methods=['GET'])
def tabpar():
   valor = int(request.args.get('valor'))
   tab = ""
   for num in range(11):
       tab += "<TR><TD>"
       tab += str(valor) + " x " + str(num) + " = " + str(valor * num)
       tab += "</TD></TR>\n"

   return render_template('tabpar.html', val=valor, tab=tab)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/nomes', methods=['POST'])
def nome():
   # Recuperando dados do formulário de index()
   n=request.form['nome']
   v=int(request.form['vezes'])

   h = str(datetime.now())

   rep=""
   for i in range(v):
       rep+="<p>" + n + "</p>\n"

   return render_template('nomes.html', hoje=h, rep=rep)

if __name__ == '__main__':
	app.run(debug=1)
