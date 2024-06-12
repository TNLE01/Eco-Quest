# Author: Truong Le

# Imports All Needed Modules
import pygame, random, time, datetime, os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image
from images import *
import customtkinter as ctk
import random


plantList = [pygame.transform.scale(pygame.image.load(plant0), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant1), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant2), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant3), (200, 200)),
             pygame.transform.scale(pygame.image.load(plant4), (200, 200))]
counter = 0

class EcoQuest():

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

        # Time Progress Bar Information
        self.timesSet = [[timeDay1, '#0080ff'], [timeDay2, '#00ffff'], [timeDay3, '#80ffff'], [timeDay4, '#00ffff'], [timeDay5, '#0080ff'], [timeNight1, '#0000ff'], [timeNight2, '#000080'], [timeNight3, '#000000'], [timeNight4, '#000080'], [timeNight5, '#0000ff']]
        self.currentTime = []

        # Seasons Progress Bar Information
        self.springSeasonSet = [springSeason, ['#6cffcf', '#a5e58d', '#009418'], [40, 80], [20, 60], -2]
        self.summerSeasonSet = [summerSeason, ['#ffb3e3', '#ff54f4', '#9a00a8'], [60, 100], [40, 80], -1]
        self.fallSeasonSet = [fallSeason, ['#d38600', '#e0e13c', '#bb1000'], [20, 60], [0, 40], -3]
        self.winterSeasonSet = [winterSeason, ['#379ed8', '#a5fdff', '#ffffff'], [0, 40], [0, 20], -4]
        #self.seasonsSet = [[springSeason, ['#6cffcf', '#a5e58d', '#009418'], [], []], [summerSeason, ['#ffb3e3', '#ff54f4', '#9a00a8'], [], []], [fallSeason, ['#d38600', '#e0e13c', '#bb1000'], [], []], [winterSeason, ['#379ed8', '#a5fdff', '#ffffff'], [], []]]

        self.currentSeasonSet = []
        self.changeSeasonSet = True

        # Weather Slider Information
        self.gameVariables['rainsSet'] = [[rainClear, '#e5ff00', 0], [rainLight, '#c8c8c8', 1], [rainModerate, '#969696', 2], [rainHeavy, '#646464', 3], [rainViolent, '#323232', 4]]
        self.gameVariables['snowsSet'] = [[snowClear, '#e5ff00', 0], [snowLight, '#c8c8c8', 0], [snowModerate, '#969696', 0], [snowHeavy, '#646464', 0], [snowViolent, '#323232', 0]]
        self.gameVariables['currentWeatherSet'] = []
        self.gameVariables['currentWeather'] = []

        # Wildlife Slider Information
        self.gameVariables['wildlifeSet'] = [[wildlifeNone, '#03652a'], [wildlifeFew, '#7d6400'], [wildlifeSeveral, '#964b00'], [wildlifeMany, '#7d3200'], [wildlifeALot, '#641900']]
        self.gameVariables['currentWildlife'] = []

        # Rating Progress Bar Information
        self.gameVariables['ratingsSet'] = [[ratingVeryBad, '#ff3600'], [ratingVeryBad, '#ff3600'], [ratingBad, '#ff7c00'], [ratingOkay, '#ffc900'], [ratingGood, '#fffb00'], [ratingVeryGood, '#9fff00'], [ratingVeryGood, '#9fff00']]
        self.gameVariables['currentRating'] = []

        # Humidity Progress Bar Information
        self.gameVariables['humiditiesSet'] = [[humidityVeryDry, '#f288ff'], [humidityVeryDry, '#f288ff'], [humidityDry, '#cc86ec'], [humidityOptimal, '#9da6e5'], [humidityHumid, '#a9dcf4'], [humidityVeryHumid, '#b9fdff'], [humidityVeryHumid, '#b9fdff']]
        self.gameVariables['currentHumidity'] = []

        # Nutrient Progress Bar Information
        self.gameVariables['nutrientsSet'] = [[nutrientExtremelyLow, '#3c1e00'], [nutrientVeryLow, '#462800'], [nutrientLow, '#503200'], [nutrientOkay, '#5a3c00'], [nutrientHigh, '#644600'], [nutrientVeryHigh, '#6e5000'], [nutrientExtremelyHigh, '#785a00']]
        self.gameVariables['currentNutrient'] = []

        # Temperature Progress Bar Information
        self.gameVariables['temperaturesSet'] = [[temperatureExtremeCold, '#000032'], [temperatureVeryCold, '#0000ff'], [temperatureCold, '#00c8ff'], [temperatureOkay, '#00c800'], [temperatureHot, '#ffc800'], [temperatureVeryHot, '#ff0000'], [temperatureExtremeHeat, '#320000']]
        self.gameVariables['currentTemperature'] = []

        # TESTING
        self.piccc = ImageTk.PhotoImage(Image.open(ecoQuestIcon))
        self.pictest = Image.open(ecoQuestIcon)
        self.buttonBackgroundimage = Image.open(buttonBackground)
        self.bgrez = ImageTk.PhotoImage(self.buttonBackgroundimage.resize((100, 50)))
        self.my_image = ctk.CTkImage(Image.open(buttonBackground))
        self.play_Image = ImageTk.PhotoImage(Image.open(playImage))

        # Used To Execute Multiple Commands Upon Other Actions
        self.extraCommandsList = []

        # See If The Game Is Running
        self.inGame = False

        # TESTING
        self.openImages()

        # Run The Main Menu
        self.mainMenu()
       # self.gameScreen()

    # TESTING
    def openImages(self):
        self.backgroundImage = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))
        #self.seasonListCTkImage = [ctk.CTkImage(Image.open(springSeason), size=(50 , 50)),
        #                           ctk.CTkImage(Image.open(summerSeason), size=(50 , 50)),
        #                           ctk.CTkImage(Image.open(fallSeason), size=(50 , 50)),
        #                           ctk.CTkImage(Image.open(winterSeason), size=(50 , 50))]

    # Main Tkinter Loop
    def mainloop(self):
        self.root.mainloop()

    # Main Menu Screen
    def mainMenu(self):
        self.mainMenuFrame = ctk.CTkFrame(self.root, width = 1250, height = 750, fg_color = 'yellow green', bg_color = 'green yellow')
        self.mainMenuFrame.grid(row = 0, column = 0)

        self.mainMenuBackgroundImageLabel = ctk.CTkLabel(self.mainMenuFrame, text = 'Main Menu Background Image Here', width = 1250, height = 750, fg_color = 'orange', bg_color = 'orange')
        self.mainMenuBackgroundImageLabel.place(x = 0, y = 0)

        self.titleLabel = ctk.CTkLabel(self.mainMenuFrame, text = 'Title Here', width = 1000, height = 175, fg_color = 'dark green', bg_color = 'transparent', )
        self.titleLabel.place(x = 125, y = 100)

        self.playButton = ctk.CTkButton(self.mainMenuFrame, text = 'Play', width = 200, height = 50, fg_color = 'limegreen', hover_color = 'forestgreen', border_color = 'saddle brown', text_color = 'saddle brown', border_width = 10, corner_radius = 0, bg_color = 'transparent', text_color_disabled = 'forestgreen', command = lambda : self.playButtonFrame(DISABLED))
        self.playButton.place(x=525, y=410)
        self.howToPlayButton = ctk.CTkButton(self.mainMenuFrame, text = 'How To Play', width = 200, height = 50, fg_color = 'limegreen', hover_color = 'forestgreen', border_color = 'saddle brown', text_color = 'saddle brown', border_width = 10, corner_radius = 0, bg_color = 'transparent', text_color_disabled = 'forestgreen', command = lambda : self.howToPlayButtonFrame(DISABLED))
        self.howToPlayButton.place(x=525, y=495)
        self.settingsButton = ctk.CTkButton(self.mainMenuFrame, text = 'Settings', width = 200, height = 50, fg_color = 'limegreen', hover_color = 'forestgreen', border_color = 'saddle brown', text_color = 'saddle brown', border_width = 10, corner_radius = 0, bg_color = 'transparent', text_color_disabled = 'forestgreen', command = lambda : self.settingsButtonFrame(DISABLED))
        self.settingsButton.place(x=525, y=580)
        self.exitButton = ctk.CTkButton(self.mainMenuFrame, text = 'Exit', width = 200, height = 50, fg_color = 'limegreen', hover_color = 'forestgreen', border_color = 'saddle brown', text_color = 'saddle brown', border_width = 10, corner_radius = 0, bg_color = 'transparent', text_color_disabled = 'forestgreen', command = lambda : self.exitButtonFrame(DISABLED))
        self.exitButton.place(x=525, y=665)

    # Disable or Enable Buttons
    def buttonStateSettings(self, buttonState, *args):
        for ar in args:
            ar.configure(state = buttonState)



    # Play Frame When Play Button Is Pressed
    def playButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.yesButtonPlayFrame, self.noButtonPlayFrame)
            self.movingFrame(2, self.playChoiceFrame, 525, 325, 525, 0 - self.playChoiceFrame.winfo_reqheight(), 0, 0.5, 1, lambda: self.playChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.playChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 200, height = 100, fg_color = "red", bg_color = 'red', corner_radius = 0)
        self.backgroundImagePlayFrame = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))
        self.backgroundImageLabelPlayFrame = ctk.CTkLabel(self.playChoiceFrame, image = self.backgroundImage, text = '')
        self.backgroundImageLabelPlayFrame.grid(column = 0, row = 0)

        self.playQuestionLabel = ctk.CTkLabel(self.playChoiceFrame, text = 'Play?', width = 200, height = 25, bg_color = 'transparent', fg_color = 'transparent')
        self.playQuestionLabel.place(x = 0, y = 0)
        self.yesButtonPlayFrame = ctk.CTkButton(self.playChoiceFrame, state = DISABLED, text = 'Yes', width = 50, height = 50, corner_radius = 0, command = self.gameScreen)
        self.yesButtonPlayFrame.place(x=25, y=25)
        self.noButtonPlayFrame = ctk.CTkButton(self.playChoiceFrame, state = DISABLED, text = 'No', width = 50, height = 50, corner_radius = 0, command = lambda: self.playButtonFrame(NORMAL))
        self.noButtonPlayFrame.place(x=125, y=25)

        self.movingFrame(0, self.playChoiceFrame, 525, 0, 525, 325, 0, 0.5, 1, lambda: self.buttonStateSettings(NORMAL, self.yesButtonPlayFrame, self.noButtonPlayFrame))
    
    # How To Play Frame When How To Play Button Is Pressed
    def howToPlayButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.yesButtonHowToPlayFrame, self.noButtonHowToPlayFrame)
            self.movingFrame(3, self.howToPlayChoiceFrame, 525 + self.howToPlayChoiceFrame.winfo_reqwidth(), 325, 1250, 325, 0, 0.5, 1, lambda: self.howToPlayChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.howToPlayChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 200, height = 100, fg_color = "red", bg_color = 'red', corner_radius = 0)
        self.backgroundImageHowToPlayFrame = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))
        self.backgroundImageLabelHowToPlayFrame = ctk.CTkLabel(self.howToPlayChoiceFrame, image = self.backgroundImageHowToPlayFrame, text = '')
        self.backgroundImageLabelHowToPlayFrame.grid(column = 0, row = 0)

        self.playQuestionLabel = ctk.CTkLabel(self.howToPlayChoiceFrame, text = 'How To Play?', width = 200, height = 25, bg_color = 'transparent', fg_color = 'transparent')
        self.playQuestionLabel.place(x = 0, y = 0)
        self.yesButtonHowToPlayFrame = ctk.CTkButton(self.howToPlayChoiceFrame, state = DISABLED, text = 'Yes', width = 50, height = 50, corner_radius = 0, command = self.root.destroy)
        self.yesButtonHowToPlayFrame.place(x=25, y=25)
        self.noButtonHowToPlayFrame = ctk.CTkButton(self.howToPlayChoiceFrame, state = DISABLED, text = 'No', width = 50, height = 50, corner_radius = 0, command = lambda: self.howToPlayButtonFrame(NORMAL))
        self.noButtonHowToPlayFrame.place(x=125, y=25)

        self.movingFrame(1, self.howToPlayChoiceFrame, 1250, 325, 525, 325, 0, 0.5, 1, lambda: self.buttonStateSettings(NORMAL, self.yesButtonHowToPlayFrame, self.noButtonHowToPlayFrame))

    # Settings Frame When Settings Button Is Pressed
    def settingsButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.yesButtonSettingsFrame, self.noButtonSettingsFrame)
            self.movingFrame(1, self.settingsChoiceFrame, 525, 325, 0 - self.settingsChoiceFrame.winfo_width(), 325, 0, 0.5, 1, lambda: self.settingsChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.settingsChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 200, height = 100, fg_color = "red", bg_color = 'red', corner_radius = 0)
        self.backgroundImageSettingsFrame = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))
        self.backgroundImageLabelSettingsFrame = ctk.CTkLabel(self.settingsChoiceFrame, image = self.backgroundImageSettingsFrame, text = '')
        self.backgroundImageLabelSettingsFrame.grid(column = 0, row = 0)

        self.playQuestionLabel = ctk.CTkLabel(self.settingsChoiceFrame, text = 'Settings?', width = 200, height = 25, bg_color = 'transparent', fg_color = 'transparent')
        self.playQuestionLabel.place(x = 0, y = 0)
        self.yesButtonSettingsFrame = ctk.CTkButton(self.settingsChoiceFrame, state = DISABLED, text = 'Yes', width = 50, height = 50, corner_radius = 0, command = self.root.destroy)
        self.yesButtonSettingsFrame.place(x=25, y=25)
        self.noButtonSettingsFrame = ctk.CTkButton(self.settingsChoiceFrame, state = DISABLED, text = 'No', width = 50, height = 50, corner_radius = 0, command = lambda: self.settingsButtonFrame(NORMAL))
        self.noButtonSettingsFrame.place(x=125, y=25)

        self.movingFrame(3, self.settingsChoiceFrame, 0, 325, 525, 325, 0, 0.5, 1, lambda: self.buttonStateSettings(NORMAL, self.yesButtonSettingsFrame, self.noButtonSettingsFrame))

    # Exit Frame When Exit Button Is Pressed
    def exitButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.yesButtonExitFrame, self.noButtonExitFrame)
            self.movingFrame(0, self.exitChoiceFrame, 525, 325 + self.exitChoiceFrame.winfo_reqheight(), 525, 750, 0, 0.5, 1, lambda: self.exitChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.exitChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 200, height = 100, fg_color = "red", bg_color = 'red', corner_radius = 0)
        self.backgroundImageExitFrame = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))
        self.backgroundImageLabelExitFrame = ctk.CTkLabel(self.exitChoiceFrame, image = self.backgroundImageExitFrame, text = '')
        self.backgroundImageLabelExitFrame.grid(column = 0, row = 0)

        self.exitQuestionLabel = ctk.CTkLabel(self.exitChoiceFrame, text = 'Exit?', width = 200, height = 25, bg_color = 'transparent', fg_color = 'transparent')
        self.exitQuestionLabel.place(x = 0, y = 0)
        self.yesButtonExitFrame = ctk.CTkButton(self.exitChoiceFrame, state = DISABLED, text = 'Yes', width = 50, height = 50, corner_radius = 0, command = self.root.destroy)
        self.yesButtonExitFrame.place(x=25, y=25)
        self.noButtonExitFrame = ctk.CTkButton(self.exitChoiceFrame, state = DISABLED, text = 'No', width = 50, height = 50, corner_radius = 0, command = lambda: self.exitButtonFrame(NORMAL))
        self.noButtonExitFrame.place(x=125, y=25)

        self.movingFrame(2, self.exitChoiceFrame, 525, 750, 525, 325, 0, 0.5, 1, lambda: self.buttonStateSettings(NORMAL, self.yesButtonExitFrame, self.noButtonExitFrame))



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

    # Will Make The Game Screen
    def gameScreen(self):
        self.inGame = True
        self.mainMenuFrame.grid_forget()
        self.gameScreenFrame = ctk.CTkFrame(self.root, width = 1250, height = 750, fg_color = 'transparent', bg_color = 'transparent')
        self.gameScreenFrame.grid(row = 0, column = 0)

        self.gameScreenPlantPlacement()
        self.gameScreenGameWindow()
        self.gameScreenEnvironmentSettings()
        self.gameScreenShop()
        self.gameScreenMenuSettings()

        self.pygameLoop()



    # Make The Game Screen PlantPlacement Frame
    def gameScreenPlantPlacement(self):
        self.plantPlacementFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 500)
        self.plantPlacementFrame.grid(row = 0, column = 0)
        self.plantPlacementBackgroundImageLabel = ctk.CTkLabel(self.plantPlacementFrame, text = 'Plant Placement Background Image Here', width = 500, height = 500, fg_color = 'red', bg_color = 'red')
        self.plantPlacementBackgroundImageLabel.place(x = 0, y = 0)

        #

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

        #

        self.currentTime = self.timesSet[0]
        self.dayNightCycleProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 150, height = 50, corner_radius = 0, determinate_speed = 1, border_width = 10)
        self.dayNightCycleProgressBar.place(x = 25, y = 25); self.dayNightCycleProgressBar.set(0)
        self.timeLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50, image = ctk.CTkImage(Image.open(self.currentTime[0]), size=(44 , 44)))
        self.timeLabel.place(x = 175, y = 25)

        self.seasonsProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 150, height = 50, corner_radius = 0, determinate_speed = .1, border_width = 10)
        self.seasonsProgressBar.place(x = 25, y = 100); self.seasonsProgressBar.set(0)
        self.seasonLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.seasonLabel.place(x = 175, y = 100)

        self.currentSeasonSet = self.springSeasonSet

        #



        self.rainLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.rainLabel.place(x = 25, y = 175)
        self.rainLabalBackground = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 225); self.rainLabalBackground.place(x = 25, y = 225)
        self.rainSlider = ctk.CTkSlider(self.environmentSettingsFrame, width = 30, height = 205, from_ = 0, to = 4, corner_radius = 0, border_width = 0, orientation = 'vertical', number_of_steps = 4, hover = FALSE)
        self.rainSlider.place(x = 35, y = 235); self.rainSlider.set(0)

        self.wildlifeLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.wildlifeLabel.place(x = 100, y = 175)
        self.wildlifeLabalBackground = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 225); self.wildlifeLabalBackground.place(x = 100, y = 225)
        self.wildlifeSlider = ctk.CTkSlider(self.environmentSettingsFrame, width = 30, height = 205, from_ = 0, to = 4, corner_radius = 0, border_width = 0, orientation = 'vertical', number_of_steps = 4, hover = FALSE, progress_color = '#005c12')
        self.wildlifeSlider.place(x = 110, y = 235); self.wildlifeSlider.set(0)



        self.ratingLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = '', width = 50, height = 50)
        self.ratingLabel.place(x = 175, y = 175)
        self.ratingProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 50, height = 225, corner_radius = 0, border_width = 10, orientation = 'vertical')
        self.ratingProgressBar.place(x = 175, y = 225); self.ratingProgressBar.set(0)

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
        self.temperatureProgressBar.set(random.randint(self.currentSeasonSet[2][0], self.currentSeasonSet[2][1])/100)

    # Make The Game Screen Shop Frame
    def gameScreenShop(self):
        self.shopFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 250)
        self.shopFrame.grid(row = 1, column = 0)
        self.shopBackgroundImageLabel = ctk.CTkLabel(self.shopFrame, text = 'Shop Background Image Here', width = 500, height = 250, fg_color = 'green', bg_color = 'green')
        self.shopBackgroundImageLabel.place(x = 0, y = 0)

        #

    # Make The Game Screen Menu Settings Frame
    def gameScreenMenuSettings(self):
        self.menuSettingsFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 250)
        self.menuSettingsFrame.grid(row = 1, column = 1)
        self.menuSettingsBackgroundImageLabel = ctk.CTkLabel(self.menuSettingsFrame, text = 'Menu Settings Background Image Here', width = 500, height = 250, fg_color = 'light green', bg_color = 'light green')
        self.menuSettingsBackgroundImageLabel.place(x = 0, y = 0)

        #


    # Handles The Game Time
    def timeSettings(self):
        self.screen.blit(self.timeSurface, (0, 0))

        self.dayNightCycleProgressBar.step()
        self.seasonsProgressBar.step()

        self.timeSurface.fill((self.currentTime[1])); self.timeSurface.set_alpha(120)

        if (self.progressBarToInt(self.dayNightCycleProgressBar) < 10):
            if self.currentTime == self.timesSet[0]: return
            self.currentTime = self.timesSet[0]
            self.temperatureProgressBar.set(random.randint(self.currentSeasonSet[2][0], self.currentSeasonSet[2][1])/100)
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
            self.currentTime = self.timesSet[5]
            self.temperatureProgressBar.set(random.randint(self.currentSeasonSet[3][0], self.currentSeasonSet[3][1])/100)
        elif (60 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 70):
            if self.currentTime == self.timesSet[6]: return
            self.currentTime = self.timesSet[6]
        elif (70 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 80):
            if self.currentTime == self.timesSet[7]: return
            self.currentTime = self.timesSet[7]
        elif (80 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 90):
            if self.currentTime == self.timesSet[8]: return
            self.currentTime = self.timesSet[8]
        elif (90 <= self.progressBarToInt(self.dayNightCycleProgressBar) < 100):
            if self.currentTime == self.timesSet[9]: return
            self.currentTime = self.timesSet[9]
        
        self.timeLabel.configure(image = ctk.CTkImage(Image.open(self.currentTime[0]), size=(44 , 44)))
        self.dayNightCycleProgressBar.configure(progress_color = self.currentTime[1])
    
    # Handles Season Chnages
    def seasonSettings(self):
        if self.progressBarToInt(self.seasonsProgressBar) < 25:
            if self.currentSeasonSet != self.springSeasonSet: self.currentSeasonSet = self.springSeasonSet; self.changeSeasonSet = True
        elif self.progressBarToInt(self.seasonsProgressBar) < 50:
            if self.currentSeasonSet != self.summerSeasonSet: self.currentSeasonSet = self.summerSeasonSet; self.changeSeasonSet = True
        elif self.progressBarToInt(self.seasonsProgressBar) < 75:
            if self.currentSeasonSet != self.fallSeasonSet: self.currentSeasonSet = self.fallSeasonSet; self.changeSeasonSet = True
        else:
            if self.currentSeasonSet != self.winterSeasonSet: self.currentSeasonSet = self.winterSeasonSet; self.changeSeasonSet = True

        if self.changeSeasonSet == True:
            self.seasonsProgressBar.configure(progress_color = self.currentSeasonSet[1][2], border_color = self.currentSeasonSet[1][0])
            self.seasonLabel.configure(image = ctk.CTkImage(Image.open(self.currentSeasonSet[0]), size=(50 , 50))) # 44, 44 for other label borders
            for child in self.environmentSettingsFrame.children.values():
                if isinstance(child, ctk.CTkLabel): child.configure(fg_color = self.currentSeasonSet[1][0])
                elif isinstance(child, ctk.CTkProgressBar): child.configure(border_color = self.currentSeasonSet[1][0])
                elif isinstance(child, ctk.CTkSlider): child.configure(bg_color = self.currentSeasonSet[1][0])
            self.environmentSettingsBackgroundImageLabel.configure(fg_color = self.currentSeasonSet[1][1])
            if self.currentSeasonSet == self.winterSeasonSet:
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
            if self.gameVariables.get(current) == self.gameVariables.get(set)[0]: return
            self.gameVariables[current] = self.gameVariables.get(set)[0]
        elif (slider.get() == 1):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[1]: return
            self.gameVariables[current] = self.gameVariables.get(set)[1]
        elif (slider.get() == 2):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[2]: return
            self.gameVariables[current] = self.gameVariables.get(set)[2]
        elif (slider.get() == 3):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[3]: return
            self.gameVariables[current] = self.gameVariables.get(set)[3]
        elif (slider.get() == 4):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[4]: return
            self.gameVariables[current] = self.gameVariables.get(set)[4]
        elif (slider.get() == 5):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[5]: return
            self.gameVariables[current] = self.gameVariables.get(set)[5]

        label.configure(image = ctk.CTkImage(Image.open(self.gameVariables[current][0]), size=(44 , 44)))
        slider.configure(button_color = self.gameVariables[current][1])
        
    # Handles The Game Rating System
    def ratingSettings(self):
        #self.ratingProgressBar.step()
        self.progressBarSettings(self.ratingProgressBar, 'currentRating', 'ratingsSet', self.ratingLabel)
    
    # Handles The Game Humidity
    def humiditySettings(self):
        #self.humidityProgressBar.step()
        if self.gameVariables.get('currentWeather') != self.gameVariables.get('currentWeatherSet')[0]:
            self.humidityProgressBar.set(self.humidityProgressBar.get() + (self.gameVariables.get('currentWeather')[2]/100))
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
            if self.gameVariables.get(current) == self.gameVariables.get(set)[0]: return
            self.gameVariables[current] = self.gameVariables.get(set)[0]
        elif (0 < self.progressBarToInt(progressBar) <= 20):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[1]: return
            self.gameVariables[current] = self.gameVariables.get(set)[1]
        elif (20 < self.progressBarToInt(progressBar) <= 40):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[2]: return
            self.gameVariables[current] = self.gameVariables.get(set)[2]
        elif (40 < self.progressBarToInt(progressBar) <= 60):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[3]: return
            self.gameVariables[current] = self.gameVariables.get(set)[3]
        elif (60 < self.progressBarToInt(progressBar) <= 80):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[4]: return
            self.gameVariables[current] = self.gameVariables.get(set)[4]
        elif (80 < self.progressBarToInt(progressBar) <= 100):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[5]: return
            self.gameVariables[current] = self.gameVariables.get(set)[5]
        elif (self.progressBarToInt(progressBar) == 100):
            if self.gameVariables.get(current) == self.gameVariables.get(set)[6]: return
            self.gameVariables[current] = self.gameVariables.get(set)[6]

        label.configure(image = ctk.CTkImage(Image.open(self.gameVariables[current][0]), size=(44 , 44)))
        progressBar.configure(progress_color = self.gameVariables[current][1])

    # Test function for plant Growth based on Counter
    def TESTINGPLANTGROWTH(self):
        global counter
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

    # Main Pygame Game Loop
    def pygameLoop(self):
        self.screen.fill((255, 255, 255))

        #pygame.draw.circle(self.screen, 'green', (250, 250), 125)
        self.TESTINGPLANTGROWTH()


        self.timeSettings()
        self.seasonSettings()
        self.rainSettings()
        self.wildlifeSettings()
        self.ratingSettings()
        self.humiditySettings()
        self.nutrientSettings()
        self.temperatureSettings()
        pygame.display.flip()
        if self.inGame == True:
            self.root.update()  
            self.root.after(500, self.pygameLoop)


    
# Starts The Game Start Up
gameInstance = EcoQuest()
gameInstance.mainloop()


















