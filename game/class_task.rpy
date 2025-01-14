init -1 python:
    class Task:
        next_id = 1
        def __init__(self, name, area, icon_idle, icon_hover, icon_x, icon_y, icon_rotation, icon_size, single_trigger = True, preconditions = {}, consequences = {}):
            self.id = Task.next_id
            self.name = name
            #self.session = session
            #self.section = section
            self.area = area
            self.icon_idle = icon_idle
            self.icon_hover = icon_hover
            self.icon_x = icon_x
            self.icon_y = icon_y
            self.icon_rotation = icon_rotation
            self.icon_size = icon_size
            self.single_trigger = single_trigger
            self.preconditions = preconditions
            self.consequences = consequences
            Task.next_id += 1
        def __str__(self):
            return "(T) " + self.name
        def __repr__(self):
            return "|T " + str(self.id) + "| " + self.name
        def Order(self):
            return 0
        def __eq__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            return self.id == other.id
        def __lt__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.Order == other.Order():
                return self.name < other.name
            return self.Order() < other.Order()
        def __le__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.Order == other.Order():
                return self.name <= other.name
            return self.Order() <= other.Order()
        def __gt__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.Order == other.Order():
                return self.name > other.name
            return self.Order() > other.Order()
        def __ge__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.Order == other.Order():
                return self.name >= other.name
            return self.Order() >= other.Order()