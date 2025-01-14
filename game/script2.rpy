label session2:
    scene black
    $ renpy.pause(3)
    "{i}3 semanas depois"
    $ send_marker("After 3 semanas depois")
    call setup20
    call setup21
    $ gameworld_runtime = Gameworld_RUNTIME()
    $ gameworld_runtime.time = Time(12, 30, 0)
    $ gameworld_runtime.dialogues_available = list(gameworld_runtime.dialogues.values())
    $ triggerstack = []
    $ currentarea = ""
    $ nextarea = ""
    $ currentdialogue = ""
    $ currentspeaker = []
    $ placeddialogues = {}
    $ populatetimer = 60
    $ area_visits = {}
    $ connection_visits = {}
    $ currentarea = gameworld_runtime.areas[1]
    $ nextarea = gameworld_runtime.areas[1]
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
    jump intro2

label start7:
    call setup22
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
    jump aula4
    
label start8:
    call setup23
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
    jump aula5

label setup20:
    $ situation = 0
    $ session = 2
    $ day = 4
    $ gameworld.dialogues = {}
    $ gameworld_runtime.dialogues = {}
    $ gameworld_runtime.dialogues_available = []
    $ gameworld_runtime.dialogues_active = []
    $ gameworld_runtime.dialogues_activeprio = []
    $ gameworld_runtime.dialogues_occurred = []
    return

