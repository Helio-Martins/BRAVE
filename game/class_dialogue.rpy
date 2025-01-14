init -1 python:
    class Dialogue:
        next_id = 1
        def __init__(self, name, chars, lines, single_trigger, preconditions, consequences, selfremove):
            self.id = Dialogue.next_id
            self.name = name
            self.chars = chars
            self.lines = lines
            self.single_trigger = single_trigger
            self.preconditions = preconditions
            self.consequences = consequences
            self.selfremove = selfremove
            if self.GetType() == 2:
                nodes = []
                for s in gameworld.chars:
                    if gameworld.chars[s].area != 0:
                        nodes.append(s.area)
                self.areas = bfs(gameworld.topology, average_distance(gameworld.topology, nodes))
            Dialogue.next_id += 1
        def __str__(self):
            return f"(D) {self.name}"
        def __repr__(self):
            return f"D {self.id}"#| {self.name}, {self.chars}, {self.preconditions}, {self.consequences}, {self.selfremove}"
        def GetType(self):
            if isinstance(self, Dialogue_Text):
                return 1
            elif isinstance(self, Dialogue_Chat):
                return 2
            elif isinstance(self, Dialogue_Localized):
                return 3
            return 0
        def __eq__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            return self.id == other.id
        def __lt__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.GetType() == other.GetType():
                return self.name < other.name
            return self.GetType() < other.GetType()
        def __le__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.GetType() == other.GetType():
                return self.name <= other.name
            return self.GetType() <= other.GetType()
        def __gt__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.GetType() == other.GetType():
                return self.name > other.name
            return self.GetType() > other.GetType()
        def __ge__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            if self.GetType() == other.GetType():
                return self.name >= other.name
            return self.GetType() >= other.GetType()
        def __ne__(self, other):
            if not isinstance(other, Dialogue):
                return NotImplemented
            return self.id != other.id

    class Dialogue_Text(Dialogue):
        def __init__(self, name, chars, lines, single_trigger, preconditions, consequences, selfremove):
            super().__init__(name, chars, lines, single_trigger, preconditions, consequences, selfremove)
            
    class Dialogue_Chat(Dialogue):
        def __init__(self, name, chars, lines, single_trigger, preconditions, consequences, selfremove, priority):
            super().__init__(name, chars, lines, single_trigger, preconditions, consequences, selfremove)
            self.priority = priority

    class Dialogue_Localized(Dialogue):
        def __init__(self, name, chars, lines, single_trigger, preconditions, consequences, selfremove, priority, area):
            super().__init__(name, chars, lines, single_trigger, preconditions, consequences, selfremove)
            self.priority = priority
            self.area = area
