#Task-1 : Optimization of Code
import os
import pyttsx3
pyttsx3.speak("This is Technical Assistant service named as Krypton")
pyttsx3.speak("How may I help you sir")

while True:
	print(r"Chat with me with your requirements:",end='')
	p=input()

	if (('run' in p) or ('execute' in p)) and (('notepad' in p) or ('editor' in p)):
		os.system("notepad")		 

	elif ('run' in p) and ('player' in p) and ('media' in p):
		os.system("wmplayer")

	elif ('run' in p) and ('chrome' in p):
  		os.system("chrome")

	elif ('run' in p) and (('microsoft' in p) or ('edge' in p)):
		os.system("msedge")

	elif ("run" in p) and (("codeblocks") or ("compiler")):
		os.system("codeblocks")	
	
	elif ("run" in p) and (("vlc player") or ("music player")):
		os.system("vlc")	

	elif ("exit" in p) or ("quit" in p):
		pyttsx3.speak("Thanks for using Krypton")
		break
	  		
	else:
		print("Sorry! We dont support your choice try different choice")
