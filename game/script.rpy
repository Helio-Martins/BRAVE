#define config.menu_include_disabled = True
define config.rollback_enabled = True
define config.allow_skipping = False
default show_image = True
default session = 0
default conhecimento = 3
default energia = 3
default socialidade = 3
default acordar = False
default player_name = "Jogador"
default player_img = 1
image side player_image = im.Scale("player/1.png", 350, 350, bilinear=True)

default tasklist = []
default task_space = []
default tasks = []
default tasks_s1 = []
default currenttask = -1
default d_coords = {1:[250, 300], 2:[300,300], 3:[200,300], 4:[250,300], 8:[600,300], 9:[950,300], 10:[800,300]}
default d_size = {1:0.8, 2:0.8, 3:0.8, 4:0.8, 8:0.8, 9:0.8, 10:0.8}
default situation = 0
default fadeinto = False

define professor = Character("Professor João", color="a9a9a9", image="professor", who_outlines=[(absolute(1), "#000000")])
image side professor = im.Scale("professor.png", 350, 350, bilinear=True)
define psicologa = Character("Psicóloga Joana", color="a9a9a9", image="psicologa", who_outlines=[(absolute(1), "#000000")])
image side psicologa = im.Scale("psicologa_face.png", 300, 300)
define grupo_alunos = Character("Grupo de alunos", color="a9a9a9", image="alunos", who_outlines=[(absolute(1), "#000000")])
image side grupo_alunos = im.Scale("alunos.png", 350, 350, bilinear=True)
define aluno = Character("Ricardo", color="a9a9a9", image="aluno", who_outlines=[(absolute(1), "#000000")])
image side aluno = im.Scale("aluno.png", 350, 350, bilinear=True)
define auxiliar = Character("Auxiliar", color="a9a9a9", image="auxiliar", who_outlines=[(absolute(1), "#000000")])
image side auxiliar = im.Scale("auxiliar.png", 350, 350, bilinear=True)
define grupo_alunos = Character("Grupo de alunos", color="a9a9a9", image="grupos_alunos", who_outlines=[(absolute(1), "#000000")])
image side grupo_alunos = im.Scale("grupos_alunos.png", 350, 350, bilinear=True)

define ab = Character("Abel Polido", color="#0e6716", image="abel", who_outlines=[(absolute(1), "#000000")])
image side abel normal = im.Scale("chars/abel/abel_normal.png", 350, 350, bilinear=True)
image side abel angry = im.Scale("chars/abel/abel_angry.png", 350, 350, bilinear=True)
image side abel happy = im.Scale("chars/abel/abel_happy.png", 350, 350, bilinear=True)
image side abel sad = im.Scale("chars/abel/abel_sad.png", 350, 350, bilinear=True)
image side abel laugh = im.Scale("chars/abel/abel_laugh.png", 350, 350, bilinear=True)
image side abel disgust = im.Scale("chars/abel/abel_disgust.png", 350, 350, bilinear=True)
image side abel surprise = im.Scale("chars/abel/abel_surprise.png", 350, 350, bilinear=True)
image side abel fear = im.Scale("chars/abel/abel_fear.png", 350, 350, bilinear=True)

define c = Character("Cármen Semedo", color="#fb73b4", image="carmen", who_outlines=[(absolute(1), "#000000")])
image side carmen normal = im.Scale("chars/carmen/carmen_normal.png", 350, 350, bilinear=True)
image side carmen angry = im.Scale("chars/carmen/carmen_angry.png", 350, 350, bilinear=True)
image side carmen happy = im.Scale("chars/carmen/carmen_happy.png", 350, 350, bilinear=True)
image side carmen sad = im.Scale("chars/carmen/carmen_sad.png", 350, 350, bilinear=True)
image side carmen laugh = im.Scale("chars/carmen/carmen_laugh.png", 350, 350, bilinear=True)
image side carmen disgust = im.Scale("chars/carmen/carmen_disgust.png", 350, 350, bilinear=True)
image side carmen surprise = im.Scale("chars/carmen/carmen_surprise.png", 350, 350, bilinear=True)

define e = Character("Estrela Nunes", color="#ffa000", image="estrela", who_outlines=[(absolute(1), "#000000")])
image side estrela normal = im.Scale("chars/estrela/estrela_normal.png", 350, 350, bilinear=True)
image side estrela angry = im.Scale("chars/estrela/estrela_angry.png", 350, 350, bilinear=True)
image side estrela happy = im.Scale("chars/estrela/estrela_happy.png", 350, 350, bilinear=True)
image side estrela sad = im.Scale("chars/estrela/estrela_sad.png", 350, 350, bilinear=True)
image side estrela laugh = im.Scale("chars/estrela/estrela_laugh.png", 350, 350, bilinear=True)
image side estrela disgust = im.Scale("chars/estrela/estrela_disgust.png", 350, 350, bilinear=True)

define h = Character("Hélder Almeida", color="#fffac8", image="helder", who_outlines=[(absolute(1), "#000000")])
image side helder normal = im.Scale("chars/helder/helder_normal.png", 350, 350, bilinear=True)
image side helder angry = im.Scale("chars/helder/helder_angry.png", 350, 350, bilinear=True)
image side helder happy = im.Scale("chars/helder/helder_happy.png", 350, 350, bilinear=True)
image side helder sad = im.Scale("chars/helder/helder_sad.png", 350, 350, bilinear=True)
image side helder laugh = im.Scale("chars/helder/helder_laugh.png", 350, 350, bilinear=True)

define i = Character("Isabel Torres", color="#ff2100", image="isabel", who_outlines=[(absolute(1), "#000000")])
image side isabel normal = im.Scale("chars/isabel/isabel_normal.png", 350, 350, bilinear=True)
image side isabel angry = im.Scale("chars/isabel/isabel_angry.png", 350, 350, bilinear=True)
image side isabel happy = im.Scale("chars/isabel/isabel_happy.png", 350, 350, bilinear=True)
image side isabel sad = im.Scale("chars/isabel/isabel_sad.png", 350, 350, bilinear=True)
image side isabel laugh = im.Scale("chars/isabel/isabel_laugh.png", 350, 350, bilinear=True)

define j = Character("Jorge Amaral", color="#ff6300", image="jorge", who_outlines=[(absolute(1), "#000000")])
image side jorge normal = im.Scale("chars/jorge/jorge_normal.png", 350, 350, bilinear=True)
image side jorge angry = im.Scale("chars/jorge/jorge_angry.png", 350, 350, bilinear=True)
image side jorge happy = im.Scale("chars/jorge/jorge_happy.png", 350, 350, bilinear=True)
image side jorge sad = im.Scale("chars/jorge/jorge_sad.png", 350, 350, bilinear=True)
image side jorge laugh = im.Scale("chars/jorge/jorge_laugh.png", 350, 350, bilinear=True)
image side jorge surprise = im.Scale("chars/jorge/jorge_surprise.png", 350, 350, bilinear=True)

define m = Character("Manuela Leitão", color="#00fff2", image="manuela", who_outlines=[(absolute(1), "#000000")])
image side manuela normal = im.Scale("chars/manuela/manuela_normal.png", 350, 350, bilinear=True)
image side manuela angry = im.Scale("chars/manuela/manuela_angry.png", 350, 350, bilinear=True)
image side manuela happy = im.Scale("chars/manuela/manuela_happy.png", 350, 350, bilinear=True)
image side manuela sad = im.Scale("chars/manuela/manuela_sad.png", 350, 350, bilinear=True)
image side manuela laugh = im.Scale("chars/manuela/manuela_laugh.png", 350, 350, bilinear=True)
image side manuela disgust = im.Scale("chars/manuela/manuela_disgust.png", 350, 350, bilinear=True)

define n = Character("Nando Sapina", color="#003cc8", image="nando", who_outlines=[(absolute(1), "#000000")])
image side nando normal = im.Scale("chars/nando/nando_normal.png", 350, 350, bilinear=True)
image side nando angry = im.Scale("chars/nando/nando_angry.png", 350, 350, bilinear=True)
image side nando happy = im.Scale("chars/nando/nando_happy.png", 350, 350, bilinear=True)
image side nando sad = im.Scale("chars/nando/nando_sad.png", 350, 350, bilinear=True)
image side nando laugh = im.Scale("chars/nando/nando_laugh.png", 350, 350, bilinear=True)
image side nando mean = im.Scale("chars/nando/nando_mean.png", 350, 350, bilinear=True)
image side nando annoyed = im.Scale("chars/nando/nando_annoyed.png", 350, 350, bilinear=True)

define p = Character("Patrícia Isidoro", color="#0070c8", image="patricia", who_outlines=[(absolute(1), "#000000")])
image side patricia normal = im.Scale("chars/patricia/patricia_normal.png", 350, 350, bilinear=True)
image side patricia angry = im.Scale("chars/patricia/patricia_angry.png", 350, 350, bilinear=True)
image side patricia happy = im.Scale("chars/patricia/patricia_happy.png", 350, 350, bilinear=True)
image side patricia sad = im.Scale("chars/patricia/patricia_sad.png", 350, 350, bilinear=True)
image side patricia laugh = im.Scale("chars/patricia/patricia_laugh.png", 350, 350, bilinear=True)
image side patricia disgust = im.Scale("chars/patricia/patricia_disgust.png", 350, 350, bilinear=True)
image side patricia annoyed = im.Scale("chars/patricia/patricia_annoyed.png", 350, 350, bilinear=True)
image side patricia surprise = im.Scale("chars/patricia/patricia_surprise.png", 350, 350, bilinear=True)

