label d_day:

# carmen, manuela, patricia
label .chat_cb1:
    hide screen clock
    "{i}Um trio de raparigas aproxima-se e ouve-se a conversa entre elas"
    $ situation = 10
    $ send_marker("before S1 SITUATION 1")
    call pass_time_dialogue
    m happy "O título da foto podia ser: {i}\"A Baleia fora de água\"{/i}."
    call pass_time_dialogue
    p disgust "Eu meti um like. Se fosse eu a andar assim de biquíni, morria!"
    call pass_time_dialogue
    c laugh "Era o que ela devia fazer."
    call pass_time_dialogue
    m happy "*Risos*"
    call pass_time_dialogue
    c laugh "Da próxima vez escrevo isso mesmo. Mata-te!"
    call pass_time_dialogue
    m happy "Sim, não fazes falta a ninguém. Vai morrer longe!"
    call pass_time_dialogue
    c laugh "*Risos*"
    call pass_time_dialogue
    p annoyed "Para, tá ali um stôr. Esconde o telemóvel."
    $ send_marker("after S1 SITUATION 1")
    gameworld_runtime.player.character "{i}Conversa estranha... Devia de descobrir de quem elas estavam a falar."
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,0,1)
    call setup_dragndrops10
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, helder, rui
label .chat_12:
    call pass_time_dialogue
    h happy "Obrigada pela ajuda pessoal. Estrela, posso ficar com o teu caderno hoje e entrego-te amanhã?"
    call pass_time_dialogue
    e happy "Sem problema, mas não te esqueças!"
    call pass_time_dialogue
    h happy "Claro, não te preocupes."
    call pass_time_dialogue
    r normal "Olhem, vocês conseguiram resolver o exercício 3.2 do teste modelo? Eu ontem bem que tentei mas não consegui."
    call pass_time_dialogue
    e normal "O 3.2? Esse acho que não fiz."
    call pass_time_dialogue
    h normal "Pois eu não consegui o exercício 3 inteiro, por isso é que vim pedir apontamentos."
    call pass_time_dialogue
    r normal "Hmm ok, eu depois pergunto ao professor na aula."
    call pass_time_dialogue
    r normal "Já agora, algum de vocês sabe do Jorge? Ele não veio à aula de ontem."
    call pass_time_dialogue
    e normal "Eu não o vi."
    call pass_time_dialogue
    h normal "Também não."
    call algo(action=Action.Movement, next_area=currentarea)

# jorge, samuel
label .chat_1:
    call pass_time_dialogue
    s normal "Sempre vens a minha casa hoje à tarde?"
    call pass_time_dialogue
    j normal "Népia, hoje não posso."
    call pass_time_dialogue
    s normal "Então? Tavas todo entusiasmado no outro dia, e agora não podes?"
    call pass_time_dialogue
    j normal "Pois eu sei, mas hoje não dá mesmo jeito."
    call pass_time_dialogue
    j normal "*telefone a tocar*"
    call pass_time_dialogue
    j normal "Pera aí, preciso de atender isto, nós depois falamos mais tarde."
    call pass_time_dialogue
    s normal "Ok na boa, até já."
    call algo(action=Action.Movement, next_area=currentarea)

# abel, nando
label .chat_2:
    call pass_time_dialogue
    n happy "Vais lá estar na sexta feira, não é, Abel? Estou a contar contigo!"
    call pass_time_dialogue
    ab happy "Já sabes que sim Nando, futebol é comigo."
    call pass_time_dialogue
    n normal "Também convidei o Jorge, tou só à espera de resposta dele."
    call pass_time_dialogue
    ab happy "Se ele vier, ficamos com a equipa cheia."
    call pass_time_dialogue
    n normal "Yeap, e ele joga bem, por isso já tá ganho."
    call pass_time_dialogue
    ab laugh "Calma campeão, é o Jorge, não é o Ronaldo!"
    call pass_time_dialogue
    n laugh "*gargalhadas*"
    call algo(action=Action.Movement, next_area=currentarea)

