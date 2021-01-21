import pyttsx3 
import os
from datetime import datetime
from datetime import date
import time
import winsound
from googlesearch import search

engine = pyttsx3.init() 
rate = engine.getProperty('rate')   
print (rate)                       
engine.setProperty('rate', 144)    

volume = engine.getProperty('volume')  
print (volume)                         
engine.setProperty('volume',0.9)    


voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)   

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

kale = input("what can i do for you today?")
    
if kale == "what is the date today?":
    engine.say("todays date is written below" )
    print("Today's date:", today)
    engine.runAndWait()
    engine.stop()

if kale == "tell me a joke":
    print("a mother told her son that a  birdie told me that someone is doing drugs")
    print("what did the son reply?")
    input()
    print()
    print("he said that you are the one talking to birds")
    
if kale == "sing a song":
    os.system("start \"\" https://www.youtube.com/watch?v=V1Pl8CzNzCw  ")

if kale == "open wikipidea":
    engine.say("opening wikipidea")
    os.system("start \"\" https://en.wikipedia.org/wiki/Wikipedia")
    engine.runAndWait()
    engine.stop()

if kale == "who is the current president of india?":
    engine.say("Shri Ram Nath Govind")
    print("Shri Ram Nath Govind")
    engine.runAndWait()
    engine.stop()

if kale == "open chrome":
    engine.say("opening chrome")
    os.system("start \"\" https://www.google.com")
    engine.runAndWait()
    engine.stop()

if kale == "open instagram":
    engine.say("opening instagram")
    os.system("start \"\" https://instagram.com")
    engine.runAndWait()
    engine.stop()

if kale == "open youtube":
    engine.say("opening youtube")
    os.system("start \"\" https://youtube.com")
    engine.runAndWait()
    engine.stop()

if kale == "open gmail":
    engine.say("opening gmail")
    os.system("start \"\" https://www.google.com/gmail/about/#")
    engine.runAndWait()
    engine.stop()

if kale == "tell the current time":
    engine.say("Current Time =" , current_time)
    print("Current Time =", current_time)
    engine.runAndWait()
    engine.stop()

if kale == "tell the recent sports news":
    engine.say("opening the recent sports news")
    os.system("start \"\" https://www.bing.com/news/search?q=Sports&qpvt=Sports&nvaug=%5bNewsVertical+Category=%22rt_Sports%22%5d&FORM=EWRE")
    engine.runAndWait()
    engine.stop()

if kale == "i need to hear some music":
    engine.say("opening spotify")
    os.system("start \"\" https://open.spotify.com/")
    engine.runAndWait()
    engine.stop()

if kale == "say something":
   
    engine.say("hello my name is kale i was made by phoenix how may i assist you today?")       
    engine.runAndWait() 
    engine.stop()

if ("what is" in kale) or ("who is" in kale) or ("who are" in kale):
   
    query = input("what do you wanna search?")      
    for j in search(query, tld="co.in", num=10, stop=1, pause=0):
        engine.say(j)
        print(j)
        engine.runAndWait()
        engine.stop()

if kale == "i want to do some shopping":
    engine.say("opening amazon")
    os.system("start \"\" https://www.amazon.in/")
    engine.runAndWait()
    engine.stop()

if kale == "what are your functions?":
    engine.say("my functions are that i can open any website you like i can even do a google serch for you or play some songs whatever you like!")
    engine.runAndWait()
    engine.stop()

if kale == "open whatsapp":
    engine.say("opening whatsapp")
    os.system("start \"\" https://web.whatsapp.com")
    engine.runAndWait()
    engine.stop()

if kale == "open map":
    engine.say("opening google maps")
    os.system("start \"\" https://www.google.com/maps/")
    engine.runAndWait()
    engine.stop()

if kale == "chat with me":
    engine.say("hello how are you today?")
    engine.runAndWait()
    engine.stop()
    response = input()
    if response == "i am fine":
        engine.say("what can i do for you")      
        engine.runAndWait()
        engine.stop()
    if response == "i am not good":
        engine.say("what happened?")      
        engine.runAndWait()
        engine.stop()














   