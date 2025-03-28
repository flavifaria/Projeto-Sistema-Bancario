#print("**********Menu**********")
#print("Criar Usuário")
#print("Depositar")
#print("Sacar")

saldo = 0
numero_saques = 0
limites_saques = 3
usuarios =[]#criei uma lista vazia , pois serão adicionados valores posteriormente
contas = []
agencia='0001'


def menu():
    print('''
        **********Menu**********
        (1) Criar Usuário
        (2) Criar Conta
        (3) Listar Contas
        (d) Depositar
        (s) Sacar
        (e) Extrato
        (q) Sair
    ''')
    return input('Qual opção deseja')

def deposito(valor,saldo):
    #  vou receber o valor do depósito e somar ao saldo
    if valor > 0 :
        saldo += valor
        #print mostrando o valor depositado
        print(f'Você depositou R${valor}')      
    else:
        print('Valor do deposito Ínválido.Verifique a quantia digitada.')
    
    return saldo

    