# isabel, tatiana
label .chat_3:
    call pass_time_dialogue
    t sad "Tens um comprimido para a dor de cabeça?"
    call pass_time_dialogue
    i sad "Acho que sim, deixa ver na mala. Tatiana, tens a certeza que estás bem?"
    call pass_time_dialogue
    t sad "Não tenho conseguido dormir nada de jeito, é só isso..."
    call algo(action=Action.Movement, next_area=currentarea)

# helder, isabel
label .chat_4:
    call pass_time_dialogue
    h normal "Sempre consegues vir este fim de semana ao Centro de Apoio?"
    call pass_time_dialogue
    i happy "Sim! Tenho tarde livre por isso só preciso das horas."
    call pass_time_dialogue
    h normal "Fixe, em princípio podes aparecer lá a partir das 9h. Tens forma de ir para lá ou precisas de boleia?"
    call pass_time_dialogue
    i normal "Aquilo fica perto da estação não é?"
    call pass_time_dialogue
    h normal "Sim, são por volta de 10 minutos a pé."
    call pass_time_dialogue
    i happy "Então sem problema, eu vou de comboio e depois faço o resto a pé."
    call pass_time_dialogue
    h happy "Ok, então eu depois falo com eles e confirmo-te as horas."
    call algo(action=Action.Movement, next_area=currentarea)

# jorge, nando
label .chat_5:
    call pass_time_dialogue
    n normal "Na sexta vamos ter aquele torneio de futebol."
    call pass_time_dialogue
    j normal "Huh-huh."
    call pass_time_dialogue
    n normal "Queres aparecer lá?"
    call pass_time_dialogue
    j normal "Hum não sei, tenho de ver."
    call pass_time_dialogue
    n annoyed "Meu, como assim tens de ver. Parece que tás com a cabeça na lua..."
    call pass_time_dialogue
    j sad "Desculpa Nando, tou só a pensar noutras cenas. Futebol? Ya, parece-me bem, mas amanhã confirmo-te, sem falta."
    call pass_time_dialogue
    n happy "Pronto, era só isso que eu queria."
    call algo(action=Action.Movement, next_area=currentarea)

# abel, rui
label .chat_6:
    call pass_time_dialogue
    ab normal "Chegaste a ver o último episódio?"
    call pass_time_dialogue
    r happy "Sim! Não estava nada à espera do final, apanhou-me completamente de surpresa..."
    call pass_time_dialogue
    ab happy "É né?! Eu fiquei à toa, como é que eles vão continuar a história na segunda temporada? Estou para ver."
    call pass_time_dialogue
    r happy "Também estou curioso, agora que a personagem principal ficou do lado dos maus, tudo pode acontecer."
    call pass_time_dialogue
    ab normal "Olha, não comentes o final com o Jorge, ele ainda não viu o episódio!"
    call pass_time_dialogue
    r normal "Não percebo o que é que ele anda a fazer, ele hoje de manhã também não apareceu na aula."
    call pass_time_dialogue
    ab normal "Eu acho que ele foi sair ontem à tarde com mais pessoal, mas não tenho a certeza. Se calhar teve a ver com isso."
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, samuel
label .chat_7:
    call pass_time_dialogue
    e normal "A Tatiana? Sabes dela?"
    call pass_time_dialogue
    s sad "Tem estado na casa de banho a maior parte do dia."
    call pass_time_dialogue
    e sad "Então? Ela está mal disposta ou algo assim?"
    call pass_time_dialogue
    s sad "Não, tu não viste o que lhe fizeram?"
    call pass_time_dialogue
    e sad "Não..."
    call pass_time_dialogue
    s sad "Eu depois desta aula conto-te."
    call algo(action=Action.Movement, next_area=currentarea)

# tatiana
label .chat_8:
    call pass_time_dialogue
    t sad "*a olhar para o telemóvel*"
    call algo(action=Action.Movement, next_area=currentarea)

