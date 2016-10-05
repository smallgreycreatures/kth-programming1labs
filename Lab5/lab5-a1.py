from frans_tv import TV 
import os


def find_file(file_name, file_path):
	return os.path.exists(file_path+"/"+file_name)


def user_input_int_handler(prompt, upper_lim, lower_lim):
	while True:
		try:
			user_input = int(input(prompt))
			if user_input < upper_lim and user_input > lower_lim:
				print("Fel val, försök igen: ")
				continue

			return user_input
		except:
			print("Detta är inget heltal, försök igen: ")

def tv_control(name, tv, channels):
	running = True
	while running:
		print(name)
		print("Tv-program:", tv.get_channel().split(':')[1], end="")
		print("Kanal: ", tv.get_channel().split(':')[0])
		print("Ljudvolym: ", tv.get_volume())
		print("1. Byt kanal")
		print("2. Sänk ljudvolym")
		print("3. Höj ljudvolym")
		print("4. Gå till huvudmenyn")
		menu_choice = user_input_int_handler("Välj: ", 1, 4)

		if menu_choice == 1:
			channel_control(tv, channels)
		elif menu_choice == 2:
			lower_volume(tv)
		elif menu_choice == 3:
			raise_volume(tv)
		elif menu_choice == 4:
			running = False

def raise_volume(tv):
	if tv.get_volume() == 10:
		print("Maxvolym")
	else:
		tv.set_volume(tv.get_volume()+1)

def lower_volume(tv):
	if tv.get_volume() == 0:
		print("Minvolym")
	else:
		tv.set_volume(tv.get_volume()-1)

def channel_control(tv, channels):
	i = 0
	while i < len(channels):
		print((i+1), channels[i])
		i+=1
	channel = user_input_int_handler("Välj: ", 1, 4)
	tv.set_channel(channels[channel-1])

def save_to_file(tv_1, tv_2):
	tv_1_str = "#\n" + "!"+ tv_1.get_channel() +"\n" + "?" + str(tv_1.get_volume()) + "\n"
	tv_2_str = "#\n" +"!"+ tv_2.get_channel() +"\n" +"?"+ str(tv_2.get_volume()) + "\n"
	file = open("tv.txt", "w")
	file.write(tv_1_str + tv_2_str)
	file.close()	

def read_tv_file(tv_list):
	file = open("tv.txt", "r")
	lines = file.readlines()
	file.close()

	tv_list_counter = -1
	for line in lines:
		if "#" in line:
			tv_list_counter +=1
		elif line.startswith("!"):
			tv_list[tv_list_counter].set_channel(line.split("!")[1])
		elif line.startswith("?"):
			tv_list[tv_list_counter].set_volume(int(line.split("?")[1]))

def tv_simulator():
	
	channels = ["MTv: Music is life", "Tv 3: Har du tur i kärlek?","Svt 1: Pengar är inte allt","Kanal 4: Vem vill inte bli miljonär?"]
	tv_1 = TV(1,1,channels)
	tv_2 = TV(1,1,channels)
	if not find_file("tv.txt", os.path.dirname(os.path.abspath(__file__))):
		tv_1 = TV(1,1,channels)
		tv_2 = TV(1,1,channels)
	else:
		tv_list = [tv_1, tv_2]
		read_tv_file(tv_list)


	running = True

	while (running):
		print("***Välkommen till TV-simulatorn, vi har två TV-apparater som kan användas i simuleringen****")
		print("1. VardagsrumsTV")
		print("2. Köks TV")
		print("3. Avsluta")
		menu_choice = user_input_int_handler("Välj: ", 0, 3)

		if menu_choice == 1:
			tv_control("VardagsrumsTV", tv_1, channels)
		elif menu_choice == 2:
			tv_control("Köks TV", tv_2, channels)
		elif menu_choice == 3:
			save_to_file(tv_1, tv_2)
			running = False


tv_simulator()