define r = Character("Rui Bento", color="#00c38c", image="rui", who_outlines=[(absolute(1), "#000000")])
image side rui normal = im.Scale("chars/rui/rui_normal.png", 350, 350, bilinear=True)
image side rui angry = im.Scale("chars/rui/rui_angry.png", 350, 350, bilinear=True)
image side rui happy = im.Scale("chars/rui/rui_happy.png", 350, 350, bilinear=True)
image side rui sad = im.Scale("chars/rui/rui_sad.png", 350, 350, bilinear=True)
image side rui laugh = im.Scale("chars/rui/rui_laugh.png", 350, 350, bilinear=True)
image side rui annoyed = im.Scale("chars/rui/rui_annoyed.png", 350, 350, bilinear=True)

define s = Character("Samuel Andrade", color="#ffe119", image="samuel", who_outlines=[(absolute(1), "#000000")])
image side samuel normal = im.Scale("chars/samuel/samuel_normal.png", 350, 350, bilinear=True)
image side samuel angry = im.Scale("chars/samuel/samuel_angry.png", 350, 350, bilinear=True)
image side samuel happy = im.Scale("chars/samuel/samuel_happy.png", 350, 350, bilinear=True)
image side samuel sad = im.Scale("chars/samuel/samuel_sad.png", 350, 350, bilinear=True)
image side samuel laugh = im.Scale("chars/samuel/samuel_laugh.png", 350, 350, bilinear=True)
image side samuel surprise = im.Scale("chars/samuel/samuel_surprise.png", 350, 350, bilinear=True)

define t = Character("Tatiana Delgado", color="#79c65d", image="tatiana", who_outlines=[(absolute(1), "#000000")])
image side tatiana normal = im.Scale("chars/tatiana/tatiana_normal.png", 350, 350, bilinear=True)
image side tatiana angry = im.Scale("chars/tatiana/tatiana_angry.png", 350, 350, bilinear=True)
image side tatiana happy = im.Scale("chars/tatiana/tatiana_happy.png", 350, 350, bilinear=True)
image side tatiana sad = im.Scale("chars/tatiana/tatiana_sad.png", 350, 350, bilinear=True)
image side tatiana laugh = im.Scale("chars/tatiana/tatiana_laugh.png", 350, 350, bilinear=True)
image side tatiana cry = im.Scale("chars/tatiana/tatiana_cry.png", 350, 350, bilinear=True)
image side tatiana surprise = im.Scale("chars/tatiana/tatiana_surprise.png", 350, 350, bilinear=True)