# sinais de alerta, substituem chats 3 e 8

# tatiana
label .chat_11:
    call pass_time_dialogue
    t normal "*a ouvir música*"
    call pass_time_dialogue
    grupo_alunos "*apontam para a Tatiana enquanto riem*"
    call pass_time_dialogue
    t sad "*esconde a cabeça entre os braços*"
    call algo(action=Action.Movement, next_area=currentarea)

# tatiana
label .chat_9:
    call pass_time_dialogue
    t normal "*a mexer no telemóvel*"
    call pass_time_dialogue
    t normal "*som de mensagem*"
    call pass_time_dialogue
    t sad "..."
    call algo(action=Action.Movement, next_area=currentarea)

# tatiana
label .chat_10:
    call pass_time_dialogue
    t cry "..."
    call algo(action=Action.Movement, next_area=currentarea)

# carmen, manuela, patricia
label .chat_13:
    call pass_time_dialogue
    c happy "Esta semana querem ir ao shopping?"
    call pass_time_dialogue
    m normal "Outra vez? Fomos a semana passada."
    call pass_time_dialogue
    c happy "Anda lá!"
    call pass_time_dialogue
    p normal "Eu não me importo."
    call pass_time_dialogue
    m normal "..."
    m normal "Logo vejo."
    call algo(action=Action.Movement, next_area=currentarea)

#####
#####
#####

# estrela
label .chat_14:
    call pass_time_dialogue
    e disgust "*concentrada a ler documentos relacionados com a viagem*"
    call algo(action=Action.Movement, next_area=currentarea)

# samuel, tatiana
label .chat_15:
    call pass_time_dialogue
    s sad "Estás melhor?"
    call pass_time_dialogue
    t sad "Sim, está tudo bem. Mais do mesmo."
    call pass_time_dialogue
    s happy "Que tal irmos sair hoje à tarde? Podemos passar naquele parque ao pé do rio."
    call pass_time_dialogue
    t happy "Boa ideia, talvez me dê um bocadinho de sossego."
    call pass_time_dialogue
    s happy "Ok, então depois das aulas eu passo pela biblioteca para imprimir um documento e depois vou ter contigo à entrada."
    call pass_time_dialogue
    t normal "Está bem."
    call algo(action=Action.Movement, next_area=currentarea)

# jorge, nando
label .chat_16:
    call pass_time_dialogue
    n annoyed "*a olhar para o telemóvel*"
    call pass_time_dialogue
    j normal "Nando! Então? O que é tás a fazer?"
    call pass_time_dialogue
    n normal "Ah, nada, nada. Onde é que íamos?"
    call pass_time_dialogue
    j normal "Ao bar. Tá tudo bem?"
    call pass_time_dialogue
    n sad "Ya, tudo. Por acaso não viste a Patrícia, pois não?"
    call pass_time_dialogue
    j happy "Não. É a tua namorada, não é minha."
    call pass_time_dialogue
    n normal "Muito engraçado. Anda masé ao bar."
    call algo(action=Action.Movement, next_area=currentarea)

# rui, isabel, abel
label .chat_17:
    call pass_time_dialogue
    r normal "Pessoal, como querem fazer com o projeto? Podemos começar a distribuir tarefas se quiserem."
    call pass_time_dialogue
    i normal "Por mim tanto faz, é como preferirem."
    call pass_time_dialogue
    ab normal "Eu não me faz diferença, podemos reunir já hoje à tarde se quiserem."
    call pass_time_dialogue
    r normal "Por mim tudo bem. E contigo Isabel?"
    call pass_time_dialogue
    i happy "Eu também posso! Passamos na biblioteca então?"
    call pass_time_dialogue
    ab normal "Ya, pode ser."
    call pass_time_dialogue
    r normal "Falamos mais tarde então."
    call algo(action=Action.Movement, next_area=currentarea)

