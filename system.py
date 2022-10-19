welcome_text = """
Seja bem vindo(a)! Escolha uma das opções abaixo para iniciar:
(1) Cadastro de recrutador
(2) Cadastro de candidato
(3) Verificar cadastros
(4) Sair
"""

atuacao_candidato = """
Qual é a sua área de atuação?
(1) Tecnologia
(2) Humanas 
(3) Engenharia
(4) Economia
(5) Outra área
"""

atuacao_recrutador = """
Qual é sua área de recrutamento?
(1) Tecnologia
(2) Humanas 
(3) Engenharia
(4) Economia
(5) Outra área
"""

recrutadores = []
candidatos = []


def confirma():
    input("Aperte ENTER para confirmar.")


def cadastro_recrutador():
    print(str("Bem-vindo, recrutador!"))
    id_recrutador = int(input("Id: "))
    nome_recrutador = str(input("Digite o seu nome completo: "))
    email_recrutador = str(input("Digite o seu email: "))
    print(str(atuacao_recrutador))
    area_recrutador = str(input("Qual a área? "))

    if nome_recrutador is not None and email_recrutador is not None and area_recrutador is not None:
        print("\nSEUS DADOS: \nId: " + str(id_recrutador) + "\nnNome: " +
              nome_recrutador + "\nEmail: " + email_recrutador + "\nÁrea: " + str(area_recrutador))
        print(str("\nDigite: \n(1) Confirmar \n(2) Corrigir\n"))
        conf_corr = int(input("RESPONDA -> "))
        if conf_corr == 1:
            recrutadores.append(
                (id_recrutador, nome_recrutador, email_recrutador, area_recrutador))
            print("Recrutador cadastrado com sucesso.")
            welcome_system()
        else:
            print(str("Corrija o seu cadastro:"))
            cadastro_recrutador()
    else:
        print(str("Cadastro não realizado. Todas as opções são obrigatórias"))
        cadastro_recrutador()


def cad_candidato():
    print(str("Bem-vindo, candidato!"))
    id_candidato = int(input("Id: "))
    nome_candidato = str(input("Digite o seu nome completo: "))
    email_candidato = str(input("Digite o seu email: "))
    print(str(atuacao_candidato))
    area_candidato = int(input("Qual a sua área? "))

    if nome_candidato is not None and email_candidato is not None and area_candidato is not None:
        print("\nSEUS DADOS: \nId: " + str(id_candidato) + "\nNome: " +
              nome_candidato + "\nEmail: " + email_candidato + "\nÁrea: " + str(area_candidato))
        print(str("\nDigite: \n(1) Confirmar \n(2) Corrigir\n"))
        conf_corr = int(input("RESPONDA -> "))
        if conf_corr == 1:
            recrutadores.append(
                (id_candidato, nome_candidato, email_candidato, area_candidato))
            print("Candidato cadastrado com sucesso.")
            welcome_system()
        elif conf_corr == 2:
            print(str("Corrija o seu cadastro:"))
            cad_candidato()
    else:
        print(str("Cadastro não realizado. Todas as opções são obrigatórias"))
        cad_candidato()


def lista_cadastro():
    listar = int(input("Você é \n(1) Recrutador \n(2) Candidato \n"))
    if listar == 1:
        print("Recrutadores cadastrados:")
        if len(recrutadores) != 0:
            for i in recrutadores:
                print(i)
        else:
            print("Nenhum recrutador foi cadastrado.")
            welcome_system()
    else:
        if len(candidatos) != 0:
            print("Usuários cadastrados:")
            for j in candidatos:
                print(j)
        else:
            print("Nenhum candidato foi cadastrado.")
            welcome_system()


def choose_number():
    option = int(input("Digite o número: "))
    if option == 1:
        cadastro_recrutador()
    elif option == 2:
        cad_candidato()
    elif option == 3:
        lista_cadastro()
    elif option == 4:
        iniciar = int(
            input("Sistema finalizado. Para iniciar novamente, tecle 1\n"))
        if iniciar == 1:
            welcome_system()
    else:
        print("Opção inválida. Escolha entre 1 a 4")


def welcome_system():
    print(str(welcome_text))
    choose_number()


welcome_system()
