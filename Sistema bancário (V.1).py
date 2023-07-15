MENU = '''
Escolha uma dentre as opções a seguir: \n
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair da conta
'''

SEPARACOES = 5*'======================'

saldo_atual = 0
saques_atuais = 0
MÁXIMO_SAQUES = 3
LIMITE_SAQUE = 500
operacoes_realizadas = []
OPCOES = ['D', 'S', 'E', 'Q']
                    
while True:
    print(f'{SEPARACOES}')
    opcao = input(f'{MENU}\n-> ').upper()
    if opcao not in OPCOES:
        print('\nOpção inválida. Tente novamente...')
    elif opcao == 'E':
        if len(operacoes_realizadas) == 0:
            print('\nNão foram realizadas movimentações.')
        else:
            print('\nSegue o extrato da conta: \n')
            for operacao in operacoes_realizadas:
                print(operacao)
            print(f'\nO saldo atual da conta é de R${saldo_atual:.2f}.')
    elif opcao == 'Q':
        break
    elif opcao == 'D':
        valor = float(input('\nInsira o valor a ser depositado: '))
        if valor > 0:
            operacoes_realizadas.append(f'+ R${valor:.2f};')
            saldo_atual += valor
        else:
            print('\nInsira um valor válido.')
    else:
        if saques_atuais < MÁXIMO_SAQUES:
            valor = float(input('\nInsira o valor a ser sacado: '))
            if valor <= LIMITE_SAQUE:
                if valor > 0:
                    if valor <= saldo_atual:
                        operacoes_realizadas.append(f'- R${valor:.2f};')
                        saldo_atual -= valor
                        saques_atuais += 1
                    else:
                        print(f'\nSaldo insuficiente. Atualmente o valor disponível é de R${saldo_atual:.2f}.')
                else:
                    print('\nInsira um valor válido.')
            else:
                print('\nO valor solicitado é maior do que o limite permitido por operação. Tente novamente.')
        else:
            print('\nLimite diário de saques atingido. Tente novamente no dia seguinte.')
    print(f'{SEPARACOES}')

print('\nSessão encerrada. Volte sempre!')
print(f'{SEPARACOES}')
