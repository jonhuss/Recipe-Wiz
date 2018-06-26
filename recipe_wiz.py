#!/usr/bin/env python2.7
# A CLI app for storing recipes
import os, sys

header = "\
  _____           _             __          ___     \n\
 |  __ \         (_)            \ \        / (_)    \n\
 | |__) |___  ___ _ _ __   ___   \ \  /\  / / _ ____\n\
 |  _  // _ \/ __| | '_ \ / _ \   \ \/  \/ / | |_  /\n\
 | | \ \  __/ (__| | |_) |  __/    \  /\  /  | |/ / \n\
 |_|  \_\___|\___|_| .__/ \___|     \/  \/   |_/___|\n\
                   | |                              \n\
                   |_|								\n"

colors = {
	'blue': '\033[94m',
	'pink': '\033[95m',
	'green': '\033[92m',
}

# Colors text
def colorize(string, color):
	if not color in colors: 
		return string
	return colors[color] + string + '\033[0m'

# Creates a new recipe when called
def new_recipe():
	name = raw_input("Enter recipe name: ")
	filename = name + ".txt"

	recipe = open(filename, "w")

	# Create a list of ingredients and write them to file
	ingredients = []

	while True:
		ingredient = raw_input("Enter ingredient(s) (done to quit): ")

		if ingredient.lower() == "done":
			break
		else:
			ingredients.append(ingredient)
			ingredients.append("\n")

	recipe.writelines(ingredients)

	# Create a list of coooking steps and write them to file
	steps = []

	while True:
		step = raw_input("Enter cooking step(s) (done to quit): ")
		
		if step.lower() == "done":
			break
		else:
			steps.append(step)
			steps.append("\n")

	recipe.writelines(steps)

	print "New recipe added!"
	raw_input("Press [Enter] to continue...")

# Shows existing recipes
# TODO: add functionality
def list_recipes():
	print "Recipe 1"
	raw_input("Press [Enter] to continue...")

# Deletes recipe(s)
# TODO: add functionality
def delete_recipe():
	print "Recipe deleted!"
	raw_input("Press [Enter] to continue...")

# Exit program
def exit():
	sys.exit()

menu_items = [
	{"New recipe": new_recipe},
	{"List recipes": list_recipes},
	{"Delete recipe": delete_recipe},
	{"Exit": exit},
]

def main():
	while True:
		os.system('cls')

		# Print ASCII art
		print colorize(header, 'pink')
		print colorize('version 0.1\n', 'green')
		# Iterate over menu array and print index and menu text
		for item in menu_items:
			print colorize("[" + str(menu_items.index(item)) + "]", 'blue') + item.keys()[0]

		choice = raw_input(">> ")

		try:
			if int(choice) < 0:
				 raise ValueError
			# Call the matching function
			menu_items[int(choice)].values()[0]()
		except (ValueError, IndexError):
			pass

if __name__ == "__main__":
	main()