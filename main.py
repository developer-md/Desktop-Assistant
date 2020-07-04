import speech_recognition as sr                        #for taking input from microphone and recognize it
import datetime                                        #for date time 
import random                                          #for choosen random values from given values
import webbrowser                                      #for open and access web
import wikipedia                                       #for access wikipedia
import os                                              #for access files 
import pyaudio                                         #for taking input from microphone
import pyttsx3                                         #for converting text into speech
import smtplib                                         #for sending mail
import tkinter as tk                                   #for creating GUI
from PIL import Image, ImageTk                         #for GUI
from tkinter import Menu,Label,Button,Entry,Scrollbar,messagebox  #for GUI
import time                                            #for access wait function
import keyboard                                        #enter auto input
import pyautogui                                       #control keyboard automatic
#from selenium import webdriver 
#from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC 
#from selenium.webdriver.common.keys import Keys 
#from selenium.webdriver.common.by import By
import pywhatkit                                        #for accessing youtube and whatsapp

#making instance of pyttsx3
en=pyttsx3.init()  
en.setProperty('rate',180)

#getting details of current voice
voices = en.getProperty('voices')       

#changes voices. o for male
#en.setProperty('voice', voices[0].id)  

#changes voices. 1 for female
en.setProperty('voice', voices[1].id)   

#global vairiables
global email
global password

#dictionary of mail addresses
mail={"jyoti":"jyotiverma0900@gmail.com",
"md":"mmr78621@gmail.com",
"shubham":"shubhamg3010@gmail.com"}

#dictionary of whatsapp contacts
contacts={"jyoti":"+918950299032",
"shubham":"+919313632443",
"md":"+919599628951"}


#speak function which speak the text comes in it.
def speak(audio):
    en.say(audio)
    en.runAndWait()

def Ex():
	exit()




#take funtion record your audio and return back to in form of text
def take():
	r= sr.Recognizer()
	with sr.Microphone() as source:
		speak("speak up")
		print("Listening.....")
		r.adjust_for_ambient_noise(source, duration=1)
		r.pause_threshold=1
		audio = r.listen(source)
	try:
		print("recognizing..")
		qr= r.recognize_google(audio)
		print(qr)
	except Exception as e:
		print(e)
		speak("sorry, say that again please..")
		return "None"
	return qr

#function for destroying GUI
def quit():
	global email
	global password
	email=e.get()
	password=e1.get()
	if email=="" or password=="":
		messagebox.showerror('Error','Oops enter mail & password')
	else:
		root.destroy()


#function for Help GUI
def aboutme():
    rot=tk.Tk()
    rot.title("panda-the assistant app")
    rot.geometry("1300x900")
    rot.resizable(0,0)
    rot.config(background="white")
    scrollbar = Scrollbar(rot)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    l4=Label(rot,text="                           Commands                                                                    Description",font=("Times",15,"bold"),bg="white")
    l4.pack(anchor=tk.W,pady=(10,0))
    l5=Label(rot,text="                              name                                                                     tell own name",font=("Times",15),bg="white")
    l5.pack(anchor=tk.W,padx=(10,0))
    l6=Label(rot,text="                          open google                                                           open google for you",font=("Times",15),bg="white")
    l6.pack(anchor=tk.W,padx=(10,0))
    l7=Label(rot,text="                          open youtube                                                         open youtube for you",font=("Times",15),bg="white")
    l7.pack(anchor=tk.W,padx=(10,0))
    l8=Label(rot,text="                       wikipedia -------                                            search wikipedia, eg:wikipedia dogs",font=("Times",15),bg="white")
    l8.pack(anchor=tk.W,padx=(10,0))
    l9=Label(rot,text="                              search                                                               search anything in google",font=("Times",15),bg="white")
    l9.pack(anchor=tk.W,padx=(10,0))
    l10=Label(rot,text="                            location                                                              find any location on map",font=("Times",15),bg="white")
    l10.pack(anchor=tk.W,padx=(10,0))
    l11=Label(rot,text="                           yourself                                                                     tell about herself",font=("Times",15),bg="white")
    l11.pack(anchor=tk.W,padx=(10,0))
    l12=Label(rot,text="                              time                                                                        tell current time",font=("Times",15),bg="white")
    l12.pack(anchor=tk.W,padx=(10,0))
    l13=Label(rot,text="                        how are you                                                                 talk about herself",font=("Times",15),bg="white")
    l13.pack(anchor=tk.W,padx=(10,0))
    l14=Label(rot,text="                        play music                                             play music for you, songs must be here D:/song",font=("Times",15),bg="white")
    l14.pack(anchor=tk.W,padx=(10,0))
    l15=Label(rot,text="                          notepad                                                     open notepad & ask for writing something",font=("Times",15),bg="white")
    l15.pack(anchor=tk.W,padx=(10,0))
    l16=Label(rot,text="                          my computer                                                                open my computer",font=("Times",15),bg="white")
    l16.pack(anchor=tk.W,padx=(10,0))
    l17=Label(rot,text="                          month                                                                         tell current month name",font=("Times",15),bg="white")
    l17.pack(anchor=tk.W,padx=(10,0))
    l18=Label(rot,text="                          mail                                                                                  send Email",font=("Times",15),bg="white")
    l18.pack(anchor=tk.W,padx=(10,0))
    l19=Label(rot,text="                          shutdown                                                                   shutdown your system",font=("Times",15),bg="white")
    l19.pack(anchor=tk.W,padx=(10,0))
    l20=Label(rot,text="                          restart                                                                          Restart your system",font=("Times",15),bg="white")
    l20.pack(anchor=tk.W,padx=(10,0))
    l21=Label(rot,text="                          day                                                                                  tell today's day",font=("Times",15),bg="white")
    l21.pack(anchor=tk.W,padx=(10,0))
    l22=Label(rot,text="                          exit                                                                                Shutdown herself",font=("Times",15),bg="white")
    l22.pack(anchor=tk.W,padx=(10,0))
    l23=Label(rot,text="                         play in youtube                                                          play anything in youtube",font=("Times",15),bg="white")
    l23.pack(anchor=tk.W,padx=(10,0))
    l24=Label(rot,text="                          use whatsapp                                                         sent messages on whatsapp",font=("Times",15),bg="white")
    l24.pack(anchor=tk.W,padx=(10,0))


