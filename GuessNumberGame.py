#!/usr/bin/python3

from tkinter import messagebox
import functools
import tkinter
import random
import os

# Easy level: 15 numbers
# Medium level: 25 numbers
# Hard level: 35 numbers

class Game:
	def __init__(self):
		self.victories = 0
		self.failures = 0
		self.vic_alerts = ["You are very good!", "Super!", "Yeah, you got it!"]
		self.fai_alerts = ["Nope!", "Wrong!", "You're wrong!"]
		self.levels = ["Easy", "Medium", "Hard1"]

	def menu(self):
		self.window = tkinter.Tk()
		self.window.title("GuessNumberGame")
		self.window.geometry("300x120")

		frame = tkinter.Frame(master=self.window)
		frame.pack()

		label = tkinter.Label(master=frame,text="Select a game level")
		label.pack()

		easy_button = tkinter.Button(master=frame,text="Easy",command=functools.partial(Game.run,self,"easy"))
		easy_button.pack()

		medium_button = tkinter.Button(master=frame,text="Medium",command=functools.partial(Game.run,self,"medium"))
		medium_button.pack()

		hard_button = tkinter.Button(master=frame,text="Hard",command=functools.partial(Game.run,self,"hard"))
		hard_button.pack()

		self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)
		self.window.mainloop()

	def run(self,level):
		self.window.destroy()
		if level == "easy":
			self.max = 15
		elif level == "medium":
			self.max = 25
		elif level == "hard":
			self.max = 35
		self.number = random.randint(1,self.max)
		self.chances = 0
		print(f"Guess a number between 1 and {self.max}.")

		while self.chances < 5:
			self.guess = int(input("Enter your guess:"))
			if self.guess == self.number:
				self.alert = random.choice(self.vic_alerts)
				self.victories += 1
				print("You won: ", self.victories, " times")
				print("You logst: ", self.failures, " times")
				Game.restart(self)
			elif self.guess < self.number:
				print("Your guess was too low")
			else:
				print("Your guess was to high")
			self.chances += 1
			print("Chances left: ", 5-self.chances)

	def restart(self):
		# Tkinter messagebox returns True if 'yes' and False if 'no'
		choice = tkinter.messagebox.askyesno(self.alert, "Play again?")
		if choice:
			os.system("clear")
			Game.menu(self)
		else:
			messagebox.showinfo("GuessNumberGame","Thanks for playing this game!")
			exit()

try:
	game = Game()
	game.menu()
except KeyboardInterrupt:
	print("User interrupted the program. Exiting...")
	exit()
