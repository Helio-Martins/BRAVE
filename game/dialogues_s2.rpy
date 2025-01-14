label d_day2:

# helder, isabel, tatiana
label .chat_cb1:
    hide screen clock
    "{i}Um grupo de alunos aproxima-se e ouve-se a conversa entre eles"
    $ situation = 40
    $ send_marker("before S2 SITUATION 1")
    call pass_time_dialogue
    i angry "Passou-se! Os meus pais também não me querem deixar ir para o Algarve. Não é por causa disso que vou tentar estragar a viagem de finalistas aos outros."
    call pass_time_dialogue
    h angry "O que merecia depois disto era ficar fora da viagem."
    call pass_time_dialogue
    t angry "Podes crer. E ameaçar que lhe batia e que lhe entrava em casa? Não acho normal!"
    call pass_time_dialogue
    h angry "Não suporto injustiças! O que aconteceu não tem desculpa."
    call pass_time_dialogue
    i angry "Só sei que se voltar a ameaçar que lhe bate, vai arrepender-se a sério!"
    $ send_marker("after S2 SITUATION 1")
    gameworld_runtime.player.character "{i}Conversa estranha... Devia de descobrir de quem estavam a falar."
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,0,1)
    call setup_dragndrops10
    call algo(action=Action.Movement, next_area=currentarea)

# manuela, patricia - sinal 5
label .chat_39:
    call pass_time_dialogue
    p normal "Viste a Cármen?"
    call pass_time_dialogue
    m normal "Entrou agora, mas disse que se ia baldar à 2º aula e ia ao café."
    call pass_time_dialogue
    p sad "Outra vez? Mas ela sempre achou mal que o Nando se baldasse às aulas..."
    call pass_time_dialogue
    m normal "Pois, também não entendo..."
    call algo(action=Action.Movement, next_area=currentarea)

# abel, rui
label .chat_40:
    call pass_time_dialogue
    ab normal "Já faltam poucos dias para sair a nova temporada. Estou mesmo ansioso."
    call pass_time_dialogue
    r normal "Yeap, mal posso esperar."
    call pass_time_dialogue
    ab normal "Ouvi dizer que uma certa personagem ia deixar de aparecer..."
    call pass_time_dialogue
    r angry "Hey, não digas spoilers!"
    call pass_time_dialogue
    ab laugh "*risos*"
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, samuel
label .chat_41:
    call pass_time_dialogue
    e normal "Hoje sempre estamos combinados para trabalhar no projeto?"
    call pass_time_dialogue
    s normal "Mais ou menos, a Tatiana disse que tinha de ir buscar a irmã à escola, por isso não pode vir. Mas nós podemos adiantar progresso à mesma."
    call pass_time_dialogue
    e normal "Tudo bem, aparece na biblioteca depois das aulas."
    call pass_time_dialogue
    s normal "Ok."
    call algo(action=Action.Movement, next_area=currentarea)

# jorge, nando
label .chat_42:
    call pass_time_dialogue
    j normal "Viste o jogo de ontem?"
    call pass_time_dialogue
    n happy "Ya, cheguei a pensar que távamos a jogar sozinhos. A outra equipa parecia que estava a jogar com a equipa B."
    call pass_time_dialogue
    j happy "Curtiste do ponta de lança a levar 3 foras de jogo?"
    call pass_time_dialogue
    n laugh "YA! Ele não deve ter dormido como deve ser."
    call pass_time_dialogue
    j laugh "Pois, só pode!"
    call algo(action=Action.Movement, next_area=currentarea)

