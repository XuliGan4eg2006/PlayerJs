import glob, os
import json
from termcolor import colored	

print(colored("""  ____     _      """, "green"))
print(colored(""" |  _ \   | |___  """, "green"))
print(colored(""" | |_) |  | / __| """, "green"))
print(colored(""" |  __/ |_| \__ \ """, "green"))
print(colored(""" |_|   \___/|___/ """, "green"))
print(colored("""                  """, "green"))
print(colored("""           by XuliGan4eg2006""", "green"))

print(colored("Wait....", "yellow"))

massiv = []

print(colored("You need link to your website with already loaded tracks in the folder. Required https!", "red"))
answer = input("Please, paste link to your website. Example: https://muzon.herokuapp.com/songs/: ")

for file in glob.glob("*.mp3"):
	massiv.append(str(file))

for i, v in enumerate(massiv):
    massiv[i] = {"title": v, "file": answer + v}
with open('result.json', 'w') as outfile:
	json.dump(massiv, outfile)

print(colored("All ready! Then go to https://playerjs.com/ and make your player. In the File column enter the contents of the file 'result.json' and have a nice day!", "green"))