label setup21:
    $ tasklist = [1, 1, 0, 0, 0, 0]
    $ task_space = [5, 11, 5, 1, 6, 12]
    $ tasks = [
        Task("Tarefa: Preparar caderno", 5, "tasks/t7i.png", "tasks/t7h.png", 650, 600, 0, 0.3),
        Task("Tarefa: Combinar trabalho", 11, "tasks/t2i.png", "tasks/t2h.png", 1550, 650, 0, 1),
        Task("Tarefa: Rever apontamentos", 5, "tasks/t5i.png", "tasks/t5h.png", 1250, 600, 0, 0.2),
        Task("Tarefa: Devolver livro", 1, "tasks/t4i.png", "tasks/t4h.png", 1300, 350, 0, 0.35),
        Task("Tarefa: Requisitar livros", 6, "tasks/t8i.png", "tasks/t8h.png", 650, 470, 0, .12),
        Task("Tarefa: Esclarecer dúvida", 12, "tasks/t6i.png", "tasks/t6h.png", -100, 350, 0, 0.5)
    ]
    $ gameworld.AddDialogue(Dialogue_Chat("MP", [7,9], "", True, {}, {}, True, True))
    $ gameworld.AddDialogue(Dialogue_Chat("AR", [1,10], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("ES", [3,11], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("JN", [6,8], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("CNP", [2,8,9], "", True, {}, {}, True, True))
    $ gameworld.AddDialogue(Dialogue_Chat("EJ", [3,6], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("ARS", [1,10,11], "", True, {}, {}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("M", [7], "", True, {}, {}, True, False))
    if socialidade > 2:
        $ gameworld.AddDialogue(Dialogue_Chat("CMP", [2,7,9], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    if socialidade > 3:
        $ gameworld.AddDialogue(Dialogue_Chat("C", [2], "", True, {}, {}, True, True))
        $ gameworld.AddDialogue(Dialogue_Chat("C", [2], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    return
label setup22:
    $ gameworld_runtime.dialogues = {}
    $ gameworld_runtime.dialogues_activeprio = []
    $ situation = 40
    $ day = 5
    $ tasklist[2] = 1
    $ tasklist[3] = 1
    if tasklist[0] == 1:
        $ tasklist[0] = 3
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("EIH", [3,5,4], "", True, {}, {}, True, True))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("AN", [1,8], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("ST", [11,12], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("MP", [7,9], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("JR", [6,10], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("NP", [8,9], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("EHIST", [3,4,5,11,12], "", True, {}, {}, True, True))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("M", [7], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("AJR", [1,6,10], "", True, {}, {}, True, False))
    if socialidade > 2:
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("E", [3], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    if socialidade > 3:
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("E", [3], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    if socialidade > 4:
        $ gameworld_runtime.AddDialogue(Dialogue_Chat("EH", [3,4], "", True, {}, {}, True, True))
    else:
        $ Dialogue_Chat("---", [], "", True, {}, {}, True, False)
    return
label setup23: 
    $ gameworld_runtime.dialogues = {}
    $ gameworld_runtime.dialogues_activeprio = []
    $ situation = 50
    $ day = 6
    $ tasklist[4] = 1
    $ tasklist[5] = 1
    if tasklist[2] == 1:
        $ tasklist[2] = 3
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("AJR", [1,6,10], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("ST", [11,12], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("EH", [3,4], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("IM", [5,7], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("NP", [8,9], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("CM", [3,7], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("ANPM", [1,8,9,7], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("ST", [11,12], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("EHI", [3,4,5], "", True, {}, {}, True, False))
    $ gameworld_runtime.AddDialogue(Dialogue_Chat("JR", [6,10], "", True, {}, {}, True, False))
    return

label task2:
    if currenttask == 0:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Acabei de preparar o meu caderno."
        $ AddSeconds(gameworld_runtime.time, int(780*(1-0.1*energia)))
        show screen clock
    elif currenttask == 1:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Combinei com os meus colegas quem fazia o quê no trabalho."
        $ AddSeconds(gameworld_runtime.time, int(480*(1-0.1*energia)))
        show screen clock
    elif currenttask == 2:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Revi os meus apontamentos."
        $ AddSeconds(gameworld_runtime.time, int(1200*(1-0.1*energia)))
        show screen clock
    elif currenttask == 3:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Devolvi o livro que o meu colega me emprestou."
        $ AddSeconds(gameworld_runtime.time, int(240*(1-0.1*energia)))
        show screen clock
    elif currenttask == 4:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Requisitei os livros de que precisava."
        $ AddSeconds(gameworld_runtime.time, int(840*(1-0.1*energia)))
        show screen clock
    elif currenttask == 5:
        hide screen clock
        hide screen clock_fade
        scene black
        with Fade(1, 1, 1)
        gameworld_runtime.player.character "{i}Esclareci a dúvida que tinha com a minha colega."
        $ AddSeconds(gameworld_runtime.time, int(900*(1-0.1*energia)))
        show screen clock
    call algo(action=Action.Movement, next_area=currentarea)

label intro2:
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,1,1)
    gameworld_runtime.player.character "{i}O pessoal anda ansioso outra vez. Será que alguém colocou outro post..."
    gameworld_runtime.player.character "{i}Estou no pátio. As aulas acabaram, tenho 30 minutos até ter de ir para casa. Tenho tarefas para fazer. O que faço?"
    show screen clock
    call algo(action=Action.Movement, next_area=nextarea)
    "something went wrong"

screen post2:
    zorder 3
    button:
        background "#00000080"
        xsize 1920
        ysize 1080
        action NullAction()
    frame:
        xsize 1700
        ysize 800
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            frame:
                text "{i}{b}~Cármen Semedo:{/b} \"Estrela, és falsa! Amanhã vais apanhar.\n Eu vou a tua casa e entro pela tua janela.\""
            hbox:
                spacing 10
                if show_image:
                    frame:
                        add "post2.png":
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
                        xsize 1200
                        text "{b}~Jorge Amaral:{/b} \"Falsa?\""
                    frame:
                        xsize 1200
                        text "{b}~Cármen Semedo:{/b} \"Não vale nada! Promete, promete e depois é falsa. Vai apanhar!\""
                    frame:
                        xsize 1200
                        text "{b}~Tatiana Delgado:{/b} \"Qual é o teu problema?\""
                    frame:
                        xsize 1200
                        text "{b}~Estrela Nunes:{/b} \"Deves pensar que tenho medo de ti.\""
                    frame:
                        xsize 1200
                        text "{b}~Cármen Semedo:{/b} \"Devias ter! Porque é que a visita tem de ser no Algarve? Só por causa da Isabel né?\""
                    frame:
                        xsize 1200
                        text "{b}~Abel Polido:{/b} \"Tenham lá calma! Também preferia mais perto. Fica muito caro.\""
                    frame:
                        xsize 1200
                        text "{b}~Isabel Torres:{/b} \"Cármen, lá porque os papás não te deixam ir não quer dizer que os outros não possam ir. Ameaças a Estrela outra vez e faço-te uma espera!\""
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle Transform("xi.png", xsize=100, ysize=100)
        hover Transform("xh.png", xsize=100, ysize=100)
        action Hide('post2'), Jump('aula5.afterpost')

label aula5:
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,1,1)
    $ situation = 55
    "{i}Passados mais alguns dias, antes do início de uma aula"
    "{i}Aproxima-se um colega teu"
    h sad "Olá, posso falar contigo? Não ia dizer nada, mas acho que devias saber o que aconteceu. A Cármen ameaçou a Estrela no Com@Viver. Não digas que fui eu a mostrar-te!"
    "{i}O Hélder mostra o telefone dele"
    $ send_marker("before POST S2")
    call screen post2
    label .afterpost:
        $ send_marker("after POST S2")
        #"{i}A aula vai começar, os alunos estão-se a sentar"
        #gameworld_runtime.player.character "{i}Hoje vamos receber um teste."
        image currentscene:
            currentarea.background
            size (config.screen_width, config.screen_height)
        scene currentscene with Fade(1,0,1)
        "{i}Após a aula"
        #if conhecimento < 3:
        #    gameworld_runtime.player.character "{i}Tive uma nota fraca, preciso de estudar mais... Se continuar assim, não vou poder ir à viagem de finalistas."
        #if conhecimento > 3:
        #    gameworld_runtime.player.character "{i}Tive uma boa nota, o estudo compensou!"
        gameworld_runtime.player.character "{i}Parece que foi a Cármen que fez o post. Se calhar a situação foi longe de mais. Tenho de pensar como prosseguir."
        gameworld_runtime.player.character "{i}Estou na sala B. As aulas acabaram, tenho 30 minutos até ter de ir para casa. Tenho tarefas para fazer. O que faço?"
        show screen clock
        
        call algo(action=Action.Movement, next_area=nextarea)
        "something went wrong"

label aula4:
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,1,1)
    $ situation = 50
    $ send_marker("before S2 SITUATION 2")
    "{i}Passados alguns dias, a meio de uma aula"
    h normal "E esta foi a nossa apresentação do trabalho. Alguma coisa que queiram perguntar, digam."
    c normal "Eu por acaso tenho uma dúvida."
    h normal "Claro, diz."
    c disgust "No vosso grupo quem é que tomou as decisões?"
    i angry "As decisões foram sempre tomadas em conjunto! Há algum problema?"
    c angry "Era só por curiosidade. É que há determinadas pessoas que gostam de decidir o que os outros fazem. Acham que são melhores do que os outros!"
    h normal "Cármen, o que estás a dizer é injusto."
    i laugh "Se tens alguma coisa a dizer, diz na cara! Experimenta só e depois vês o que acontece a seguir."
    c angry "Isto não é contigo, não te metas! É com a tua amiguinha. Ela que responda se tem coragem."
    i angry "Atreve-te a fazer alguma coisa."
    s normal "Stôr, não ligue. Elas já se acalmam. Estão só a brincar."
    $ send_marker("after S2 SITUATION 2")
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,0,1)
    call setup_dragndrops20
    "{i}Depois da aula acabar"
    professor "Cármen, gostava de falar contigo."
    c normal "Stôr, agora não posso. Preciso mesmo de ir à casa de banho, desculpe. Podemos falar no final da 2ª aula?"
    professor "Está bem, falamos depois."
    gameworld_runtime.player.character "{i}Existe animosidade entre a Cármen e os outros alunos; pela conversa deles parece que foi ela a fazer o post. Quem é que ela terá ameaçado?"
    gameworld_runtime.player.character "{i}Estou na sala A. As aulas acabaram, tenho 30 minutos até ter de ir para casa. Tenho tarefas para fazer. O que faço?"
    show screen clock
    call algo(action=Action.Movement, next_area=nextarea)
    "something went wrong"