# carmen, nando, patricia - sinal 3
label .chat_43:
    call pass_time_dialogue
    n normal "Logo à tarde vou ao canil e precisava de uma ajuda. Alguém pode vir comigo?"
    call pass_time_dialogue
    p sad "Desculpa amor, hoje não posso! Tenho de estudar para o teste. Mas vou contigo para a semana, prometo."
    call pass_time_dialogue
    n normal "E tu, Cármen?"
    call pass_time_dialogue
    c disgust "Isso não é cena para mim. Esquece! Fico a cheirar a xixi de cão, nem pensar!"
    call pass_time_dialogue
    n sad "Era pouco tempo. Precisava mesmo de alguém hoje para me ajudar."
    call pass_time_dialogue
    c disgust "Não percebo como é que consegues gastar tantas horas a fazer esse tipo de coisas. Tenho cenas mais úteis para fazer com a minha vida!"
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, jorge
label .chat_44:
    call pass_time_dialogue
    j normal "Já sabes se vamos para o Algarve ou como é?"
    call pass_time_dialogue
    e angry "Honestamente Samuel, não faço ideia e neste momento não quero saber."
    call pass_time_dialogue
    j sad "Então? Que agressividade é essa?"
    call pass_time_dialogue
    e disgust "Desculpa, mas tou com um stress enorme. A Cármen anda-me a chatear a cabeça e francamente tou a ficar farta."
    call pass_time_dialogue
    j sad "Calma. Não vale a pena stressar. Isto vai a votos de qualquer das formas, até sabermos o resultado só temos de esperar."
    call pass_time_dialogue
    e disgust "E é suposto eu ignorar o que ela disse no Com@Viver?"
    call pass_time_dialogue
    j sad "Nisso tens razão, mas achas mesmo que ela faria isso? Ignora só."
    call pass_time_dialogue
    e disgust "Veremos."
    call algo(action=Action.Movement, next_area=currentarea)

# abel, rui, samuel
label .chat_45:
    call pass_time_dialogue
    ab happy "Ontem estávamos a jogar fixe! Quase que chegávamos a 5 vitórias seguidas."
    call pass_time_dialogue
    s happy "Sim, começo a achar que consigo ir para profissional."
    call pass_time_dialogue
    ab happy "Calma mano, primeiro acaba a escola, depois pensa nos jogos."
    call pass_time_dialogue
    s happy "Óbvio, estava a gozar, mas quem sabe um dia vais me ver lá no palco a representar o país."
    call pass_time_dialogue
    r happy "Quando acordares desse sonho avisa-me!"
    call algo(action=Action.Movement, next_area=currentarea)

# manuela
label .chat_46:
    call pass_time_dialogue
    m normal "*a mexer no telemóvel*"
    call algo(action=Action.Movement, next_area=currentarea)

# sinais de alerta, substituem chats 0 e 5

# carmen, manuela, patricia - sinal 1
label .chat_47:
    call pass_time_dialogue
    p surprise "Ela canta super bem!"
    call pass_time_dialogue
    c normal "Eu canto muito melhor do que ela. Não percebo como é que ela tem tantos seguidores. Já viram o vídeo que publiquei?"
    call pass_time_dialogue
    m happy "Claro! Tu estás top, babe!"
    call pass_time_dialogue
    c normal "Não se esqueçam de pôr like e partilhar só o meu vídeo para ser viral. Vou concorrer ao próximo The Voice, sabiam?"
    call algo(action=Action.Movement, next_area=currentarea)

# carmen - sinal 2
label .chat_48:
    call pass_time_dialogue
    c angry "*concentrada no telemóvel*"
    call algo(action=Action.Movement, next_area=currentarea)

# carmen - sinal 4
label .chat_49:
    call pass_time_dialogue
    c normal "*a andar enquanto olha para o telemóvel*"
    call pass_time_dialogue
    c surprise "*tropeça nos atacadores e cai*"
    call pass_time_dialogue
    c angry "..."
    call pass_time_dialogue
    c angry "*dá um pontapé na parede e vai-se embora*"
    call algo(action=Action.Movement, next_area=currentarea)

#####
#####
#####

