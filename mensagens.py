def bem_vindo():
    print("Bem vindo ao Denuncia.school.")

def login():
    print("Insira o seu nome:")

def senha():
    print("Insira a sua senha:")

def voltar():
    print("Aperte ENTER para voltar ao menu principal.")

def menu_aluno(nome):
    texto = f"""
Bem-vindo, {nome.title()}
Escolha uma opção:
1 - Criar uma nova denúncia
2 - Acompanhar minhas denúncias
3 - Ler informações
4 - Ver opções de Perfil
5 - Sair
    """
    print(texto)

def menu_admin(nome):
    texto = f"""
Bem-vindo,{nome}
== MODO ADMINISTRADOR ATIVADO ==
Escolha uma opção:
1 - Gerenciar denúncias
2 - Sair
    """
    print(texto)


def opcao_errada():
    print("Você escolheu uma opção inválida. Tente novamente.")


def informativo():
    texto = """LOREM IPSUM TESTE TESTE 123123123"""
    print(texto)


def escolher_modo_denuncia():
    print("Você deseja criar uma denúncia Anônima? (s/n)")


def criar_denuncia():
    print("Para criar a sua denúncia, escreva o conteúdo da denúncia, e em seguida, aperte ENTER:")


def denuncia_criada():
    print("\nDenúncia criada com Sucesso!")


def quantidade_denuncias(denuncia_contador):
    print(f"Você tem {denuncia_contador} denúncias.")
    print("Digite qual denúncia você deseja saber o Status:")

def menu_perfil():
    texto = f"""
Escolha uma opção:
1 - Alterar a Senha
2 - Excluir a sua conta
3 - Voltar
    """
    print(texto)


def menu_excluir_conta():
    print("Deseja REALMENTE excluir a sua conta? (s/n)")


def conta_excluida_com_sucesso():
   print("Conta excluida com Sucesso. Pressione ENTER para continuar.")

def conta_atualizada_com_sucesso():
   print("Conta atualizada com Sucesso. Pressione ENTER para continuar.")

def menu_login():
    print("Selecione uma das opções à seguir: ")

    texto = f"""
1 - Login aluno
2 - Login ADMIN
3 - Cadastrar
    """
    print(texto)


def login_errado():
    print("Houve um erro de autenticação.")


def menu_cadastrar():
    print("Para cadastrar um novo aluno, siga as instruções a seguir:")

def menu_cadastrar_nome():
    print("Insira o nome do aluno a ser cadastrado: ")

def menu_cadastrar_matricula():
    print("Insira a matrícula do aluno a ser cadastrado: ")

def conta_cadastrada_com_sucesso():
    print("Conta cadastrada com Sucesso. Pressione ENTER para continuar.")


def erro_ao_cadastrar():
    print("Houve um erro ao cadastrar o aluno. Pressione ENTER para continuar.")


def menu_alterar_senha():
    print("Para alterar a sua senha, siga as instruções a seguir:")


def ler_denuncia(quantidade):
    print(f"Você tem {quantidade} denúncias para ler. Insira o número da Mensagem:")


def lista_informativos():
    lista = [
        "1. Como identificar que estou sendo vítima de assédio escolar? ",
        "2. Como identificar que estou sendo vítima de perseguição? ",
        "3. Como identificar se fui vítima de estupro? ",
        "4. Como identificar que estou sendo vítima de bullying? ",
        "5. Qual a importância da denúncia? ",
        "6. O que fazer se você for a vítima e estiver sofrendo? ",
        "7. O que fazer se você estiver visualizando uma pessoa sendo vítima de algo? ",
        "8. O que fazer se você for mãe/pai e seu/sua filho(a) estiver sofrendo algum tipo de violência? ",
        "9. O que acontece quando eu denuncio no aplicativo? ",
        "10. É possível saber quem fez a denúncia anônima? ",
        "11. Quais as consequências do bullying na vitima?",
        "12. Quais são as penalidades para quem pratica o bullying?",
    ]

    for i in lista:
        print(i)
        print("=" * int(70))