label setup:
    $ gameworld.AddArea(Area('Patio', 'areas/patio1.jpg'))          # 1
    $ gameworld.AddArea(Area('Escadas1A', 'areas/esc1a.jpg'))       # 2
    $ gameworld.AddArea(Area('Escadas1B', 'areas/esc1b.jpg'))       # 3
    $ gameworld.AddArea(Area('Corredor1', 'areas/corr1.jpg'))       # 4
    $ gameworld.AddArea(Area('Sala1', 'areas/sala1.jpg'))           # 5
    $ gameworld.AddArea(Area('Biblioteca', 'areas/biblio1a.jpg'))   # 6
    $ gameworld.AddArea(Area('Gabinete', 'areas/gab1b.jpg'))        # 7
    $ gameworld.AddArea(Area('Escadas2A', 'areas/esc2a.jpg'))       # 8
    $ gameworld.AddArea(Area('Escadas2B', 'areas/esc2b.jpg'))       # 9
    $ gameworld.AddArea(Area('Corredor2', 'areas/corr2.jpg'))       # 10
    $ gameworld.AddArea(Area('Sala2', 'areas/sala2.jpg'))           # 11
    $ gameworld.AddArea(Area('Estudo', 'areas/estudo2b.jpg'))       # 12
    $ gameworld.AddConnection(Connection([1,2], Time(0, 0, 60), [[230,445],[910,980]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [270, 180], [1,1]))
    $ gameworld.AddConnection(Connection([1,3], Time(0, 0, 60), [[1090,450],[910,980]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [0, 180], [1,1]))
    $ gameworld.AddConnection(Connection([2,4], Time(0, 0, 20), [[1850,490],[0,490]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [90, 270], [1,1]))
    $ gameworld.AddConnection(Connection([2,6], Time(0, 0, 20), [[190,500],[1850,490]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [0, 90], [1,1]))
    $ gameworld.AddConnection(Connection([2,8], Time(0, 0, 30), [[910,200],[250,700]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [315, 180], [1,1]))
    $ gameworld.AddConnection(Connection([3,4], Time(0, 0, 20), [[0,490],[1850,490]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [270, 90], [1,1]))
    $ gameworld.AddConnection(Connection([3,7], Time(0, 0, 20), [[1658,500],[0,490]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [0, 270], [1,1]))
    $ gameworld.AddConnection(Connection([3,9], Time(0, 0, 30), [[930,200],[1800,600]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [45, 135], [1,1]))
    $ gameworld.AddConnection(Connection([4,5], Time(0, 0, 20), [[1200,550],[1750,450]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [90, 90], [1,1]))
    $ gameworld.AddConnection(Connection([8,10], Time(0, 0, 20), [[1850,490],[0,490]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [90, 270], [1,1]))
    $ gameworld.AddConnection(Connection([9,10], Time(0, 0, 20), [[0,490],[1850,490]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [270, 90], [1,1]))
    $ gameworld.AddConnection(Connection([10,11], Time(0, 0, 20), [[620,550],[220,450]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [270, 270], [1,1]))
    $ gameworld.AddConnection(Connection([9,12], Time(0, 0, 20), [[900,550],[1850,490]], 
        ['connection_red','connection_red'], ['connection_yellow','connection_yellow'], [270, 90], [1,1]))
    return

label setup1:
    $ session = 1
    $ tasklist = [1, 1, 0, 0, 0, 0]
    $ task_space = [5, 11, 6, 12, 11, 1]
    $ tasks = [
        Task("Tarefa: Tirar dúvidas", 5, "tasks/t1i.png", "tasks/t1h.png", 700, 253, 0, 0.2),
        Task("Tarefa: Preparar apresentação", 11, "tasks/t2i.png", "tasks/t2h.png", 1550, 650, 0, 1),
        Task("Tarefa: Tirar fotocópias", 6, "tasks/t3i.png", "tasks/t3h.png", 100, 500, 0, 0.35),
        Task("Tarefa: Ajudar colega", 12, "tasks/t4i.png", "tasks/t4h.png", -300, 200, 0, 1),
        Task("Tarefa: Fazer exercícios", 11, "tasks/t5i.png", "tasks/t5h.png", 500, 680, 0, .2),
        Task("Tarefa: Comprar rifa", 1, "tasks/t6i.png", "tasks/t6h.png", 1300, 350, 0, 0.35)
    ]

    $ gameworld.AddChar(Char("Abel", "", "", 0, "chars/abel/body.png"))         # 1
    $ gameworld.AddChar(Char("Carmen", "", "", 0, "chars/carmen/body.png"))     # 2
    $ gameworld.AddChar(Char("Estrela", "", "", 0, "chars/estrela/body.png"))   # 3
    $ gameworld.AddChar(Char("Helder", "", "", 0, "chars/helder/body.png"))     # 4
    $ gameworld.AddChar(Char("Isabel", "", "", 0, "chars/isabel/body.png"))     # 5
    $ gameworld.AddChar(Char("Jorge", "", "", 0, "chars/jorge/body.png"))       # 6
    $ gameworld.AddChar(Char("Manuela", "", "", 0, "chars/manuela/body.png"))   # 7
    $ gameworld.AddChar(Char("Nando", "", "", 0, "chars/nando/body.png"))       # 8
    $ gameworld.AddChar(Char("Patricia", "", "", 0, "chars/patricia/body.png")) # 9
    $ gameworld.AddChar(Char("Rui", "", "", 0, "chars/rui/body.png"))           # 10
    $ gameworld.AddChar(Char("Samuel", "", "", 0, "chars/samuel/body.png"))     # 11
    $ gameworld.AddChar(Char("Tatiana", "", "", 0, "chars/tatiana/body.png"))   # 12

    $ gameworld.AddDialogue(Dialogue_Chat("JS", [6,11], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("AN", [1,8], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("IT", [5,12], "", True, {}, {}, True, True))
    $ gameworld.AddDialogue(Dialogue_Chat("HI", [4,5], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("JN", [6,8], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("AR", [1,10], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("ES", [3,11], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("T", [12], "", True, {}, {}, True, True))
    if socialidade > 2:
        $ gameworld.AddDialogue(Dialogue_Chat("T", [12], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    if socialidade > 3:
        $ gameworld.AddDialogue(Dialogue_Chat("T", [12], "", True, {}, {}, True, True))
        $ gameworld.AddDialogue(Dialogue_Chat("T", [12], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    $ gameworld.AddDialogue(Dialogue_Chat("EHR", [3,4,10], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("CMP", [2,7,9], "", True, {}, {}, True, False))
    return
label setup2:
    $ situation = 10
    $ day = 2
    $ tasklist[2] = 1
    $ tasklist[3] = 1
    if tasklist[1] == 1:
        $ tasklist[1] = 3

    $ gameworld_runtime.dialogues = {}
    $ gameworld_runtime.dialogues_activeprio = []
    #$ gameworld_runtime.dialogues_active = []
    #$ gameworld_runtime.dialogues_available = []
    #$ gameworld_runtime.dialogues_occurred = []

    $ gameworld_runtime.AddDialogue(Dialogue_Chat("E", [3], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("ST", [11,12], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("JN", [6,8], "", True, {}, {}, True, True))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("AIR", [1,5,10], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("H", [4], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("CMP", [2,7,9], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("EST", [3,11,12], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("N", [8], "", True, {}, {}, True, True))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("HI", [4,5], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("C", [2], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("AJR", [1,6,10], "", True, {}, {}, True, False))
    if socialidade > 2:
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("N", [8], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    if socialidade > 3:
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("JN", [6,8], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    if socialidade > 4:
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("MP", [7,9], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    return
label setup3:
    $ situation = 20
    $ day = 3
    $ tasklist[4] = 1
    $ tasklist[5] = 1
    if tasklist[3] == 1:
        $ tasklist[3] = 3
    $ gameworld_runtime.dialogues = {}
    $ gameworld_runtime.dialogues_activeprio = []

    #$ gameworld.AddDialogue(Dialogue_Chat("ACEHMNP", [], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("AJR", [1,6,10], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("ST", [11,12], "", True, {}, {}, True, True))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("EH", [3,4], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("IM", [5,7], "", True, {}, {}, True, False))
    if socialidade > 2: 
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("CNP", [2,8,9], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    if socialidade > 3: 
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("CP", [], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("AN", [1,8], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("M", [7], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("H", [4], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("JST", [6,11,12], "", True, {}, {}, True, False))
    if socialidade > 4: 
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("EIR", [3,5,10], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    return

label start:
    "Bem vindo ao jogo! Vamos começar com um pequeno tutorial. Clica com o rato para passares entre mensagens."
    jump tutorial
    
label tutorial:
    "Tu és um aluno do 9º ano que se juntou a uma turma recentemente, e tens 3 objetivos no jogo:"
    "1. Ter boas notas nos testes e exames para poder ir à viagem de finalistas"
    "2. Investigar situações de cyberbullying, descobrir informação e refletir sobre elas"
    "3. Fazer as tuas tarefas de aluno"
    "Cada um destes objetivos é igualmente importante, por isso tens de tentar manter um equílibrio para conseguir fazer tudo o melhor que puderes."
    image tutorialscene:
        "areas/patio1.jpg"
        size (config.screen_width, config.screen_height)
    scene tutorialscene
    "Em termos de jogabilidade, o jogo é jogado apenas com o rato."
    image tutorialarrow:
        "connections/red.png"
        size (50, 50)
        xpos 240
        ypos 510
        rotate 270
    show tutorialarrow
    "Para andar entre areas, basta clicares nas setas vermelhas que aparecem."
    image tutorialchat:
        "chars/estrela/body.png"
        xpos 1440
        ypos 910
        zoom 0.7
    show tutorialchat
    "Para além de andar pela escola, podes interagir com personagens, escutando as conversas entre elas."
    image tutorialtask:
        "tasks/t2i.png"
        xpos 740
        ypos 710
        zoom 0.7
    show tutorialtask
    "Também podes interagir com objetos ou pessoas para concluires as tuas tarefas."
    show screen clock
    "Em cima à esquerda, tens acesso a vários menus. Vamos agora falar sobre cada um, começando da esquerda para a direita."
    "{b}{u}Estatísticas{/b}{/u} - Ao longo do jogo, poderás aumentar e diminuir as tuas estatísticas."
    "Cada estatística tem um objetivo diferente:\n
    - Conhecimento: ajuda-te a ter melhores notas\n
    - Energia: ajuda-te a ser mais eficiente\n
    - Socialidade: ajuda-te a investigar o caso de cyberbullying"
    "{b}{u}Tarefas{/b}{/u} - A tua lista de tarefas. Tem atenção que algumas delas têm prioridade sobre outras."
    "{b}{u}Mapa{/b}{/u} - Um mapa da escola, para te conseguires orientar melhor."
    "{b}{u}Casa{/b}{/u} - O jogo está dividido em tempos na escola, e tempos em casa. Sempre que quiseres ir para casa mais cedo, podes usar este botão."
    "{b}{u}Pensamentos{/b}{/u} - Consoante o caso de cyberbullying, este menu ajuda-te a saberes como proceder a investigação do caso. Os alunos comunicam numa rede social chamada Com@Viver à qual tu não tens acesso, e tens de investigar o que despoletou as situações/conversas entre os alunos."
    "Depois de observares certos acontecimentos entre alunos, os teus pensamentos serão atualizados. Sempre que quiseres feedback nas tuas reflexões sobre o caso, podes visitar a psicóloga da escola, Joana, no seu gabinete."
    "{b}{u}Relógio{/b}{/u} - Andar pela escola, fazer tarefas e escutar conversas custa tempo. Quando estás na escola, terás 30 minutos para fazer o que quiseres. Após o tempo acabar, irás para casa e a história avancará."
    "O teu objetivo como jogador é gerir o teu tempo para completares os 3 objetivos. Sempre que quiseres ver o tutorial novamente, podes clicar no ? ao lado do relógio."
    if session == 0:
        jump start1
    else:
        call algo(action=Action.Movement, next_area=nextarea)

label start1:
    python:
        player_name = renpy.input("Insere o teu nome:", length=20)
        player_name = player_name.strip()
        player_name = player_name.title()

        if not player_name:
            player_name = "Jogador"
        player_name_dim = player_name.split()[0]
    "Escolhe a tua personagem {w=2}{nw}"
    call screen pick_char
    jump start2

screen pick_char:
    hbox:
        xalign 0.5
        yalign 0.5
        for ii in range(4): 
            vbox:
                for jj in range(3):
                    frame:
                        imagebutton:
                            idle "player/"+str(ii*3+jj+1)+".png"
                            action SetVariable('player_img', ii*3+jj+1), Jump('start2')

label start2:
    $ send_marker("After name")
    image side player_image:
        choice(player_img == 1):
            Transform("player/1.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 2):
            Transform("player/2.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 3):
            Transform("player/3.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 4):
            Transform("player/4.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 5):
            Transform("player/5.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 6):
            Transform("player/6.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 7):
            Transform("player/7.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 8):
            Transform("player/8.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 9):
            Transform("player/9.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 10):
            Transform("player/10.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 11):
            Transform("player/11.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
        choice(player_img == 12):
            Transform("player/12.png", xsize=400, ysize=437, xoffset=-22,yoffset=25)
    jump start3

label start3:
    call setup
    call setup1
    $ gameworld_runtime = Gameworld_RUNTIME()
    $ gameworld_runtime.time = Time(12, 30, 0)
    $ gameworld_runtime.dialogues_available = list(gameworld_runtime.dialogues.values())
    #$ gameworld_runtime.dialogues_available.append(gameworld_runtime.dialogues_active.copy())
    #$ gameworld_runtime.dialogues_active = []
    $ triggerstack = []
    $ currentarea = ""
    $ nextarea = ""
    $ currentdialogue = ""
    $ currentspeaker = []
    $ placeddialogues = {}
    $ populatetimer = 60
    $ area_visits = {}
    $ connection_visits = {}

    $ currentarea = gameworld_runtime.areas[6]
    $ nextarea = gameworld_runtime.areas[6]
    call stat_check0
    python:
        for a in gameworld_runtime.areas:
            area_visits[a] = 0
        for a in gameworld_runtime.connections:
            connection_visits[a] = 0
        for d in gameworld_runtime.dialogues_available.copy():
            gameworld_runtime.dialogues_available.remove(d)
            if d.priority:
                gameworld_runtime.dialogues_activeprio.append(d)
            else:
                gameworld_runtime.dialogues_active.append(d)
    $ renpy.set_return_stack([])
    jump intro

label start4:
    call setup2
    $ gameworld_runtime.time = Time(12, 30, 0)
    $ gameworld_runtime.dialogues_available = list(gameworld_runtime.dialogues.values())
    $ gameworld_runtime.dialogues_available[0:0] = gameworld_runtime.dialogues_active.copy()
    $ gameworld_runtime.dialogues_active = []
    $ triggerstack = []
    $ currentarea = ""
    $ nextarea = ""
    $ currentdialogue = ""
    $ currentspeaker = []
    $ placeddialogues = {}
    $ populatetimer = 60
    $ area_visits = {}
    $ connection_visits = {}

    $ currentarea = gameworld_runtime.areas[11]
    $ nextarea = gameworld_runtime.areas[11]
    python:
        for a in gameworld_runtime.areas:
            area_visits[a] = 0
        for a in gameworld_runtime.connections:
            connection_visits[a] = 0
        print(gameworld_runtime.dialogues_available.copy())
        for d in gameworld_runtime.dialogues_available.copy():
            gameworld_runtime.dialogues_available.remove(d)
            if d.priority:
                gameworld_runtime.dialogues_activeprio.append(d)
            else:
                gameworld_runtime.dialogues_active.append(d)
    $ renpy.set_return_stack([])
    jump aula2
    
label start5:
    call setup3
    $ gameworld_runtime.time = Time(12, 30, 0)
    $ gameworld_runtime.dialogues_available = list(gameworld_runtime.dialogues.values())
    $ gameworld_runtime.dialogues_available[0:0] = gameworld_runtime.dialogues_active.copy()
    $ gameworld_runtime.dialogues_active = []
    $ triggerstack = []
    $ currentarea = ""
    $ nextarea = ""
    $ currentdialogue = ""
    $ currentspeaker = []
    $ placeddialogues = {}
    $ populatetimer = 60
    $ area_visits = {}
    $ connection_visits = {}

    $ currentarea = gameworld_runtime.areas[5]
    $ nextarea = gameworld_runtime.areas[5]
    python:
        for a in gameworld_runtime.areas:
            area_visits[a] = 0
        for a in gameworld_runtime.connections:
            connection_visits[a] = 0
        for d in gameworld_runtime.dialogues_available.copy():
            gameworld_runtime.dialogues_available.remove(d)
            if d.priority:
                gameworld_runtime.dialogues_activeprio.append(d)
            else:
                gameworld_runtime.dialogues_active.append(d)
    $ renpy.set_return_stack([])
    jump aula3

screen post:
    zorder 3
    button:
        background "#00000080"
        xsize 1920
        ysize 1080
        action NullAction()
    frame:
        xsize 1200
        ysize 700
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            frame:
                text "{i}{b}BossLikeMe14:{/b} \"Tatiana sua otária, és feia e gorda! Nem\n penses que vais na viagem de finalistas! LOL!\""
            hbox:
                spacing 10
                if show_image:
                    frame:
                        add "post.png":
                            xsize 384
                            ysize 576
                        #else:
                        #    xsize 384
                        #    ysize 576
                        #    background "black"
                vbox:
                    yalign 0.5
                    spacing 5
                    frame:
                        text "{i}{b}~Patrícia Isidoro{/b} colocou um gosto"
                    text ""
                    frame:
                        xsize 700
                        text "{b}~Abel Polido:{/b} \"Nando gostas mazé dela man! Mesmo se anda com todos. LOL!\""
                    frame:
                        xsize 700
                        text "{b}~Manuela Leitão:{/b} \"Ela só tem gordura! LOL!\""
                    frame:
                        xsize 700
                        text "{b}~Cármen Semedo:{/b} \"Eu não vou se ela for!\""
                    frame:
                        xsize 700
                        text "{b}~Rui Bento:{/b} \"Malta! Parem lá com isso! Não quero gente ordinária na viagem.\""
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle Transform("xi.png", xsize=100, ysize=100)
        hover Transform("xh.png", xsize=100, ysize=100)
        action Hide('post'), Jump('aula3.afterpost')

label aula3:
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,1,1)
    $ situation = 25
    "{i}Passados mais alguns dias, antes do início de uma aula"
    "{i}Aproxima-se um colega teu"
    aluno "Oi, [player_name]. Uma amiga minha partilhou este post comigo. A Cármen é da tua turma, não é?"
    "{i}O aluno mostra o telefone dele"
    $ send_marker("before POST S1")
    call screen post
    label .afterpost:
        $ send_marker("after POST S1")
        "{i}A aula vai começar, os alunos estão-se a sentar"
        gameworld_runtime.player.character "{i}Hoje vamos receber um teste."
        image currentscene:
            currentarea.background
            size (config.screen_width, config.screen_height)
        scene currentscene with Fade(1,0,1)
        "{i}Após a aula"
        $ nota_s1 = "3* Normal"
        if conhecimento == 1:
            $ nota_s1 = "1* Fraca"
            gameworld_runtime.player.character "{i}Tive uma nota fraquíssima... Se continuar assim, não vou poder ir à viagem de finalistas."
        if conhecimento == 2:
            $ nota_s1 = "2* Má"
            gameworld_runtime.player.character "{i}Tive uma má nota, preciso de estudar mais..."
        if conhecimento == 4:
            $ nota_s1 = "4* Boa"
            gameworld_runtime.player.character "{i}Tive uma boa nota, o estudo compensou!"
        if conhecimento == 5:
            $ nota_s1 = "5* Excelente"
            gameworld_runtime.player.character "{i}Tive uma nota excelente, viagem de finalistas aqui vou eu!"
        gameworld_runtime.player.character "{i}Parece que foi o Nando que fez o post. Se calhar a situação foi longe de mais. Tenho de pensar como prosseguir."
        gameworld_runtime.player.character "{i}Estou na sala B. As aulas acabaram, tenho 30 minutos até ter de ir para casa. Tenho tarefas para fazer. O que faço?"
        show screen clock
        
        call algo(action=Action.Movement, next_area=nextarea)
        "something went wrong"

label aula2:
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,1,1)
    $ situation = 20
    $ send_marker("before S1 SITUATION 2")
    "{i}Passados alguns dias, no final de uma aula"
    i sad "Malta, já sabem o que aconteceu à Tatiana?"
    e normal "O quê? Não sei de nada."
    i angry "Andam a partilhar uma foto dela em biquíni a dizer que ela é feia e gorda."
    s sad "Eu até acho que ela está bem gira."
    i angry "Isto é bué grave! Ela tem estado fechada na casa de banho."
    c angry "Ela é que leva tudo a sério! Foi só no gozo."
    e angry "Dizes isso porque não é contigo!"
    s angry "Temos de fazer alguma coisa para a ajudar."
    h angry "Epá não sei se me vou meter nesse filme. Ainda sobra para nós!"
    $ send_marker("after S1 SITUATION 2")
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,0,1)
    call setup_dragndrops20
    gameworld_runtime.player.character "{i}Está confirmado que a Tatiana era a pessoa no post. Mas se não foi ela que postou, quem terá sido?"
    gameworld_runtime.player.character "{i}Estou na sala A. As aulas acabaram, tenho 30 minutos até ter de ir para casa. Tenho tarefas para fazer. O que faço?"
    show screen clock
    call algo(action=Action.Movement, next_area=nextarea)
    "something went wrong"

label intro:
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,1,1)
    gameworld_runtime.player.character "{i}Estou na biblioteca. As aulas acabaram, tenho 30 minutos até ter de ir para casa. Tenho tarefas para fazer. O que faço?"
    show screen clock
    call algo(action=Action.Movement, next_area=nextarea)
    "something went wrong"

label algo(action, next_area):
    hide screen exitchat
    show screen clock
    if gameworld_runtime.time.hour > 12:
        gameworld_runtime.player.character "{i}Já são 13h00. Tenho de ir para casa."
        jump home
    #python:
        # updates world gamestates
        #for g in list(gameworld_runtime.gamestates.values()):
        #    if g.GetType() > 3:
        #        if g.Prime():
        #            g.value = True
        #        else:
        #            g.value = False
        # checks dialogues
        #for d in gameworld_runtime.dialogues_available.copy():
        #    gameworld_runtime.dialogues_available.remove(d)
        #    if d.priority:
        #        gameworld_runtime.dialogues_activeprio.append(d)
        #    else:
        #        gameworld_runtime.dialogues_active.append(d)
            #triggered = True
            #for gid,value in list(d.preconditions.items()):
            #    if value != gameworld_runtime.gamestates[gid].value:
            #        triggered = False
            #        break
            #    elif d.single_trigger:
            #        break
            #if triggered:
            #    gameworld_runtime.dialogues_available.remove(d)
            #    if d.priority:
            #        gameworld_runtime.dialogues_activeprio.append(d)
            #    else:
            #        gameworld_runtime.dialogues_active.append(d)
        #gameworld_runtime.dialogues_active.sort()
        #for d in gameworld_runtime.dialogues_active:
        #    if d.GetType() == 1:
        #        currentdialogue = d
        #        renpy.call(dialogue)
        # checks tasks
        #for t in gameworld_runtime.tasks_available.copy():
        #    print(t)
        #    print(t)
        #    print(t)
        #    triggered = True
        #    for gid,value in list(t.preconditions.items()):
        #        if value != gameworld_runtime.gamestates[gid].value:
        #            triggered = False
        #            break
        #        elif t.single_trigger:
        #            break
        #    if triggered:
        #        print("reeee")
        #        print("reeee")
        #        print("reeee")
        #        gameworld_runtime.tasks_available.remove(d)
        #        gameworld_runtime.tasks_active.append(t)
        # checks events
        #for e in gameworld_runtime.events_available.copy():
        #    triggered = True
        #    for gid,value in list(e.preconditions.items()):
        #        if value != gameworld_runtime.gamestates[gid].value:
        #            triggered = False
        #            break
        #        elif e.single_trigger:
        #            result = e.Trigger()
        #            if result != "":
        #                triggerstack.append(result)
        #            gameworld_runtime.Consequences(e.consequences)
        #            break
    if populatetimer >= 60:
        $ populatetimer = 0
        $ gameworld_runtime.Populate()
    $ renpy.set_return_stack([])
    $ nextarea = next_area
    jump expression 'room'

label room:
    if nextarea.locked:
        $ nextarea = currentarea
        "Cannot access room: locked"
        jump room
    else:
        $ currentarea = nextarea
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene
    if fadeinto:
        $ fadeinto = False
        call screen room with Fade(.8,0,.8)
    call screen room

screen room:
    if currentarea.id in placeddialogues:
        default nchars = len(placeddialogues[currentarea.id].chars)
        default composite_args = [(300*nchars,880)]
        for i in range(nchars):
            $ composite_args.append((250*i, 0))
            $ composite_args.append(gameworld_runtime.chars[placeddialogues[currentarea.id].chars[i]].body)
        default idle_image = Composite(*composite_args)
        default sol = Solid("#FFEE97", xsize=1920, ysize=880, xalign=0.5, yalign=0.5)
        default hover_image = AlphaMask(Solid("#fff", xsize=300*nchars+100, ysize=880, xalign=0.5, yalign=0.5), idle_image)
        imagebutton:
            xpos d_coords[currentarea.id][0]
            ypos d_coords[currentarea.id][1]
            idle Transform(idle_image, zoom=d_size[currentarea.id])
            hover Transform(hover_image, zoom=d_size[currentarea.id])
            action Jump('dialogue')
            focus_mask True
    else:
        if session == 1 and situation == 0 and currentarea.id in {1,2,3,4,8,9,10}:
            timer 1 action Jump('d_day.chat_cb1')
        if session == 1 and situation == 25 and currentarea.id in {1,2,3,4,8,9,10}:
            timer 1 action Jump('d_day.chat_cb3')
        if session == 2 and situation == 0 and currentarea.id in {1,2,3,4,8,9,10}:
            timer 1 action Jump('d_day2.chat_cb1')
        if session == 2 and situation == 55 and currentarea.id in {1,2,3,4,8,9,10}:
            timer 1 action Jump('d_day2.chat_cb3')
        if currentarea.id == 7:
            default idle_image = "psicologa.png"
            default sol = Solid("#FFEE97", xsize=1920, ysize=1080)
            default hover_image = AlphaMask(Solid("#fff", xsize=1920, ysize=1080), idle_image)
            imagebutton:
                xpos 500
                ypos 351
                idle Transform(idle_image)
                hover Transform(hover_image)
                action Jump('d_psicologa')
                focus_mask True
    #for t in gameworld_runtime.tasks_active:
    #    if t.area == currentarea.id:
    #        imagebutton:
    #            xpos t.icon_x
    #            ypos t.icon_y
    #            idle Frame(t.icon_idle)
    #            hover Frame(t.icon_hover)
    #            at rot(t.icon_rotation)
    #            xsize int(100*t.icon_size)
    #            ysize int(100*t.icon_size)
    #            action SetVariable('currenttask', t), Jump('task')
    #            focus_mask True
    for t in range(len(tasklist)):
        if tasklist[t] == 1 and task_space[t] == currentarea.id:
            imagebutton:
                xpos tasks[t].icon_x
                ypos tasks[t].icon_y
                idle Transform(tasks[t].icon_idle, zoom=tasks[t].icon_size)
                hover Transform(tasks[t].icon_hover, zoom=tasks[t].icon_size)
                at rot(tasks[t].icon_rotation)
                action SetVariable('currenttask', t), Jump('task')
                focus_mask True
                tooltip tasks[t].name
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                xalign 0.1
                text tooltip
    for c_id in currentarea.connections:
        imagebutton:
            xpos gameworld.connections[c_id].icon_xy[gameworld.connections[c_id].Index(currentarea.id)][0]
            ypos gameworld.connections[c_id].icon_xy[gameworld.connections[c_id].Index(currentarea.id)][1]
            idle Frame(gameworld.connections[c_id].icon_idle[gameworld.connections[c_id].Index(currentarea.id)])
            hover Frame(gameworld.connections[c_id].icon_hover[gameworld.connections[c_id].Index(currentarea.id)])
            at rot(gameworld.connections[c_id].icon_rotation[gameworld.connections[c_id].Index(currentarea.id)])
            xsize int(50*gameworld.connections[c_id].icon_size[gameworld.connections[c_id].Index(currentarea.id)])
            ysize int(50*gameworld.connections[c_id].icon_size[gameworld.connections[c_id].Index(currentarea.id)])
            action [If(currentarea.id in {5,6,7,11,12} or (currentarea.connections[c_id] in {5,6,7,11,12}), SetVariable('fadeinto', True)), Function(AddTime, gameworld_runtime.time, gameworld.connections[c_id].time),
                IncrementVariable('populatetimer', gameworld.connections[c_id].time.second), Call('algo', action=Action.Movement, next_area=gameworld_runtime.areas[currentarea.connections[c_id]])]
            focus_mask True

label dialogue:
    $ renpy.set_return_stack([])
    $ currentdialogue = placeddialogues[currentarea.id]
    $ registo += '\nDialogue '+str(currentdialogue.name)+" "+str(currentdialogue.id)
    $ placeddialogues.pop(currentarea.id)
    if currentdialogue.priority:
        $ gameworld_runtime.dialogues_activeprio.remove(currentdialogue)
    else:
        $ gameworld_runtime.dialogues_active.remove(currentdialogue)
    $ gameworld_runtime.dialogues_occurred.append(currentdialogue)
    $ populatetimer = 60
    show screen exitchat
    hide screen clock
    hide screen clock_fade
    if session == 1:
        jump expression 'd_day.chat_'+str(currentdialogue.id)
    if session == 2:
        jump expression 'd_day2.chat_'+str(currentdialogue.id)
    #show screen exitchat
    #python:
    #    gameworld_runtime.dialogues_active.remove(currentdialogue)
    #    gameworld_runtime.dialogues_occurred.append(currentdialogue)
    #    gameworld_runtime.Consequences(currentdialogue.consequences)
    #    populatetimer = 60
    #    for dline in currentdialogue.lines:
    #        currentspeaker = [dline[0],dline[1]]
    #        if dline[0] == 0:
    #            renpy.say(gameworld_runtime.player, dline[2])
    #        else:
    #            renpy.say(gameworld_runtime.chars[dline[0]].character, dline[2])
    #        AddSeconds(gameworld_runtime.time, 3)
    #hide screen exitchat
    #call algo(action=Action.Movement, next_area=currentarea) from _call_algo_1

label task:
    $ registo += '\nTask '+str(currenttask)
    $ renpy.set_return_stack([])
    $ tasklist[currenttask] = 2
    if session == 1:
        jump task1
    elif session == 2:
        jump task2
label task1:
    if currenttask == 0:
        gameworld_runtime.player.character "Posso tirar uma dúvida professor?"
        professor "Claro, como posso ajudar?"
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Tirei as dúvidas que tinha."
        $ AddSeconds(gameworld_runtime.time, int(780*(1-0.1*energia)))
        show screen clock
    elif currenttask == 1:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Acabei a minha parte da apresentação."
        $ AddSeconds(gameworld_runtime.time, int(840*(1-0.1*energia)))
        show screen clock
    elif currenttask == 2:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Tirei as fotocópias dos apontamentos."
        $ AddSeconds(gameworld_runtime.time, int(480*(1-0.1*energia)))
        show screen clock
    elif currenttask == 3:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Ajudei o meu colega a fazer os trabalhos de casa."
        $ AddSeconds(gameworld_runtime.time, int(900*(1-0.1*energia)))
        show screen clock
    elif currenttask == 4:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Acabei os exercícios que a professora pediu."
        $ AddSeconds(gameworld_runtime.time, int(1200*(1-0.1*energia)))
        show screen clock
    elif currenttask == 5:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Comprei uma rifa para ajudar a suportar o canil."
        $ AddSeconds(gameworld_runtime.time, int(240*(1-0.1*energia)))
        show screen clock
    #$ renpy.set_return_stack([])
    #python:
    #    gameworld_runtime.tasks_active.remove(currenttask)
    #    gameworld_runtime.tasks_occurred.append(currenttask)
    #    gameworld_runtime.Consequences(currenttask.consequences)
    call algo(action=Action.Movement, next_area=currentarea)

screen exitchat:
    zorder 1
    
    #if currentspeaker != []:
    #    add "editor/portraits/portrait ([currentspeaker[0]])/portrait ([currentspeaker[1]]).png":
    #        xalign 0.0
    #        yalign 1.0
    #        xsize 350
    #        ysize 350
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle Transform("xi.png", xsize=100, ysize=100)
        hover Transform("xh.png", xsize=100, ysize=100)
        action Hide('exitchat'), Call('algo', action=Action.Movement, next_area=currentarea)
        tooltip "Deixar de ouvir"
    
    $ tooltip = GetTooltip()
    if tooltip:
        frame:
            xalign 0.94
            yalign 0.02
            text "[tooltip]"

screen clock:
    zorder 1
    frame:
        xalign 1.0
        yalign 0.0
        xsize 110
        ysize 60
        frame:
            background "black"
    frame:
        xsize 50
        ysize 50
        xpos 1750
        ypos 7
        textbutton "?":
            xalign 0.5
            yalign 0.5
            text_color "#333"
            action Jump("tutorial")
    if situation > 0:
        imagebutton:
            xpos 290
            ypos 5
            idle Transform("case.png", xsize=64, ysize=64)
            at zoom_hover
            action Jump('case_help')
    imagebutton:
        xpos 220
        ypos 5
        idle Transform("house.png", xsize=64, ysize=64)
        at zoom_hover
        action Show('house')
    imagebutton:
        xpos 150
        ypos 5
        idle Transform("map.png", xsize=64, ysize=64)
        at zoom_hover
        action Show('map')
    imagebutton:
        xpos 80
        ypos 5
        idle Transform("tasks/menu.png", xsize=64, ysize=64)
        at zoom_hover
        action Show('task_list')
    imagebutton:
        xpos 5
        ypos 5
        idle Transform("avatar.png", xsize=64, ysize=64)
        at zoom_hover
        action Show('avatar_stats')
    if session == 0:
        text "12:43":
            size 50
            xpos 1820
            ypos 10
            font "digital-7.ttf"
            color "#eee"
        imagebutton:
            xpos 290
            ypos 5
            idle Transform("case.png", xsize=64, ysize=64)
            at zoom_hover
            action Jump('case_help')
        button:
            background "#00000000"
            xsize 1920
            ysize 100
            action NullAction()
    else:
        text str(gameworld_runtime.time)[:5]:
            size 50
            xpos 1820
            ypos 10
            font "digital-7.ttf"
            if gameworld_runtime.time.minute >= 30:
                if gameworld_runtime.time.minute < 35:
                    color "#0ea"
                elif gameworld_runtime.time.minute < 40:
                    color "#0e0"
                elif gameworld_runtime.time.minute < 45:
                    color "#ae0"
                elif gameworld_runtime.time.minute < 50:
                    color "#ee0"
                elif gameworld_runtime.time.minute < 55:
                    color "#ea0"
                else:
                    color "#e00"
            else:
                color "#e00"
    timer 1 repeat True action ToggleScreen('clock_fade')

screen map:
    zorder 3
    button:
        background "#00000080"
        xsize 1920
        ysize 1080
        action Hide('map')
    add "map1.png"
    text "Pátio":
        xpos 865
        ypos 865
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        color "#eee"
    #text "Escadas":
    #    xpos 620
    #    ypos 665
    #    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    #    color "#eee"
    #text "Corredor":
    #    xpos 865
    #    ypos 665
    #    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    #    color "#eee"
    text "Sala B":
        xpos 865
        ypos 465
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        color "#eee"
    text "Biblioteca":
        xpos 365
        ypos 665
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        color "#eee"
    text "Gabinete\nda\nPsicóloga":
        xpos 1365
        ypos 665
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        color "#eee"
    #text "Corredor":
    #    xpos 865
    #    ypos 265
    #    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    #    color "#eee"
    text "Sala A":
        xpos 865
        ypos 65
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        color "#eee"
    text "Sala de\nEstudo":
        xpos 1365
        ypos 265
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        color "#eee"
    
screen house:
    zorder 3
    button:
        background "#00000080"
        xsize 1920
        ysize 1080
        action Hide('house')
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            text "Tens a certeza que queres ir para casa mais cedo?" xalign 0.5
            hbox:
                xalign 0.5
                spacing 700
                frame:
                    textbutton "Não" action Hide('house')
                frame:
                    textbutton "Sim" action Hide('house'), Jump('home')

screen avatar_stats:
    zorder 3
    button:
        background "#000000c0"
        xsize 1920
        ysize 1080
        action Hide('avatar_stats')
    vbox:
        xalign 0.17
        yalign 0.315
        spacing 50
        text "Conhecimento":
            xoffset -15
            yalign 0.5
            size 50
            color "#0bb"
            bold True
            outlines[ (absolute(3), "#333", absolute(0), absolute(0)) ]
        text "Energia":
            xoffset -15
            yalign 0.5
            size 50
            color "#bb0"
            bold True
            outlines[ (absolute(3), "#333", absolute(0), absolute(0)) ]
        text "Socialidade":
            xoffset -15
            yalign 0.5
            size 50
            color "#b0b"
            bold True
            outlines[ (absolute(3), "#333", absolute(0), absolute(0)) ]
    vbox:
        xalign 0.7
        yalign 0.3
        spacing 10
        hbox:
            spacing 5
            for i in range(conhecimento):
                add "stat1.png":
                    yalign 0.5
                    zoom 0.5
            for i in range(5-conhecimento):
                add "stat4.png":
                    yalign 0.5
                    zoom 0.5
        hbox:
            spacing 5
            for i in range(energia):
                add "stat2.png":
                    yalign 0.5
                    zoom 0.5
            for i in range(5-energia):
                add "stat4.png":
                    yalign 0.5
                    zoom 0.5
        hbox:
            spacing 5
            for i in range(socialidade):
                add "stat3.png":
                    yalign 0.5
                    zoom 0.5
            for i in range(5-socialidade):
                add "stat4.png":
                    yalign 0.5
                    zoom 0.5

screen clock_fade:
    zorder 2
    frame:
        xsize 7
        ysize 30
        xpos 1852
        ypos 12
        background "black"

label case_help:
    if day == 1:
        gameworld_runtime.player.character "{i}Devia de tentar perceber quem é a colega no post que as raparigas estavam a falar. Sempre que quiser posso falar com a Joana para obter feedback nas minhas reflexões."
    elif day == 2:
        gameworld_runtime.player.character "{i}O post era sobre a Tatiana. Devia de tentar perceber quem é que publicou a fotografia. Sempre que quiser posso falar com a Joana para obter feedback nas minhas reflexões."
    elif day == 3:
        gameworld_runtime.player.character "{i}O Nando é o autor da publicação. Tenho de refletir sobre a situação. Sempre que quiser posso falar com a Joana para obter feedback nas minhas reflexões."
    elif day == 4:
        gameworld_runtime.player.character "{i}Devia de tentar perceber quem fez um post a ameaçar alguém. Sempre que quiser posso falar com a Joana para obter feedback nas minhas reflexões."
    elif day == 5:
        gameworld_runtime.player.character "{i}A Cármen criou o post com a ameaça. Devia de tentar perceber quem é que ela ameaçou. Sempre que quiser posso falar com a Joana para obter feedback nas minhas reflexões."
    elif day == 6:
        gameworld_runtime.player.character "{i}A Estrela é a pessoa ameaçada. Tenho de refletir sobre a situação. Sempre que quiser posso falar com a Joana para obter feedback nas minhas reflexões."
    jump expression 'room'

screen task_list:
    zorder 3
    button:
        background "#00000080"
        xsize 1920
        ysize 1080
        action Hide('task_list')
    add "tasks/menulist.png":
        xalign 0.5
        yalign 0.5
        xsize 896
        ysize 896
    if session == 1:
        vbox:
            xpos 620
            ypos 330
            text "- Tirar algumas dúvidas com o professor de\n matemática (Sala B, ~15m)":
                size 40
                font "Huge Salmon.otf"
                if tasklist[0] != 1:
                    strikethrough True
            text "- Preparar a minha apresentação de grupo\n para amanhã (Sala A, ~15m)":
                size 40
                font "Huge Salmon.otf"
                if tasklist[1] != 1:
                    strikethrough True
            if tasklist[2] != 0:
                text "- Fazer fotocópias dos apontamentos do meu\n colega (Biblioteca, ~10m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[2] != 1:
                        strikethrough True
            if tasklist[3] != 0:
                text "- Ajudar o meu colega com os trabalhos de\n casa (Sala de Estudo, ~15m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[3] != 1:
                        strikethrough True
            if tasklist[4] != 0:
                text "- Fazer os exercícios para a aula de inglês de\n amanhã (Sala A, ~20m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[4] != 1:
                        strikethrough True
            if tasklist[5] != 0:
                text "- Comprar uma rifa da minha colega\n para apoiar o canil (Pátio, ~5m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[5] != 1:
                        strikethrough True
    if session == 2:
        vbox:
            xpos 620
            ypos 330
            text "- Preparar o meu caderno para tirar\n apontamentos para amanhã (Sala B, ~15m)":
                size 40
                font "Huge Salmon.otf"
                if tasklist[0] != 1:
                    strikethrough True
            text "- Combinar com os meus colegas a divisão do\n trabalho de grupo (Sala A, ~10m)":
                size 40
                font "Huge Salmon.otf"
                if tasklist[1] != 1:
                    strikethrough True
            if tasklist[2] != 0:
                text "- Rever os apontamentos antes do teste de\n inglês (Sala B, ~20m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[2] != 1:
                        strikethrough True
            if tasklist[3] != 0:
                text "- Devolver um livro emprestado a um colega\n (Pátio, ~5m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[3] != 1:
                        strikethrough True
            if tasklist[4] != 0:
                text "- Ir à biblioteca requisitar uns livros\n (Biblioteca, ~15m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[4] != 1:
                        strikethrough True
            if tasklist[5] != 0:
                text "- Esclarecer uma dúvida com a colega\n antes do teste (Sala de Estudo, ~15m)":
                    size 40
                    font "Huge Salmon.otf"
                    if tasklist[5] != 1:
                        strikethrough True
    vbox:
        xpos 610
        ypos 325
        spacing 50
        for i in tasklist:
            if i == 2:
                add "tasks/check.png":
                    xsize 50
                    ysize 50
            elif i == 3:
                add "tasks/cross.png":
                    xsize 50
                    ysize 50
            else:
                text "":
                    size 40

init python:
    class Action(IntEnum):
        Movement = 1
        Dialogue = 2
        Task = 3

default triggerstack = []
default currentarea = ""
default nextarea = ""
default currentdialogue = ""
default currentspeaker = []
default placeddialogues = {}
default populatetimer = 60
default area_visits = {}
default connection_visits = {}

label home:
    $ registo += "\n--- Fim do dia "+str(day)
    hide screen clock
    hide screen clock_fade
    scene sunset:
        xsize 1920
        ysize 1080
    with Fade(1, 0, 3)
    scene bedroom:
        xsize 1920
        ysize 1080
    with Fade(1, 1, 1)
    call stat_check
    gameworld_runtime.player.character "{i}Hoje foi um dia cheio. Vou refletir um pouco."
    if day == 1:
        $ registo += '\n\nConsegui identificar quem é a colega no post?'
        menu:
            gameworld_runtime.player.character "{i}Consegui identificar quem é a colega no post?"
            "Sim":
                jump .quem1

            "Não":
                jump .porque1
        label .quem1:
            $ abc = renpy.input("{i}Quem é? (Escreve apenas o nome)", length=500)
            $ resp_s11 += abc
            $ registo += '\n'+abc
            $ abc = renpy.input("{i}Como identifiquei?", length=500)
            $ registo += '\n'+abc
            jump .next1
        label .porque1:
            $ abc = renpy.input("{i}Porque não consegui?", length=500)
            $ registo += '\n'+abc
        label .next1:    
            gameworld_runtime.player.character "Já chega de reflexões por agora. Vou dormir."
        scene black
        with Fade(1,0,1)
        jump start4
    if day == 2:
        $ registo += '\n\nConsegui descobrir quem foi o autor do post?'
        menu:
            gameworld_runtime.player.character "{i}Consegui descobrir quem foi o autor do post?"
            "Sim":
                jump .quem2

            "Não":
                jump .porque2
        label .quem2:
            $ abc = renpy.input("{i}Quem foi? (Escreve apenas o nome)", length=500)
            $ resp_s12 += abc
            $ registo += '\n'+abc
            $ abc = renpy.input("{i}Como identifiquei?", length=500)
            $ registo += '\n'+abc
            jump .next2
        label .porque2:
            $ abc = renpy.input("{i}Porque não consegui?", length=500)
            $ registo += '\n'+abc
        label .next2:    
            gameworld_runtime.player.character "Já chega de reflexões por agora. Vou dormir."
        scene black
        with Fade(1,0,1)
        jump start5
    if day == 3:
        $ registo += '\n\nSei o que posso fazer para intervir?'
        menu:
            gameworld_runtime.player.character "{i}Sei o que posso fazer para intervir?"
            "Muito":
                $ registo += '\nMuito'
            "Algo":
                $ registo += '\nAlgo'
            "Pouco":
                $ registo += '\nPouco'
            "Nada":
                $ registo += '\nNada'
        $ registo += '\nSou capaz de ajudar a resolver a situação apesar de ser difícil?'
        menu:
            gameworld_runtime.player.character "{i}Sou capaz de ajudar a resolver a situação apesar de ser difícil?"
            "Muito":
                $ registo += '\nMuito'
            "Algo":
                $ registo += '\nAlgo'
            "Pouco":
                $ registo += '\nPouco'
            "Nada":
                $ registo += '\nNada'
        $ registo += '\nQuero dedicar-me a resolver esta situação?'
        menu:
            gameworld_runtime.player.character "{i}Quero dedicar-me a resolver esta situação?"
            "Muito":
                $ registo += '\nMuito'
            "Algo":
                $ registo += '\nAlgo'
            "Pouco":
                $ registo += '\nPouco'
            "Nada":
                $ registo += '\nNada'
        $ abc = renpy.input("{i}Podes adicionar um comentário extra sobre a situação", length=500)
        $ registo += '\n'+abc
        scene black
        with Fade(1,0,1)
        jump ends2
    if day == 4:
        $ registo += '\n\nConsegui identificar quem foi a colega que colocou o post?'
        menu:
            gameworld_runtime.player.character "{i}Consegui identificar quem foi a colega que colocou o post?"
            "Sim":
                jump .quem4

            "Não":
                jump .porque4
        label .quem4:
            $ abc = renpy.input("{i}Quem foi? (Escreve apenas o nome)", length=500)
            $ resp_s21 += abc
            $ registo += '\n'+abc
            $ abc = renpy.input("{i}Como identifiquei?", length=500)
            $ registo += '\n'+abc
            jump .next4
        label .porque4:
            $ abc = renpy.input("{i}Porque não consegui?", length=500)
            $ registo += '\n'+abc
        label .next4:    
            gameworld_runtime.player.character "Já chega de reflexões por agora. Vou dormir."
        scene black
        with Fade(1,0,1)
        jump start7
    if day == 5:
        $ registo += '\n\nConsegui descobrir quem é a colega que foi ameaçada?'
        menu:
            gameworld_runtime.player.character "{i}Consegui descobrir quem é a colega que foi ameaçada?"
            "Sim":
                jump .quem5

            "Não":
                jump .porque5
        label .quem5:
            $ abc = renpy.input("{i}Quem é? (Escreve apenas o nome)", length=500)
            $ resp_s22 += abc
            $ registo += '\n'+abc
            $ abc = renpy.input("{i}Como identifiquei?", length=500)
            $ registo += '\n'+abc
            jump .next5
        label .porque5:
            $ abc = renpy.input("{i}Porque não consegui?", length=500)
            $ registo += '\n'+abc
        label .next5:    
            gameworld_runtime.player.character "Já chega de reflexões por agora. Vou dormir."
        scene black
        with Fade(1,0,1)
        jump start8
    if day == 6:
        $ registo += '\n\nSei o que posso fazer para intervir?'
        menu:
            gameworld_runtime.player.character "{i}Sei o que posso fazer para intervir?"
            "Muito":
                $ registo += '\nMuito'
            "Algo":
                $ registo += '\nAlgo'
            "Pouco":
                $ registo += '\nPouco'
            "Nada":
                $ registo += '\nNada'
        $ registo += '\nSou capaz de ajudar a resolver a situação apesar de ser difícil?'
        menu:
            gameworld_runtime.player.character "{i}Sou capaz de ajudar a resolver a situação apesar de ser difícil?"
            "Muito":
                $ registo += '\nMuito'
            "Algo":
                $ registo += '\nAlgo'
            "Pouco":
                $ registo += '\nPouco'
            "Nada":
                $ registo += '\nNada'
        $ registo += '\nQuero dedicar-me a resolver esta situação?'
        menu:
            gameworld_runtime.player.character "{i}Quero dedicar-me a resolver esta situação?"
            "Muito":
                $ registo += '\nMuito'
            "Algo":
                $ registo += '\nAlgo'
            "Pouco":
                $ registo += '\nPouco'
            "Nada":
                $ registo += '\nNada'
        $ abc = renpy.input("{i}Podes adicionar um comentário extra sobre a situação", length=500)
        $ registo += '\n'+abc
        scene black
        with Fade(1,0,1)
        jump end
    
label stat_check0:
    $ chosen_stats = 0
    menu:
        gameworld_runtime.player.character "{i}Qual é a minha maior prioridade?\n\n{u}Estatística será aumentada em +1"
        "{b}{color=#0bb}Conhecimento ([conhecimento]/5){/color}{/b}\n{color=#333}Preparar-me para o exame" if conhecimento < 5:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ conhecimento += 1
            $ chosen_stats = 10
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Conhecimento ([conhecimento]/5){/color}{/b}\n-valor máximo-" if conhecimento > 4:
            $ conhecimento += 0
        "{b}{color=#bb0}Energia ([energia]/5){/color}{/b}\n{color=#333}Manter uma boa rotina de descanso" if energia < 5:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ energia += 1
            $ chosen_stats = 20
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Energia ([energia]/5){/color}{/b}\n-valor máximo-" if energia > 4:
            $ energia += 0
        "{b}{color=#b0b}Socialidade ([socialidade]/5){/color}{/b}\n{color=#333}Socializar com os meus colegas" if socialidade < 5:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ socialidade += 1
            $ chosen_stats = 30
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Socialidade ([socialidade]/5){/color}{/b}\n-valor máximo-" if socialidade > 4:
            $ socialidade += 0
    menu:
        gameworld_runtime.player.character "{i}Qual é a minha menor prioridade?\n\n{u}Estatística será diminuída em -1"
        "{b}{color=#0bb}Conhecimento ([conhecimento]/5){/color}{/b}\n{color=#333}Rever a matéria para o exame" if chosen_stats != 10 and conhecimento > 1:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ conhecimento -= 1
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Conhecimento ([conhecimento]/5) +1{/color}{/b}\n-selecionado-" if chosen_stats == 10:
            $ conhecimento -= 0
        "!{b}{color=#999}Conhecimento ([conhecimento]/5){/color}{/b}\n-valor mínimo-" if conhecimento < 2:
            $ conhecimento -= 0
        "{b}{color=#bb0}Energia ([energia]/5){/color}{/b}\n{color=#333}Manter uma boa rotina de descanso" if chosen_stats != 20 and energia > 1:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ energia -= 1
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Energia ([energia]/5) +1{/color}{/b}\n-selecionado-" if chosen_stats == 20:
            $ energia -= 0
        "!{b}{color=#999}Energia ([energia]/5){/color}{/b}\n-valor mínimo-" if energia < 2:
            $ conhecimento -= 0
        "{b}{color=#b0b}Socialidade ([socialidade]/5){/color}{/b}\n{color=#333}Socializar com os meus colegas" if chosen_stats != 30 and socialidade > 1:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ socialidade -= 1
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Socialidade ([socialidade]/5) +1{/color}{/b}\n-selecionado-" if chosen_stats == 30:
            $ socialidade -= 0
        "!{b}{color=#999}Socialidade ([socialidade]/5){/color}{/b}\n-valor mínimo-" if socialidade < 2:
            $ conhecimento -= 0
    return

label stat_check:
    $ chosen_stats = 0
    menu:
        gameworld_runtime.player.character "{i}O que quero fazer agora à noite?\n\n{u}Estatística será aumentada em +1"
        "{b}{color=#0bb}Conhecimento ([conhecimento]/5){/color}{/b}\n{color=#333}Rever a matéria para o teste" if conhecimento < 5:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ conhecimento += 1
            $ chosen_stats = 10
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Conhecimento ([conhecimento]/5){/color}{/b}\n-valor máximo-" if conhecimento > 4:
            $ conhecimento += 0
        "{b}{color=#bb0}Energia ([energia]/5){/color}{/b}\n{color=#333}Dormir cedo para ficar descansado" if energia < 5:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ energia += 1
            $ chosen_stats = 20
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Energia ([energia]/5){/color}{/b}\n-valor máximo-" if energia > 4:
            $ energia += 0
        "{b}{color=#b0b}Socialidade ([socialidade]/5){/color}{/b}\n{color=#333}Ir falar online com amigos" if socialidade < 5:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ socialidade += 1
            $ chosen_stats = 30
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Socialidade ([socialidade]/5){/color}{/b}\n-valor máximo-" if socialidade > 4:
            $ socialidade += 0
    menu:
        gameworld_runtime.player.character "{i}Não tenho tempo para tudo, o que sacrifico?\n\n{u}Estatística será diminuída em -1"
        "{b}{color=#0bb}Conhecimento ([conhecimento]/5){/color}{/b}\n{color=#333}Rever a matéria para o teste" if chosen_stats != 10 and conhecimento > 1:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ conhecimento -= 1
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Conhecimento ([conhecimento]/5) +1{/color}{/b}\n-selecionado-" if chosen_stats == 10:
            $ conhecimento -= 0
        "!{b}{color=#999}Conhecimento ([conhecimento]/5){/color}{/b}\n-valor mínimo-" if conhecimento < 2:
            $ conhecimento -= 0
        "{b}{color=#bb0}Energia ([energia]/5){/color}{/b}\n{color=#333}Dormir cedo para ficar descansado" if chosen_stats != 20 and energia > 1:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ energia -= 1
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Energia ([energia]/5) +1{/color}{/b}\n-selecionado-" if chosen_stats == 20:
            $ energia -= 0
        "!{b}{color=#999}Energia ([energia]/5){/color}{/b}\n-valor mínimo-" if energia < 2:
            $ conhecimento -= 0
        "{b}{color=#b0b}Socialidade ([socialidade]/5){/color}{/b}\n{color=#333}Ir falar online com amigos" if chosen_stats != 30 and socialidade > 1:
            show screen avatar_stats with Fade(.4,0,.4)
            $ renpy.pause(.4)
            $ socialidade -= 1
            $ renpy.pause(.8)
            hide screen avatar_stats
        "!{b}{color=#999}Socialidade ([socialidade]/5) +1{/color}{/b}\n-selecionado-" if chosen_stats == 30:
            $ socialidade -= 0
        "!{b}{color=#999}Socialidade ([socialidade]/5){/color}{/b}\n-valor mínimo-" if socialidade < 2:
            $ conhecimento -= 0
    return

label ends2:
    $ tasks_s1 = tasklist.copy()
    "Chegaste ao fim da primeira parte! Quando quiseres, podes clicar no rato para proceder para a segunda parte."
    #"Chegaste ao fim do jogo! Por favor, vai à pasta do jogo e procura pelo ficheiro {u}registo.txt{/u} e envia-o para o seguinte mail: helio.martins@tecnico.ulisboa.pt\nObrigado pela tua participação!"
    jump session2

label end:
    $ registo += "\n\n"+str(ses_fb)
    python:
        try:
            with open(os.path.join(os.path.dirname(renpy.config.gamedir), "registo_"+player_name+".txt"), 'w') as f:
                f.write(registo)
                f.close()
        except Exception as exception:
            pass
    jump endend

label endend:
    if conhecimento == 1:
        $ nota_s2 = "1* Fraca"
    if conhecimento == 2:
        $ nota_s2 = "2* Má"
    if conhecimento == 3:
        $ nota_s2 = "3* Normal"
    if conhecimento == 4:
        $ nota_s2 = "4* Boa"
    if conhecimento == 5:
        $ nota_s2 = "5* Excelente"
    "Obrigado por jogares o jogo!"
    call screen final_stats
    jump endend

screen final_stats:
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            hbox:
                spacing 50
                vbox:
                    for ta in tasks_s1:
                        if ta == 2:
                            text "Tarefa [ta] Completa" color "#0a0"
                        else:
                            text "Tarefa [ta] Falhada" color "#a00"
                vbox:
                    for tb in tasklist:
                        if tb == 2:
                            text "Tarefa [tb] Completa" color "#0a0"
                        else:
                            text "Tarefa [tb] Falhada" color "#a00"
            text ""
            text "Sessão 1"
            text "Pessoa que aparecia no post - Tatiana"
            text "Resposta dada: "+resp_s11
            text "Pessoa que publicou o post - Nando"
            text "Resposta dada: "+resp_s12
            text ""
            text "Sessão 2"
            text "Pessoa que ameaçou no post - Cármen"
            text "Resposta dada: "+resp_s21
            text "Pessoa que foi ameaçada no post - Estrela"
            text "Resposta dada: "+resp_s22
            text ""
            text "Nota do teste: "+nota_s1
            text "Nota do exame: "+nota_s2

default registo = ""
default resp_s11 = ""
default resp_s12 = ""
default resp_s21 = ""
default resp_s22 = ""
default nota_s1 = ""
default nota_s2 = ""

label d_psicologa:
    $ renpy.set_return_stack([])
    hide screen clock
    hide screen clock_fade
    $ registo += "\nFalou com psicóloga Joana"
    gameworld_runtime.player.character "Olá Joana, tudo bem?"
    psicologa "Olá, [player_name]! O que te traz por cá?"
    menu:
        "Pedir feedback " if situation >= 10 and session == 1:
            $ registo += "\nFeedback da psicóloga Joana"
            gameworld_runtime.player.character "Queria saber a tua opinião sobre um assunto..."
            $ AddSeconds(gameworld_runtime.time, int(20*situation*(1-0.1*energia)))

        "Pedir feedback " if situation >= 40 and session == 2:
            $ registo += "\nFeedback da psicóloga Joana"
            gameworld_runtime.player.character "Queria saber a tua opinião sobre um assunto..."
            $ AddSeconds(gameworld_runtime.time, int(20*(situation-30)*(1-0.1*energia)))

        "Não perguntar nada":
            gameworld_runtime.player.character "Estava só de passagem, obrigado."
            jump room
    scene black with Fade(1,0,1)
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,0,1)
    gameworld_runtime.player.character "{i}Graças à Joana, recebi o seguinte feedback:"
    if session == 1:
        call screen feedback
    if session == 2:
        call screen feedback2
    show screen clock
    show screen clock_fade
    jump room

screen feedback:
    zorder 3
    button:
        background "#00000080"
        xsize 1920
        ysize 1080
        action NullAction()
    grid 2 1:
        area (186, 105, 1024, 120)
        frame:
            background "#999"
            xsize 512
            ysize 120
            text "Reflexão" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
        frame:
            background "#999"
            xsize 1018+18
            ysize 120
            text "Feedback" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
    vpgrid:
        area (186, 225, 1548, 650)
        cols 3
        draggable False
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.5
        for j in range (int(situation / 10)):
            default curr_list = []
            if j == 0:
                $ curr_list = drag_options_10
                $ curr_fb = drag_feedback_10
            elif j == 1:
                $ curr_list = drag_options_20
                $ curr_fb = drag_feedback_20
            elif j == 2:
                if situation == 31:
                    $ curr_list = drag_options_31
                    $ curr_fb = drag_feedback_31
                else:
                    $ curr_list = drag_options_32
                    $ curr_fb = drag_feedback_32
            frame:
                background "#bbb"
                xsize 512
                ysize 120
                text "Situação "+str(j+1) yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                background "#bbb"
                xsize 1018
                ysize 120
                text "" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                xsize 0
                background "#bbb"
            for k in range(len(ses_fb[j])):
                frame:
                    if k % 2 == 0:
                        background "#eee"
                    else:
                        background "#fff"
                    xsize 512
                    ysize 120
                    text "\""+curr_list[k]+"\"" yalign 0.5 size 23 italic 1 color "#111" xalign 0.5 text_align 0.5
                frame:
                    if k % 2 == 0:
                        background "#eee"
                    else:
                        background "#fff"
                    xsize 1018
                    ysize 120
                    text curr_fb[k][0] yalign 0.5 size 23 bold 1 color curr_fb[k][1] text_align 0.5 xalign 0.5
                frame:
                    xsize 0
                    background "#bbb"
    frame:
        xpos 186+512-1
        ypos 105
        xsize 2
        ysize 770
        background "#000"
    frame:
        xpos 186
        ypos 224
        xsize 1548
        ysize 2
        background "#000"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle Transform("xi.png", xsize=100, ysize=100)
        hover Transform("xh.png", xsize=100, ysize=100)
        action Return()

screen feedback2:
    zorder 3
    button:
        background "#00000080"
        xsize 1920
        ysize 1080
        action NullAction()
    grid 2 1:
        area (186, 105, 1024, 120)
        frame:
            background "#999"
            xsize 512
            ysize 120
            text "Reflexão" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
        frame:
            background "#999"
            xsize 1018+18
            ysize 120
            text "Feedback" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
    vpgrid:
        area (186, 225, 1548, 650)
        cols 3
        draggable False
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.5
        for j in range (int((situation-30) / 10)):
            default curr_list = []
            if j == 0:
                $ curr_list = drag_options_40
                $ curr_fb = drag_feedback_40
            elif j == 1:
                $ curr_list = drag_options_50
                $ curr_fb = drag_feedback_50
            elif j == 2:
                if situation == 61:
                    $ curr_list = drag_options_61
                    $ curr_fb = drag_feedback_61
                else:
                    $ curr_list = drag_options_62
                    $ curr_fb = drag_feedback_62
            frame:
                background "#bbb"
                xsize 512
                ysize 120
                text "Situação "+str(j+1) yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                background "#bbb"
                xsize 1018
                ysize 120
                text "" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                xsize 0
                background "#bbb"
            for k in range(len(ses_fb[j])):
                frame:
                    if k % 2 == 0:
                        background "#eee"
                    else:
                        background "#fff"
                    xsize 512
                    ysize 120
                    text "\""+curr_list[k]+"\"" yalign 0.5 size 23 italic 1 color "#111" xalign 0.5 text_align 0.5
                frame:
                    if k % 2 == 0:
                        background "#eee"
                    else:
                        background "#fff"
                    xsize 1018
                    ysize 120
                    text curr_fb[k][0] yalign 0.5 size 23 bold 1 color curr_fb[k][1] text_align 0.5 xalign 0.5
                frame:
                    xsize 0
                    background "#bbb"
    frame:
        xpos 186+512-1
        ypos 105
        xsize 2
        ysize 770
        background "#000"
    frame:
        xpos 186
        ypos 224
        xsize 1548
        ysize 2
        background "#000"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle Transform("xi.png", xsize=100, ysize=100)
        hover Transform("xh.png", xsize=100, ysize=100)
        action Return()

screen texton:
    hbox:
        vbox:
            text "dialogos"
            for iu in gameworld_runtime.dialogues.values():
                text str(iu)
        vbox:
            text "available"
            for iu in gameworld_runtime.dialogues_available:
                text str(iu)
        vbox:
            text "active"
            for iu in gameworld_runtime.dialogues_active:
                text str(iu)