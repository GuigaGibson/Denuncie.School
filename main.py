import denunciaCRUD
import funcoes
import mensagens

# Variáveis globais
nome_usuario = ''
senha_usuario = ''
tipo_usuario = 1
matricula_usuario = 0


def limpar_usuario():
    global nome_usuario, tipo_usuario, senha_usuario, matricula_usuario

    nome_usuario = ''
    senha_usuario = ''
    tipo_usuario = 1
    matricula_usuario = 0

def criar_denuncia():
    mensagens.escolher_modo_denuncia()
    escolhido = str(input())
    mensagens.criar_denuncia()
    if escolhido.upper() == 'S':
        denunciaCRUD.criar_denuncia(nome_usuario, True)
    else:
        denunciaCRUD.criar_denuncia(nome_usuario, False)

    mensagens.denuncia_criada()
    mensagens.voltar()
    input()
    menu_aluno()


# to-do
def acompanhar_minhas_denuncias():
    denunciaCRUD.visualizar_denuncia(nome_usuario)

    mensagens.voltar()
    input()
    menu_aluno()


# to-do
def ler_informativo():
    funcoes.info()
    mensagens.voltar()
    input()
    menu_aluno()


def mensagem_opcao_errada():
    print("Você escolheu uma opção inválida. Tente novamente.")


def menu_alterar_senha():
    mensagens.menu_alterar_senha()
    funcoes.alterar(nome_usuario)

    mensagens.conta_excluida_com_sucesso()
    input()
    limpar_usuario()
    menu_login()


def menu_excluir_conta():
    mensagens.menu_excluir_conta()
    escolhido = str(input())
    if escolhido.upper() == 'S':
        funcoes.del_usu(nome_usuario)
        mensagens.conta_excluida_com_sucesso()
        input()
        limpar_usuario()
        menu_login()
    else:
        menu_perfil()


def menu_perfil():
    mensagens.menu_perfil()
    escolhido = int(input())
    if escolhido == 1:
        menu_alterar_senha()
    if escolhido == 2:
        menu_excluir_conta()


def menu_aluno():
    mensagens.menu_aluno(nome_usuario)
    escolhido = int(input())
    if escolhido == 1:
        criar_denuncia()
    if escolhido == 2:
        acompanhar_minhas_denuncias()
    if escolhido == 3:
        ler_informativo()
    if escolhido == 4:
        menu_perfil()
    if escolhido == 5:
        limpar_usuario()
        menu_login()
    else:
        mensagens.opcao_errada()
        menu_aluno()


def menu_admin():
    mensagens.menu_admin(nome_usuario)
    escolhido = int(input())
    if escolhido == 1:
        denunciaCRUD.status()
    if escolhido == 2:
        limpar_usuario()
        menu_login()
    else:
        menu_admin()



def menu_login_aluno():
    global nome_usuario
    global senha_usuario

    mensagens.login()
    nome_usuario = str(input())

    mensagens.senha()
    senha_usuario = str(input())

    # Colocar logica login aluno
    if funcoes.login(nome_usuario, senha_usuario,"0"):
        menu_aluno()
    else:
        mensagens.login_errado()
        mensagens.voltar()
        input()
        menu_login()


def menu_cadastrar():
    mensagens.menu_cadastrar()
    mensagens.menu_cadastrar_nome()
    nome = str(input())
    mensagens.menu_cadastrar_matricula()
    matricula = str(input())

    if funcoes.cadastrar(nome, matricula):
        mensagens.conta_cadastrada_com_sucesso()
        input()
        menu_login()
    else:
        mensagens.erro_ao_cadastrar()
        input()
        menu_login()

def menu_login_admin():
    global nome_usuario
    global senha_usuario

    mensagens.login()
    nome_usuario = str(input())

    mensagens.senha()
    senha_usuario = str(input())

    # Colocar logica login aluno
    if funcoes.login(nome_usuario, senha_usuario,"1"):
        menu_admin()
    else:
        mensagens.login_errado()
        mensagens.voltar()
        input()
        menu_login()


def menu_login():
    mensagens.bem_vindo()
    mensagens.menu_login()
    escolhido = int(input())

    if escolhido == 1:
        menu_login_aluno()
    if escolhido == 2:
        menu_login_admin()
    if escolhido == 3:
        menu_cadastrar()
    else:
        mensagens.opcao_errada()
        menu_login()


if __name__ == '__main__':
    menu_login()
