
reviews_aquecimento = [
    {
        'film_id': 'tt0076759',
        'user_id': 'marcos',
        'comment': 'gostei'
    },
    {
        'film_id': 'tt0076759',
        'user_id': 'lucio',
        'comment': 'achei legal'
    },
    {
        'film_id': 'tt1211837',
        'user_id': 'lucio',
        'comment': 'estranho'
    }
]

'''
A proxima atividade vai ter tudo a ver com essa
estrutura acima.

A idéia é que ela representa uma lista
de avaliacoes que os usuarios fizeram,
dando sua opiniao sobre alguns filmes.

Cada avaliacao está representada
como um dicionario com 3 chaves
'''

'''
primeiramente, façamos uma funcao
consulta que, dados o film_id e o user_id
devolve o dicionario da avaliacao
'''

def consulta(film_id,user_id):
    tamanho=(len(reviews_aquecimento))
    for valor in range(tamanho):
        dic_de_consulta=reviews_aquecimento[valor]
        if film_id == dic_de_consulta['film_id'] and user_id ==dic_de_consulta['user_id']:
            return reviews_aquecimento[valor]
        else:
            pass
    return 'nao encontrado'
'''
Agora, façamos uma funcao que adiciona uma nova avaliacao
'''

def adiciona(film_id,user_id,comment):
    '''
    tamanho=(len(reviews_aquecimento))
    for valor in range(tamanho):
        dic_de_consulta=reviews_aquecimento[valor]
        if film_id == dic_de_consulta['film_id'] and user_id ==dic_de_consulta['user_id']:
            reviews_aquecimento.pop(valor)
        else:
            pass
    return reviews_aquecimento.append({'film_id':film_id,'user_id':user_id,'comment':comment})
    '''
    consultado=consulta.(film_id,user_id)
    if consultado='nao encontrado':
        nova_av={}
        nova_av['film_id'] = film_id
        nova_av['user_id'] = user_id
        nova_av['comment'] = comment
        reviews_aquecimento.append(nova_av)
    else:
        consultado['comment']=comment

        

'''
Agora, façamos um upgrade na adiciona:
    se o usuario ja avaliou esse filme,
    ao inves de adicionar uma nova avaliacao,
    mudamos a avaliacao existente.
'''
