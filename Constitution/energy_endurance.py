def calcLvlEnergy(weight,time,avgSpeed):
    KineticEnergy = (weight*pow(avgSpeed,2))/2
    totalEnergy = KineticEnergy*time
    levelEnergy = 50344
    level = 0
    while levelEnergy < totalEnergy:
        levelEnergy *= 1.25
        level += 1
    return level
    
print(calcLvlEnergy(60,4200,2.4))