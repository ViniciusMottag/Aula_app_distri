from flask import Flask,request,jsonify


app = Flask(__name__) 

database={}
database['ALUNO']=[]

#na url /alunos
#com verbo post
@app.route("/alunos",methods=['POST'])
def adiciona_aluno():
	#vou receber um dicionario via json
	dici=request.json
	#e colocar na lista
	database['ALUNO'].append(dici)
	return jsonify(database['ALUNO'])

@app.route("/alunos",methods=['GET'])
def retorna_alunos():
	return jsonify(database['ALUNO'])

@app.route("/alunos/<int:id_recebido>",methods=['GET'])
def consulta_aluno_por_id(id_recebido):
	tamanho=len(database)
	for valor in range(tamanho):
		comparacao=database['id']
		if comparacao == id_recebido:
			return jsonify(database['id'])
		else:
			pass


@app.route("/") 
def hello(): 
	return "Hello World!"




if __name__ == '__main__':
    	app.run(host='localhost', port=5002, debug=True) 