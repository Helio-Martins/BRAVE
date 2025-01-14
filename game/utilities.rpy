init -10 python:
    import pylsl
    import copy
    from copy import deepcopy
    from enum import IntEnum
    from collections import deque 

init -9 python:
    def bfs(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        return distances
    def average_distance(graph, nodes):
        all_distances = {node: bfs(graph, node) for node in graph}
        min_avg_distance = float('inf')
        best_node = None
        for node in graph:
            total_distance = sum(all_distances[node][target] for target in nodes)
            if len(nodes) != 0:
                avg_distance = total_distance / len(nodes)
            else:
                avg_distance = 0
            if avg_distance < min_avg_distance:
                min_avg_distance = avg_distance
                best_node = node
        return best_node

    class Time:
        def __init__(self, hour=0, minute=0, second=0):
            self._initialized = True
            self.hour = hour
            self.minute = minute
            self.second = second
        def __str__(self):
            return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        def __repr__(self):
            return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        def __eq__(self, other):
            if not isinstance(other, Time):
                return NotImplemented
            return (self.hour, self.minute, self.second) == (other.hour, other.minute, other.second)
        def __lt__(self, other):
            if not isinstance(other, Time):
                return NotImplemented
            return (self.hour, self.minute, self.second) < (other.hour, other.minute, other.second)
        def __le__(self, other):
            if not isinstance(other, Time):
                return NotImplemented
            return (self.hour, self.minute, self.second) <= (other.hour, other.minute, other.second)
        def __gt__(self, other):
            if not isinstance(other, Time):
                return NotImplemented
            return (self.hour, self.minute, self.second) > (other.hour, other.minute, other.second)
        def __ge__(self, other):
            if not isinstance(other, Time):
                return NotImplemented
            return (self.hour, self.minute, self.second) >= (other.hour, other.minute, other.second)
        def __ne__(self, other):
            if not isinstance(other, Time):
                return NotImplemented
            return (self.hour, self.minute, self.second) != (other.hour, other.minute, other.second)
    
    def AddTime(time, time2):
        total_seconds = time2.hour * 3600 + time2.minute * 60 + time2.second
        return AddSeconds(time, total_seconds)
    def AddSeconds(time, seconds):
        total_seconds = (time.hour) * 3600 + (time.minute) * 60 + (time.second) + int(seconds)
        time.hour = total_seconds // 3600
        total_seconds %= 3600
        time.minute = total_seconds // 60
        time.second = total_seconds % 60
    def AddHour(time, hour):
        time.hour += hour
        if time.hour > 23:
            time.hour -= 24
        if time.hour < 0:
            time.hour += 24
    def AddMinute(time, minute):
        time.minute += minute
        if time.minute > 59:
            time.minute -= 60
        if time.minute < 0:
            time.minute += 60
    def AddSecond(time, second):
        time.second += second
        if time.second > 59:
            time.second -= 60
        if time.second < 0:
            time.second += 60

    def CopySet(a, b):
        a.clear()
        for x in b:
            a.append(x)
        return
    def AddSet(a, b):
        a.append(b)
        return
    def SortedCopySet(a, b):
        CopySet(a, b)
        a.sort()
    def CopyDict(a, b):
        a.clear()
        for x in b:
            a[x] = deepcopy(b[x])
        return
    def SortedCopyDict(a, b):
        CopyDict(a, dict(sorted(b.items())))
        return
    def AddToDict(a, b, c):
        a[b] = c
        return
    def RemoveFromDict(a, b):
        a.pop(b)
        return
    def MoveList(l, oi, ni):
        l.insert(ni, l.pop(oi))
        return

transform rot(r):
    rotate r

transform vflip:
    yzoom -1.0

transform zoomed(z):
    zoom z

transform sim_portrait():
    xalign 0.0
    yalign 1.0
    xsize 250
    ysize 250

transform zoom_hover:
    on hover:
        zoom 1.5
    on idle:
        zoom 1.0

image connection_red:
    "images/connections/red.png"
    xsize 100 ysize 100
image connection_green:
    "images/connections/green.png"
    xsize 100 ysize 100
image connection_blue:
    "images/connections/blue.png"
    xsize 100 ysize 100
image connection_cyan:
    "images/connections/cyan.png"
    xsize 100 ysize 100
image connection_magenta:
    "images/connections/magenta.png"
    xsize 100 ysize 100
image connection_yellow:
    "images/connections/yellow.png"
    xsize 100 ysize 100
image connection_default:
    "images/connections/default.png"
    xsize 100 ysize 100

label pass_time_dialogue:
    $ AddSeconds(gameworld_runtime.time, 10)
    return