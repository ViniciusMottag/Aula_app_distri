from flask import Flask,request,jsonify


app = Flask(__name__) 

database={}
database['ALUNO']=[]
database['PROFESSOR']=[]
database['DISCIPLINA']=[]

@app.route("/") 
def all():
        return jsonify(database)

@app.route('/alunos', methods=['GET'])
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores', methods=['GET'])
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/disciplinas',methods=['GET'])
def disciplina():
	return jsonify(database['DISCIPLINA'])

#na url /alunos
#com verbo post
@app.route("/alunos",methods=['POST'])
def adiciona_aluno():
	#vou receber um dicionario via json
	dici=request.json
	#e colocar na lista
	tamanho=len(database['ALUNO'])
	for id_busca in range(tamanho):
		if dici['id'] == database['ALUNO'][id_busca]['id']:
			dic_erro = {'erro': 'id ja utilizada'}
			return jsonify(dic_erro), 400
	if 'nome' not in dici:
		dic_erro = {'erro': 'aluno sem nome'}
		return jsonify(dic_erro), 400
	database['ALUNO'].append(dici)
	return jsonify(database['ALUNO'])

@app.route("/alunos",methods=['GET'])
def retorna_alunos():
	return jsonify(database['ALUNO'])

@app.route("/alunos/<int:id_recebido>",methods=['GET'])
def consulta_aluno_por_id(id_recebido):
	for id_busca in database['ALUNO']:
		if id_busca['id'] == id_recebido:
			return jsonify(id_busca)
	dic_erro = {'erro': 'aluno nao encontrado'}
	return jsonify(dic_erro), 400

@app.route("/reseta",methods=['POST'])
def reseta_lista():
	database['ALUNO']=[]
	database['PROFESSOR']=[]
	database['DISCIPLINA']=[]
	return jsonify(database)

@app.route("/alunos/<int:id_recebido>",methods=['DELETE'])
def deleta_aluno(id_recebido):
	tamanho=len(database['ALUNO'])
	for id_busca in range(tamanho):
		if database['ALUNO'][id_busca]['id'] == id_recebido:
			del database['ALUNO'][id_busca]
			return jsonify(database['ALUNO'])
	dic_erro = {'erro': 'aluno nao encontrado'}
	return jsonify(dic_erro), 400

@app.route('/alunos/<int:id_recebido>', methods=['PUT'])
def edita_aluno(id_recebido):
	dici = request.json
	lenght_alunos = len(database['ALUNO'])
	for aluno in range(lenght_alunos):
		if 'nome' not in dici:
			dic_erro = {'erro': 'aluno sem nome'}
			return jsonify(dic_erro), 400

		elif database['ALUNO'][aluno]['id'] == id_recebido:
			novo_nome = dici['nome']
			database['ALUNO'][aluno]['nome'] = novo_nome
			return 'ID aluno alterado: {}'.format(id_recebido)
	
	dic_erro = {'erro': 'aluno nao encontrado'}
	return jsonify(dic_erro), 400

#PROFESSORES COMEÇA AQUI
@app.route("/professores",methods=['POST'])
def adiciona_prof():
	#vou receber um dicionario via json
	dici=request.json
	#e colocar na lista
	tamanho=len(database['PROFESSOR'])
	for id_busca in range(tamanho):
		if dici['id'] == database['PROFESSOR'][id_busca]['id']:
			dic_erro = {'erro': 'id ja utilizada'}
			return jsonify(dic_erro), 400
	if 'nome' not in dici:
		dic_erro = {'erro': 'professor sem nome'}
		return jsonify(dic_erro), 400
	database['PROFESSOR'].append(dici)
	return jsonify(database['PROFESSOR'])
	
@app.route("/professores/<int:id_recebido>",methods=['GET'])
def consulta_prof_por_id(id_recebido):
	for id_busca in database['PROFESSOR']:
		if id_busca['id'] == id_recebido:
			return jsonify(id_busca)
	dic_erro = {'erro': 'professor nao encontrado'}
	return jsonify(dic_erro), 400

