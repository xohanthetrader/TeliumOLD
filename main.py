import random
from PIL import Image

# Variables

num_modules = 17
module = 1
last_module = 0
possible_moves = []
alive = True
won = False
power = 50
fuel = 500
locked = 0 #Locked module
queen = 0
vent_shafts = []
info_panels = 0
workers = [0]
image_path = "map.png"

#Procedures
def load_module():
	global module, possible_moves
	possible_moves = get_modules_from(module)
	output_module()

def get_modules_from(module):
	moves = []
	text_file = open("Charles_Darwin/module" + str(module) + ".txt","r")
	for counter in range(0,4):
		move_read = text_file.readline()
		move_read = int(move_read.strip())
		if move_read != 0:
			moves.append(move_read)
	text_file.close()
	return moves

def output_module():
	global module
	print(f"\n ---------------------------------------- \n You are in module {module} \n")

def output_moves():
	global possible_moves
	print("\n From here you can move to modues: |",end = "")
	for  move in possible_moves:
		print(move,"| ",end = "")
	print()

def get_action():
	global module,last_module,possible_moves,power
	valid_action = False
	while not valid_action:
		print("What do you want to do next ? (MOVE, SCANNER)")
		action = sanitize(input(">"))
		if action[0] == "MOVE":
			if action[1] != 0:
				move = action[1]	
			else:
				move = int(input("What module do you want to move to: "))
		if move in possible_moves:
			valid_action = True
			last_module = module
			module = move
				
		else:
			print("The module must be connected to the current module")
	power -= 1

def check_power():
	global alive
	if power <= 0:
		alive = False

def sanitize(input):
	inputs = input.split()
	if "M" in inputs[0].upper():
		inputs[0] = "MOVE"	
	try:
		inputs[1] = int(inputs[1])
	except:
		inputs.append(0)
	return inputs
	
#Main

img = Image.open(image_path)
print("Do you wish to see a map? y/[n]")
want_image = input(">")
if want_image == "y":
	img.show()

while alive and not won:
	load_module()
	check_power()
	if (not won) and alive:
		output_moves()
		get_action()

if won:
	print("The queen is trapped and you burnt it with your flamethrower \n Game over you win")
	img.close()
if not alive:
	print("Station has run out of power No life supprt you die")
	img.close()