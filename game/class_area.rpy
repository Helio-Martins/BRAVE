init -1 python:
    class Area:
        next_id = 1
        def __init__(self, name, background):
            self.id = Area.next_id
            self.name = name
            self.background = background
            self.connections = {} # Stores connections, key is connection_id, value is other area id
            self.locked = False
            self.dialogue = 0
            self.tasks = []
            Area.next_id += 1
        def Lock(self):
            self.locked = True
        def Unlock(self):
            self.locked = False
        def Toggle(self):
            self.locked = not self.locked
        def __str__(self):
            return f"(AREA) {self.name}"
        def __repr__(self):
            return f"AREA {self.id}| {self.name}: {self.connections}"      