# helder
label .chat_18:
    call pass_time_dialogue
    h happy "*focado no telemóvel*"
    call algo(action=Action.Movement, next_area=currentarea)

# carmen, manuela, patricia
label .chat_19:
    call pass_time_dialogue
    p disgust "Ela agora vai acalmar."
    call pass_time_dialogue
    c disgust "E se não acalmar, já sabe o que acontece se continua com as tretas dela."
    call pass_time_dialogue
    m happy "Mudando de assunto, vocês já viram quem vai dar um concerto no verão? Tou bué entusiasmada!"
    call pass_time_dialogue
    p happy "Sim, temos de ir ver!"
    call pass_time_dialogue
    c happy "Bora! Eu já falei com os meus pais, eles deixam-me ir!"
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, samuel, tatiana
label .chat_20:
    call pass_time_dialogue
    e normal "Pessoal, podíamos ver do projeto já este fim de semana? Tenho receio que depois não tenha tempo para fazer tudo, já assumindo que o plano da viagem corre perfeitamente."
    call pass_time_dialogue
    t normal "Sim, sem problemas. Eu este sábado à tarde estou disponível."
    call pass_time_dialogue
    s normal "Eu também. Falamos online?"
    call pass_time_dialogue
    e normal "Sim, acho que para primeiro dia não precisamos de estar presentes."
    call pass_time_dialogue
    t normal "A que horas querem marcar?"
    call pass_time_dialogue
    e normal "Por mim pode ser logo a seguir ao almoço, às 13h00."
    call pass_time_dialogue
    s normal "Às 13h00 eu ainda não estou em casa, podemos fazer às 14h00?"
    call pass_time_dialogue
    e normal "Claro, por mim é na boa."
    call pass_time_dialogue
    t normal "Está bem, fica marcado para as 14h00."
    call algo(action=Action.Movement, next_area=currentarea)

# nando
label .chat_21:
    call pass_time_dialogue
    n mean "Pensava que te tinha avisado para não passares ao pé de mim!"
    call pass_time_dialogue
    aluno "Desculpa Nando, foi sem querer... Eu vou embora!"
    call pass_time_dialogue
    n mean "Vai, vai, eu ajudo-te!"
    call pass_time_dialogue
    n mean "*empurra o outro aluno*"
    call pass_time_dialogue
    aluno "*foge a correr*"
    call pass_time_dialogue
    n mean "Bem me parecia..."
    call algo(action=Action.Movement, next_area=currentarea)

# helder, isabel
label .chat_22:
    call pass_time_dialogue
    i happy "Só quero acabar o secundário para pedir aos meus pais para ir viajar!"
    call pass_time_dialogue
    h normal "Onde é que estás a pensar ir?"
    call pass_time_dialogue
    i normal "Não tenho nenhum país específico que queira ir, mas gostava de visitar cidades com arranhas céus. Nunca estive num prédio alto."
    call pass_time_dialogue
    h happy "Eu pessoalmente também gostaria de viajar daqui a uns anos, mas provavelmente seria para visitar sítios com serras, montanhas e paisagens. O melhor que a natureza tiver para oferecer."
    call pass_time_dialogue
    i happy "Esses sítios também parecem ser incriveís. Temos de combinar uma viagem para irmos e convidamos mais pessoas para virem também!"
    call algo(action=Action.Movement, next_area=currentarea)

# carmen
label .chat_23:
    call pass_time_dialogue
    c normal "*a ouvir música*"
    call algo(action=Action.Movement, next_area=currentarea)

# abel, jorge, rui
label .chat_24:
    call pass_time_dialogue
    ab normal "Jorge, precisava de fala contigo acerca do torneio."
    call pass_time_dialogue
    j sad "Desculpa, agora não posso. Tou mesmo mega ocupado. Já falamos."
    call pass_time_dialogue
    j sad "*vai embora*"
    call pass_time_dialogue
    r normal "O que se passa com ele?"
    call pass_time_dialogue
    ab normal "Não sei, mas ele anda a agir de forma bué estranha."
    call algo(action=Action.Movement, next_area=currentarea)

