def saque(saldo_atual, valor, extrato, limite_saque, saques_realizados, máximo_saques):
    if saques_realizados >= máximo_saques:
        print('\nOperação encerrada! O número permitido de saques diários foi atingido.')
    elif valor > limite_saque:
        print('\nOperação encerrada! O valor solicitado é maior que o limite por saque.')
    elif valor > saldo_atual:
        print('\nOperação encerrada! O saldo é insuficiente.')
    elif valor > 0:
        saldo_atual -= valor
        saques_realizados += 1
        extrato.append(f'-R${valor:.2f}')
        print(f'\nSaque de R${valor:.2f} realizado!')
    else:
        print('\nOperação encerrada! Insira um valor válido.')
    return (saldo_atual, extrato, saques_realizados)

def deposito(saldo_atual, valor, extrato):
    if valor > 0:
        saldo_atual += valor
        extrato.append(f'+ R${valor:.2f}')
        print(f'\nDepósito de R${valor:.2f} realizado!')
    else:
        print('\nOperação encerrada! Insira um valor válido.')
    return (saldo_atual, extrato)

def emitir_extrato(saldo_atual, extrato):
    if len(extrato) == 0:
        print('\nNão foram realizadas movimentações nesta conta.')
    else:
        print('\nSegue o extrato da conta: \n')
        for operacao in extrato:
            print(operacao)
        print(f'\nO saldo atual da conta é de R${saldo_atual:.2f}.')

def novo_usuario(usuarios_cadastrados):
    cpf = input('\nInforme o CPF do novo usuário: ').replace('-', '').replace('.', '')
    if len(cpf)!= 11:
        print('\nInsira um CPF válido!')
    elif cpf in usuarios_cadastrados:
        print('\nOperação encerrada! Já existe um usuário cadastrado com o CPF informado.')
    else:
        nome = input('\nInforme o nome completo do usuário: ')
        data_nascimento = input('\nInforme a data de nascimento do usuário (dd/mm/aaaa): ')
        endereco = input('\nInforme o endereço do usuário (logradouro, número - bairro - cidade/sigla do estado): ')
        usuarios_cadastrados[cpf] = {'nome':nome, 'data_nascimento':data_nascimento, 'endereco':endereco}
        print('\nUsuário cadastrado com sucesso!')
    return (usuarios_cadastrados)

def nova_conta(agencia, numero_conta, usuarios_cadastrados, contas_cadastradas):
    cpf = input('\nInforme o CPF do novo usuário: ').replace('-', '').replace('.', '')
    if len(cpf)!= 11:
        print('\nInsira um CPF válido!')
    elif cpf not in usuarios_cadastrados:
        print('\nOperação encerrada! Não existe um usuário cadastrado com o CPF informado.')
    else:
        contas_cadastradas[numero_conta] = {'agencia':agencia, 'usuario':usuarios_cadastrados[cpf]['nome']}
        print('\nConta criada com sucesso!')
    return (contas_cadastradas)

def exibir_contas(contas_cadastradas):
    if len(contas_cadastradas) == 0:
        print('\nNão existem contas cadastradas.')
    else:
        for conta in contas_cadastradas:
            print(f'''
    Agência: {contas_cadastradas[conta]['agencia']}
    Conta: {conta}
    Titular: {contas_cadastradas[conta]['usuario']}
            ''')

def main():
    MENU = '''Escolha uma dentre as opções a seguir:
    
    [DP] Depósito
    [SQ] Saque
    [EX] Extrato
    [NU] Novo usuário
    [NC] Nova conta
    [EC] Exibir contas
    [QT] Sair da conta
    '''
    
    SEPARACOES = 5*'======================'
    saldo_atual = 0
    AGENCIA = '0001'
    MÁXIMO_SAQUES = 3
    LIMITE_SAQUE = 500
    saques_realizados = 0
    contas_cadastradas = {}
    operacoes_realizadas = []
    usuarios_cadastrados = {}
    OPCOES = ['DP', 'SQ', 'EX', 'NU', 'NC', 'EC', 'QT']
                        
    while True:
        print(f'{SEPARACOES}')
        opcao = input(f'{MENU}\n-> ').upper()
        if opcao not in OPCOES:
            print('\nOpção inválida. Tente novamente.')
        elif opcao == 'EX':
            emitir_extrato(saldo_atual, extrato = operacoes_realizadas)
        elif opcao == 'QT':
            break
        elif opcao == 'DP':
            valor = float(input('Informe o valor a ser depositado: '))
            saldo_atual, operacoes_realizadas = deposito(saldo_atual, valor, operacoes_realizadas)
        elif opcao == 'SQ':
            valor = float(input('Informe o valor a ser sacado: '))
            saldo_atual, operacoes_realizadas, saques_realizados = saque(
                saldo_atual = saldo_atual,
                valor = valor,
                extrato = operacoes_realizadas,
                limite_saque = LIMITE_SAQUE,
                saques_realizados = saques_realizados,
                máximo_saques = MÁXIMO_SAQUES
                )
        elif opcao == 'NU':
            usuarios_cadastrados = novo_usuario(usuarios_cadastrados = usuarios_cadastrados)
        elif opcao == 'NC':
            contas_cadastradas = nova_conta(
                agencia = AGENCIA,
                numero_conta = str(len(list(contas_cadastradas)) + 1),
                usuarios_cadastrados = usuarios_cadastrados,
                contas_cadastradas = contas_cadastradas)
        else:
            exibir_contas(contas_cadastradas = contas_cadastradas)
    print('\nSessão encerrada. Volte sempre!')
    print(f'{SEPARACOES}')
main()
