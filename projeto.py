renda_mensal = 0
renda_informada = 0
total_gastos = 0
quantidade_gastos = 0
alimentacao = 0
transporte = 0
lazer = 0
saude = 0
outros = 0
opcao = 0
# Declarei as variáveis antes do loop pra os valores não mudarem durante a execução do programa

while opcao != 6: # O programa irá repetir enquando a variável opção for diferente de 6
    print("---------------------------------------")
    print("|         Controle de gasto:          |")
    print("---------------------------------------")
    print("|   1. Informar renda mensal.         |")
    print("|   2. Cadastrar gasto.               |")
    print("|   3. Consultar gasto.               |")
    print("|   4. Consultar situação financeira. |")
    print("|   5. Ver estatísticas.              |")
    print("|   6. Sair                           |")
    print("---------------------------------------")

    opcao = int(input("Escolha uma das opções: "))
    print("A opção escolhida foi", opcao)

    if opcao == 1: # Se a opção escolhida for 1, então a pessoa vai digitar o valor da sua renda mensal
        renda_mensal = float(input("Informe sua renda mensal: R$ "))

        while renda_mensal < 0: # Se a pessoa digitar um valor negativo, o programa vai proibir e pedir pra digitar a renda novamente
            print("A renda não pode ser negativa.")
            renda_mensal = float(input("Informe sua renda mensal: R$ "))

        renda_informada = 1
        print("Renda mensal cadastrada: R$", renda_mensal)

    elif opcao == 2: # Se a opção for 2, vai mostrar as opções de gastos e mandar escolher um dos gastos e colocar o valor gasto
        print("---------------------------------------")
        print("|              Descrição:             |")
        print("---------------------------------------")
        print("|   1. Alimentação.                   |")
        print("|   2. Transporte.                    |")
        print("|   3. Lazer.                         |")
        print("|   4. Saúde.                         |")
        print("|   5. Outros.                        |")
        print("---------------------------------------")

        categoria = int(input("Escolha uma das opções de gasto: "))

        while categoria < 1 or categoria > 5: # Enquanto a pessoa não digitar uma opção entre 1 e 5 vai ficar repetindo para escolher uma opção de gasto
            print("Categoria inválida.")
            categoria = int(input("Escolha uma opção de 1 a 5: "))

        valor = float(input("Informe o valor do gasto: R$ "))

        while valor < 0.01:
            print("O gasto deve ser de pelo menos R$ 0.01.")
            valor = float(input("Informe o valor do gasto: R$ "))

        if categoria == 1:
            alimentacao = alimentacao + valor
        elif categoria == 2:
            transporte = transporte + valor
        elif categoria == 3:
            lazer = lazer + valor
        elif categoria == 4:
            saude = saude + valor
        elif categoria == 5:
            outros = outros + valor

        total_gastos = total_gastos + valor
        quantidade_gastos = quantidade_gastos + 1

        if quantidade_gastos == 1:
            maior_gasto = valor
            menor_gasto = valor
        else:
            if valor > maior_gasto:
                maior_gasto = valor
            if valor < menor_gasto:
                menor_gasto = valor

        print("Gasto cadastrado com sucesso!")

    elif opcao == 3: # Se a opção for 3 vai primeiro ver se tem gastos cadastrados, depois vai informar os gastos se houver
        if quantidade_gastos == 0:
            print("Nenhum gasto foi cadastrado.")
        else:
            print("Seus gastos por categoria:")
            print("Alimentação: R$", alimentacao)
            print("Transporte: R$", transporte)
            print("Lazer: R$", lazer)
            print("Saúde: R$", saude)
            print("Outros: R$", outros)
            print("Total gasto no mês: R$", total_gastos)

    elif opcao == 4: # Se a opção for 4 vai primeiro ver se tem renda informada, depois vai fazer os cálculos se tiver renda
        if renda_informada == 0:
            print("Informe sua renda mensal na opção 1.")
        else:
            saldo = renda_mensal - total_gastos

            print("Renda mensal: R$", renda_mensal)
            print("Total gasto: R$", total_gastos)
            print("Saldo disponível: R$", saldo)

            if saldo > 0:
                print("Você está dentro do orçamento.")
            elif saldo == 0:
                print("Você atingiu o limite do orçamento.")
            else:
                valor_ultrapassado = total_gastos - renda_mensal
                print("Você ultrapassou o orçamento em R$", valor_ultrapassado)

    elif opcao == 5: # Se a opção for 5 vai primeiro ver se tem gastos cadastrados, depois faz os cálculos se tiver gastos
        if quantidade_gastos == 0:
            print("Cadastre um gasto para ver as estatísticas.")
        else:
            media_gastos = total_gastos / quantidade_gastos

            print("Quantidade de gastos:", quantidade_gastos)
            print("Total gasto: R$", total_gastos)
            print("Média dos gastos: R$", media_gastos)
            print("Maior gasto: R$", maior_gasto)
            print("Menor gasto: R$", menor_gasto)

            if renda_mensal > 0:
                percentual = total_gastos / renda_mensal * 100
                print("Porcentagem da renda utilizada:", percentual, "%")

    elif opcao == 6: # Se a opção for 6 vai finalizar o programa
        print("Programa encerrado.")

    else: # Se a opção for diferente de 1 a 6 vai mandar escolher uma opção válida
        print("Opção inválida. Escolha de 1 a 6.")