# manuela, patricia
label .chat_27:
    call pass_time_dialogue
    p sad "O Nando já não pode dar mais faltas. Está sempre a ir para a rua. Já falei com ele, mas não quer saber."
    call pass_time_dialogue
    m sad "Linda, não fiques assim."
    call algo(action=Action.Movement, next_area=currentarea)

# sinais de alerta, substituem chats 2 e 7

# jorge, nando
label .chat_26:
    call pass_time_dialogue
    j normal "O comentário do BossLikeMe_14 ontem às 2 da manhã era teu?"
    call pass_time_dialogue
    n normal "Ya, essa é a minha outra conta. Sabes como é mano."
    call algo(action=Action.Movement, next_area=currentarea)

# nando
label .chat_25:
    call pass_time_dialogue
    n mean "*chuta um caixote do lixo*"
    call pass_time_dialogue
    auxiliar "*aproxima-se do Nando com ar de zangada*"
    call pass_time_dialogue
    n laugh "*vira costas à auxiliar e vai-se embora*"
    call algo(action=Action.Movement, next_area=currentarea)

#####
#####
#####

# abel, carmen, estrela, helder, manuela, nando, patricia
label .chat_cb3:
    hide screen clock
    "{i}Um grupo grande de alunos está a ter uma discussão"
    $ situation = 30
    $ send_marker("before S1 SITUATION 3")
    call pass_time_dialogue
    n laugh "Mano, a Tatiana é o maior desperdício de oxigénio que anda por aí!"
    call pass_time_dialogue
    p disgust "Tem a mania que é melhor do que os outros, só porque passa os dias a estudar. Normal, não tem vida."
    call pass_time_dialogue
    ab laugh "Não tem vida, mas anda com todos."
    call pass_time_dialogue
    c laugh "*risos*"
    call pass_time_dialogue
    m happy "*risos*"
    call pass_time_dialogue
    e sad "Não veem que ela está bué mal? O que fizeram foi horrível!"
    call pass_time_dialogue
    n laugh "*finge que chora* Ah, coitadinha! Buáaaaa."
    call pass_time_dialogue
    p angry "Ela sabe bem o que me fez primeiro!"
    call pass_time_dialogue
    e angry "Se fizerem mais alguma cena vou falar com o DT."
    call pass_time_dialogue
    c angry "Não sejas uma falsa, Estrela. Lá porque és delegada de turma, pensas que mandas."
    call pass_time_dialogue
    n angry "Cala a boca, Estrela! Quem se meter nisto leva no focinho! E os seus amiguinhos todos."
    call pass_time_dialogue
    h angry "Epá, calma que eu não tenho nada a ver com isto."
    call pass_time_dialogue
    e disgust "Queres ser outra vez suspenso, Nando? Não te bastou o ano passado?"
    call pass_time_dialogue
    n laugh "Eu faço o que quero! Ninguém manda em mim, ainda não percebeste?"
    $ send_marker("after S1 SITUATION 3")
    image currentscene:
        currentarea.background
        size (config.screen_width, config.screen_height)
    scene currentscene with Fade(1,0,1)
    call setup_dragndrops30
    call algo(action=Action.Movement, next_area=currentarea)

