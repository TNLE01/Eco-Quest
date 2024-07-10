from images import *

waterLevelPictures = [waterLevel0, waterLevel1, waterLevel2, waterLevel3, waterLevel4]

class soilSpot():

    def __init__(self, posX, posY):
        
        self.posX = posX
        self.posY = posY
        self.currentTime = ''
        self.waterLevel = 0
        self.waterLevelPicture = waterLevelPictures[0]
        self.currentHumidity = ''
        self.currentNutrient = ''
        self.currentTemperature = ''
        self.currentPlant = 'Empty'

    def getCurrent(self, time, weather, humidity, nutrient, temperature):
        self.waterLevelCheck(weather)
        self.currentTime = time[0]
        self.currentHumidity = humidity[0]
        self.currentNutrient = nutrient[0]
        self.currentTemperature = temperature[0]

    def waterLevelCheck(self, weather):
        self.waterLevel += weather[3]
        if (0 <= self.waterLevel < 5):
            self.waterLevelPicture = waterLevelPictures[0]
        elif (5 <= self.waterLevel < 10):
            self.waterLevelPicture = waterLevelPictures[1]
        elif (10 <= self.waterLevel < 15):
            self.waterLevelPicture = waterLevelPictures[2]
        elif (15 <= self.waterLevel < 20):
            self.waterLevelPicture = waterLevelPictures[3]
        elif (20 <= self.waterLevel < 30):
            self.waterLevelPicture = waterLevelPictures[4]
        elif (30 <= self.waterLevel):
            self.waterLevel = 30
        #print(self.waterLevel)

    def placePlant(self, plant):
        self.currentPlant = plant

    def removePlant(self):
        self.currentPlant = 'Empty'

    def testGrowth(self):
        if self.currentPlant != 'Empty':
            self.currentPlant.testGrowth(self.waterLevel, 'ADD LATER', self.currentHumidity, self.currentNutrient, self.currentTemperature)
            self.waterLevel -= self.currentPlant.waterNeeded
            if self.waterLevel < 0:
                self.waterLevel = 0