@app.route("/professores/<int:id_recebido>",methods=['DELETE'])
def deleta_prof(id_recebido):
	tamanho=len(database['PROFESSOR'])
	for id_busca in range(tamanho):
		if database['PROFESSOR'][id_busca]['id'] == id_recebido:
			del database['PROFESSOR'][id_busca]
			return jsonify(database['PROFESSOR'])
	dic_erro = {'erro': 'professor nao encontrado'}
	return jsonify(dic_erro), 400

@app.route('/professores/<int:id_recebido>', methods=['PUT'])
def edita_prof(id_recebido):
	dici = request.json
	lenght_alunos = len(database['PROFESSOR'])
	for aluno in range(lenght_alunos):
		if 'nome' not in dici:
			dic_erro = {'erro': 'professor sem nome'}
			return jsonify(dic_erro), 400

		elif database['PROFESSOR'][aluno]['id'] == id_recebido:
			novo_nome = dici['nome']
			database['PROFESSOR'][aluno]['nome'] = novo_nome
			return 'ID professor alterado: {}'.format(id_recebido)
	
	dic_erro = {'erro': 'professor nao encontrado'}
	return jsonify(dic_erro), 400

#INCLUSÃO AJUSTES E CONSULTA COMEÇA AQUI DE DISCIPLINA
@app.route("/disciplinas",methods=['POST'])
def adiciona_disciplina():
	#vou receber um dicionario via json
	dici=request.json
	#e colocar na lista
	tamanho=len(database['DISCIPLINA'])

	lista_campos = ["carga_horaria","id","nome","plano_ensino","status"]
	
	
	if dici not in lista_campos:
		dic_erro = {'erro': 'campo não encontrado'}
		return jsonify(dic_erro), 400

	for id_busca in range(tamanho):
		if dici['id'] == database['DISCIPLINA'][id_busca]['id']:
			dic_erro = {'erro': 'id ja utilizada'}
			return jsonify(dic_erro), 400
	if 'nome' not in dici:
		dic_erro = {'erro': 'Disciplina sem nome'}
		return jsonify(dic_erro), 400
	database['DISCIPLINA'].append(dici)
	return jsonify(database['DISCIPLINA'])

@app.route("/disciplinas/<int:id_recebido>",methods=['GET'])
def consulta_disci_por_id(id_recebido):
	for id_busca in database['DISCIPLINA']:
		if id_busca['id'] == id_recebido:
			return jsonify(id_busca)
	dic_erro = {'erro': 'disciplina nao encontrada'}
	return jsonify(dic_erro), 400

@app.route("/disciplinas/<int:id_recebido>",methods=['DELETE'])
def deleta_disc(id_recebido):
	tamanho=len(database['DISCIPLINA'])
	for id_busca in range(tamanho):
		if database['DISCIPLINA'][id_busca]['id'] == id_recebido:
			del database['DISCIPLINA'][id_busca]
			return jsonify(database['DISCIPLINA'])
	dic_erro = {'erro': 'disciplina nao encontrada'}
	return jsonify(dic_erro), 400

@app.route('/disciplinas/<int:id_recebido>', methods=['PUT'])
def edita_disc(id_recebido):
	dici = request.json
	lenght_disc = len(database['DISCIPLINA'])
	for disciplina in range(lenght_disc):
		if 'nome' not in dici:
			dic_erro = {'erro': 'disciplina sem nome'}
			return jsonify(dic_erro), 400

		elif database['DISCIPLINA'][disciplina]['id'] == id_recebido:
			novo_nome = dici['nome']
			database['DISCIPLINA'][disciplina]['nome'] = novo_nome
			return 'ID disciplina alterado: {}'.format(id_recebido)
	
	dic_erro = {'erro': 'disciplina nao encontrada'}
	return jsonify(dic_erro), 400




@app.route("/") 
def hello(): 
	return "Hello World!"




if __name__ == '__main__':
    	app.run(host='localhost', port=5002, debug=True) 