#function for show about developer 
def aboutdeveloper():
    about=tk.Tk()
    about.title("panda-the assistant app")
    about.geometry("920x720")
    about.resizable(0,0)
    about.config(background="black")
    label=Label(about,text="Oops!\n404\nNot Found",font=("Times",15,"bold"),bg="black",fg="white")
    label.pack(pady=(200,10))


#function for saving mail and password
def submit():
	global email
	global password
	email=e.get()
	password=e1.get()
	if email=="" or password=="":
		messagebox.showerror('Error','Oops enter mail & password')
	else:
		messagebox.showinfo('success','Added successfully')

def show():
	global email
	global password
	print(email)
	print(password)



#function for sending mail 
def sendemail(to,content):
	global email
	global password
	svr=smtplib.SMTP('smtp.gmail.com',587)
	svr.ehlo()
	svr.starttls()
	svr.login(email,password)
	svr.sendmail(password,to,content)
	svr.close()


#create main GUI
root=tk.Tk()
root.title("panda-the assistant app")
#root.iconbitmap('logo1.ico')
root.geometry("1100x800")
root.resizable(0,0)
root.config(background="white")

#creating menu bar
menubar=Menu(root)

#help option
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About me",command=aboutme)
menubar.add_cascade(label="Help",menu=helpmenu)

#About option
aboutmenu=Menu(menubar,tearoff=0)
aboutmenu.add_command(label="About developer",command=aboutdeveloper)
menubar.add_cascade(label="About",menu=aboutmenu)

#exit option
exitmenu=Menu(menubar,tearoff=0)
exitmenu.add_command(label="Exit",command=Ex)
menubar.add_cascade(label="Exit",menu=exitmenu)

#put menubar in GUI
root.config(menu=menubar)


#main icon at top of GUI
img = ImageTk.PhotoImage(Image.open("icon2.png"))  # PIL solution
l1=Label(root,image=img,border=0)
l1.pack(pady=(10,10))

#label for email
l2=Label(root,text="Email:",border=0,font=("consalis",15),bg="white",fg="black")
l2.pack(pady=(10,10))

#input email
e=Entry(root,width=25,font=("consalis",11),bd=2,insertbackground="black")
e.pack(pady=(10,10))

#label for password
l3=Label(root,text="Password:",border=0,font=("consalis",15),bg="white",fg="black")
l3.pack(pady=(10,10))

#input password
e1=Entry(root,show="*",width=25,font=("consalis",11),bd=2,insertbackground="black")
e1.pack(pady=(10,10))

#button for submit the email and password
b1=Button(text="submit",font=("times",12),command=submit,width=10,border=2,bg="skyblue")
b1.pack(pady=(10,10))


#put a Label
note=Label(root,text="Note: Before you start go in help upper left corner\nbecause after clicking on start it will disapear.",font=("consalis",10),bg="white",fg="red")
note.pack(pady=(10,10))

#create a start button with image
img1 = ImageTk.PhotoImage(Image.open("start2.png"))  # PIL solution
b=Button(text="",image=img1,border=0,command=quit)
b.pack(pady=(30,10))

#put a label
footer=Label(root,text="click to start",border=0,font=("consalis",15),bg="white",fg="blueviolet")
footer.pack(pady=(10,10))

#put a Label
l=Label(root,text="developed by team triangle:",width=100,font=("consalis",20),bg="black",fg="gold")
l.pack(pady=(20,10))


#start GUI
root.mainloop()


