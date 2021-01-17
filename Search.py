import pyautogui as p 
import webbrowser as w 
import time


def googleSearch():
	#Taking input from user 
	x = input("Search: ") 

	#Delay for stability 
	time.sleep(0.1) 
	w.open('www.google.co.uk') 

	#Presses enter 
	p.press('enter') 

	#Waits for browser to load, change for internet speed
	time.sleep(0.3)

	#Types the input provided 
	p.write(x) 

	#Delay for stability 
	time.sleep(0.1)

	#Presses enter 
	p.press('enter')

	time.sleep(1)

googleSearch()