# abel, jorge, rui
label .chat_28:
    call pass_time_dialogue
    ab normal "Jorge, tu vens ao torneio sexta feira não vens? Tens andado meio desaparecido."
    call pass_time_dialogue
    j normal "Epa ya, tive uma consulta de dentista e outras coisas, tudo ao mesmo tempo. Em princípio na sexta vou ao torneio. "
    call pass_time_dialogue
    ab laugh "Fixe! Vê lá se consegues tirar a bola ao adversário desta vez!"
    call pass_time_dialogue
    r laugh "*risos*"
    call pass_time_dialogue
    j happy "Metes muita piada Abel, mas da outra vez fui eu que marquei o golo de vitória!"
    call pass_time_dialogue
    ab happy "Lá isso é verdade, e honestamente foi um bom golo!"
    call pass_time_dialogue
    j happy "Então e tu Rui, não queres vir também? Há sempre a chance de alguém faltar."
    call pass_time_dialogue
    r happy "Até ia mas futebol não é comigo. Mas obrigado pelo convite."
    call pass_time_dialogue
    ab laugh "Não sei até que ponto alguém faltaria, depois tinham de enfrentar o Nando."
    call pass_time_dialogue
    r normal "Por falar em Nando, onde é que ele anda? Queria falar com ele que ultimamente ele anda a abusar um bocado."
    call pass_time_dialogue
    j angry "Rui, faz como eu e não te metas nisso. Se não tem nada a ver contigo, para quê te meteres ao barulho?"
    call pass_time_dialogue
    r angry "Pah eu não sou assim, se eu vejo uma cena mal, vou dizer o que penso."
    call algo(action=Action.Movement, next_area=currentarea)

# samuel, tatiana - posts
label .chat_29:
    call pass_time_dialogue
    s sad "Não fiques assim, não vale a pena."
    call pass_time_dialogue
    t sad "Eu sei. Não te preocupes. Isto já passa."
    call pass_time_dialogue
    s sad "Chegaste a falar com a tua irmã? Sempre vamos sair todos amanhã à tarde?"
    call pass_time_dialogue
    t sad "Não, desculpa, esqueci-me. Hoje quando chegar a casa eu falo com ela."
    call pass_time_dialogue
    s sad "Ok, sem problemas. Se precisares de alguma coisa, diz."
    call pass_time_dialogue
    t sad "..."
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, helder - atividades
label .chat_30:
    call pass_time_dialogue
    h normal "Que atividades tens planeadas, Estrela?"
    call pass_time_dialogue
    e normal "Por agora, ainda só tenho duas. Estou à espera de resposta do Jorge para avançar com esta parte."
    call pass_time_dialogue
    h normal "Ah ok. E em relação à viagem, já sabes se vamos para a Costa ou para o Algarve?"
    call pass_time_dialogue
    e normal "Ainda não está definido, mas parece-me que vai ser no Algarve."
    call pass_time_dialogue
    h happy "Fixe!"
    call pass_time_dialogue
    e normal "Pena que nem toda a gente partilhe do teu entusiasmo, senão isto já estava decidido."
    call pass_time_dialogue
    h normal "Pois, a Cármen não tem facilitado a marcação da viagem. Já para não falar do que elas andam a dizer no Com@Viver."
    call pass_time_dialogue
    e angry "A este ponto é só vergonhoso o que estão a fazer."
    call algo(action=Action.Movement, next_area=currentarea)

# isabel, manuela - ballet
label .chat_31:
    call pass_time_dialogue
    i happy "Ainda não acredito que ganhaste o concurso Manuela! Parabéns!"
    call pass_time_dialogue
    m happy "Obrigada! Nem imaginas o quão nervosa eu estava no dia da prova!"
    call pass_time_dialogue
    i happy "Nem quero imaginar. Mas o ano passado já tinhas ido a um concurso não era?"
    call pass_time_dialogue
    m normal "Sim, mas este ano a pressão era maior. Deve ser o último ano em que vou competir."
    call pass_time_dialogue
    i normal "A sério? Pensava que ias continuar no ballet durante muito tempo."
    call pass_time_dialogue
    m sad "Não sei, já estou no ballet há imensos anos e queria tentar outras coisas. Ainda tenho de decidir."
    call algo(action=Action.Movement, next_area=currentarea)

