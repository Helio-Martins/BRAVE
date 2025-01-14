init python:
    import random
    class Gameworld:
        def __init__(self):
            self.player = Char_Player("[player_name]", "#808080", "", Character("[player_name]", image="player_image", color="#808080"))
            self.sections = [1,2,3]  
            self.topology = {}
            self.areas = {}
            self.connections = {}
            self.chars = {}
            self.gamestates = {}
            self.dialogues = {}
            self.tasks = {}
            self.events = {}
        def __str__(self):
            return f"(W) {self.areas}"
        def __repr__(self):
            return f"W| {self.areas}"
        def AddArea(self, area):
            self.areas[area.id] = deepcopy(area)
            self.topology[area.id] = []
            return
        def AddConnection(self, connection):
            self.connections[connection.id] = deepcopy(connection)
            self.areas[connection.areas[0]].connections[connection.id] = connection.areas[1]
            self.areas[connection.areas[1]].connections[connection.id] = connection.areas[0]
            self.topology[connection.areas[0]].append(connection.areas[1])
            self.topology[connection.areas[1]].append(connection.areas[0])
            return
        def AddChar(self, char):
            self.chars[char.id] = deepcopy(char)
            return
        def AddGamestate(self, gamestate):
            self.gamestates[gamestate.id] = deepcopy(gamestate)
            return
        def AddDialogue(self, dialogue):
            self.dialogues[dialogue.id] = deepcopy(dialogue)
            self.AddGamestate(Gamestate_Dialogue(dialogue.name, False))
            return
        def AddTask(self, task):
            self.tasks[task.id] = deepcopy(task)
            self.AddGamestate(Gamestate_Task(task.name, False))
            return
        def AddEvent(self, event):
            self.events[event.id] = deepcopy(event)
            self.AddGamestate(Gamestate_Event(event.name, False))
            return

    class Gameworld_RUNTIME(Gameworld):
        def __init__(self):
            self.player = deepcopy(gameworld.player)
            self.sections = [1,2,3]
            self.topology = deepcopy(gameworld.topology)
            self.areas = deepcopy(gameworld.areas)
            self.connections = deepcopy(gameworld.connections)
            self.chars = deepcopy(gameworld.chars)
            self.gamestates = deepcopy(gameworld.gamestates)
            self.dialogues = deepcopy(gameworld.dialogues)
            self.tasks = deepcopy(gameworld.tasks)
            self.events = deepcopy(gameworld.events)
            self.gamestates_occurred = []
            self.dialogues_activeprio = []
            self.dialogues_active = []
            self.dialogues_available = []
            self.dialogues_occurred = []
            self.tasks_active = []
            self.tasks_available = list(self.tasks.values())
            self.tasks_occurred = []
            self.events_available = list(self.events.values())
            self.events_occurred = []
            self.time = Time()
        def Consequences(self, cons):
            for gid,v in list(cons.items()):
                self.gamestates[gid].value = v
        def Populate(self):
            d_areas = [1,2,3,4,8,9,10]
            d_chars = [1,2,3,4,5,6,7,8,9,10,11,12]
            if currentarea.id in d_areas:
                d_areas.remove(currentarea.id)
            random.shuffle(d_areas)
            random.shuffle(d_chars)
            store.placeddialogues = {}
            self.dialogues_activeprio.sort()
            char_used = False

            ds = self.dialogues_activeprio
            random.shuffle(ds)
            # prio placed
            for d in ds:
                for c in d.chars:
                    if c not in d_chars:
                        char_used = True
                        break
                if char_used:
                    char_used = False
                    continue
                if d.GetType() == 3 and d.area not in placeddialogues:
                    placeddialogues[d.area] = d
                    ds.remove(d)
                    d_areas.remove(d.area)
                    for c in d.chars:
                        d_chars.remove(c)
            random.shuffle(ds)
            # prio normal
            for d in ds:
                if d_areas == {}:
                    break
                for c in d.chars:
                    if c not in d_chars:
                        char_used = True
                        break
                if char_used:
                    char_used = False
                    continue
                for a in d_areas:
                    if d.GetType() == 2:
                        placeddialogues[a] = d
                        d_areas.remove(a)
                        for c in d.chars:
                            d_chars.remove(c)
                        break

            ds = self.dialogues_active
            random.shuffle(ds)
            # placed
            for d in ds:
                for c in d.chars:
                    if c not in d_chars:
                        char_used = True
                        break
                if char_used:
                    char_used = False
                    continue
                if d.GetType() == 3 and d.area not in placeddialogues:
                    placeddialogues[d.area] = d
                    ds.remove(d)
                    d_areas.remove(d.area)
                    for c in d.chars:
                        d_chars.remove(c)
            random.shuffle(ds)
            # normal
            for d in ds:
                if d_areas == {}:
                    break
                for c in d.chars:
                    if c not in d_chars:
                        char_used = True
                        break
                if char_used:
                    char_used = False
                    continue
                for a in d_areas:
                    if d.GetType() == 2:
                        placeddialogues[a] = d
                        d_areas.remove(a)
                        for c in d.chars:
                            d_chars.remove(c)
                        break





        def Populate2(self):
            store.placeddialogues = {}
            print("populating")
            self.dialogues_activeprio.sort()
            ds = self.dialogues_activeprio
            for d in ds:
                if d.GetType() == 3 and d.area not in placeddialogues:
                    placeddialogues[d.area] = d
                    ds.remove(d)
                else:
                    break
            random.shuffle(ds)
            for d in ds:
                for a in d.areas:
                    if a not in placeddialogues:
                        print("place")
                        print(d)
                        print("place")
                        placeddialogues[a] = d
                        break
            ds = self.dialogues_active
            for d in ds:
                print("d in ds")
                if d.GetType() == 3 and d.area not in placeddialogues:
                    placeddialogues[d.area] = d
                    ds.remove(d)
                else:
                    break
            random.shuffle(ds)
            print("O")
            print(ds)
            for d in ds:
                print("d2 in ds")
                for a in d.areas:
                    print(f"for {a}")
                    if a not in placeddialogues:
                        print("place")
                        print(d)
                        print("place")
                        placeddialogues[a] = d
                        break
            #print(gameworld_runtime.dialogues_active)
            #for d in enumerate(self.dialogues_active.values()):
            #    ars[i].dialogue = d
            #ars = random.sample(list(self.areas.values()), len(self.areas))
            #for a in ars:
            #    a.dialogue = 0


       