menu = """

(d) Depositar
(s) Sacar
(e) Extrato
(q) Sair

==>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")
            print(f"Saldo atual: R${saldo:.2f}\n")
        else:
            print("Operação falhou!! Informe um valor válido.")
        
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))
        
        excedeu_saldo = valor > saldo
        
        exedeu_limite = valor > limite
        
        exedeu_saques = numero_saques > LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou!! Saldo Insuficiente.")
            
        elif exedeu_limite:
            print("Operação falhou!! Limite por Saque é de R$ 500,00")
        
        elif exedeu_saques:
            print("Operação falhou!! Limite de saques exedidos!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso!")
            print(f"Saldo atual: R${saldo:.2f}\n")
        
    elif opcao == "e":
        print("\n================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Opcao inválida, por favor selecione novamente a opção desejada.")