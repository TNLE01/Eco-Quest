from images import *

class plant():

    def __init__(self, name, image, growthStages, growthStagesCounter, waterNeeded, wildlifeNeeded, humidity, nutrient, temperature, dyingCount):

        self.name = name
        self.image = image
        self.growthStages = growthStages # Should Be List
        self.growthStagesCounter = growthStagesCounter # Should Be List
        self.waterNeeded = waterNeeded
        self.wildlifeNeeded = wildlifeNeeded
        self.humidity = humidity # Three List [[Best], [Good], [Bad], [Worst]]
        self.nutrient = nutrient # Three List [[Best], [Good], [Bad], [Worst]]
        self.temperature = temperature # # Three List [[Best], [Good], [Bad], [Worst]]

        self.currentStage = growthStages[0] # Current Stage
        self.currentStageCounter = 1
        self.stageCounter = 0 # Counter For Growth, When It Gets High Enough The Current Stage Will Change
        self.maxStages = len(growthStages)
        
        self.dyingCount = dyingCount
        self.dyingCounter = 0

        self.harvest = False

        self.mood = 50

    def testGrowth(self, currentWater, currentWildlife, currentHumidity, currentNutrient, currentTemperature):
        
        if self.harvest == False:
            
            if currentWater >= self.waterNeeded:
                self.stageCounter += 2
                self.mood += 2
            elif currentWater == 0:
                self.dyingCounter += 1
                self.mood += 1
            elif currentWater < self.waterNeeded:
                self.stageCounter += 1
                self.mood -= 1

            if currentHumidity in self.humidity[0]:
                self.stageCounter += 2
                self.mood += 2
            elif currentHumidity in self.humidity[1]:
                self.stageCounter += 1
                self.mood += 1
            elif currentHumidity in self.humidity[2]:
                self.stageCounter += 0
            elif currentHumidity in self.humidity[3]:
                self.dyingCounter += 1 
                self.mood -= 1

            if currentNutrient in self.nutrient[0]:
                self.stageCounter += 2
                self.mood += 2
            elif currentNutrient in self.nutrient[1]:
                self.stageCounter += 1
                self.mood += 1
            elif currentNutrient in self.nutrient[2]:
                self.stageCounter += 0
            elif currentNutrient in self.nutrient[3]:
                self.dyingCounter += 1
                self.mood -= 1

            if currentTemperature in self.temperature[0]:
                self.stageCounter += 2
                self.mood += 2
            elif currentTemperature in self.temperature[1]:
                self.stageCounter += 1
                self.mood += 1
            elif currentTemperature in self.temperature[2]:
                self.stageCounter += 0
            elif currentTemperature in self.temperature[3]:
                self.dyingCounter += 1
                self.mood -= 1

            if self.mood > 100:
                self.mood = 100
            elif self.mood < 0:
                self.mood = 0

            if self.dyingCounter == self.dyingCount:
                print('plant die')
                self.mood = 0

            if self.stageCounter > self.growthStagesCounter[self.currentStageCounter]:
                self.currentStage = self.growthStages[self.currentStageCounter]
                self.currentStageCounter += 1
                if self.currentStageCounter == self.maxStages:
                    self.harvest = True


#
# humidity - 'Very Dry', 'Very Dry', 'Dry', 'Optimal', 'Humid', 'Very Humid', 'Very Humid'
# nutrient - 'Extremely Low Nutrient', 'Very Low Nutrient', 'Low Nutrient', 'Okay Nutrient', 'High Nutrient', 'Very High Nutrient', 'Extremely High Nutrient'
# temperature - 'Extreme Cold', 'Very Cold', 'Cold', 'Okay', 'Hot', 'Very Hot', 'Extreme Heat'

plantBasicType = plant('Basic Testing Plant', plant4, [plantSeed, plant1, plant2, plant3, plant4, plant5], [0, 100, 200, 300, 400, 500], # [0, 500, 1000, 1500, 2400][0, 50, 100, 150, 200]
                       2, 1,
                       [['Optimal'], ['Humid'], ['Dry'], ['Very Dry', 'Very Humid']],
                       [['High Nutrient', 'Very High Nutrient'], ['Low Nutrient', 'Okay Nutrient'], ['Very Low Nutrient'], ['Extremely Low Nutrient', 'Extremely High Nutrient']], 
                       [['Okay'], ['Hot', 'Very Hot'], ['Very Cold', 'Cold', 'Extreme Heat'], ['Extreme Cold']], 
                       100)