command=""


#main loop
while True:
	time.sleep(1)
	command=take().lower()
	if "name" in command or "who are you" in command:
		s=["my name is pandaa","sir, I am pandaa","my names pandaa"]
		hr=int(datetime.datetime.now().hour)
		if hr>=0 and hr<12:
			speak("good morining")
		elif hr>=12 and hr<18:
			speak("good afternoon")
		elif hr>=18 and hr<20:
			speak("good evening")
		else:
			speak("good night")
		speak(random.choice(s))

	elif "open google" in command:
		webbrowser.open("google.com")
		time.sleep(1)
		speak("opening google")
	elif "open youtube" in command:
		webbrowser.open("youtube.com")
		time.sleep(1)
		speak("opening youtube")
	elif "wikipedia" in command:
		command=command.replace("wikipedia","")
		speak("searching wikipedia")
		result=wikipedia.summary(command,sentences=2)
		speak("according to wikipedia")	
		print(result)
		speak(result)
	elif "search" in command:
		speak("what do you want to search for?")
		s=take()
		url='https://google.com/search?q='+s
		webbrowser.get().open(url)
		time.sleep(2)
		speak(f"Here is result what I found for {s}")
	elif "location" in command:
		speak("what do you want to search for?")
		s=take()
		url='https://google.nl/maps/place/'+s+'/&amp;'
		webbrowser.get().open(url)
		time.sleep(3)
		speak(f"Here is result what i found for {s}")
	elif "time" in command:
		time=datetime.datetime.now().strftime("%H:%M:%S")
		speak(f"sir, the time is {time}")
	elif "day" in command:
		d=datetime.datetime.now().strftime("%A")
		speak(f"Today is {d}")
	elif "date" in command:
		c=datetime.datetime.now().strftime("%d")
		v=datetime.datetime.now().strftime("%B")
		speak(f"Today's date is {c}")
		speak(v)
	elif "month" in command:
		m=datetime.date.now().strftime("%B")
		speak(f"month is {m}")
	elif "yourself" in command:
		speak("hello sir, my name is pandaa. I'am your personal assistant. I'am developed by developer MD. How may I help you sir")
	elif "how are you" in command or "what's up" in command or "how's you" in command:
		s=["I am fine","I'am good.","I don't want to talk.","I am so tired pleases leave me alone.","today I'am so bored","don't talk to me"]
		speak(random.choice(s))
	elif "notepad" in command:
		path="C:\\Windows\\notepad.exe"
		os.startfile(path)
		speak("opening notepad")
		speak("Are you want write somthing")
		q=take().lower()
		if "yes" in q:
			speak("Okay tell me what should I write for you")
			time.sleep(1)
			content=take()
			keyboard.write(content)
			speak("Are want to save this")
			q=take().lower()
			if "yes" in q:
				pyautogui.hotkey('ctrl','s')
				name=["new","first","test","testing file","tested","neww"]
				keyboard.write(random.choice(name))
				pyautogui.press('enter')
				speak("your file is saved")
		else:
			speak("okay...")
	elif "my computer" in command:
		path="C:\\Windows\\explorer.exe"
		os.startfile(path)
		time.sleep(1)
		speak("opening my computer")
	elif "play music" in command:
		dir="D:\\song"
		song=os.listdir(dir)
		speak("enjoy....I found something new for you it will start soon.")
		os.startfile(os.path.join(dir,random.choice(song)))
	elif "mail" in command:
		try:
			speak("whom you want to send mail")
			v=take().lower()
			speak("what should I say")
			content=take()
			to=mail.get(v)
			sendemail(to,content)
			speak("email has been sent")
		except Exception as e:
			print(e)
			speak("sorry,something went wrong")
	elif "shutdown" in command:
		speak("are you sure")
		ans=take().lower()
		if "yes" in ans:
			speak("okay sure sir, byee. have a good day")
			os.system("shutdown /s /t 1")
	elif "restart" in command:
		speak("are you sure")
		ans=take().lower()
		if "yes" in ans:
			speak("okay sure sir,")
			os.system("shutdown /r /t 1")
	elif "play in youtube" in command:
		speak("what you want to play")
		v=take()
		pywhatkit.playonyt(v)
	elif "open whatsapp" in command:
		webbrowser.open("webwhatsapp.com")
		time.sleep(1)
		speak("opening whatsapp")
	elif "use whatsapp" in command:
		speak("whom you want to send message")
		cc=take().lower()
		speak("what is the message")
		msg=take()
		con=contacts.get(cc)
		h=datetime.datetime.now().hour
		m=datetime.datetime.now().minute
		m=m+2
		speak("It will take nearly two minutes for setup whatsapp")
		pywhatkit.sendwhatmsg(con,msg,h,m)		
		time.sleep(116)
		speak("message successfully sent")
	elif "exit" in command:
		speak("sure sir, byeee. have a  good day")
		exit()






