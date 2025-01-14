init -1 python:
    class Gamestate:
        next_id = 1
        def __init__(self, name, value):
            self.id = Gamestate.next_id
            self.name = name
            self.value = value
            Gamestate.next_id += 1
        def __str__(self):
            return f"{self.name}"
        def __repr__(self):
            return f"G {self.id}| {self.name}, Value: {self.value}"
        def Prime(self):
            return True
        def UpdateData(self, name, value, property1, property2):
            self.name = name
            self.value = value
        def GetType(self):
            if isinstance(self, Gamestate_Dialogue):
                return 1
            elif isinstance(self, Gamestate_Task):
                return 2
            elif isinstance(self, Gamestate_Event):
                return 3
            elif isinstance(self, Gamestate_TIME_AFTER):
                return 4
            elif isinstance(self, Gamestate_TIME_BETWEEN):
                return 5
            elif isinstance(self, Gamestate_CURRENT_AREA):
                return 6
            elif isinstance(self, Gamestate_AREA_VISITS):
                return 7
            elif isinstance(self, Gamestate_CONNECTION_VISITS):
                return 8
            return 0
        def __eq__(self, other):
            if not isinstance(other, Gamestate):
                return NotImplemented
            return self.id == other.id
        def __lt__(self, other):
            if not isinstance(other, Gamestate):
                return NotImplemented
            return self.GetType() < other.GetType() and self.name < other.name
        def __le__(self, other):
            if not isinstance(other, Gamestate):
                return NotImplemented
            return self.GetType() <= other.GetType() and self.name <= other.name
        def __gt__(self, other):
            if not isinstance(other, Gamestate):
                return NotImplemented
            return self.GetType() > other.GetType() and self.name > other.name
        def __ge__(self, other):
            if not isinstance(other, Gamestate):
                return NotImplemented
            return self.GetType() >= other.GetType() and self.name >= other.name
        def __ne__(self, other):
            if not isinstance(other, Gamestate):
                return NotImplemented
            return self.id != other.id

    class Gamestate_Dialogue(Gamestate):
        def __init__(self, name, value):
            super().__init__(name, value)
        def __str__(self):
            return f"(GD) {self.name}"
        def __repr__(self):
            return f"GD {self.id}| {self.name}, Value: {self.value}"
    
    class Gamestate_Task(Gamestate):
        def __init__(self, name, value):
            super().__init__(name, value)
        def __str__(self):
            return f"(GT) {self.name}"
        def __repr__(self):
            return f"GT {self.id}| {self.name}, Value: {self.value}"
    
    class Gamestate_Event(Gamestate):
        def __init__(self, name, value):
            super().__init__(name, value)
        def __str__(self):
            return f"(GE) {self.name}"
        def __repr__(self):
            return f"GE {self.id}| {self.name}, Value: {self.value}"
    
    class Gamestate_TIME_AFTER(Gamestate):
        def __init__(self, name, value, time):
            super().__init__(name, value)
            self.time = time
        def __repr__(self):
            return f"G {self.id}| {self.name}, Value: {self.value}, TIME_AFTER: {self.time}"
        def Prime(self):
            if self.time < gameworld_runtime.time: 
                return True
            return False
        def UpdateData(self, name, value, property1, property2):
            self.name = name
            self.value = value
            self.time = propert1

    class Gamestate_TIME_BETWEEN(Gamestate):
        def __init__(self, name, value, time1, time2):
            super().__init__(name, value)
            self.time1 = time1
            self.time2 = time2
        def __repr__(self):
            return f"G {self.id}| {self.name}, Value: {self.value}, TIME_BETWEEN: {self.time1}-{self.time2}"
        def Prime(self):
            if self.time1 <= gameworld_runtime.time and self.time2 >= gameworld_runtime.time: 
                return True
            return False
        def UpdateData(self, name, value, property1, property2):
            self.name = name
            self.value = value
            self.time1 = property1
            self.time2 = property2

    class Gamestate_CURRENT_AREA(Gamestate):
        def __init__(self, name, value, area):
            super().__init__(name, value)
            self.area = area
        def __repr__(self):
            return f"G {self.id}| {self.name}, Value: {self.value}, CURRENT_AREA: {self.area}"
        def Prime(self):
            if gameworld_runtime.areas[self.area] == sim_currentarea: 
                return True
            return False
        def UpdateData(self, name, value, property1, property2):
            self.name = name
            self.value = value
            self.area = property1

    class Gamestate_AREA_VISITS(Gamestate):
        def __init__(self, name, value, area, visits):
            super().__init__(name, value)
            self.area = area
            self.visits = visits
        def __repr__(self):
            return f"G {self.id}| {self.name}, Value: {self.value}, AREA_VISITS: {self.area} {self.visits}"
        def Prime(self):
            if sim_area_visits[self.area] >= visits: 
                return True
            return False
        def UpdateData(self, name, value, property1, property2):
            self.name = name
            self.value = value
            self.area = property1
            self.visits = property2

    class Gamestate_CONNECTION_VISITS(Gamestate):
        def __init__(self, name, value, connection, visits):
            super().__init__(name, value)
            self.connection = connection
            self.visits = visits
        def __repr__(self):
            return f"G {self.id}| {self.name}, Value: {self.value}, CONNECTION_VISITS: {self.connection} {self.visits}"
        def Prime(self):
            if sim_connection_visits[self.connection] >= visits: 
                return True
            return False
        def UpdateData(self, name, value, property1, property2):
            self.name = name
            self.value = value
            self.connection = property1
            self.visits = property2

    class Gamestate_Type(IntEnum):
        NORMAL = 0
        TIME_AFTER = 1
        TIME_BETWEEN = 2
        CURRENT_AREA = 3
        AREA_VISITS = 4
        CONNECTION_VISITS = 5