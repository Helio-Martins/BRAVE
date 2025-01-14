default seconds = 0
default minutes = 0
default hours = 0
default day = 1

label setup_clock:
    python:
        def add_time(s = 0, m = 0, h = 0):
            global seconds, minutes, hours, day
            seconds += s
            while seconds >= 60:
                seconds -= 60
                minutes += 1
            minutes += m
            while minutes >= 60:
                minutes -= 60
                hours += 1
            hours += h
            while hours >= 24:
                hours -= 24
                day += 1
            return

screen clock:
    text "[hours:0=2]:[minutes:0=2]:[seconds:0=2]":
        size 45
        xpos 1700
        color "#fff"
        outlines [(2, "#000", 0, 0)]