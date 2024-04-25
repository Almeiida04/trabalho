opcao = input("Digite uma opção 'A, B, C, D ou E': ").upper()

if opcao == "A":
    dianasci = int(input("Digite o dia que você nasceu : "))
    mesnasci = int(input("Digite o mês que você nasceu "))
    diasquefaltam = 365 - (mesnasci - 1) * 30 + dianasci

    if diasquefaltam < 1:
        diasquefaltam += 365
    print("Faltam {} para seu aniversário. ".format(diasquefaltam))

elif opcao == "B":
    M = int(input("Insira o primeiro dígito da conta bancária: "))
    C = int(input("Insira o segundo dígito da conta bancária: "))
    D = int(input("Insira o terceiro dígito da conta bancária: "))
    U = int(input("Insira o quarto dígito da conta bancária: "))
    R = (M * U + C*D)
    V = R % 7
    print("Resultado = : ",V)

elif opcao == "C":
    horainicial = float(input("Digite a hora inicial: "))
    horafinal = float(input("Digite a hora final: "))
    duracao = horafinal - horainicial
    
    if duracao < 1 or duracao > 24:
        print("Duração inválida: ")
    else:
        print("A duração do jogo é de {} horas: ".format(duracao))

elif opcao == "D":
    opcao = input("Escolha uma opção '1 ou 2': ")
    if opcao == '1':
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        if base <= 0 or altura <= 0:
            print("Erro! A base e altura necessitam ser positivas ")
        else:
            area = (base * altura) / 2
            print("A área do triângulo é {}: ".format(area))
    elif opcao == '2':
        ladoA = float(input("Digite o valor do lado a: "))
        ladoB = float(input("Digite o valor do lado b: "))
        ladoC = float(input("Digite o valor do lado c: "))
        if ladoA >= ladoB + ladoC:
            print("Nenhum triangulo foi formado, tente novamente! ")
        elif ladoA ** 2 == ladoB ** 2 + ladoC ** 2:
            print("Triângulo retângulo. ")
        else:
            print("Não é retângulo. ")

elif opcao == "E":
    print("Fim. ")
else:
    print("Opção inválida. ")
