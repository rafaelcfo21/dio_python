menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo =  0
limite = 500
extrato = ""
numero_saque = 0
limite_saques = 3

while True:

  opcao = input(menu)

  if opcao == "d":
     valor = float(input("Informe o valor do depósito: "))

     if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} \n"
     else:
      print("operação falhou! O valor informado é inválido.")   


  elif opcao == "s":
       valor = float(input("Informe o valor do Saque: "))

       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite
       excedeu_saques = numero_saque >= limite_saques

       if excedeu_saldo:
          print("Operação falhou! Você não tem saldo suficiente.")

       elif excedeu_limite:
          print("Operação falhou! O valor do saque escede o limite.")

       elif excedeu_saques:
          print("Operação falhou! Número máximo de saques excedido")

       elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saque += 1

       else:
         print("Operação falhou! O valor informado é inválido")        

  elif opcao == "e":
    print("\n ===============Extrato===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========================================")

  elif opcao =="q":
    break 

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")  