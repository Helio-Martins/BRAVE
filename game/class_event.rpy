init -1 python:
    class Event:
        next_id = 1
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            self.id = Event.next_id
            self.name = name
            self.target = target
            self.single_trigger = single_trigger
            self.preconditions = preconditions
            self.consequences = consequences
            Event.next_id += 1
        def Target(self):
            return ""
        def Trigger(self):
            return -1
        def __str__(self):
            return f"(E) {self.name}"
        def __repr__(self):
            return f"E {self.id}| {self.name}, {self.single_trigger}, {self.preconditions}, {self.consequences}"
        def GetType(self):
            if isinstance(self, Event_ENABLE_AREA):
                return 1
            elif isinstance(self, Event_DISABLE_AREA):
                return 2
            elif isinstance(self, Event_TOGGLE_AREA):
                return 3
            if isinstance(self, Event_ENABLE_CONNECTION):
                return 4
            elif isinstance(self, Event_DISABLE_CONNECTION):
                return 5
            elif isinstance(self, Event_TOGGLE_CONNECTION):
                return 6
            if isinstance(self, Event_ACTIVATE_GAMESTATE):
                return 7
            elif isinstance(self, Event_DEACTIVATE_GAMESTATE):
                return 8
            elif isinstance(self, Event_TOGGLE_GAMESTATE):
                return 9
            elif isinstance(self, Event_FORCE_DIALOGUE):
                return 10
            elif isinstance(self, Event_REMOVE_DIALOGUE):
                return 11
            elif isinstance(self, Event_FORCE_EVENT):
                return 12
            elif isinstance(self, Event_REMOVE_EVENT):
                return 13
            return 0
        def __eq__(self, other):
            if not isinstance(other, Event):
                return NotImplemented
            return self.id == other.id
        def __lt__(self, other):
            if not isinstance(other, Event):
                return NotImplemented
            if self.GetType == other.GetType():
                return self.name < other.name
            return self.GetType() < other.GetType()
        def __le__(self, other):
            if not isinstance(other, Event):
                return NotImplemented
            if self.GetType == other.GetType():
                return self.name <= other.name
            return self.GetType() <= other.GetType()
        def __gt__(self, other):
            if not isinstance(other, Event):
                return NotImplemented
            if self.GetType == other.GetType():
                return self.name > other.name
            return self.GetType() > other.GetType()
        def __ge__(self, other):
            if not isinstance(other, Event):
                return NotImplemented
            if self.GetType == other.GetType():
                return self.name >= other.name
            return self.GetType() >= other.GetType()
        def __ne__(self, other):
            if not isinstance(other, Event):
                return NotImplemented
            return self.id != other.id

    class Event_ENABLE_AREA(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.areas[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            gameworld_runtime.areas[self.target].locked = False
            return ""

    class Event_DISABLE_AREA(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.areas[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            gameworld_runtime.areas[self.target].locked = True
            print("aaa")
            print("aaa")
            print("aaa")
            print("aaa")
            print("aaa")
            return ""

    class Event_TOGGLE_AREA(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.areas[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            gameworld_runtime.areas[self.target].locked = not gameworld_runtime.areas[self.target].locked
            return ""

    class Event_ENABLE_CONNECTION(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.entries[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            gameworld_runtime.entries[self.target].locked = False
            return ""

    class Event_DISABLE_CONNECTION(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.entries[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            gameworld_runtime.entries[self.target].locked = True
            return ""
        
    class Event_TOGGLE_CONNECTION(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.entries[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            gameworld_runtime.entries[self.target].locked = not gameworld_runtime.entries[self.target].locked
            return ""

    class Event_ACTIVATE_GAMESTATE(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.gamestates[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            if self.target in gameworld_runtime.inactive_gamestates:
                gameworld_runtime.inactive_gamestates.remove(self.target)
                gameworld_runtime.active_gamestates.append(self.target)
            return ""

    class Event_DEACTIVATE_GAMESTATE(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.gamestates[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            if self.target in gameworld_runtime.active_gamestates:
                gameworld_runtime.active_gamestates.remove(self.target)
                gameworld_runtime.inactive_gamestates.append(self.target)
            return ""

    class Event_TOGGLE_GAMESTATE(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.gamestates[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            if self.target in gameworld_runtime.inactive_gamestates:
                gameworld_runtime.inactive_gamestates.remove(self.target)
                gameworld_runtime.active_gamestates.append(self.target)
            else:
                gameworld_runtime.active_gamestates.remove(self.target)
                gameworld_runtime.inactive_gamestates.append(self.target)
            return ""

    class Event_FORCE_DIALOGUE(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.dialogues[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            if self.target in gameworld_runtime.available_dialogues or self.target in gameworld_runtime.active_dialogues:
                return f"dialogue_{self.target}"
            return ""

    class Event_REMOVE_DIALOGUE(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.dialogues[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            if self.target in gameworld_runtime.available_dialogues:
                gameworld_runtime.available_dialogues.discard(self.target)
            if self.target in gameworld_runtime.active_dialogues:
                gameworld_runtime.active_dialogues.discard(self.target)
            return ""

    class Event_FORCE_EVENT(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.events[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            if self.target in gameworld_runtime.events_available:
                return gameworld_runtime.events[self.target].Trigger(self)
            return ""

    class Event_REMOVE_EVENT(Event):
        def __init__(self, name, target, single_trigger, preconditions, consequences):
            super().__init__(name, target, single_trigger, preconditions, consequences)
        def Target(self):
            return gameworld_runtime.events[self.target].name
        def Trigger(self):
            gameworld_runtime.events_available.remove(self)
            gameworld_runtime.events_occurred.append(self)
            if self.target in gameworld_runtime.events_available:
                gameworld_runtime.events_available.remove(self.target)
            return ""

    class Event_Type(IntEnum):
        ENABLE_AREA = 0
        DISABLE_AREA = 1
        TOGGLE_AREA = 2
        ENABLE_CONNECTION = 3
        DISABLE_CONNECTION = 4
        TOGGLE_CONNECTION = 5
        ACTIVATE_GAMESTATE = 6
        DEACTIVATE_GAMESTATE = 7
        TOGGLE_GAMESTATE = 8
        FORCE_DIALOGUE = 9
        REMOVE_DIALOGUE = 10
        FORCE_EVENT = 11
        REMOVE_EVENT = 12