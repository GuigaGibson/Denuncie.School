import mensagens

def cadastrados(n):
    # Devolve a matriz contendo os dados dos alunos gerais(!=1) ou dos ja cadastrados(1)
    try:
        if n == 1:
            arquivo = open("cadastrados.txt", "r")
            teste = arquivo.readlines()
            arquivo.close()
        else:
            arquivo = open("alunos.txt", "r")
            teste = arquivo.readlines()
            arquivo.close()
        matriz = []
        for i in teste:
            lista = i[0 : len(i) - 1].split(";")  # apagando o \n
            matriz.append(lista)
        return matriz
    except FileNotFoundError:
        print("Arquivo não encontrado.")
#######################################################################


def checar(nome, matricula):  # checa se o nome ja foi cadastrado
    nome = nome.upper()
    matriz = cadastrados(1)
    for i in matriz:
        if nome == i[0]:
            if matricula == i[-1]:
                return 0  # nome ja cadastrado
    return 1  # nome nao cadastrado


#######################################################################


def login(nome, senha, tipo):
    matriz = cadastrados(1)
    nome = nome.upper()
    for i in matriz:
        if nome in i:
            if tipo == i[2]:
                if i[1] == senha:  # senha correta
                    return True
                else:
                    print("Senha incorreta")
                    return False  # senha errada
            else:
                print("Tipo de usuário inválido")
                return False
    print("Nome não encontrado")
    return False  # nome nao cadastrado


#######################################################################


def cadastrar(nome, matricula):
    try:
        op = checar(nome, matricula)
        if op == 0:
            print("Aluno já cadastrado.")
            return False
        else:
            nome = nome.upper()
            alunos = cadastrados(2)
            for i in range(len(alunos)):
                if nome == alunos[i][0]:
                    # print(alunos[i][-1])
                    if matricula == alunos[i][-1]:
                        senha = input("Digite uma senha: ")
                        sub = alunos[i][:]  # Copiando a linha do aluno
                        sub.insert(1, senha)
                        # Abrindo uma matriz com os alunos cadastrados, para ordenar e inserir o novo
                        alunos_cadastrados = cadastrados(1)
                        alunos_cadastrados.append(sub)
                        alunos_cadastrados.sort(key=lambda x: x[0])
                        # agora abrir e colar no arquivo
                        arquivo = open("cadastrados.txt", "w")
                        for linha in alunos_cadastrados:
                            aluno = ";".join(linha)
                            arquivo.write(aluno + "\n")
                        arquivo.close()
                        print("Aluno encontrado e cadastrado.")
                        return True
                    print("Número divergente de Matrícula.")
                    return False
            print("Aluno não encontrado.")
            return False
    except FileNotFoundError:
        print("Arquivo não encontrado. Não foi possível realizar o cadastro.")

#######################################################################


def alterar(nome):
    nome = nome.upper()
    alunos = cadastrados(1)
    for i in range(len(alunos)):
        if alunos[i][0] == nome:
            x = i
            break
    else:
        return 0  # ERRO Nome nao encontrado
    while True:
        senha = input("Digite a senha anterior: ")
        if senha != alunos[x][1]:
            print("Senha incorreta.")
        else:
            break
    senha = input("Digite a sua nova senha: ")
    alunos[x][1] = senha
    # reenscrever a matriz
    arquivo = open("cadastrados.txt", "w")
    for linha in alunos:
        aluno = ";".join(linha)
        arquivo.write(aluno + "\n")
    arquivo.close()
    print("Senha alterada com sucesso!")
    return True  # tudo ok


#######################################################################


def del_usu(nome):
    nome = nome.upper()
    alunos = cadastrados(1)  # pegando a matriz de alunos cadastrados
    for i in range(len(alunos)):
        if alunos[i][0] == nome:
            x = i
            break
    else:
        return 0  # ERRO Nome nao encontrado
    del alunos[x]
    # reescrever a matriz sem o aluno
    arquivo = open("cadastrados.txt", "w")
    for linha in alunos:
        aluno = ";".join(linha)
        arquivo.write(aluno + "\n")
    arquivo.close()
    return True  # voltou tudo certo


#######################################################################

def info():
    mensagens.lista_informativos()
    respostas = mensagens.respostas_informativos()
    opc = int(input("digite a opção: "))
    print(respostas[opc - 1])
