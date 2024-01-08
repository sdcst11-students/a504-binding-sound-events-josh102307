import tkinter as tk
from tkinter import *
import playsound
import pygame

def play_sound1():
   pygame.mixer.music.load("error_CDOxCYm.mp3")
   pygame.mixer.music.play()

def play_sound2():
   pygame.mixer.music.load("vine-boom.mp3")
   pygame.mixer.music.play()

def play_sound3():
   pygame.mixer.music.load("tmp_7901-951678082.mp3")
   pygame.mixer.music.play()

def play_sound4():
   pygame.mixer.music.load("y2mate_VKI8qDn.mp3")
   pygame.mixer.music.play()

window = tk.Tk()
window.title("Soundboard")
window.geometry("500x500")

pygame.mixer.init()


b1 = tk.Button(window, text="sound1", command=play_sound1)
b1.pack(pady=30)

b2 = tk.Button(window, text="sound2", command=play_sound2)
b2.pack(pady=30)

b3 = tk.Button(window, text="sound3", command=play_sound3)
b3.pack(pady=30)

b4 = tk.Button(window, text="sound4", command=play_sound4)
b4.pack(pady=30)


window.mainloop()