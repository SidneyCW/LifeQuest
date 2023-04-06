def calcLvl(runDistanceKm):
    levelDistance = 0.8
    level = 0
    while levelDistance < runDistanceKm:
        levelDistance *= 1.25
        level += 1
    return level