# estrela, isabel, helder - sinal
label .chat_50:
    call pass_time_dialogue
    i normal "Bora ao cinema depois das aulas ver aquele filme fixe que eu falei?"
    call pass_time_dialogue
    e sad "Não sei, está-me a apetecer ir para casa, fica para outro dia."
    call pass_time_dialogue
    i normal "Então combinamos para amanhã?"
    call pass_time_dialogue
    e sad "Amanhã não devo ir às aulas, não tou com cabeça para isso."
    call algo(action=Action.Movement, next_area=currentarea)

# abel, nando
label .chat_51:
    call pass_time_dialogue
    ab normal "Estás a pensar ir ao jogo no sábado?"
    call pass_time_dialogue
    n normal "Não sei, tenho que falar com a Patrícia primeiro. Tu vais?"
    call pass_time_dialogue
    ab normal "Em princípio sim, mas preferia não estar a ir sozinho."
    call pass_time_dialogue
    n normal "Tá-se bem, eu depois digo-te qualquer coisa."
    call algo(action=Action.Movement, next_area=currentarea)

# samuel, tatiana
label .chat_52:
    call pass_time_dialogue
    s normal "Preciso de passar na biblioteca daqui a bocado. Vens comigo?"
    call pass_time_dialogue
    t normal "Sim, vamos. Aproveito para ver se há algum livro de interesse lá."
    call pass_time_dialogue
    s happy "Fixe."
    call algo(action=Action.Movement, next_area=currentarea)

# manuela, patricia
label .chat_53:
    call pass_time_dialogue
    m happy "A ida à praia no outro dia foi mesmo fixe!"
    call pass_time_dialogue
    p happy "Claro, quem tem as melhores ideias sempre? Sou eu!"
    call pass_time_dialogue
    c happy "Queres ir este fim de semana novamente?"
    call pass_time_dialogue
    p normal "Tenho que falar com os meus pais primeiro, mas à partida sim"
    call algo(action=Action.Movement, next_area=currentarea)

# jorge, rui
label .chat_54:
    call pass_time_dialogue
    j normal "Hoje à noite, queres jogar um bocado? Amanhã não vai haver a primeira aula."
    call pass_time_dialogue
    r normal "Ainda vou passar na Associação mas depois disso estou disponível."
    call pass_time_dialogue
    j normal "Mais ou menos a que horas, 18h00?"
    call pass_time_dialogue
    r normal "Aponta para as 18h30, mais coisa menos coisa."
    call algo(action=Action.Movement, next_area=currentarea)

#####

# nando, patricia
label .chat_55:
    call pass_time_dialogue
    p happy "Este fim de semana vens jantar a casa dos meus pais, não te esqueças."
    call pass_time_dialogue
    n normal "Sim, sim. Não vou esquecer."
    call pass_time_dialogue
    p normal "Disseste isso da outra vez. Certifica-te que não te esqueces mesmo."
    call pass_time_dialogue
    n annoyed "Pronto, eu coloco um alarme no telemóvel. Contente?"
    call pass_time_dialogue
    p happy "Sim!"
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, helder, isabel, samuel, tatiana - sinal 1
label .chat_56:
    call pass_time_dialogue
    t happy "A sério?"
    call pass_time_dialogue
    i happy "Sim, isso aconteceu mesmo!"
    call pass_time_dialogue
    h laugh "*risos*"
    call pass_time_dialogue
    e normal "*recebe uma notificação no telemóvel*"
    e normal "..."
    e angry "..."
    call pass_time_dialogue
    e angry "*atira com o telemóvel para dentro da mochila*"
    call algo(action=Action.Movement, next_area=currentarea)

# manuela
label .chat_57:
    call pass_time_dialogue
    m normal "*a utilizar o telemóvel*"
    call algo(action=Action.Movement, next_area=currentarea)

