init -1 python:
    class Char:
        next_id = 1
        def __init__(self, name, color, portrait, area, body):
            self.id = Char.next_id
            self.name = name
            self.color = color
            self.portrait = portrait
            self.area = area
            self.body = body
            #self.character = Character(name, color=color, image=portrait)
            Char.next_id += 1
        def __str__(self):
            return f"(S) {self.name}"
        def __repr__(self):
            if self.area != 0:
                return f"S {self.id}| {self.name}, {self.color}, {self.portrait}, {gameworld.areas[self.area].name}, {self.body}"
            else:
                return f"S {self.id}| {self.name}, {self.color}, {self.portrait}, No Area, {self.body}"

    class Char_Player(Char):
        def __init__(self, name, color, portrait, character):
            self.name = name
            self.color = color
            self.portrait = portrait
            self.character = character
        def __str__(self):
            return f"(Player) {self.name}"
        def __repr__(self):
            return f"Player| {self.name}, {self.color}, {self.portrait}"
