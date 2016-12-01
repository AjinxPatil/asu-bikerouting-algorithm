#!/usr/bin/python
#
# Customized A* search algorithm for bike routing in ASU Campus
# Author: Ajinkya Patil
#

def pathfinding(map, start, goal):
    reach = PriorityQueue()
    reach.put(start, 0)
    antecedents = {}
    path_costs = {}
    antecedents[start] = None
    path_costs[start] = start_time
    while not reach.empty():
        current = reach.get()
        if current == goal:
            break
        for next in map.neighbors(current, path_costs[current]):
            new_cost = path_costs[current] + map.cost(next, path_costs[current])
            if next not in path_costs or new_cost < path_costs[next]:
                path_costs[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                reach.put(next, priority)
                antecedents[next] = current
    return antecedents

def cost(next, time_at_current):
    time_from_current = 0.125 if next in map.roads else 0.167
    path_time = time_from_current + time_at_current
    people = 0
    cdf = 1
    for neighbor in map.obstacles_nearby(next, path_time):   
        if neighbor in schedule:
        for event_strength in map.schedule[neighbor][path_time]:
            people = people + event_strength
            if people >= HIGH:
                cdf = 1.5
            elif people > MEDIUM:
                cdf = 1.333
            else:
                cdf = 1.167
    return path_time * cdf

def heuristic(next, goal):
    (x1, y1) = next
    (x2, y2) = goal
    return (abs(x1 - x2) + abs(y1 - y2)) / 800

def obstacles_nearby(current, path_time):
    (x, y) = current
    nearby = [(x, y + 1), (x - 1, y + 1), (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    return set([p for p in nearby if p in map.obstacles])

def neighbors(current, path_time):
    (x, y) = current
    nearby = [(x, y + 1), (x - 1, y), (x, y - 1), (x + 1, y)]
    if path_time > WOZT_START and path_time < WOZT_END:
        return set([p for p in nearby if p not in map.obstacles and p not in map.walkonlys])
    return set([p for p in nearby if p not in map.obstacles])