# abel, jorge, rui
label .chat_58:
    call pass_time_dialogue
    j normal "É verdade Rui, como anda isso da Associação?"
    call pass_time_dialogue
    r normal "Vai bem, o pessoal anda a fazer um bom trabalho."
    call pass_time_dialogue
    ab normal "Não sei como arranjas tempo para isso, para as aulas e ainda consegues jogar connosco."
    call pass_time_dialogue
    r laugh "Muita força de vontade!"
    call pass_time_dialogue
    ab laugh "*risos*"
    call algo(action=Action.Movement, next_area=currentarea)

# sinais de alerta, substituem chats 0 e 5

# estrela - sinal
label .chat_59:
    call pass_time_dialogue
    e angry "Mãe, já disse que está tudo bem!"
    call pass_time_dialogue
    e normal "..."
    call pass_time_dialogue
    e normal "Tive nega mas não se passa nada. Só tenho de estudar mais aquela matéria."
    call pass_time_dialogue
    e normal "Não, não vi a tua mensagem porque tinha o telemóvel desligado."
    call pass_time_dialogue
    e angry "Porquê? Porque não me apetece ter o telemóvel ligado! Qual é o problema?"
    call algo(action=Action.Movement, next_area=currentarea)

# estrela - sinal
label .chat_60:
    call pass_time_dialogue
    e sad "*a desenhar num caderno*"
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, helder - sinal
label .chat_61:
    call pass_time_dialogue
    h normal "Tiveste quanto no teste?"
    call pass_time_dialogue
    e sad "Tirei negativa..."
    call pass_time_dialogue
    h sad "Então? Mas tu fartaste-te de estudar!"
    call pass_time_dialogue
    e sad "..."
    call algo(action=Action.Movement, next_area=currentarea)

#####
#####
#####

# abel, manuela, nando, patricia
label .chat_cb3:
    hide screen clock
    "{i}Um grupo de alunos está a falar e ouve-se"
    $ situation = 60
    $ send_marker("before S2 SITUATION 3")
    call pass_time_dialogue
    p angry "Acham normal que a Isabel tenha dito à Cármen que lhe fazia uma espera?"
    call pass_time_dialogue
    m angry "Sabiam que ela agora é super amiguinha da Tatiana?"
    call pass_time_dialogue
    ab normal "O que ela precisa é que eu lhe ensine judo. Uahh!"
    call pass_time_dialogue
    ab normal "*faz movimentos de judo*"
    call pass_time_dialogue
    n laugh "*risos*"
    call pass_time_dialogue
    n normal "Não se preocupem, comigo eles não se metem. Têm de passar por mim para chegar a vocês."
    call pass_time_dialogue
    p normal "O meu herói! O que era mesmo top era fazer um vídeo do Abel a treinar judo com a Cármen e meter na net. Tipo aquele filme, Karate Kid."
    call pass_time_dialogue
    n normal "Se queres eu faço o vídeo, na boa."
    call pass_time_dialogue
    ab normal "Ya e identificamos a Estrela, a Isabel e a Tatiana."
    call pass_time_dialogue
    m sad "Não sei se é boa ideia..."
    call pass_time_dialogue
    p normal "Era só para as assustar, relaxa."
    call pass_time_dialogue
    ab happy "Pessoal, ia ser excelente!"
    $ send_marker("after S2 SITUATION 3")
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,0,1)
    call setup_dragndrops30
    call algo(action=Action.Movement, next_area=currentarea)

# abel, jorge, rui
label .chat_62:
    call pass_time_dialogue
    r normal "Abel, juntas-te a nós hoje?"
    call pass_time_dialogue
    ab normal "A fazer o quê?"
    call pass_time_dialogue
    j laugh "Jogar obviamente!"
    call pass_time_dialogue
    ab happy "Boooooooooooooooora!"
    call algo(action=Action.Movement, next_area=currentarea)

