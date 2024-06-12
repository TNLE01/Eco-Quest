# Author: Truong Le

import pygame, random, time, datetime, os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image
from images import *
import customtkinter as ctk

class EcoQuest():

    def __init__(self):

        self.root = Tk()
        self.root.title("Eco Quest")
        self.root.iconphoto(False, tk.PhotoImage(file = ecoQuestIcon))

        self.root.geometry("1250x750")
        self.root.minsize(width = 1250, height = 750)
        self.root.maxsize(width = 1250, height = 750)

        self.piccc = ImageTk.PhotoImage(Image.open(ecoQuestIcon))
        self.pictest = Image.open(ecoQuestIcon)
        self.buttonBackgroundimage = Image.open(buttonBackground)
        self.bgrez = ImageTk.PhotoImage(self.buttonBackgroundimage.resize((100, 50)))
        self.my_image = ctk.CTkImage(Image.open(buttonBackground))
        self.play_Image = ImageTk.PhotoImage(Image.open(playImage))

        self.extraCommandsList = []
        self.inGame = False

        self.mainMenu()
       # self.gameScreen()


    def mainloop(self):
        self.root.mainloop()

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

    def buttonStateSettings(self, buttonState, *args):
        for ar in args:
            ar.configure(state = buttonState)



    def playButtonFrame(self, buttonState):
        if buttonState == DISABLED:
            self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton)
        if buttonState == NORMAL:
            self.buttonStateSettings(DISABLED, self.yesButtonPlayFrame, self.noButtonPlayFrame)
            self.movingFrame(2, self.playChoiceFrame, 525, 325, 525, 0 - self.playChoiceFrame.winfo_reqheight(), 0, 0.5, 1, lambda: self.playChoiceFrame.destroy(), lambda: self.buttonStateSettings(buttonState, self.playButton, self.howToPlayButton, self.settingsButton, self.exitButton))
            return

        self.playChoiceFrame = ctk.CTkFrame(self.mainMenuFrame, width = 200, height = 100, fg_color = "red", bg_color = 'red', corner_radius = 0)
        self.backgroundImagePlayFrame = ctk.CTkImage(Image.open(buttonBackground), size=(200 , 100))
        self.backgroundImageLabelPlayFrame = ctk.CTkLabel(self.playChoiceFrame, image = self.backgroundImagePlayFrame, text = '')
        self.backgroundImageLabelPlayFrame.grid(column = 0, row = 0)

        self.playQuestionLabel = ctk.CTkLabel(self.playChoiceFrame, text = 'Play?', width = 200, height = 25, bg_color = 'transparent', fg_color = 'transparent')
        self.playQuestionLabel.place(x = 0, y = 0)
        self.yesButtonPlayFrame = ctk.CTkButton(self.playChoiceFrame, state = DISABLED, text = 'Yes', width = 50, height = 50, corner_radius = 0, command = self.gameScreen)
        self.yesButtonPlayFrame.place(x=25, y=25)
        self.noButtonPlayFrame = ctk.CTkButton(self.playChoiceFrame, state = DISABLED, text = 'No', width = 50, height = 50, corner_radius = 0, command = lambda: self.playButtonFrame(NORMAL))
        self.noButtonPlayFrame.place(x=125, y=25)

        self.movingFrame(0, self.playChoiceFrame, 525, 0, 525, 325, 0, 0.5, 1, lambda: self.buttonStateSettings(NORMAL, self.yesButtonPlayFrame, self.noButtonPlayFrame))
    
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

    def extraCommandsHandling(self):
        if(len(self.extraCommandsList)) != 0:
            for i in self.extraCommandsList: self.root.after(100, i)
            self.extraCommandsList = []


    def progressBarToInt(self, progressBar):
        return int(progressBar.get() * 100)


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




    def gameScreenPlantPlacement(self):
        self.plantPlacementFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 500)
        self.plantPlacementFrame.grid(row = 0, column = 0)
        self.plantPlacementBackgroundImageLabel = ctk.CTkLabel(self.plantPlacementFrame, text = 'Plant Placement Background Image Here', width = 500, height = 500, fg_color = 'red', bg_color = 'red')
        self.plantPlacementBackgroundImageLabel.place(x = 0, y = 0)

        #


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

    
    def gameScreenEnvironmentSettings(self):
        self.environmentSettingsFrame = ctk.CTkFrame(self.gameScreenFrame, width = 250, height = 750)
        self.environmentSettingsFrame.grid(row = 0, column = 2, rowspan = 2)
        self.environmentSettingsBackgroundImageLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = 'Environment Settings Background Image Here', width = 250, height = 750, fg_color = 'purple', bg_color = 'purple')
        self.environmentSettingsBackgroundImageLabel.place(x = 0, y = 0)

        #
        self.dayNightCycleProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 150, height = 50, corner_radius = 0, progress_color = 'blue', determinate_speed = 1, border_width = 10)
        self.dayNightCycleProgressBar.place(x = 25, y = 25)
        self.dayNightCycleProgressBar.set(0)
        self.timeLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = 'Time', width = 50, height = 50)
        self.timeLabel.place(x = 175, y = 25)

        self.seasonsProgressBar = ctk.CTkProgressBar(self.environmentSettingsFrame, width = 150, height = 50, corner_radius = 0, progress_color = 'light blue', determinate_speed = 0.1, border_width = 10)
        self.seasonsProgressBar.place(x = 25, y = 100)
        self.seasonsProgressBar.set(0)
        self.seasonLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = 'Seasons', width = 50, height = 50)
        self.seasonLabel.place(x = 175, y = 100)

        self.rainLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = 'Rain', width = 50, height = 50)
        self.rainLabel.place(x = 25, y = 175)
        self.rainSlider = ctk.CTkSlider(self.environmentSettingsFrame, width = 50, height = 200, from_ = 0, to = 5, corner_radius = 0, border_width = 25, orientation = 'vertical', number_of_steps = 5)
        self.rainSlider.place(x = 25, y = 225)

        self.wildlifeLabel = ctk.CTkLabel(self.environmentSettingsFrame, text = 'Wildlife', width = 50, height = 50)
        self.wildlifeLabel.place(x = 100, y = 175)
        self.wildlifeSlider = ctk.CTkSlider(self.environmentSettingsFrame, width = 50, height = 200, from_ = 0, to = 5, corner_radius = 0, border_width = 25, orientation = 'vertical', number_of_steps = 5)
        self.wildlifeSlider.place(x = 100, y = 225)

        self.ratingProgressBar = ctk.CTkLabel(self.environmentSettingsFrame, text = 'Rating', width = 50, height = 50)
        self.ratingProgressBar.place(x = 175, y = 175)
        self.ratingProgressBar = ctk.CTkSlider(self.environmentSettingsFrame, width = 50, height = 200, from_ = 0, to = 5, corner_radius = 0, border_width = 25, orientation = 'vertical', number_of_steps = 5)
        self.ratingProgressBar.place(x = 175, y = 225)



    def gameScreenShop(self):
        self.shopFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 250)
        self.shopFrame.grid(row = 1, column = 0)
        self.shopBackgroundImageLabel = ctk.CTkLabel(self.shopFrame, text = 'Shop Background Image Here', width = 500, height = 250, fg_color = 'green', bg_color = 'green')
        self.shopBackgroundImageLabel.place(x = 0, y = 0)

        #



    def gameScreenMenuSettings(self):
        self.menuSettingsFrame = ctk.CTkFrame(self.gameScreenFrame, width = 500, height = 250)
        self.menuSettingsFrame.grid(row = 1, column = 1)
        self.menuSettingsBackgroundImageLabel = ctk.CTkLabel(self.menuSettingsFrame, text = 'Menu Settings Background Image Here', width = 500, height = 250, fg_color = 'light green', bg_color = 'light green')
        self.menuSettingsBackgroundImageLabel.place(x = 0, y = 0)

        #


    def timeCycle(self):
        self.screen.blit(self.timeSurface, (0, 0))
        self.dayNightCycleProgressBar.step()
        if self.progressBarToInt(self.dayNightCycleProgressBar) < 25: self.dayNightCycleProgressBar.configure(progress_color = 'light yellow'); self.timeSurface.fill(('light yellow')); self.timeSurface.set_alpha(120)
        elif self.progressBarToInt(self.dayNightCycleProgressBar) < 50: self.dayNightCycleProgressBar.configure(progress_color = 'yellow'); self.timeSurface.fill(('yellow')); self.timeSurface.set_alpha(120)
        elif self.progressBarToInt(self.dayNightCycleProgressBar) < 75: self.dayNightCycleProgressBar.configure(progress_color = 'gold'); self.timeSurface.fill(('gold')); self.timeSurface.set_alpha(120)
        else: self.dayNightCycleProgressBar.configure(progress_color = 'black'); self.timeSurface.fill(('black')); self.timeSurface.set_alpha(120)
        self.seasonsProgressBar.step()
        if self.progressBarToInt(self.seasonsProgressBar) < 25: self.seasonsProgressBar.configure(progress_color = 'gray')
        elif self.progressBarToInt(self.seasonsProgressBar) < 50: self.seasonsProgressBar.configure(progress_color = 'yellow')
        elif self.progressBarToInt(self.seasonsProgressBar) < 75: self.seasonsProgressBar.configure(progress_color = 'brown')
        else: self.seasonsProgressBar.configure(progress_color = 'white')

    def pygameWeather(self):
        return

    def pygameLoop(self):
        self.screen.fill((255, 255, 255))

        pygame.draw.circle(self.screen, 'green', (250, 250), 125)

        self.timeCycle()
        self.pygameWeather()
        pygame.display.flip()
        if self.inGame == True:
            self.root.update()  
            self.root.after(100, self.pygameLoop)


    

gameInstance = EcoQuest()
gameInstance.mainloop()


