def respostas_informativos():
    return [
        "1. Você pode estar sendo vítima de assédio quando ocorrem situações persistentes e indesejadas de natureza sexual, moral ou psicológica. Podendo ser comentários ou piadas de natureza sexual ou inadequada direcionados a você, insinuações sexuais não solicitadas ou propostas indesejadas, comportamento invasivo, como olhares constantes, toques indesejados ou invasão do seu espaço pessoal, comentários depreciativos, insultos e humilhações frequentes. Como também, ameaças verbais ou físicas, exclusão social intencional ou isolamento por parte de colegas ou superiores, difamação, disseminação de rumores ou exposição pública de informações pessoais constrangedoras. Se você está enfrentando essas situações, é importante saber que você não está sozinha(o) e pode buscar apoio e orientação. Converse com alguém de confiança, como um adulto responsável, professor(a), orientador(a) escolar ou profissional de recursos humanos, para obter ajuda e tomar medidas para proteger seus direitos e bem-estar.",
        "2. Você pode estar sendo vítima de perseguição quando ocorrem situações persistentes e indesejadas de monitoramento, vigilância ou assédio por parte de alguém. Alguns sinais são a observação constante por parte de uma pessoa ou grupo, mesmo em locais diferentes, recebimento frequente de mensagens, ligações ou e-mails ameaçadores ou intimidadores. Danos à sua propriedade pessoal, como vandalismo ou roubo, monitoramento online excessivo, como perseguição em redes sociais ou invasão de privacidade. Como também, seguimento físico, onde você percebe que está sendo seguido ou vigiado, espalhamento de rumores ou informações falsas sobre você. Ameaças verbais ou físicas direcionadas a você. Se você suspeita que está sendo vítima de perseguição, é importante buscar ajuda imediatamente, você não está sozinho(a). Converse com um adulto de confiança, como um familiar, amigo próximo ou autoridade competente, para que eles possam ajudá-lo a tomar as medidas necessárias para garantir sua segurança e bem-estar.",
        "3. O estupro é uma forma de violência sexual que pode deixar marcas físicas e emocionais profundas. Há alguns sinais fortes como as lesões físicas, como os hematomas, os arranhões, os cortes ou lacerações na região genital ou em outras partes do corpo. Dor ou desconforto na região genital ou anal e sangramento vaginal ou anal. Podem ocorrer problemas de saúde relacionados à atividade sexual não consensual, como as infecções sexualmente transmissíveis (ISTs). No entanto, há os sinais sutis, como o ato da relação sexual mesmo você mostrando que não tem interesse ou, até mesmo, dizendo que não quer. Sem a sua autorização é estupro, podendo ser seu namorado, podendo ser seu amigo ou alguém que tenha afeto. Continuar fazendo algo no seu corpo, sem a sua autorização, é estupro e estupro é crime! Se você suspeita que foi estuprada, é importante buscar ajuda imediatamente. Procure um serviço de saúde para avaliação médica e tratamento de possíveis lesões ou infecções, e procure apoio emocional de um profissional de saúde mental ou de um grupo de apoio a vítimas de violência sexual. Além disso, considere denunciar o crime às autoridades competentes para garantir que o agressor seja responsabilizado pelos seus atos.",
        "4. O bullying pode ser identificado por meio de alguns sinais como comportamento agressivo ou hostil de colegas em relação a você de forma constante, insultos, apelidos ofensivos ou comentários humilhantes direcionados a você. Exclusão social frequente, sendo deixado de fora de atividades ou grupos, ameaças físicas, intimidação ou violência. Danos físicos ou materiais causados por outras pessoas. Se você suspeita que está sendo vítima de bullying, é importante buscar ajuda imediatamente. Converse com um adulto de confiança, como um(a) professor(a), orientador(a) escolar ou seus pais, para que possam tomar as medidas necessárias para garantir sua segurança e bem-estar.",
        "5. Denunciar um crime é fundamental para garantir que a justiça seja feita e que o agressor seja responsabilizado pelos seus atos. Além disso, a denúncia pode ajudar a prevenir que outras pessoas sejam vítimas do mesmo tipo de violência. Quando uma denúncia é feita, as autoridades competentes podem investigar o caso e tomar as medidas necessárias para proteger a vítima e punir o agressor. A denúncia também pode ser um passo importante para a recuperação da vítima, pois permite que ela receba apoio emocional e psicológico, bem como tratamento médico e terapêutico, se necessário. É importante lembrar que a denúncia é um direito da vítima e que ela não deve ser culpabilizada ou estigmatizada por ter sido vítima de violência.",
        "6. Se você é vítima na escola, é importante tomar algumas medidas para lidar com a situação e buscar apoio. Fale com alguém de confiança: Procure um adulto em quem você confia, como um(a) professor(a), orientador(a) educacional, coordenador(a) ou seus pais. Compartilhe suas experiências e emoções para que eles possam te apoiar e ajudar. Documente as ocorrências: Anote detalhes sobre os incidentes, incluindo datas, horários, locais e descrição do que aconteceu. Isso pode ser útil para relatar o problema às autoridades escolares e ter um registro dos eventos. Procure ajuda de profissionais: Busque o apoio de psicólogos, assistentes sociais ou outros profissionais especializados em lidar com situações. Eles podem oferecer suporte emocional e orientação para enfrentar a situação. Mantenha-se seguro(a): Se possível, evite situações em que você possa estar sozinho com os agressores. Procure estar perto de amigos ou em áreas supervisionadas pela escola. Conheça seus direitos: Informe-se sobre as políticas e diretrizes da escola. Conheça seus direitos e exija que a escola tome medidas para garantir sua segurança. Não reaja com violência: Evite responder com violência física ou verbal, pois isso pode piorar a situação. Procure manter a calma e buscar soluções pacíficas. Promova a conscientização: Considere falar sobre sua experiência com outras pessoas, seja através de campanhas escolares ou em grupos de apoio. Isso pode ajudar a conscientizar sobre o problema e encorajar outras vítimas a buscar ajuda. Lembre-se de que você não está sozinho(a) e tem o direito de ser tratado com respeito e segurança na escola. Busque apoio e denuncie o que estiver passando para que as medidas adequadas possam ser tomadas para resolver a situação.",
        "7. Se você presenciar alguém sendo vítima de algo na escola, é importante tomar algumas medidas para ajudar e garantir a segurança da pessoa. Aqui estão algumas sugestões: Intervenha de forma segura: Se for seguro fazê-lo, intervenha na situação, interrompendo o comportamento prejudicial. Por exemplo, você pode chamar a atenção dos agressores, distraí-los ou pedir ajuda a um adulto responsável. Ofereça apoio: Após intervir, aproxime-se da pessoa que está sendo vítima e mostre empatia. Pergunte como ela está e ofereça apoio emocional. Mostre que você está ali para ajudar e que ela não está sozinha. Reporte o incidente: Informe imediatamente um adulto responsável na escola, como um professor, orientador educacional ou diretor. Relate o incidente de forma clara e objetiva, fornecendo detalhes sobre o que aconteceu e quem estava envolvido. Seja um aliado: Mostre solidariedade e apoio contínuo à pessoa que está sendo vítima. Esteja presente para ouvi-la, encorajá-la e ajudá-la a buscar ajuda adicional, se necessário. Promova a conscientização: Converse com seus colegas sobre a importância de respeitar os outros e combater o bullying. Organize atividades educativas ou campanhas de conscientização na escola para promover um ambiente seguro e acolhedor. Lembre-se de que é fundamental agir com responsabilidade e segurança ao intervir em uma situação de violência ou bullying. Priorize a segurança de todos os envolvidos e busque apoio de adultos responsáveis para lidar com a situação adequadamente.",
        "8. Se você suspeita que seu filho está sofrendo algum tipo de violência na escola, é importante agir prontamente para garantir a segurança e o bem-estar dele. Aqui estão algumas medidas que você pode tomar: Converse com seu filho: Tenha uma conversa aberta e acolhedora com seu filho, encorajando-o a compartilhar suas experiências na escola. Ouça atentamente e valide seus sentimentos, demonstrando apoio e empatia. Contate a escola: Entre em contato com a escola para relatar suas preocupações. Agende uma reunião com o professor, orientador educacional ou diretor para discutir a situação e buscar soluções. Documente as ocorrências: Anote detalhadamente os incidentes de violência relatados por seu filho, incluindo datas, horários, pessoas envolvidas e descrição dos eventos. Essas informações podem ajudar na investigação e tomada de medidas adequadas. Colabore com a escola: Trabalhe em parceria com a escola para resolver o problema. Compartilhe as informações que você coletou e discuta possíveis estratégias para garantir a segurança de seu filho, como monitoramento mais atento, intervenção educacional ou mediação entre as partes envolvidas. Busque apoio externo: Se necessário, procure apoio de profissionais especializados, como psicólogos, assistentes sociais ou terapeutas, para ajudar seu filho a lidar com as consequências emocionais da violência. Considere denunciar: Se a escola não tomar medidas adequadas para resolver a situação ou se houver evidências claras de crime, você pode considerar fazer uma denúncia às autoridades competentes, como a polícia ou o conselho tutelar. Lembre-se de que é importante agir com calma e assertividade, priorizando o bem-estar de seu filho. A colaboração entre pais e escola é essencial para enfrentar e prevenir a violência escolar.",
        "9. A equipe de suporte do aplicativo irá revisar a denúncia e tomar as medidas necessárias para resolver o problema. Isso pode incluir uma atenção maior nas atitudes da pessoa ou grupo denunciado ou, até mesmo, entrar em contato, dependendo do caso. Sendo uma denúncia anônima ou não, haverá um passo a passo mostrando o andamento e a atualização do processo da denúncia. Se a denúncia envolver uma atividade criminosa, o aplicativo pode encaminhar as informações para as autoridades competentes para investigação e ação legal. Lembre-se de que é importante denunciar qualquer tipo de comportamento inadequado escolar ou ilegal no aplicativo para garantir a segurança e o bem-estar dos usuários. No entanto, é importante usar os recursos de denúncia com responsabilidade e evitar fazer denúncias falsas ou mal-intencionadas, pois isso pode prejudicar outras pessoas e afetar a credibilidade do sistema de denúncias.",
        "10. Não é possível saber quem fez a denúncia mesmo sendo ela anônima.",
        "11. O bullying pode ter consequências graves e duradouras na vida de uma pessoa. Aqui estão algumas das possíveis consequências: Problemas emocionais: O bullying pode causar ansiedade, depressão, baixa autoestima, isolamento social e outros problemas emocionais que podem afetar a saúde mental e o bem-estar da pessoa. Problemas físicos: O bullying pode causar lesões físicas, como hematomas, cortes ou fraturas, que podem afetar a saúde física da pessoa. Problemas acadêmicos: O bullying pode afetar o desempenho acadêmico da pessoa, levando à falta de motivação, dificuldades de concentração e outros problemas que podem prejudicar o aprendizado.Problemas sociais: O bullying pode afetar as habilidades sociais da pessoa, tornando-a mais isolada e menos propensa a desenvolver relacionamentos saudáveis com outras pessoas.Problemas comportamentais: O bullying pode levar a comportamentos agressivos ou violentos por parte da pessoa que sofreu o bullying, bem como a comportamentos de risco, como uso de drogas ou álcool. Problemas de saúde mental a longo prazo: O bullying pode levar a problemas de saúde mental a longo prazo, como transtorno de estresse pós-traumático (TEPT), transtorno de ansiedade generalizada (TAG) ou transtorno depressivo maior (TDM). É importante lembrar que o bullying não é culpa da pessoa que sofre, e que ela tem direito a apoio e proteção para superar as consequências dessa violência. Se você ou alguém que você conhece está sofrendo bullying, é importante buscar ajuda e apoio para lidar com as consequências e prevenir futuros episódios de violência.",
        "12. As penalidades para quem pratica bullying podem variar dependendo da gravidade do caso e das leis do país ou estado em que ocorreu. No Brasil, a Lei nº 13.185/2015 estabelece que as escolas têm a responsabilidade de adotar medidas de prevenção e combate ao bullying, e que os agressores devem ser punidos de acordo com as normas disciplinares e o Estatuto da Criança e do Adolescente (ECA). Entre as penalidades previstas pelo ECA para quem pratica bullying, estão: Advertência: A escola pode aplicar uma advertência verbal ou escrita ao agressor, alertando-o sobre as consequências de seu comportamento. Suspensão: O agressor pode ser suspenso da escola por um período determinado, como forma de punição e para garantir a segurança dos demais alunos. Transferência: Em casos graves, a escola pode transferir o agressor para outra instituição de ensino. Medidas socioeducativas: Em casos mais graves, o agressor pode ser submetido a medidas socioeducativas, como acompanhamento psicológico ou participação em programas de ressocialização. Além disso, em casos de violência física ou psicológica grave, o agressor pode ser responsabilizado criminalmente e sujeito a medidas previstas pelo Código Penal Brasileiro, como detenção ou reclusão. Lembre-se de que é importante denunciar casos de bullying para garantir a segurança e o bem-estar das vítimas e prevenir futuros episódios de violência. A escola e as autoridades competentes devem tomar medidas adequadas para punir os agressores e proteger as vítimas.",
    ]