# samuel, tatiana
label .chat_63:
    call pass_time_dialogue
    t surprise "Ah, esqueci-me de comprar folhas de teste!"
    call pass_time_dialogue
    s normal "Eu tenho a mais, posso-te emprestar."
    call pass_time_dialogue
    t happy "Obrigada, eu depois pago-te de volta."
    call pass_time_dialogue
    s happy "Não é preciso."
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, helder
label .chat_64:
    call pass_time_dialogue
    h normal "Precisas de ajuda com a viagem, Estrela?"
    call pass_time_dialogue
    e normal "Não, deixa estar. Estou a fazer uma pausa disso por agora."
    call pass_time_dialogue
    h normal "Ok, mas se precisares de alguma coisa, já sabes."
    call pass_time_dialogue
    e normal "Eu sei, obrigada."
    call algo(action=Action.Movement, next_area=currentarea)

# isabel, manuela - ballet
label .chat_65:
    call pass_time_dialogue
    i normal "Vi o que escreveste no Com@Viver. Estás mesmo a pensar sair do ballet?"
    call pass_time_dialogue
    m sad "Não sei... Eu gosto daquilo mas não tenho a certeza se quero ficar lá para sempre."
    call pass_time_dialogue
    i sad "Eu percebo. É uma decisão dificíl."
    call pass_time_dialogue
    m sad "..."
    call algo(action=Action.Movement, next_area=currentarea)

# nando, patricia
label .chat_66:
    call pass_time_dialogue
    p normal "Nando, esta semana vamos às compras."
    call pass_time_dialogue
    n annoyed "Que seca... Porque não vais com a Cármen?"
    call pass_time_dialogue
    p happy "Não sei onde ela anda, mas de qualquer das formas, tu tens de vir connosco!"
    call pass_time_dialogue
    n annoyed "..."
    call algo(action=Action.Movement, next_area=currentarea)

##########

# carmen, manuela
label .chat_67:
    call pass_time_dialogue
    c normal "E que tal irmos sexta feira?"
    call pass_time_dialogue
    m normal "Parece-me bem."
    call pass_time_dialogue
    c happy "Ainda bem!"
    call algo(action=Action.Movement, next_area=currentarea)

# abel, nando, patricia, manuela
label .chat_68:
    call pass_time_dialogue
    ab happy "Pessoal, quando é que vamos a um concerto novamente? Não fui neste último por isso estou com a vontade toda."
    call pass_time_dialogue
    n happy "Por mim era já amanhã."
    call pass_time_dialogue
    p normal "Sim, nós não temos aulas nem nada."
    call pass_time_dialogue
    n laugh "Uma pessoa pode sempre imaginar!"
    call algo(action=Action.Movement, next_area=currentarea)

# samuel, tatiana
label .chat_69:
    call pass_time_dialogue
    s normal "Este fim de semana queres ir dar um passeio àquele parque perto do da outra vez?"
    call pass_time_dialogue
    t normal "Por mim sim. Podemos falar com a Isabel e o resto do pessoal para virem também."
    call pass_time_dialogue
    s normal "Yeap, eu falo com eles."
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, helder, isabel
label .chat_70:
    call pass_time_dialogue
    i happy "O que nós devíamos fazer era uma viagemzinha nas férias."
    call pass_time_dialogue
    e normal "Aonde?"
    call pass_time_dialogue
    i happy "Não interessa o lugar! Um sítio qualquer para relaxar."
    call pass_time_dialogue
    e happy "E o dinheiro para isso?"
    call pass_time_dialogue
    h laugh "Pois, sonhar também é relaxante e custa menos!"
    call algo(action=Action.Movement, next_area=currentarea)

# jorge, rui
label .chat_71:
    call pass_time_dialogue
    j normal "Depois manda-me uma mensagem quando estiveres despachado."
    call pass_time_dialogue
    r normal "Yeap, não te preocupes. Tenta não jogar muito sem mim."
    call pass_time_dialogue
    j happy "Claro!"
    call algo(action=Action.Movement, next_area=currentarea)

label .chat_72:
    
