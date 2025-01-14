init -1 python:
    class Connection:
        next_id = 1
        def __init__(self, areas, time, icon_xy, icon_idle, icon_hover, icon_rotation = 0, icon_size = 1):
            self.id = Connection.next_id
            self.areas = areas
            self.time = time
            self.icon_xy = icon_xy
            self.icon_idle = icon_idle
            self.icon_hover = icon_hover
            self.icon_rotation = icon_rotation
            self.icon_size = icon_size
            self.locked = False
            Connection.next_id += 1
        def Lock(self):
            self.locked = True
        def Unlock(self):
            self.locked = False
        def Toggle(self):
            self.locked = not self.locked
        def Index(self, area):
            if area == self.areas[0]:
                return 0
            else:
                return 1
        def Destination(self, area):
            if area == self.areas[0]:
                return areas[1]
            else:
                return areas[0]
        def __str__(self):
            return f"{gameworld.areas[self.areas[0]].name}->\n<-{gameworld.areas[self.areas[1]].name}"
        def __repr__(self):
            return f"CONNECT {self.id}| {gameworld.areas[self.origin].name}<->{gameworld.areas[self.destination].name}"