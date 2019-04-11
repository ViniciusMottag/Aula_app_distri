lista=[{'id':20,nome:"Mario"}]

def consulta_aluno_por_id(id_recebido):
	tamanho=len(database)
	for valor in range(tamanho):
		comparacao=database[valor]['id']
		if comparacao == id_recebido:
			return jsonify(database[valor]['id'])
		else:
			pass

    return 'Nao encontrado'

print(consulta_aluno_por_id(20))