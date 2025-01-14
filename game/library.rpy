default gameworld = Gameworld()
default gameworld_runtime = None

image connection_red:
    "images/editor/connections/red.png"
    xsize 100 ysize 100
image connection_green:
    "images/editor/connections/green.png"
    xsize 100 ysize 100
image connection_blue:
    "images/editor/connections/blue.png"
    xsize 100 ysize 100
image connection_cyan:
    "images/editor/connections/cyan.png"
    xsize 100 ysize 100
image connection_magenta:
    "images/editor/connections/magenta.png"
    xsize 100 ysize 100
image connection_yellow:
    "images/editor/connections/yellow.png"
    xsize 100 ysize 100
image connection_default:
    "images/editor/connections/default.png"
    xsize 100 ysize 100

image task_book:
    "images/editor/task_icons/book.png"
    xsize 100 ysize 100
image task_books:
    "images/editor/task_icons/books.png"
    xsize 100 ysize 100
image task_files:
    "images/editor/task_icons/files.png"
    xsize 100 ysize 100
image task_laptop:
    "images/editor/task_icons/laptop.png"
    xsize 100 ysize 100
image task_notebook_1:
    "images/editor/task_icons/notebook_1.png"
    xsize 100 ysize 100
image task_notebook_2:
    "images/editor/task_icons/notebook_2.png"
    xsize 100 ysize 100

default default_area = "editor/areas/area (0).jpg"
default default_portrait = "editor/portraits/portrait (0).png"
default default_body = "editor/bodies/body (0).png"
default default_bodya = "editor/bodies/body (0).png"
default connection_images = ['connection_red', 'connection_green', 'connection_blue', 'connection_cyan', 'connection_magenta', 'connection_yellow']
default task_objects = ['task_book', 'task_books', 'task_files', 'task_laptop', 'task_notebook_1', 'task_notebook_2']

label populate_areas:
    $ gameworld.AddArea(Area("Area A", "editor/areas/area (1).jpg"))
    $ gameworld.AddArea(Area("Area B", "editor/areas/area (2).jpg"))
    $ gameworld.AddArea(Area("Area C", "editor/areas/area (3).jpg"))
    $ gameworld.AddArea(Area("Area D", "editor/areas/area (8).jpg"))
    return

label populate_connections:
    $ gameworld.AddEntry(Entry(1, 2, 5, 1600, 540, 'connection_red', 'connection_green', 90, 2))
    $ gameworld.AddEntry(Entry(2, 1, 5, 1920-1600, 540, 'connection_red', 'connection_green', -90, 2))
    $ gameworld.AddEntry(Entry(2, 3, 5, 1600, 240, 'connection_cyan', 'connection_yellow', 45, 1))
    $ gameworld.AddEntry(Entry(3, 2, 5, 1920-1600, 1080-240, 'connection_cyan', 'connection_yellow', 225, 1))
    $ gameworld.AddEntry(Entry(2, 4, 5, 735, 630, 'connection_blue', 'connection_magenta', 180, 3))
    $ gameworld.AddEntry(Entry(4, 2, 5, 735, 1080-830, 'connection_blue', 'connection_magenta', 0, 3))
    return

label populate_students:
    $ gameworld.AddStudent(Char("Afonso", "#e6194B", "editor/portraits/portrait (1).png", 1, "editor/bodies/body (1).png",
    Character("Afonso", color="#e6194B", image="editor/portraits/portrait (1).png")))
    $ gameworld.AddStudent(Char("Bruna", "#3cb44b", "editor/portraits/portrait (2).png", 2, "editor/bodies/body (2).png",
    Character("Bruna", color="#3cb44b", image="editor/portraits/portrait (2).png")))
    $ gameworld.AddStudent(Char("Carolina", "#ffe119", "editor/portraits/portrait (3).png", 3, "editor/bodies/body (3).png",
    Character("Carolina", color="#ffe119", image="editor/portraits/portrait (3).png")))
    $ gameworld.AddStudent(Char("Diogo", "#4363d8", "editor/portraits/portrait (4).png", 2, "editor/bodies/body (4).png",
    Character("Diogo", color="#4363d8", image="editor/portraits/portrait (4).png")))
    $ gameworld.AddStudent(Char("Elsa", "#911eb4", "editor/portraits/portrait (5).png", 1, "editor/bodies/body (5).png",
    Character("Elsa", color="#911eb4", image="editor/portraits/portrait (5).png")))
    $ gameworld.AddStudent(Char("Filipe", "#42d4f4", "editor/portraits/portrait (6).png", 0, "editor/bodies/body (6).png",
    Character("Filipe", color="#42d4f4", image="editor/portraits/portrait (6).png")))
    $ Afonso = Character("Afonso", color="#e6194B", image="editor/portraits/portrait (1).png")
    $ Bruna = Character("Bruna", color="#3cb44b", image="editor/portraits/portrait (2).png")
    $ Carolina = Character("Carolina", color="#ffe119", image="editor/portraits/portrait (3).png")
    $ Diogo = Character("Diogo", color="#4363d8", image="editor/portraits/portrait (4).png")
    $ Elsa = Character("Elsa", color="#911eb4", image="editor/portraits/portrait (5).png")
    $ Filipe = Character("Filipe", color="#42d4f4", image="editor/portraits/portrait (6).png")
    return

label populate_dialogues:
    $ gameworld.AddDialogue(Dialogue_Chat("Ice Cream", [1,2], [[1,1,"Sou o Afonso."],[2,3,"Sou a Bruna."]], True, {}, {1:True}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("Football", [3,4], [[3,3,"Olá."],[4,4,"Acho que ouvi a porta do pátio a fechar."]], True, {}, {2:True}, True, False))
    $ gameworld.AddDialogue(Dialogue_Chat("Videogames", [5,6], [[5,5,"Terceiro diálogo."],[6,6,"Este diálogo só aparece se falámos com o Afonso e a Bruna."]], True, {1:True}, {3:True}, True, False))
    return

label populate_events:
    $ gameworld.AddEvent(Event_DISABLE_AREA("Lock Patio", 4, True, {2:True}, {4:True}))
    return

label populate_tasks:
    #####
    return

label populate_gamestates:
    $ gameworld.AddGamestate(Gamestate_TIME_AFTER("TIME AFTER 30s", False, Time(0,0,30)))
    return