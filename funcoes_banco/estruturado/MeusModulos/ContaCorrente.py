from . import Clientes

class LimiteCreditoExcedidoException(Exception):
    pass #nao precisa fazer nada nessa classe, ela ja define a excessao nova

#crie aqui uma nova excessao LimiteTransferenciaExcedidoException

def credito(valor, cliente, limite_credito, limite_transferencia):
    cliente['saldo'] = valor + cliente['saldo']

def debito(valor, cliente, limite_credito, limite_transferencia):
    saque_max = cliente['saldo']+limite_credito
    if valor > saque_max:
        raise LimiteCreditoExcedidoException
    cliente['saldo'] = cliente['saldo'] - valor
    
def transferencia(lista_clientes,id_cliente_doador,id_cliente_receptor,valor,limite_credito,limite_transferencia):
    Clientes.minhafuncao()
    pass

