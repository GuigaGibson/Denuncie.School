"""
NOME | ANONIMO | PROTOCOLO | DENUNCIA | ANONIMO | PROTOCOLO | DENUNCIA |
JOSE    N          1222        ...        S        222         ...

"""


def matriz_denuncia():
    arquivo = open("denuncias.txt", "r")
    teste = arquivo.readlines()
    arquivo.close()
    matriz = []
    for i in teste:
        lista = i[0 : len(i) - 1].split("|")  # apagando o \n
        matriz.append(lista)
    return matriz


def checar_denuncia(nome):
    matriz = matriz_denuncia()
    for i in matriz:
        if i[0] == nome:
            return True
    else:
        return False


def criar_denuncia(nome,tipo): 
    if tipo==False:#normal
        anonimo="N"
    else:#anonimo
        anonimo="S"
    denuncia=input("Digite a sua denuncia: \n").upper()
    protocolo=str(len(matriz_denuncia()) + 1)
    lista=[nome.upper(),anonimo,protocolo,denuncia,'1']
    arquivo = open("denuncias.txt", "a")
    aluno = "|".join(lista)
    arquivo.write(aluno+"\n")
    arquivo.close()

def visualizar_denuncia(nome):
    nome=nome.upper()
    matriz=matriz_denuncia()
    for i in matriz:
        if i[0]==nome:
            if i[1]=="S":
                print("(ANONIMA)",end=" ")
            print(i[3])
            if i[-1]=="1":
                print("-Denúncia enviada-")
                print("\n")
            elif i[-1]=="2":
                print("-Denúncia em análise-")
                print("\n")
            else:
                print("-Denúncia finalizada-")
                print("\n")


def status():  # ADMIN
    matriz = matriz_denuncia()
    lista = []

    for i in range(len(matriz)):
        if matriz[i][-1] == "3":
            lista.append(matriz[i])
            continue
        if matriz[i][1] == "S":
            print("ANONIMO")
        else:
            print(matriz[i][0])
        print(f"Denuncia {i}, Status: {matriz[i][-1]}\n{matriz[i][3]}")
        print("")
        lista.append(matriz[i])

    opc = int(input("Deseja alterar o status de qual denúncia?\nNúmero: "))
    sts = input("1 Enviado\n2 Lido\n3 Finalizado\nOpção: ")
    print("")
    # Verificando se a opcao eh valida
    if 0 <= opc < len(lista):
        # Substituindo o valor na ultima coluna
        lista[opc][-1] = sts
        print(f"Status da denúncia {opc} alterado para {sts}")
    else:
        print("Índice de denúncia inválido")

    #SALVANDO NO ARQUIVO
    arquivo = open("denuncias.txt", "w")
    for i in lista:
        aluno = "|".join(i)
        arquivo.write(aluno+"\n")
    arquivo.close()

# Exemplo de uso:
visualizar_denuncia("Bruno Eduardo")