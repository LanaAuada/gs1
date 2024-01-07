
#opção de alimentos plantáveis, temperatura recomendada e meios para melhorar a condição do alimento 
#hortaliça, tempero, fungo, fruta

import re
def verificar_senha(senha):
    if not re.search("\d{5}", senha) or len(senha) > 5:
        erro = "A senha deve conter 5 números"
        return erro
resposta = "sim"
msgFinal = []
erro=" "
try:
    #área de cadastro e validação 
    print("CADASTRO")
    print("Informe seu nome: ")
    nome= input()
    if re.search("\d",nome):
        erro = "O nome não pode conter números"
        raise ValueError
    print("Informe seu e-mail: ")
    email= input()
    if not re.search("@",email):
        erro = "O email precisa conter @"
        raise ValueError
    print("Digite uma senha numérica de 5 dígitos: ")
    senha = input()
    erro = verificar_senha(senha)
    if erro:
        raise ValueError(erro)
    
    while resposta.lower() == "sim":
        print("Informe o que será plantado")
        print("\nDigite (1) para hortaliças.\nDigite (2) para temperos.\nDigite (3) para cogumelos.")
        temp = 0
        col = " "
        escolha = int(input())
        if escolha == 1:
            temp = "15 a 20"
            print("Informe o número do grupo que a hortaliça se encaixa: \nGrupo 1[Abobrinha; Mostarda; Pepino; Rabanete; Rúcula]\nGrupo 2[Alface; Almeirão; Brócolis; Couve; Escarola; Morango; Quiabo; Melancia]\nGrupo 3[Abóbora; Batata; Berinjela; Cenoura; Chuchu; Couve-flor; Jiló; Pimentão; Repolho; Tomate]")
            grupo = int(input())
            if grupo == 1:
                col = "Entre 1 a 2 meses"
                nomeGrupo="Grupo 1[Abobrinha; Mostarda; Pepino; Rabanete; Rúcula]"
            elif grupo == 2:
                col = "Entre 2 a 3 meses"
                nomeGrupo="Grupo 2[Alface; Almeirão; Brócolis; Couve; Escarola; Morango; Quiabo; Melancia]"
            elif grupo==3:
                col = "Entre 3 a 4 meses"
                nomeGrupo="Grupo 3[Abóbora; Batata; Berinjela; Cenoura; Chuchu; Couve-flor; Jiló; Pimentão; Repolho; Tomate]"
            else:
                erro="Por favor, digite um número válido"
                raise ValueError
            print(f"A temperatura recomendada para esse grupo é: {temp} graus celcius")
            print(f"O tempo de colheita recomendado é: {col}")
            msgFinal.append(f"Hortaliça do {nomeGrupo}")
        elif escolha == 2:
            temp="21 a 25"
            print("Informe o número do grupo que o tempero se encaixa: \nGrupo 1[Salsa; Manjericão; Coentro; Hortelã]\nGrupo 2[Cebolinha; Tomilho; Orégano]\nGrupo 3[Pimenta; Sálvia; Alecrim]")
            grupo = int(input())
            if grupo == 1:
                nomeGrupo="Grupo 1[Salsa; Manjericão; Coentro; Hortelã]"
                col = "Entre 60 a 70 dias"
            elif grupo == 2:
                nomeGrupo="Grupo 2[Cebolinha; Tomilho; Orégano]"
                col = "Entre 70 a 80 dias"
            elif grupo==3:
                nomeGrupo="Grupo 3[Pimenta; Sálvia; Alecrim]"
                col = "Entre 80 e 90 dias"
            else:
                erro="Por favor, digite um número válido"
                raise ValueError
            print(f"A temperatura recomendada para esse grupo é: {temp} graus celcius")
            print(f"O tempo de colheita recomendado é: {col}")
            msgFinal.append(f"Tempero do {nomeGrupo}")
        elif escolha==3:
            temp = "15 a 23"
            print("Informe o número do cogumelo: \n1- Shimeji\n2- Champignon\n3- Shiitake")
            cog = int(input())
            if cog == 1:
                nomeCogumelo="Shimeji"
                col = "Entre 1 a 2 meses"
            elif cog == 2:
                nomeCogumelo="Champignon"
                col = "Entre 2 a 3 meses"
            elif cog==3:
                nomeCogumelo="Shiitake"
                col = "Entre 3 a 5 meses"
            else:
                erro="Por favor, digite um número válido"
                raise ValueError
            print(f"A temperatura recomendada para o cogumelo é: {temp} graus celcius")
            print(f"O tempo de colheita recomendado é: {col}")
            msgFinal.append(f"Cogumelo {nomeCogumelo}")
        
        else:
            erro="Por favor, digite um número válido"
            raise ValueError

        print("Deseja cadastrar outro produto?")
        resposta=input()
        if resposta.lower()!="sim" and resposta.lower()!="não":
            erro= "Por favor, digite sim ou não"
            raise ValueError
        print("Você Cadastrou:")
        for i in range(len(msgFinal)):
            print(msgFinal[i])
                
except:
    print(erro)
finally:
    print("Obrigada por usar nossos serviços.")