# carmen, nando, patricia
label .chat_32:
    call pass_time_dialogue
    n mean "Viste bem Patrícia? Ela nem falou mais depois do meu post."
    call pass_time_dialogue
    c disgust "Ela também não ia adicionar nada de relevante."
    call pass_time_dialogue
    p disgust "Com sorte aprendeu a lição e não volta a colocar aqueles posts provocadores que ela mete."
    call pass_time_dialogue
    n normal "De qualquer das formas, se ela te volta a chatear diz-me que eu trato da situação."
    call pass_time_dialogue
    p normal "Eu sei. Mas tens de ter cuidado, no outro dia vi oS professores a falarem entre si."
    call pass_time_dialogue
    n normal "Não te preocupes, eles não sabem de nada."
    call algo(action=Action.Movement, next_area=currentarea)

# carmen, patricia
label .chat_33:
    call pass_time_dialogue
    c disgust "É preciso ter lata. Agora anda pela escola a fingir que chora."
    call pass_time_dialogue
    p disgust "Era tão mais simples se ela mudasse de escola. A vida de todos melhorava."
    call pass_time_dialogue
    c disgust "Sim, ela não ia fazer falta a ninguém."
    call pass_time_dialogue
    p disgust "A ninguém não. Ia fazer falta ao Samuel. Já viste como ele anda colado a ela?"
    call pass_time_dialogue
    c disgust "Claro, ele sabe que não arranja melhor."
    call pass_time_dialogue
    p disgust "Mesmo. Lá nisso eles são perfeitos um para outro."
    call algo(action=Action.Movement, next_area=currentarea)

# abel, nando - generico
label .chat_34:
    call pass_time_dialogue
    ab normal "Viste o jogo de ontem?"
    call pass_time_dialogue
    n happy "Ya, cheguei a pensar que távamos a jogar sozinhos. A outra equipa parecia que estava a jogar com a equipa B."
    call pass_time_dialogue
    ab happy "Curtiste do ponta de lança a levar 3 foras de jogo?"
    call pass_time_dialogue
    n laugh "YA! Ele não deve ter dormido como deve ser."
    call pass_time_dialogue
    ab laugh "Pois, só pode!"
    call algo(action=Action.Movement, next_area=currentarea)

# manuela
label .chat_35:
    call pass_time_dialogue
    m normal "*a ouvir música*"
    call algo(action=Action.Movement, next_area=currentarea)

# helder
label .chat_36:
    call pass_time_dialogue
    h normal "*a comer uma sandes*"
    call algo(action=Action.Movement, next_area=currentarea)

# jorge, samuel, tatiana
label .chat_37:
    call pass_time_dialogue
    s normal "Olha ele, então? Onde tens andado?"
    call pass_time_dialogue
    j normal "Dentista, e muitas outras coisas. Tenho andado ocupado."
    call pass_time_dialogue
    t normal "Tem cuidado, os professores não gostam que faltem às aulas."
    call pass_time_dialogue
    j normal "Eu sei, tenho de pedir à minha mãe um atestado do dentista para dar ao stôr."
    call pass_time_dialogue
    s happy "Bom saber que não se passa nada contigo. Para a próxma diz alguma cena ao pessoal."
    call pass_time_dialogue
    j happy "Ya, não te preocupes."
    call algo(action=Action.Movement, next_area=currentarea)

# estrela, isabel, rui
label .chat_38:
    call pass_time_dialogue
    r angry "Ele disse isso?"
    call pass_time_dialogue
    e angry "Sim."
    call pass_time_dialogue
    i sad "Isto está bué grave pessoal."
    call pass_time_dialogue
    e angry "Pois. Acho que tenho mesmo de falar com o D.T."
    call pass_time_dialogue
    r angry "Não fales já. Eu quero falar com ele primeiro."
    call pass_time_dialogue
    i sad "Rui, não sei se isso é boa ideia... Vocês ainda vão entrar numa luta."
    call pass_time_dialogue
    r angry "Eu não tenciono lutar, e nem o Nando é assim tão parvo."
    call pass_time_dialogue
    e angry "Tens mesmo a certeza disso? Tens mais fé nele do que devias."
    call algo(action=Action.Movement, next_area=currentarea)

