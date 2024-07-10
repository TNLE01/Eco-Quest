# Author: Truong Le


# Import Needed Modules ----------------------------------------------------------------------------------------------------


# Imports All Needed Modules 
import pygame, random, time, datetime, os, math, copy
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image
import customtkinter as ctk

from images import *
from shopItemClass import *
from soilSpot import *

plantList = [pygame.transform.scale(pygame.image.load(plant0), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant1), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant2), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant3), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant4), (200, 200))]
counter = 0
# Main Game Class ----------------------------------------------------------------------------------------------------


# Main Game Class
class EcoQuest():


    # Settings Up ----------------------------------------------------------------------------------------------------


    # Set Up Window As Well As All Game Elements Needed
    def __init__(self):

        # Set Up Window Icon Picture
        self.root = Tk()
        self.root.title("Eco Quest")
        self.root.iconphoto(False, tk.PhotoImage(file = ecoQuestIcon))

        # Set Up Window
        self.root.geometry("1250x750")
        self.root.minsize(width = 1250, height = 750)
        self.root.maxsize(width = 1250, height = 750)

        # Dictionary With All The Game Data
        self.gameVariables = {}

        # Ingame Timer
        self.gameTimer = 0

        # Ingame Year Day Counter
        self.yearDayCounter = 0

        # Time Progress Bar Information
        self.timesSet = [[timeDay1, '#0080ff'], [timeDay2, '#00ffff'], [timeDay3, '#80ffff'], [timeDay4, '#00ffff'], [timeDay5, '#0080ff'], [timeNight1, '#0000ff'], [timeNight2, '#000080'], [timeNight3, '#000000'], [timeNight4, '#000080'], [timeNight5, '#0000ff']]
        self.currentTime = []

        # Seasons Progress Bar Information
        self.gameVariables['seasonsSet'] = [['Spring', springSeason, ['#6cffcf', '#a5e58d', '#009418'], [40, 80], [20, 60], seasonSpringBackground],
                                            ['Summer', summerSeason, ['#ffb3e3', '#ff54f4', '#9a00a8'], [60, 100], [40, 80], seasonSummerBackground],
                                            ['Fall', fallSeason, ['#d38600', '#e0e13c', '#bb1000'], [20, 60], [0, 40], seasonFallBackground],
                                            ['Winter', winterSeason, ['#379ed8', '#a5fdff', '#ffffff'], [0, 40], [0, 20], seasonWinterBackground]]
        self.gameVariables['currentSeason'] = []

        # Weather Slider Information
        self.gameVariables['rainsSet'] = [['Clear Skies', rainClear, '#e5ff00', 0], ['Light Rain', rainLight, '#c8c8c8', 1], ['Moderate Rain', rainModerate, '#969696', 2], ['Heavy Rain', rainHeavy, '#646464', 3], ['Violet Rain', rainViolent, '#323232', 4]]
        self.gameVariables['snowsSet'] = [['Clear Skies', snowClear, '#e5ff00', 0], ['Light Snow', snowLight, '#c8c8c8', 0], ['Moderate Snow', snowModerate, '#969696', 0], ['Heavy Snow', snowHeavy, '#646464', 0], ['Violet Snow', snowViolent, '#323232', 0]]
        self.gameVariables['currentWeatherSet'] = []
        self.gameVariables['currentWeather'] = []

        # Wildlife Slider Information
        self.gameVariables['wildlifeSet'] = [['No Wildlife', wildlifeNone, '#03652a'], ['Few Wildlife', wildlifeFew, '#7d6400'], ['Several Wildlife', wildlifeSeveral, '#964b00'], ['Many Wildlife', wildlifeMany, '#7d3200'], ['A lot of Wildlife', wildlifeALot, '#641900']]
        self.gameVariables['currentWildlife'] = []

        # Rating Progress Bar Information
        self.gameVariables['ratingsSet'] = [['Very Bad', ratingVeryBad, '#ff3600'], ['Very Bad', ratingVeryBad, '#ff3600'], ['Bad', ratingBad, '#ff7c00'], ['Okay', ratingOkay, '#ffc900'], ['Good', ratingGood, '#fffb00'], ['Very Good', ratingVeryGood, '#9fff00'], ['Very Good', ratingVeryGood, '#9fff00']]
        self.gameVariables['currentRating'] = []

        # Humidity Progress Bar Information
        self.gameVariables['humiditiesSet'] = [['Very Dry', humidityVeryDry, '#f288ff'], ['Very Dry', humidityVeryDry, '#f288ff'], ['Dry', humidityDry, '#cc86ec'], ['Optimal', humidityOptimal, '#9da6e5'], ['Humid', humidityHumid, '#a9dcf4'], ['Very Humid', humidityVeryHumid, '#b9fdff'], ['Very Humid', humidityVeryHumid, '#b9fdff']]
        self.gameVariables['currentHumidity'] = []

        # Nutrient Progress Bar Information
        self.gameVariables['nutrientsSet'] = [['Extremely Low Nutrient', nutrientExtremelyLow, '#3c1e00', soilLevel0], ['Very Low Nutrient', nutrientVeryLow, '#462800', soilLevel1], ['Low Nutrient', nutrientLow, '#503200', soilLevel2], ['Okay Nutrient', nutrientOkay, '#5a3c00', soilLevel3], ['High Nutrient', nutrientHigh, '#644600', soilLevel4], ['Very High Nutrient', nutrientVeryHigh, '#6e5000', soilLevel5], ['Extremely High Nutrient', nutrientExtremelyHigh, '#785a00', soilLevel6]]
        self.gameVariables['currentNutrient'] = []

        # Temperature Progress Bar Information
        self.gameVariables['temperaturesSet'] = [['Extreme Cold', temperatureExtremeCold, '#000032'], ['Very Cold', temperatureVeryCold, '#0000ff'], ['Cold', temperatureCold, '#00c8ff'], ['Okay', temperatureOkay, '#00c800'], ['Hot', temperatureHot, '#ffc800'], ['Very Hot', temperatureVeryHot, '#ff0000'], ['Extreme Heat', temperatureExtremeHeat, '#320000']]
        self.gameVariables['currentTemperature'] = []

        # Used To Execute Multiple Commands Upon Other Actions
        self.extraCommandsList = []

        # See If The Game Is Running
        self.inGame = False
        self.firstGame = True

        # TESTING
        self.openImages()

        # Game Speed
        self.gameSpeed = 500

        # Player Inventory
        self.inventory = []

        # Plant Placement Spots
        self.plantPlacementSpots = []

        # Day Night Alpha
        self.setAlpha = 16

        # Game Font
        #self.gameFont = ctk.CTkFont(family = 'Plau', size = 20, weight = 'bold')

        # Moving Frame Speed
        self.frameSpeed = 1 # 0.5 before

        # Run The Main Menu
        self.mainMenu()
       # self.gameScreen()


    # Main Loop And Main Menu ----------------------------------------------------------------------------------------------------


    # TESTING
    def openImages(self):
        self.backgroundImage = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))
        #self.seasonListCTkImage = [ctk.CTkImage(Image.open(springSeason), size=(50 , 50)),
        #                           ctk.CTkImage(Image.open(summerSeason), size=(50 , 50)),
        #                           ctk.CTkImage(Image.open(fallSeason), size=(50 , 50)),
        #                           ctk.CTkImage(Image.open(winterSeason), size=(50 , 50))]

    # Game Font
    def gameFont(self, *args, **kwargs):
        return ctk.CTkFont(family = 'Plau', size = kwargs.get('size', 20), weight = 'bold')

    # Main Tkinter Loop
    def mainloop(self):
        self.root.mainloop()

    # Main Menu Screen
    def mainMenu(self):
        self.mainMenuFrame = ctk.CTkFrame(self.root, width = 1250, height = 750, fg_color = 'yellow green', bg_color = 'green yellow')
        self.mainMenuFrame.grid(row = 0, column = 0)
        # image = ctk.CTkImage(Image.open(self.gameVariables[current][1]), size=(44 , 44))
        self.mainMenuBackgroundImageLabel = ctk.CTkLabel(self.mainMenuFrame, text = '', width = 1250, height = 750, fg_color = 'orange', bg_color = 'orange', image = ctk.CTkImage(Image.open(mainMenuImage), size = (1250 , 750)))
        self.mainMenuBackgroundImageLabel.place(x = 0, y = 0)

        self.titleLabel = ctk.CTkLabel(self.mainMenuFrame, text = '', width = 1000, height = 176, fg_color = 'dark green', bg_color = 'transparent', image = ctk.CTkImage(Image.open(titleCard), size = (1000 , 176)))
        self.titleLabel.place(x = 125, y = 100)

        self.playButton = self.buttonStyle(self.mainMenuFrame, 'Play', 200, 50, 'accept', command = lambda : self.playButtonFrame(DISABLED)); self.playButton.place(x = 525, y = 410)
        self.howToPlayButton = self.buttonStyle(self.mainMenuFrame, 'How To Play', 200, 50, 'accept', command = lambda : self.howToPlayButtonFrame(DISABLED)); self.howToPlayButton.place(x = 525, y = 495)
        self.settingsButton = self.buttonStyle(self.mainMenuFrame, 'Settings', 200, 50, 'accept', command = lambda : self.settingsButtonFrame(DISABLED)); self.settingsButton.place(x = 525, y = 580)
        self.exitButton = self.buttonStyle(self.mainMenuFrame, 'Exit', 200, 50, 'accept', command = lambda : self.exitButtonFrame(DISABLED)); self.exitButton.place(x = 525, y = 665)

    # Disable or Enable Buttons
    def buttonStateSettings(self, buttonState, *args):
        for ar in args:
            ar.configure(state = buttonState)

    # Make Button Style So It Doesn't Need To Be Repeated
    def buttonStyle(self, root, text, width, height, type, *args, **kwargs):
        if type == 'accept':
            return ctk.CTkButton(root, text = text, width = width, height = height, corner_radius = 0,
                                 fg_color = '#00c000', bg_color = 'transparent', hover_color = '#007e00', border_color = '#5a3c00',
                                 text_color = '#5a3c00', border_width = 10, text_color_disabled = '#007e00',
                                 command = kwargs.get('command', None), font = self.gameFont(), state = kwargs.get('state', NORMAL),
                                 image = kwargs.get('image', None))
        else:
            return ctk.CTkButton(root, text = text, width = width, height = height, corner_radius = 0,
                                 fg_color = '#c00000', bg_color = 'transparent', hover_color = '#7e0000', border_color = '#3c5a00',
                                 text_color = '#3c5a00', border_width = 10, text_color_disabled = '#7e0000',
                                 command = kwargs.get('command', None), font = self.gameFont(), state = kwargs.get('state', NORMAL),
                                 image = kwargs.get('image', None))


    # Play Frame When Play Button Is Pressed
    def playButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.startingSpring, self.startingSummer, self.startingFall, self.startingWinter, self.cancelButtonPlayFrame)
            self.movingFrame(2, self.playChoiceFrame, 362.5, 250, 362.5, 0 - self.playChoiceFrame.winfo_reqheight(), 0, self.frameSpeed, 1, lambda: self.playChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.playChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 525, height = 250, fg_color = 'transparent', bg_color = 'transparent', corner_radius = 0)
        #self.backgroundImagePlayFrame = ctk.CTkImage(Image.open(buttonBackground), size = (325 , 100))
        
        self.playLabelInfo = ctk.CTkLabel(self.playChoiceFrame, text = 'Select Starting Season', width = 525, height = 25, text_color = '#5a3c00', font = self.gameFont(size = 15))
        self.playLabelInfo.place(x = 0, y = 0)

        self.startingSpring = self.buttonStyle(self.playChoiceFrame, '', 100, 100, 'accept', command = lambda: self.gameScreen(self.gameVariables['seasonsSet'][0]), state = DISABLED, image = ctk.CTkImage(Image.open(springSeasonMini), size = (64, 64)))
        self.startingSpring.place(x = 25, y = 50)
        self.startingSpring.bind('<Enter>', lambda x: self.playLabelInfo.configure(text = 'Good Balance Temperature And Humidity'))
        self.startingSpring.bind('<Leave>', lambda x: self.playLabelInfo.configure(text = 'Select Starting Season'))

        self.startingSummer = self.buttonStyle(self.playChoiceFrame, '', 100, 100, 'accept', command = lambda: self.gameScreen(self.gameVariables['seasonsSet'][1]), state = DISABLED, image = ctk.CTkImage(Image.open(summerSeasonMini), size = (64, 64)))
        self.startingSummer.place(x = 150, y = 50)
        self.startingSummer.bind('<Enter>', lambda x: self.playLabelInfo.configure(text = 'Very High Temperatures And Wet Humidity'))
        self.startingSummer.bind('<Leave>', lambda x: self.playLabelInfo.configure(text = 'Select Starting Season'))

        self.startingFall = self.buttonStyle(self.playChoiceFrame, '', 100, 100, 'accept', command = lambda: self.gameScreen(self.gameVariables['seasonsSet'][2]), state = DISABLED, image = ctk.CTkImage(Image.open(fallSeasonMini), size = (64, 64)))
        self.startingFall.place(x = 275, y = 50)
        self.startingFall.bind('<Enter>', lambda x: self.playLabelInfo.configure(text = 'Chilly Temperatures And Average Humidity'))
        self.startingFall.bind('<Leave>', lambda x: self.playLabelInfo.configure(text = 'Select Starting Season'))

        self.startingWinter = self.buttonStyle(self.playChoiceFrame, '', 100, 100, 'accept', command = lambda: self.gameScreen(self.gameVariables['seasonsSet'][3]), state = DISABLED, image = ctk.CTkImage(Image.open(winterSeasonMini), size = (64, 64)))
        self.startingWinter.place(x = 400, y = 50)
        self.startingWinter.bind('<Enter>', lambda x: self.playLabelInfo.configure(text = 'Freezing Temperatures With Little To No Humidity, Added Snow'))
        self.startingWinter.bind('<Leave>', lambda x: self.playLabelInfo.configure(text = 'Select Starting Season'))

        self.cancelButtonPlayFrame = self.buttonStyle(self.playChoiceFrame, 'Cancel', 225, 50, 'refuse', command = lambda: self.playButtonFrame(NORMAL), state = DISABLED)
        self.cancelButtonPlayFrame.place(x = 150, y = 175)
        self.cancelButtonPlayFrame.bind('<Enter>', lambda x: self.playLabelInfo.configure(text = 'Cancel Season Selection'))
        self.cancelButtonPlayFrame.bind('<Leave>', lambda x: self.playLabelInfo.configure(text = 'Select Starting Season'))

        self.movingFrame(0, self.playChoiceFrame, 362.5, 0, 362.5, 250, 0, self.frameSpeed, 1, lambda: self.buttonStateSettings(NORMAL, self.startingSpring, self.startingSummer, self.startingFall, self.startingWinter, self.cancelButtonPlayFrame))#, self.yesButtonPlayFrame, self.cancelButtonPlayFrame))
    
    # How To Play Frame When How To Play Button Is Pressed
    def howToPlayButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.closeButtonHowToPlayFrame)
            self.movingFrame(3, self.howToPlayChoiceFrame, 350 + self.howToPlayChoiceFrame.winfo_reqwidth(), 50, 1250, 50, 0, self.frameSpeed, 1, lambda: self.howToPlayChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.howToPlayChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 550, height = 650,  fg_color = 'transparent', bg_color = 'transparent', corner_radius = 0)
        #self.backgroundImageHowToPlayFrame = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))

        self.howToPlayLabelInfo = ctk.CTkLabel(self.howToPlayChoiceFrame, text = 'How To Play?', width = 550, height = 25, text_color = '#5a3c00', font = self.gameFont(size = 15))
        self.howToPlayLabelInfo.place(x = 0, y = 0)

        self.howToPlayTab = ctk.CTkTabview(self.howToPlayChoiceFrame, width = 500, height = 500, corner_radius = 0, border_width = 0, text_color = '#5a3c00', 
                                           bg_color = '#007e00', segmented_button_selected_color = '#007e00', segmented_button_selected_hover_color = '#00c000', 
                                           segmented_button_unselected_color = '#00c000', segmented_button_unselected_hover_color = '#007e00', fg_color = '#007e00')
        self.howToPlayTab.place(x = 25, y = 50)
        self.howToPlayTabInfo = self.howToPlayTab.add('Info')
        self.howToPlayTabTime = self.howToPlayTab.add('Time')
        self.howToPlayTabSeasons = self.howToPlayTab.add('Seasons')
        self.howToPlayTabWeather = self.howToPlayTab.add('Weather')
        self.howToPlayTabWildlife = self.howToPlayTab.add('Wildlife')
        self.howToPlayTabRating = self.howToPlayTab.add('Rating')
        self.howToPlayTabHumidity = self.howToPlayTab.add('Humidity')
        self.howToPlayTabNutrient = self.howToPlayTab.add('Nutrient')
        self.howToPlayTabTemperature = self.howToPlayTab.add('Temperature')
        '''
        self.infoTextBox = ctk.CTkTextbox(self.howToPlayTabInfo, width = 100, height = 100, corner_radius = 0, font = self.gameFont(size = 15), activate_scrollbars = False)#, fg_color = 'green')
        self.infoTextBox.insert('0.0', 'new text to insertfdfdfd f')
        self.infoTextBox.place(x = 0, y = 0)
        '''
        # frame is 500 by 464
        # howToPlayTabInfo
        self.samplePic1 = ctk.CTkLabel(self.howToPlayTabInfo, width = 250, height = 250, text = '', image = ctk.CTkImage(Image.open(demo4), size = (200, 200)))
        self.samplePic1.place(x = 0, y = 0)
        self.samplePic2 = ctk.CTkLabel(self.howToPlayTabInfo, width = 250, height = 250, text = '', image = ctk.CTkImage(Image.open(demo3), size = (200, 200)))
        self.samplePic2.place(x = 250, y = 0)
        self.infoHowToPlay = ctk.CTkLabel(self.howToPlayTabInfo, width = 250, height = 250, justify = 'left', text = 'The game is played by planting seeds \nand helping them grow.'
                                          + ' Growing \nthe plants fully will net you points. \nScore a high score with as few \nplants dying.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoHowToPlay.place(x = 0, y = 250)

        # howToPlayTabTime
        self.sampleDay1 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeDay1), size = (90, 90))); self.sampleDay1.place(x = 0, y = 0)
        self.sampleDay2 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeDay2), size = (90, 90))); self.sampleDay2.place(x = 100, y = 0)
        self.sampleDay3 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeDay3), size = (90, 90))); self.sampleDay3.place(x = 200, y = 0)
        self.sampleDay4 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeDay4), size = (90, 90))); self.sampleDay4.place(x = 300, y = 0)
        self.sampleDay5 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeDay5), size = (90, 90))); self.sampleDay5.place(x = 400, y = 0)
        self.sampleDay6 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeNight1), size = (90, 90))); self.sampleDay6.place(x = 0, y = 100)
        self.sampleDay7 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeNight2), size = (90, 90))); self.sampleDay7.place(x = 100, y = 100)
        self.sampleDay8 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeNight3), size = (90, 90))); self.sampleDay8.place(x = 200, y = 100)
        self.sampleDay9 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeNight4), size = (90, 90))); self.sampleDay9.place(x = 300, y = 100)
        self.sampleDay10 = ctk.CTkLabel(self.howToPlayTabTime, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(timeNight5), size = (90, 90))); self.sampleDay10.place(x = 400, y = 100)

        self.infoTime = ctk.CTkLabel(self.howToPlayTabTime, width = 250, height = 250, justify = 'left', text = 'These are the time cycles that the \nday will go through. Plants will grow \nbetter during certain parts of the day.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)

        # howToPlayTabSeasons
        self.sampleSeason1 = ctk.CTkLabel(self.howToPlayTabSeasons, width = 125, height = 125, text = '', image = ctk.CTkImage(Image.open(springSeason), size = (100, 100))); self.sampleSeason1.place(x = 0, y = 0)
        self.sampleSeason2 = ctk.CTkLabel(self.howToPlayTabSeasons, width = 125, height = 125, text = '', image = ctk.CTkImage(Image.open(summerSeason), size = (100, 100))); self.sampleSeason2.place(x = 125, y = 0)
        self.sampleSeason3 = ctk.CTkLabel(self.howToPlayTabSeasons, width = 125, height = 125, text = '', image = ctk.CTkImage(Image.open(fallSeason), size = (100, 100))); self.sampleSeason3.place(x = 250, y = 0)
        self.sampleSeason4 = ctk.CTkLabel(self.howToPlayTabSeasons, width = 125, height = 125, text = '', image = ctk.CTkImage(Image.open(winterSeason), size = (100, 100))); self.sampleSeason4.place(x = 375, y = 0)

        self.infoTime = ctk.CTkLabel(self.howToPlayTabSeasons, width = 250, height = 250, justify = 'left', text = 'These are the season cycles that the \nyear will go through. The seasons will \naffect the humidity, temperature, \nand weather.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)

        # howToPlayTabWeather
        self.sampleWeather1 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(rainClear), size = (90, 90))); self.sampleWeather1.place(x = 0, y = 0)
        self.sampleWeather2 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(rainLight), size = (90, 90))); self.sampleWeather2.place(x = 100, y = 0)
        self.sampleWeather3 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(rainModerate), size = (90, 90))); self.sampleWeather3.place(x = 200, y = 0)
        self.sampleWeather4 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(rainHeavy), size = (90, 90))); self.sampleWeather4.place(x = 300, y = 0)
        self.sampleWeather5 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(rainViolent), size = (90, 90))); self.sampleWeather5.place(x = 400, y = 0)
        self.sampleWeather6 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(snowClear), size = (90, 90))); self.sampleWeather6.place(x = 0, y = 100)
        self.sampleWeather7 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(snowLight), size = (90, 90))); self.sampleWeather7.place(x = 100, y = 100)
        self.sampleWeather8 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(snowModerate), size = (90, 90))); self.sampleWeather8.place(x = 200, y = 100)
        self.sampleWeather9 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(snowHeavy), size = (90, 90))); self.sampleWeather9.place(x = 300, y = 100)
        self.sampleWeather10 = ctk.CTkLabel(self.howToPlayTabWeather, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(snowViolent), size = (90, 90))); self.sampleWeather10.place(x = 400, y = 100)

        self.infoTime = ctk.CTkLabel(self.howToPlayTabWeather, width = 250, height = 250, justify = 'left', text = 'These are the weather options during \ngameplay. It can help water plants \nand wet the soil.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)


        # howToPlayTabWildlife
        self.sampleWeather1 = ctk.CTkLabel(self.howToPlayTabWildlife, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(wildlifeNone), size = (90, 90))); self.sampleWeather1.place(x = 0, y = 0)
        self.sampleWeather2 = ctk.CTkLabel(self.howToPlayTabWildlife, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(wildlifeFew), size = (90, 90))); self.sampleWeather2.place(x = 100, y = 0)
        self.sampleWeather3 = ctk.CTkLabel(self.howToPlayTabWildlife, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(wildlifeSeveral), size = (90, 90))); self.sampleWeather3.place(x = 200, y = 0)
        self.sampleWeather4 = ctk.CTkLabel(self.howToPlayTabWildlife, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(wildlifeMany), size = (90, 90))); self.sampleWeather4.place(x = 300, y = 0)
        self.sampleWeather5 = ctk.CTkLabel(self.howToPlayTabWildlife, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(wildlifeALot), size = (90, 90))); self.sampleWeather5.place(x = 400, y = 0)
        
        self.infoTime = ctk.CTkLabel(self.howToPlayTabWildlife, width = 250, height = 250, justify = 'left', text = 'These are the wildlife options during \ngameplay. It can help with plant \ngrowth.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)

        # howToPlayTabRating
        self.sampleRating1 = ctk.CTkLabel(self.howToPlayTabRating, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(ratingVeryBad), size = (90, 90))); self.sampleRating1.place(x = 0, y = 0)
        self.sampleRating2 = ctk.CTkLabel(self.howToPlayTabRating, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(ratingBad), size = (90, 90))); self.sampleRating2.place(x = 100, y = 0)
        self.sampleRating3 = ctk.CTkLabel(self.howToPlayTabRating, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(ratingOkay), size = (90, 90))); self.sampleRating3.place(x = 200, y = 0)
        self.sampleRating4 = ctk.CTkLabel(self.howToPlayTabRating, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(ratingGood), size = (90, 90))); self.sampleRating4.place(x = 300, y = 0)
        self.sampleRating5 = ctk.CTkLabel(self.howToPlayTabRating, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(ratingVeryGood), size = (90, 90))); self.sampleRating5.place(x = 400, y = 0)
        
        self.infoTime = ctk.CTkLabel(self.howToPlayTabRating, width = 250, height = 250, justify = 'left', text = 'The ratings tell you how your plants \nare doing.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)

        # howToPlayTabHumidity
        self.sampleHumidity1 = ctk.CTkLabel(self.howToPlayTabHumidity, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(humidityVeryDry), size = (90, 90))); self.sampleHumidity1.place(x = 0, y = 0)
        self.sampleHumidity2 = ctk.CTkLabel(self.howToPlayTabHumidity, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(humidityDry), size = (90, 90))); self.sampleHumidity2.place(x = 100, y = 0)
        self.sampleHumidity3 = ctk.CTkLabel(self.howToPlayTabHumidity, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(humidityOptimal), size = (90, 90))); self.sampleHumidity3.place(x = 200, y = 0)
        self.sampleHumidity4 = ctk.CTkLabel(self.howToPlayTabHumidity, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(humidityHumid), size = (90, 90))); self.sampleHumidity4.place(x = 300, y = 0)
        self.sampleHumidity5 = ctk.CTkLabel(self.howToPlayTabHumidity, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(humidityVeryHumid), size = (90, 90))); self.sampleHumidity5.place(x = 400, y = 0)
        
        self.infoTime = ctk.CTkLabel(self.howToPlayTabHumidity, width = 250, height = 250, justify = 'left', text = 'These are the humidity ratings, \ntelling you how wet the area currently \nis. Plants have preferred humidity.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)

        # howToPlayTabNutrient
        self.sampleNutrient1 = ctk.CTkLabel(self.howToPlayTabNutrient, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(nutrientExtremelyLow), size = (90, 90))); self.sampleNutrient1.place(x = 0, y = 0)
        self.sampleNutrient2 = ctk.CTkLabel(self.howToPlayTabNutrient, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(nutrientVeryLow), size = (90, 90))); self.sampleNutrient2.place(x = 100, y = 0)
        self.sampleNutrient3 = ctk.CTkLabel(self.howToPlayTabNutrient, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(nutrientLow), size = (90, 90))); self.sampleNutrient3.place(x = 200, y = 0)
        self.sampleNutrient4 = ctk.CTkLabel(self.howToPlayTabNutrient, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(nutrientOkay), size = (90, 90))); self.sampleNutrient4.place(x = 300, y = 0)
        self.sampleNutrient5 = ctk.CTkLabel(self.howToPlayTabNutrient, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(nutrientHigh), size = (90, 90))); self.sampleNutrient5.place(x = 400, y = 0)
        self.sampleNutrient6 = ctk.CTkLabel(self.howToPlayTabNutrient, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(nutrientVeryHigh), size = (90, 90))); self.sampleNutrient6.place(x = 150, y = 100)
        self.sampleNutrient7 = ctk.CTkLabel(self.howToPlayTabNutrient, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(nutrientExtremelyHigh), size = (90, 90))); self.sampleNutrient7.place(x = 250, y = 100)
        

        self.infoTime = ctk.CTkLabel(self.howToPlayTabNutrient, width = 250, height = 250, justify = 'left', text = 'These are the nutrient ratings, which \nwill help the plants grow. Note that \ntoo high a nutrient can have the \nopposite effect.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)

        # howToPlayTabTemperature
        self.sampleTemperature1 = ctk.CTkLabel(self.howToPlayTabTemperature, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(temperatureExtremeCold), size = (90, 90))); self.sampleTemperature1.place(x = 0, y = 0)
        self.sampleTemperature2 = ctk.CTkLabel(self.howToPlayTabTemperature, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(temperatureVeryCold), size = (90, 90))); self.sampleTemperature2.place(x = 100, y = 0)
        self.sampleTemperature3 = ctk.CTkLabel(self.howToPlayTabTemperature, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(temperatureCold), size = (90, 90))); self.sampleTemperature3.place(x = 200, y = 0)
        self.sampleTemperature4 = ctk.CTkLabel(self.howToPlayTabTemperature, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(temperatureOkay), size = (90, 90))); self.sampleTemperature4.place(x = 300, y = 0)
        self.sampleTemperature5 = ctk.CTkLabel(self.howToPlayTabTemperature, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(temperatureHot), size = (90, 90))); self.sampleTemperature5.place(x = 400, y = 0)
        self.sampleTemperature6 = ctk.CTkLabel(self.howToPlayTabTemperature, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(temperatureVeryHot), size = (90, 90))); self.sampleTemperature6.place(x = 150, y = 100)
        self.sampleTemperature7 = ctk.CTkLabel(self.howToPlayTabTemperature, width = 100, height = 100, text = '', image = ctk.CTkImage(Image.open(temperatureExtremeHeat), size = (90, 90))); self.sampleTemperature7.place(x = 250, y = 100)
        

        self.infoTime = ctk.CTkLabel(self.howToPlayTabTemperature, width = 250, height = 250, justify = 'left', text = 'These are the temperature ratings. \nSome will happen more than others \nduring the different seasons.', font = self.gameFont(size = 25), text_color = '#5a3c00')
        self.infoTime.place(x = 0, y = 250)








        self.closeButtonHowToPlayFrame = self.buttonStyle(self.howToPlayChoiceFrame, 'Close', 225, 50, 'refuse', command = lambda: self.howToPlayButtonFrame(NORMAL), state = DISABLED)
        self.closeButtonHowToPlayFrame.place(x = 137.5, y = 575)
        
        self.movingFrame(1, self.howToPlayChoiceFrame, 1250, 50, 350, 50, 0, self.frameSpeed, 1, lambda: self.buttonStateSettings(NORMAL, self.closeButtonHowToPlayFrame))

    # Settings Frame When Settings Button Is Pressed
    def settingsButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.speedButtonSettingsFrame, self.closeButtonSettingsFrame)
            self.movingFrame(1, self.settingsChoiceFrame, 487.5, 275, 0 - self.settingsChoiceFrame.winfo_width(), 275, 0, self.frameSpeed, 1, lambda: self.settingsChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.settingsChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 275, height = 200, fg_color = 'transparent', bg_color = 'transparent', corner_radius = 0)
        #self.backgroundImageSettingsFrame = ctk.CTkImage(Image.open(buttonBackground), size = (200 , 100))

        self.settingsLabelInfo = ctk.CTkLabel(self.settingsChoiceFrame, text = 'Settings', width = 275, height = 25, text_color = '#5a3c00', font = self.gameFont(size = 15))
        self.settingsLabelInfo.place(x = 0, y = 0)

        def changeSpeed():
            match self.frameSpeed:
                case 1:
                    self.frameSpeed = 4
                case 4:
                    self.frameSpeed = 7
                case 7:
                    self.frameSpeed = 10
                case 10:
                    self.frameSpeed = 1
            self.speedButtonSettingsFrame.configure(text = 'Speed : ' + str(self.frameSpeed))

        self.speedButtonSettingsFrame = self.buttonStyle(self.settingsChoiceFrame, 'Speed : ' + str(self.frameSpeed), 225, 50, 'accept', command = lambda: changeSpeed(), state = DISABLED)
        self.speedButtonSettingsFrame.place(x = 25, y = 50)
        self.speedButtonSettingsFrame.bind('<Enter>', lambda x: self.settingsLabelInfo.configure(text = 'Change Frame Speed'))
        self.speedButtonSettingsFrame.bind('<Leave>', lambda x: self.settingsLabelInfo.configure(text = 'Settings'))

        self.closeButtonSettingsFrame = self.buttonStyle(self.settingsChoiceFrame, 'Close', 225, 50, 'refuse', command = lambda: self.settingsButtonFrame(NORMAL), state = DISABLED)
        self.closeButtonSettingsFrame.place(x = 25, y = 125)
        self.closeButtonSettingsFrame.bind('<Enter>', lambda x: self.settingsLabelInfo.configure(text = 'Close Settings'))
        self.closeButtonSettingsFrame.bind('<Leave>', lambda x: self.settingsLabelInfo.configure(text = 'Settings'))

        self.movingFrame(3, self.settingsChoiceFrame, 0, 275, 487.5, 275, 0, self.frameSpeed, 1, lambda: self.buttonStateSettings(NORMAL, self.speedButtonSettingsFrame, self.closeButtonSettingsFrame))

    # Exit Frame When Exit Button Is Pressed
    def exitButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.yesButtonExitFrame, self.cancelButtonExitFrame)
            self.movingFrame(0, self.exitChoiceFrame, 487.5, 275 + self.exitChoiceFrame.winfo_reqheight(), 487.5, 750, 0, self.frameSpeed, 1, lambda: self.exitChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.exitChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 275, height = 200, fg_color = 'transparent', bg_color = 'transparent', corner_radius = 0)
        #self.backgroundImageExitFrame = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))

        self.exitLabelInfo = ctk.CTkLabel(self.exitChoiceFrame, text = 'Exit?', width = 275, height = 25, text_color = '#5a3c00', font = self.gameFont(size = 15))
        self.exitLabelInfo.place(x = 0, y = 0)

        self.yesButtonExitFrame = self.buttonStyle(self.exitChoiceFrame, 'Accept', 225, 50, 'accept', command = self.root.destroy, state = DISABLED)
        self.yesButtonExitFrame.place(x = 25, y = 50)
        self.yesButtonExitFrame.bind('<Enter>', lambda x: self.exitLabelInfo.configure(text = 'Comfirm Exit?'))
        self.yesButtonExitFrame.bind('<Leave>', lambda x: self.exitLabelInfo.configure(text = 'Exit?'))
        
        self.cancelButtonExitFrame = self.buttonStyle(self.exitChoiceFrame, 'Cancel', 225, 50, 'refuse', command = lambda: self.exitButtonFrame(NORMAL), state = DISABLED)
        self.cancelButtonExitFrame.place(x = 25, y = 125)
        self.cancelButtonExitFrame.bind('<Enter>', lambda x: self.exitLabelInfo.configure(text = 'Cancel Exit?'))
        self.cancelButtonExitFrame.bind('<Leave>', lambda x: self.exitLabelInfo.configure(text = 'Exit?'))

        self.movingFrame(2, self.exitChoiceFrame, 487.5, 750, 487.5, 275, 0, self.frameSpeed, 1, lambda: self.buttonStateSettings(NORMAL, self.yesButtonExitFrame, self.cancelButtonExitFrame))


    # Extra Functions To Help With Math And Frames Commands ----------------------------------------------------------------------------------------------------


    # Animated Frames That Move From One Side Of The Screen To The Other
    def movingFrame(self, direction, frame, startx, starty, endx, endy, state, speed, update, *extraCommands):
        if len(extraCommands) != 0: self.extraCommandsList = extraCommands
        if state == 0:
            self.frameWidth = frame.winfo_reqwidth()
            self.frameHeight = frame.winfo_reqheight()

        # TOP TO BOTTOM
        if direction == 0:
            if state == 0:
                newY = starty - self.frameHeight
                frame.place(x = startx, y = newY)
                self.root.after(update, lambda: self.movingFrame(direction, frame, startx, newY, endx, endy, 1, speed, update))
            else:
                starty += speed
                if starty > endy:
                    frame.place(x = startx, y = endy)
                    self.extraCommandsHandling()
                    return
                else:
                    frame.place(x = startx, y = starty)
                    self.root.after(update, lambda: self.movingFrame(direction, frame, startx, starty, endx, endy, 1, speed, update))

        # RIGHT TO LEFT
        elif direction == 1:
            if state == 0:
                frame.place(x = startx, y = starty)
                self.root.after(update, lambda: self.movingFrame(direction, frame, startx, starty, endx, endy, 1, speed, update))
            else:
                startx -= speed
                if startx < endx:
                    frame.place(x = endx, y = starty)
                    self.extraCommandsHandling()
                    return
                else:
                    frame.place(x = startx, y = starty)
                    self.root.after(update, lambda: self.movingFrame(direction, frame, startx, starty, endx, endy, 1, speed, update))
        
        # BOTTOM TO TOP
        elif direction == 2:
            if state == 0:
                frame.place(x = startx, y = starty)
                self.root.after(update, lambda: self.movingFrame(direction, frame, startx, starty, endx, endy, 1, speed, update))
            else:
                starty -= speed
                if starty < endy:
                    frame.place(x = startx, y = endy)
                    self.extraCommandsHandling()
                    return
                else:
                    frame.place(x = startx, y = starty)
                    self.root.after(update, lambda: self.movingFrame(direction, frame, startx, starty, endx, endy, 1, speed, update))
        
        # LEFT TO RIGHT
        elif direction == 3:
            if state == 0:
                newX = startx - self.frameWidth
                frame.place(x = newX, y = starty)
                self.root.after(update, lambda: self.movingFrame(direction, frame, newX, starty, endx, endy, 1, speed, update))
            else:
                startx += speed
                if startx > endx:
                    frame.place(x = endx, y = starty)
                    self.extraCommandsHandling()
                    return
                else:
                    frame.place(x = startx, y = starty)
                    self.root.after(update, lambda: self.movingFrame(direction, frame, startx, starty, endx, endy, 1, speed, update))
        
        elif direction == 5:
            return int()

    # Executing Multiple Commands
    def extraCommandsHandling(self):
        if(len(self.extraCommandsList)) != 0:
            for i in self.extraCommandsList: self.root.after(100, i)
            self.extraCommandsList = []

    # Progress Bar Decimal Number To Integer
    def progressBarToInt(self, progressBar):
        return int(progressBar.get() * 100)


    # Main Game Window ----------------------------------------------------------------------------------------------------


    # Will Make The Game Screen
    def gameScreen(self, startingSeason):
        self.gameTimer = 0
        self.inGame = True
        self.mainMenuFrame.destroy()

        self.stockShop()

        if self.firstGame:
            self.gameScreenFrame = ctk.CTkFrame(self.root, width = 1250, height = 750, fg_color = 'transparent', bg_color = 'transparent')
            self.gameScreenFrame.grid(row = 0, column = 0)
            self.gameScreenPlantPlacement()
            self.gameScreenGameWindow()
            self.gameScreenEnvironmentSettings()
            self.gameScreenShop()
            self.gameScreenMenuSettings()
            self.firstGame = False
        else:
            self.gameScreenFrame.grid(row = 0, column = 0)
        self.startingConditions(startingSeason)
        self.pygameLoop()

    # Set Game Speed
    def gameSpeedSetting(self):
        if self.gameSpeed == 500:
            self.gameSpeed = 100
        else:
            self.gameSpeed = 500
    
    # Exit The Current Game
    def exitCurrentGame(self):
        self.inGame = False
        self.gameScreenFrame.forget()
        self.mainMenu()

    # Stock Shop Items
    def stockShop(self):
        # [Name, Image, Count, Cost, Type, ]
        self.plantsStock = [plantBasic, plantBasic, plantBasic, plantBasic]
        self.itemsStock = [fertilizerSmall, fertilizerMid, fertilizerBig]
        self.fertilizersStock = [fertilizerBig, fertilizerBig, fertilizerBig, itemNet]
        self.measurementsStock = [fertilizerSmall, itemNet, fertilizerBig, itemNet]

    # Get Info For Current Item
    def itemInfoScreen(self, item):
        pass

    # Handles Shop Items
    def buyFromShop(self, item):
        print(item.name); print(item.cost); print(item.inStock); print(item.type)

    # Make The Game Screen PlantPlacement Frame
    def gameScreenPlantPlacement(self):
        self.plantPlacementFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 500)
        self.plantPlacementFrame.grid(row = 0, column = 0)
        self.plantPlacementBackgroundImageLabel = ctk.CTkLabel(self.plantPlacementFrame, text = '', width = 500, height = 500, fg_color = 'red', bg_color = 'red')
        self.plantPlacementBackgroundImageLabel.place(x = 0, y = 0)


        # The Main Game Window The User Controls ----------------------------------------------------------------------------------------------------


        self.hotBarTab = ctk.CTkTabview(self.plantPlacementFrame, width = 450, height = 475, corner_radius = 0, border_width = 10, text_color = 'black')
        self.hotBarTab.place(x = 25, y = 25)
        self.hotBarTabPlantPlacement = self.hotBarTab.add('Farm')
        self.hotBarTabInventory = self.hotBarTab.add('Inventory')
        self.hotBarTabItemInfo = self.hotBarTab.add('Item Info')


        self.hotBarPlantPlacement = ctk.CTkFrame(self.hotBarTabPlantPlacement, width = 10, height = 10, corner_radius = 0)
        self.hotBarPlantPlacement.pack(fill = 'both', expand = 1)

        self.hotBarInventoryTab = ctk.CTkTabview(self.hotBarTabInventory, width = 10, height = 10, corner_radius = 0, border_width = 10, text_color = 'black')
        self.hotBarInventoryTab.pack(fill = 'both', expand = 1)

        self.hotBarInventoryTabPlants = self.hotBarInventoryTab.add('Plants')
        self.hotBarInventoryTabItems = self.hotBarInventoryTab.add('Items')
        self.hotBarInventoryTabFertilizers = self.hotBarInventoryTab.add('Fertilizers')
        self.hotBarInventoryTabMeasurements = self.hotBarInventoryTab.add('Measurements')

        self.hotBarInventoryPlants = ctk.CTkScrollableFrame(self.hotBarInventoryTabPlants, width = 10, height = 10, corner_radius = 0)
        self.hotBarInventoryPlants.pack(fill = 'both', expand = 1)
        self.hotBarInventoryTabItems = ctk.CTkScrollableFrame(self.hotBarInventoryTabItems, width = 10, height = 10, corner_radius = 0)
        self.hotBarInventoryTabItems.pack(fill = 'both', expand = 1)
        self.hotBarInventoryTabFertilizers = ctk.CTkScrollableFrame(self.hotBarInventoryTabFertilizers, width = 10, height = 10, corner_radius = 0)
        self.hotBarInventoryTabFertilizers.pack(fill = 'both', expand = 1)
        self.hotBarInventoryTabMeasurements = ctk.CTkScrollableFrame(self.hotBarInventoryTabMeasurements, width = 10, height = 10, corner_radius = 0)
        self.hotBarInventoryTabMeasurements.pack(fill = 'both', expand = 1)



        self.hotBarItemInfo = ctk.CTkFrame(self.hotBarTabItemInfo, width = 10, height = 10, corner_radius = 0)
        self.hotBarItemInfo.pack(fill = 'both', expand = 1)




    # Make The Game Screen Game Window Frame
    def gameScreenGameWindow(self):
        self.gameWindowFrame = Frame(self.gameScreenFrame, width = 500, height = 500)
        self.gameWindowFrame.grid(row = 0, column = 1)
    
        os.environ['SDL_WINDOWID'] = str(self.gameWindowFrame.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        
        pygame.display.init()
        self.screen = pygame.display.set_mode()
        self.timeSurface = pygame.Surface((500, 500), pygame.SRCALPHA)
        #self.pygameLoop()

        #

    # Make The Game Screen EnvironmentSettings Frame
    def gameScreenEnvironmentSettings(self):
        self.environmentSettingsFrame = ctk.CTkFrame(self.gameScreenFrame, width = 250, height = 750)
        self.environmentSettingsFrame.grid(row = 0, column = 2, rowspan = 2)
        self.environmentSettingsBackgroundImageLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 250, height = 750, fg_color = 'purple', bg_color = 'purple')
        self.environmentSettingsBackgroundImageLabel.place(x = 0, y = 0)


        # Main Game Element That Changes The Game The Most ----------------------------------------------------------------------------------------------------


        self.dayNightCycleProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 150, height = 50, corner_radius = 0, determinate_speed = 1, border_width = 10)
        self.dayNightCycleProgressBar.place(x = 25, y = 25); self.dayNightCycleProgressBar.set(0)
        self.timeLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.timeLabel.place(x = 175, y = 25)

        self.seasonsProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 150, height = 50, corner_radius = 0, determinate_speed = .1, border_width = 10)
        self.seasonsProgressBar.place(x = 25, y = 100); self.seasonsProgressBar.set(0)
        self.seasonLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.seasonLabel.place(x = 175, y = 100)


        # Info Bars For The Current Game State That Are User Controlled ----------------------------------------------------------------------------------------------------


        self.rainLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.rainLabel.place(x = 25, y = 175)
        self.rainLabalBackground = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 226); self.rainLabalBackground.place(x = 25, y = 224)
        self.rainSlider = ctk.CTkSlider(self.environmentSettingsFrame, width = 30, height = 205, corner_radius = 0, from_ = 0, to = 4, border_width = 0, orientation = 'vertical', number_of_steps = 4, hover = FALSE)
        self.rainSlider.place(x = 35, y = 235); self.rainSlider.set(0)

        self.wildlifeLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.wildlifeLabel.place(x = 100, y = 175)
        self.wildlifeLabalBackground = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 226); self.wildlifeLabalBackground.place(x = 100, y = 224)
        self.wildlifeSlider = ctk.CTkSlider(self.environmentSettingsFrame, width = 30, height = 205, corner_radius = 0, from_ = 0, to = 4, border_width = 0, orientation = 'vertical', number_of_steps = 4, hover = FALSE, progress_color = '#005c12')
        self.wildlifeSlider.place(x = 110, y = 235); self.wildlifeSlider.set(0)


        # Info Bars For The Current Game State That Changes Based On Current Game State ----------------------------------------------------------------------------------------------------


        self.ratingLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.ratingLabel.place(x = 175, y = 175)
        self.ratingProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 50, height = 226, corner_radius = 0, border_width = 10, orientation = 'vertical')
        self.ratingProgressBar.place(x = 175, y = 224); self.ratingProgressBar.set(0)

        self.humidityLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.humidityLabel.place(x = 25, y = 475)
        self.humidityProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 50, height = 200, corner_radius = 0, border_width = 10, orientation = 'vertical')
        self.humidityProgressBar.place(x = 25, y = 525); self.humidityProgressBar.set(0)

        self.nutrientLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.nutrientLabel.place(x = 100, y = 475)
        self.nutrientProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 50, height = 200, corner_radius = 0, border_width = 10, orientation = 'vertical')
        self.nutrientProgressBar.place(x = 100, y = 525); self.nutrientProgressBar.set(0)

        self.temperatureLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.temperatureLabel.place(x = 175, y = 475)
        self.temperatureProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 50, height = 200, corner_radius = 0, border_width = 10, orientation = 'vertical')
        self.temperatureProgressBar.place(x = 175, y = 525); self.temperatureProgressBar.set(0)

    # Make The Game Screen Shop Frame
    def gameScreenShop(self):
        self.shopFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 250)
        self.shopFrame.grid(row = 1, column = 0)
        self.shopBackgroundImageLabel = ctk.CTkLabel(self.shopFrame, text = '', width = 500, height = 250, fg_color = 'green', bg_color = 'green')
        self.shopBackgroundImageLabel.place(x = 0, y = 0)


        # Game Shops ----------------------------------------------------------------------------------------------------


        self.shopTabs = ctk.CTkTabview(self.shopFrame, width = 450, height = 200, corner_radius = 0, border_width = 10, text_color = 'black')
        self.shopTabs.place(x = 25, y = 25)
        self.shopTabPlants = self.shopTabs.add('Plants')
        self.shopTabItems = self.shopTabs.add('Items')
        self.shopTabFertilizers = self.shopTabs.add('Fertilizers')
        self.shopTabMeasurements = self.shopTabs.add('Measurements')

        self.shopPlants = ctk.CTkScrollableFrame(self.shopTabPlants, width = 10, height = 10, corner_radius = 0, orientation = 'horizontal')
        self.shopPlants.pack(fill = 'both', expand = 1)
        self.shopItems = ctk.CTkScrollableFrame(self.shopTabItems, width = 10, height = 10, corner_radius = 0, orientation = 'horizontal')
        self.shopItems.pack(fill = 'both', expand = 1)
        self.shopFertilizers = ctk.CTkScrollableFrame(self.shopTabFertilizers, width = 10, height = 10, corner_radius = 0, orientation = 'horizontal')
        self.shopFertilizers.pack(fill = 'both', expand = 1)
        self.shopMeasurements = ctk.CTkScrollableFrame(self.shopTabMeasurements, width = 10, height = 10, corner_radius = 0, orientation = 'horizontal')
        self.shopMeasurements.pack(fill = 'both', expand = 1)
        
        # Need To Make Extra Frames Since There Is A Bug With .place() In CTkScrollableFrame
        self.shopPlantsFrame = ctk.CTkFrame(self.shopPlants, width = len(self.plantsStock) * 128, height = 128, corner_radius = 0); self.shopPlantsFrame.pack(fill = 'both', expand = 1)
        self.shopItemsFrame = ctk.CTkFrame(self.shopItems, width = len(self.itemsStock) * 128, height = 128, corner_radius = 0); self.shopItemsFrame.pack(fill = 'both', expand = 1)
        self.shopFertilizerFrame = ctk.CTkFrame(self.shopFertilizers, width = len(self.fertilizersStock) * 128, height = 128, corner_radius = 0); self.shopFertilizerFrame.pack(fill = 'both', expand = 1)
        self.shopMeasurementsFrame = ctk.CTkFrame(self.shopMeasurements, width = len(self.measurementsStock) * 128, height = 128, corner_radius = 0); self.shopMeasurementsFrame.pack(fill = 'both', expand = 1)

        # Add Buttons To Buy Shop Items       
        def addShopButtons(stock, frame):
            counter = 0
            for item in stock:
                self.placeHolder = ctk.CTkButton(frame, text = '', image = ctk.CTkImage(Image.open(item.image), size = (108 , 108)), width = 128, height = 128, corner_radius = 0, command = lambda item = item: self.itemInfoScreen(item))
                self.placeHolder.place(x = counter, y = 0); counter += 128
                





        addShopButtons(self.plantsStock, self.shopPlantsFrame); addShopButtons(self.itemsStock, self.shopItemsFrame); addShopButtons(self.fertilizersStock, self.shopFertilizerFrame); addShopButtons(self.measurementsStock, self.shopMeasurementsFrame)

 



    # Make The Game Screen Menu Settings Frame
    def gameScreenMenuSettings(self):
        self.menuSettingsFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 250)
        self.menuSettingsFrame.grid(row = 1, column = 1)
        self.menuSettingsBackgroundImageLabel = ctk.CTkLabel(self.menuSettingsFrame, text = '', width = 500, height = 250, fg_color = 'light green', bg_color = 'light green')
        self.menuSettingsBackgroundImageLabel.place(x = 0, y = 0)


        # Main Menu Settings And Info ----------------------------------------------------------------------------------------------------


        self.moneyLabel = ctk.CTkLabel(self.menuSettingsFrame, text = 'Money', width = 250, height = 50, image = ctk.CTkImage(Image.open(iconMoney)), compound = 'left')
        self.moneyLabel.place(x = 0, y = 25)

        self.scoreLabel = ctk.CTkLabel(self.menuSettingsFrame, text = 'Score', width = 250, height = 50)
        self.scoreLabel.place(x = 250, y = 25)

        self.infoLabel = ctk.CTkLabel(self.menuSettingsFrame, text = 'Info', width = 500, height = 50)
        self.infoLabel.place(x = 0, y = 100)

        self.speedButton = ctk.CTkButton(self.menuSettingsFrame, text = 'Speed', width = 150, height = 50, fg_color = 'limegreen', hover_color = 'forestgreen', border_color = 'saddle brown', text_color = 'saddle brown', border_width = 10, corner_radius = 0, bg_color = 'transparent', text_color_disabled = 'forestgreen', command = self.gameSpeedSetting)
        self.speedButton.place(x = 0, y = 175)

        self.idkButton = ctk.CTkButton(self.menuSettingsFrame, text = 'IDK', width = 150, height = 50, fg_color = 'limegreen', hover_color = 'forestgreen', border_color = 'saddle brown', text_color = 'saddle brown', border_width = 10, corner_radius = 0, bg_color = 'transparent', text_color_disabled = 'forestgreen', command = self.gameSpeedSetting)
        self.idkButton.place(x = 175, y = 175)

        self.exitGameButton = ctk.CTkButton(self.menuSettingsFrame, text = 'Exit', width = 150, height = 50, fg_color = 'limegreen', hover_color = 'forestgreen', border_color = 'saddle brown', text_color = 'saddle brown', border_width = 10, corner_radius = 0, bg_color = 'transparent', text_color_disabled = 'forestgreen', command = self.exitCurrentGame)
        self.exitGameButton.place(x = 350, y = 175)

    # Handles The Game Time
    def timeSettings(self):
        self.screen.blit(self.timeSurface, (0, 0))
        if self.dayNightCycleProgressBar.get() == 1:
            self.dayNightCycleProgressBar.set(0)
        if self.seasonsProgressBar.get() == 1 and self.yearDayCounter == 21:
            self.seasonsProgressBar.set(0)
            self.yearDayCounter = 1
        if self.gameTimer != 0:
            self.dayNightCycleProgressBar.set(round(self.dayNightCycleProgressBar.get() + .01, 3))
        #self.seasonsProgressBar.step()

        self.timeSurface.fill((self.currentTime[1])); self.timeSurface.set_alpha(self.setAlpha)

        if (self.progressBarToInt(self.dayNightCycleProgressBar) < 10):
            if self.currentTime == self.timesSet[0]: return
                #if self.gameTimer != 0: return
            self.currentTime = self.timesSet[0]; self.setAlpha = 16
            self.temperatureProgressBar.set(random.randint(self.gameVariables['currentSeason'][3][0], self.gameVariables['currentSeason'][3][1])/100)
            self.yearDayCounter += 1
        elif (10 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 20):
            if self.currentTime == self.timesSet[1]: return
            self.currentTime = self.timesSet[1]
        elif (20 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 30):
            if self.currentTime == self.timesSet[2]: return
            self.currentTime = self.timesSet[2]
        elif (30 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 40):
            if self.currentTime == self.timesSet[3]: return
            self.currentTime = self.timesSet[3]
        elif (40 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 50):
            if self.currentTime == self.timesSet[4]: return
            self.currentTime = self.timesSet[4]
        elif (50 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 60):
            if self.currentTime == self.timesSet[5]: return
            self.currentTime = self.timesSet[5]; self.setAlpha = 64
            self.temperatureProgressBar.set(random.randint(self.gameVariables['currentSeason'][3][0], self.gameVariables['currentSeason'][3][1])/100)
        elif (60 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 70):
            if self.currentTime == self.timesSet[6]: return
            self.currentTime = self.timesSet[6]
        elif (70 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 80):
            if self.currentTime == self.timesSet[7]: return
            self.currentTime = self.timesSet[7]
        elif (80 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 90):
            if self.currentTime == self.timesSet[8]: return
            self.currentTime = self.timesSet[8]
        elif (90 <= self.progressBarToInt(self.dayNightCycleProgressBar) <= 100):
            if self.currentTime == self.timesSet[9]: return
            self.currentTime = self.timesSet[9]
        
        #if self.gameTimer != 0:
        self.seasonsProgressBar.set(round(self.seasonsProgressBar.get() + .005, 3))
        print(f'Day {self.yearDayCounter} and {self.seasonsProgressBar.get()} and {self.gameTimer} and {self.dayNightCycleProgressBar.get()}')
        #print(self.progressBarToInt(self.seasonsProgressBar))
        self.timeLabel.configure(image = ctk.CTkImage(Image.open(self.currentTime[0]), size=(44 , 44)))
        self.dayNightCycleProgressBar.configure(progress_color = self.currentTime[1])
    
    # Handles Season Chnages
    def seasonSettings(self):
        
        if (0 <= self.progressBarToInt(self.seasonsProgressBar) < 25):
            if self.gameVariables.get('currentSeason') == self.gameVariables.get('seasonsSet')[0]:
                if self.gameTimer != 0: return
            self.gameVariables['currentSeason'] = self.gameVariables.get('seasonsSet')[0]
        elif (25 <= self.progressBarToInt(self.seasonsProgressBar) < 50):
            if self.gameVariables.get('currentSeason') == self.gameVariables.get('seasonsSet')[1]:
                if self.gameTimer != 0: return
            self.gameVariables['currentSeason'] = self.gameVariables.get('seasonsSet')[1]
        elif (50 <= self.progressBarToInt(self.seasonsProgressBar) < 75):
            if self.gameVariables.get('currentSeason') == self.gameVariables.get('seasonsSet')[2]:
                if self.gameTimer != 0: return
            self.gameVariables['currentSeason'] = self.gameVariables.get('seasonsSet')[2]
        elif (75 <= self.progressBarToInt(self.seasonsProgressBar) <= 100):
            if self.gameVariables.get('currentSeason') == self.gameVariables.get('seasonsSet')[3]:
                if self.gameTimer != 0: return
            self.gameVariables['currentSeason'] = self.gameVariables.get('seasonsSet')[3]


        self.seasonLabel.configure(image = ctk.CTkImage(Image.open(self.gameVariables['currentSeason'][1]), size = (50 , 50))) # 44, 44 for other label borders
        self.seasonsProgressBar.configure(progress_color = self.gameVariables['currentSeason'][2][2], border_color = self.gameVariables['currentSeason'][2][0])
        '''
        for child in self.environmentSettingsFrame.children.values():
            if isinstance(child, ctk.CTkLabel): child.configure(fg_color = self.gameVariables['currentSeason'][2][0])
            elif isinstance(child, ctk.CTkProgressBar): child.configure(border_color = self.gameVariables['currentSeason'][2][0])
            elif isinstance(child, ctk.CTkSlider): child.configure(bg_color = self.gameVariables['currentSeason'][2][0])
        '''
        sC0 = self.gameVariables['currentSeason'][2][0] # Seasonal Color 0
        sC1 = self.gameVariables['currentSeason'][2][1] # Seasonal Color 1
        sC2 = self.gameVariables['currentSeason'][2][2] # Seasonal Color 2
        for frames in [self.plantPlacementFrame, self.environmentSettingsFrame, self.shopFrame, self.menuSettingsFrame]:
            for child in frames.children.values():
                if isinstance(child, ctk.CTkLabel): child.configure(fg_color = sC0)
                elif isinstance(child, ctk.CTkProgressBar): child.configure(border_color = sC0)
                elif isinstance(child, ctk.CTkSlider): child.configure(bg_color = sC0)
                elif isinstance(child, ctk.CTkTabview): child.configure(fg_color = sC0, bg_color = sC0, border_color = sC0, segmented_button_selected_color = sC2, segmented_button_selected_hover_color = sC1)

        self.plantPlacementBackgroundImageLabel.configure(fg_color = self.gameVariables['currentSeason'][2][1])
        self.environmentSettingsBackgroundImageLabel.configure(fg_color = self.gameVariables['currentSeason'][2][1])
        self.shopBackgroundImageLabel.configure(fg_color = self.gameVariables['currentSeason'][2][1])
        self.menuSettingsBackgroundImageLabel.configure(fg_color = self.gameVariables['currentSeason'][2][1])

        self.hotBarInventoryTab.configure(fg_color = sC0, bg_color = sC0, border_color = sC0, segmented_button_selected_color = sC2, segmented_button_selected_hover_color = sC1)


        if self.gameVariables['currentSeason'] == self.gameVariables.get('seasonsSet')[3]:
            self.gameVariables['currentWeatherSet'] = self.gameVariables['snowsSet']
            self.rainSlider.configure(progress_color = '#ffffff')
        else:
            self.gameVariables['currentWeatherSet'] = self.gameVariables['rainsSet']
            self.rainSlider.configure(progress_color = '#0000ff')
        self.changeSeasonSet = False
    
    # Handles The Game Weather
    def rainSettings(self):
        self.sliderSettings(self.rainSlider, 'currentWeather', 'currentWeatherSet', self.rainLabel)
    
    # Handles The Game Wildlide
    def wildlifeSettings(self):
        self.sliderSettings(self.wildlifeSlider, 'currentWildlife', 'wildlifeSet', self.wildlifeLabel)
    
    # Handles The Game Sliders, Will Update Current Settings
    def sliderSettings(self, slider, current, set, label):
        
        if (slider.get() == 0):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[0]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[0]
        elif (slider.get() == 1):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[1]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[1]
        elif (slider.get() == 2):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[2]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[2]
        elif (slider.get() == 3):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[3]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[3]
        elif (slider.get() == 4):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[4]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[4]
        elif (slider.get() == 5):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[5]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[5]

        label.configure(image = ctk.CTkImage(Image.open(self.gameVariables[current][1]), size=(44 , 44)))
        slider.configure(button_color = self.gameVariables[current][2])
        
    # Handles The Game Rating System
    def ratingSettings(self):
        #self.ratingProgressBar.step()
        self.progressBarSettings(self.ratingProgressBar, 'currentRating', 'ratingsSet', self.ratingLabel)
    
    # Handles The Game Humidity
    def humiditySettings(self):
        #self.humidityProgressBar.step()
        if self.gameVariables.get('currentWeather') != self.gameVariables.get('currentWeatherSet')[0]:
            if self.humidityProgressBar.get() < self.temperatureProgressBar.get():
                self.humidityProgressBar.set(self.humidityProgressBar.get() + (self.gameVariables.get('currentWeather')[3]/100))
        else:
            self.humidityProgressBar.set(self.humidityProgressBar.get() - 0.01)


        self.progressBarSettings(self.humidityProgressBar, 'currentHumidity', 'humiditiesSet', self.humidityLabel)
    
    # Handles The Game Plant Soil Nutrient
    def nutrientSettings(self):
        #self.nutrientProgressBar.step()
        self.progressBarSettings(self.nutrientProgressBar, 'currentNutrient', 'nutrientsSet', self.nutrientLabel)
    
    # Handles The Game Temperature Based on Time And Seasons
    def temperatureSettings(self):
        #self.temperatureProgressBar.step()
        self.progressBarSettings(self.temperatureProgressBar, 'currentTemperature', 'temperaturesSet', self.temperatureLabel)

    # Handles The Game ProgressBars, Will Update Current Settings
    def progressBarSettings(self, progressBar, current, set, label):
        if (self.progressBarToInt(progressBar) == 0):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[0]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[0]
        elif (0 < self.progressBarToInt(progressBar) <= 20):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[1]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[1]
        elif (20 < self.progressBarToInt(progressBar) <= 40):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[2]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[2]
        elif (40 < self.progressBarToInt(progressBar) <= 60):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[3]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[3]
        elif (60 < self.progressBarToInt(progressBar) <= 80):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[4]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[4]
        elif (80 < self.progressBarToInt(progressBar) < 100):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[5]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[5]
        elif (self.progressBarToInt(progressBar) == 100):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[6]:
                if self.gameTimer != 0: return
            self.gameVariables[current] = self.gameVariables.get(set)[6]
        label.configure(image = ctk.CTkImage(Image.open(self.gameVariables[current][1]), size=(44 , 44)))
        progressBar.configure(progress_color = self.gameVariables[current][2])

    # Sets Up Random Starting Conditions For This Round
    def startingConditions(self, startingSeason):
        
        if startingSeason == self.gameVariables.get('seasonsSet')[0]:
            self.seasonsProgressBar.set(0); self.yearDayCounter = 1
            print('spring')
        elif startingSeason == self.gameVariables.get('seasonsSet')[1]:
            self.seasonsProgressBar.set(0.25); self.yearDayCounter = 6
            print('summer')
        elif startingSeason == self.gameVariables.get('seasonsSet')[2]:
            self.seasonsProgressBar.set(.5); self.yearDayCounter = 11
            print('fall')
        elif startingSeason == self.gameVariables.get('seasonsSet')[3]:
            self.seasonsProgressBar.set(.75); self.yearDayCounter = 16
            print('winter')

        self.currentTime = self.timesSet[0]
        self.timeLabel.configure(image = ctk.CTkImage(Image.open(self.currentTime[0]), size=(44 , 44)))
        self.dayNightCycleProgressBar.configure(progress_color = self.currentTime[1])
        self.gameVariables['currentSeason'] = startingSeason
        if startingSeason == self.gameVariables.get('seasonsSet')[3]:
            self.gameVariables['currentWeatherSet'] = self.gameVariables.get('snowsSet')
        else:
            self.gameVariables['currentWeatherSet'] = self.gameVariables.get('rainsSet')

        self.setAlpha = 16
        self.dayNightCycleProgressBar.set(0)
        #self.seasonsProgressBar.set(0)
        self.rainSlider.set(0)
        self.wildlifeSlider.set(0)
        self.ratingProgressBar.set(0)
        self.humidityProgressBar.set(0)
        self.nutrientProgressBar.set(0)
        self.temperatureProgressBar.set((random.randint(startingSeason[3][0], startingSeason[3][1]))/100)
        self.placeSoilSpots()
        
        self.setFarm()

    def placeSoilSpots(self):
        self.plantPlacementSpots.clear()
        posX = 50
        posY = 50
        for i in range(8):
            posX = 50
            for i in range(8):
                self.plantPlacementSpots.append(soilSpot(posX, posY))
                posX += 50
            posY += 50

        #for i in self.plantPlacementSpots:
        #    i.currentPlant = copy.deepcopy(plantBasicType)
        

    def updateSoilSpots(self):
        for soil in self.plantPlacementSpots:
            soil.getCurrent(self.currentTime,
                            self.gameVariables['currentWeather'],
                            self.gameVariables['currentHumidity'],
                            self.gameVariables['currentNutrient'],
                            self.gameVariables['currentTemperature'])
        self.TESTINGPLANTGROWTH()


    # Test function for plant Growth based on Counter
    def TESTINGPLANTGROWTH(self):
        '''
        global counter
        self.screen.blit(pygame.transform.scale(pygame.image.load(iconMoney), (200, 200)), (100, 100))
        counter += 1
        if counter < 10:
            self.screen.blit(plantList[0], (200, 200))
        elif 10 <= counter < 20:
            self.screen.blit(plantList[1], (200, 200))
        elif 20 <= counter < 30:
            self.screen.blit(plantList[2], (200, 200))
        elif 30 <= counter < 40:
            self.screen.blit(plantList[3], (200, 200))
        elif 40 <= counter:
            self.screen.blit(plantList[4], (200, 200))
        '''
        totalMood = 0
        totalPlants = 0
        for soil in self.plantPlacementSpots:
            self.screen.blit(pygame.transform.scale(pygame.image.load(soil.waterLevelPicture), (50, 50)), (soil.posX, soil.posY))
            
            if soil.currentPlant != 'Empty':
                totalPlants += 1
                soil.testGrowth()
                self.screen.blit(pygame.transform.scale(pygame.image.load(soil.currentPlant.currentStage), (50, 100)), (soil.posX, soil.posY - 50))
                totalMood += soil.currentPlant.mood
                #print(soil.currentPlant.stageCounter)
        if totalPlants != 0:
            self.ratingProgressBar.set((totalMood / totalPlants) / 100)

    def environmentSettingsCaller(self):
        #self.timeSettings()
        self.seasonSettings()
        self.rainSettings()
        self.wildlifeSettings()
        self.ratingSettings()
        self.humiditySettings()
        self.nutrientSettings()
        self.temperatureSettings()

    def screenUpdateSettings(self):
        self.screen.blit(pygame.transform.scale(pygame.image.load(self.gameVariables.get('currentNutrient')[3]), (500, 500)), (0, 0))
        self.screen.blit(pygame.transform.scale(pygame.image.load(self.gameVariables.get('currentSeason')[5]), (500, 500)), (0, 0))

    # Testing Concept

    # Farm Frame Is width = 430, height = 418
    def setFarm(self): 
        #buttonTest = ctk.CTkButton(self.hotBarPlantPlacement, width = 430, height = 418, corner_radius = 0)
        #buttonTest.place(x = 0, y = 0)
        #print('placed')
        posX = 0
        posY = 0
        count = 1
        for i in range(8):
            posX = 0
            for i in range(8):
                buttonTest = ctk.CTkButton(self.hotBarPlantPlacement, width = 53.75, height = 52.25, corner_radius = 0, text = count, command = lambda count = count: self.plantPlant(count))
                buttonTest.place(x = posX, y = posY)
                count += 1
                posX += 53.75
            posY += 52.25

    def plantPlant(self, plantPlace):
        if self.plantPlacementSpots[plantPlace - 1].currentPlant == 'Empty':
            self.plantPlacementSpots[plantPlace - 1].currentPlant = copy.deepcopy(plantBasicType)



    # Main Pygame Game Loop
    def pygameLoop(self):
        if self.inGame == True:
            self.screen.fill((255, 255, 255))

            #pygame.draw.circle(self.screen, 'green', (250, 250), 125)


            #self.TESTINGPLANTGROWTH()

            self.environmentSettingsCaller()
            self.screenUpdateSettings()
            self.updateSoilSpots()


            self.timeSettings()
            


            pygame.display.flip()
        #if self.inGame == True:
            self.root.update()
            self.gameTimer += 1
            self.root.after(self.gameSpeed, self.pygameLoop)


# Starts The Game----------------------------------------------------------------------------------------------------

   
# Starts The Game Start Up
gameInstance = EcoQuest()
gameInstance.mainloop()


















