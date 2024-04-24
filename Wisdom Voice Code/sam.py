import speech_recognition as sr # recognise speech
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import pyjokes
from datetime import datetime, timedelta
import os # to remove created audio files
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests
import pywhatkit
import smtplib 
from twilio.rest import Client
import wikipedia
import pygame
import geocoder
from geopy.distance import geodesic
import re
from twilio.rest import Client
import json
import pyowm
import threading
import cv2
import numpy as np
import matplotlib.pyplot as plt

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name


def respond(text):
    Ip_info = requests.get('https://api.ipdata.co?api-key=6041bc33705b86d28bd988d16ef62ac5ad7c7ec9b0ccea22207c0f0b').json()
    #  27 find object
    if 'describe this' in text:
        engine_speak("detecting objects")
        find_object()
     # 1: greeting 
    if there_exists(['hey','hi','hello', 'good morning']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):

        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name}, {person_obj.name}") #gets users name from voice input
        else:
            engine_speak(f"My name is {asis_obj.name}. what's your name?") #incase you haven't provided your name.
        

    if there_exists(["my name is"]):
        person_name = text.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
        
    
    if there_exists(["what is my name","can you tell me my name"]):
        engine_speak("Your name must be " + person_obj.name)

    
    if there_exists(["your name will be"]):
        asis_name = text.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object
      

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)
        

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)
        

    
    #  5 : meaning
    if there_exists(["search",])  and 'youtube' not in text:
        person=text.replace('search for','')
        info=wikipedia.summary(person, 1)
        url = "https://www.google.com/search?q=about+ " + person
        webbrowser.get().open(url)
        print(info)
        engine_speak(info)
        wait()
    if there_exists(["meaning for"])  and 'youtube' not in text:
        person=text.replace('meaning for','')
        info=wikipedia.summary(person, 1)
        url = "https://www.google.com/search?q=about+ " + person
        webbrowser.get().open(url)
        print(info)
        engine_speak(info)
        wait()
    if there_exists(["information"])  and 'youtube' not in text:
        person=text.replace('information on','')
        info=wikipedia.summary(person, 1)
        url = "https://www.google.com/search?q=about+ " + person
        webbrowser.get().open(url)
        print(info)
        engine_speak(info)
        wait()
    if there_exists(["about"])  and 'youtube' not in text:
        person=text.replace('about','')
        info=wikipedia.summary(person, 1)
        url = "https://www.google.com/search?q=about+ " + person
        webbrowser.get().open(url)
        print(info)
        engine_speak(info)
        wait()
    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = text.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        wait()
        engine_speak("Here is what I found for " + search_term + "on youtube")
    if there_exists(["play"]):
        song = text.replace('play', '')
        # subprocess.run(['python', 'SkipYTAds/skip_ads.py', f'https://youtube.com/watch?v={song}'])
        engine_speak('Playing' + song)

        try:
            pywhatkit.playonyt(song)
            skipadd() 
        except Exception as e:
            print("error")
            # print("An error occur red while trying to play the song:", e)
            # print('Playing' + song)
            # engine_speak('Playing' + song)
            # pywhatkit.playonyt(song)  
        wait()  

    
    if there_exists(["video on"]):
        topic= text.replace("video on",'')
        url= "https://www.youtube.com/results?search_query=" + topic
        engine_speak("Here is what I found for " + topic + "on youtube")
        pywhatkit.playonyt(url)
        wait()
        
     #7: get price
    if there_exists(["price of"]):
        search_term = text.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
        wait()
    


    #  #8 time table
    # if there_exists(["show my time table"]):
    #     im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
    #     im.show()
    
     #8 weather
    if there_exists(["weather"]):
        engine_speak("Weather status of what city?")
        city = record_audio(timeout=10)
        get_weather(city)
        wait()
     

     #9 stone paper scisorrs
    if there_exists(["game"]):
        text = record_audio("choose among rock paper or scissor",timeout=10)
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=text
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")
        wait()

     #10 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)
        wait()

    #11 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):

        opr = text.split()[1]
        engine_speak(text)
        if opr == '+':
            engine_speak(int(text.split()[0]) + int(text.split()[2]))
        elif opr == '-':
            engine_speak(int(text.split()[0]) - int(text.split()[2]))
        elif opr == 'multiply' or 'x':
            engine_speak(int(text.split()[0]) * int(text.split()[2]))
        elif opr == 'divide':
            engine_speak(int(text.split()[0]) / int(text.split()[2]))
        elif opr == 'power':
            engine_speak(int(text.split()[0]) ** int(text.split()[2]))
        else:
            engine_speak("Wrong Operator")
        wait()
        
    # #12 screenshot
    # if there_exists(["capture","my screen","screenshot"]):
    #     myScreenshot = pyautogui.screenshot()
    #     myScreenshot.save('C:\Users\IAS\Pictures\Screenshots\screen.png')
    #     wait()
    
    
     #13 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition= text.replace("definition of",'')
        url = urllib.parse.quote('https://en.wikipedia.org/wiki/' + definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found '+definitions[1])
            else:
                engine_speak ('Here is what i found '+definitions[2])
        else:
                engine_speak("im sorry i could not find the definition for "+definition)
        wait()

    #14 Current city or region
    if there_exists(["where am i",'where i am']):
        if 'region' in Ip_info:
            loc = Ip_info['region']
            engine_speak(f"You must be somewhere in {loc}")
        else:
            engine_speak("Sorry, unable to determine your location.")
   
   #15 Current location as per Google maps
    if there_exists(["what is my exact location", 'exact location']):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")  
        wait()
    # 16 send to a known person
    if there_exists(['email to samira', 'email to varsha']) :
            try:
                engine_speak("What should I say?")
                content = record_audio(timeout=10)
                to = "2016128@saec.ac.in"   
                sendEmail(to, content)
                engine_speak("Email has been sent !")
            except Exception as e:
                print(e)
                engine_speak("I am not able to send this email")  
            wait()
    #17 send an mail
    if there_exists(['send a mail','send mail', 'send an email','mail']) :
            try:
                engine_speak("What should I say?")
                content = record_audio(timeout=15)
                engine_speak(content)
                engine_speak("is it what you wanted to say yes or no")
                ans = record_audio(timeout=5)
                if ans == 'yes'or ans =='yes it is' : 
                    engine_speak("please say the TO address except the extension and say it letter by letter")
                    print("please say the TO address")
                    # to = input()  
                    to = record_audio(timeout=15)
                    to= to.strip()
                    to = re.sub(r'\s', '',to+"@gmail.com")
                    if re.match(r'^[\w\.-]+@[\w\.-]+$', to):
                        engine_speak(to)
                        engine_speak("is the mail id correct")

                        ans = record_audio()
                        if ans =='yes' or  ans=='yes it is':
                            
                            sendEmail(to, content)
                            engine_speak("Email has been sent !")
                        else:
                            engine_speak("whom should i send")
                            to = record_audio(timeout=15)
                            to= to.strip()
                            to = re.sub(r'\s', '',to+"@gmail.com")
                            if re.match(r'^[\w\.-]+@[\w\.-]+$', to):
                                engine_speak(to)
                                sendEmail(to, content)
                                engine_speak("Email has been sent !")
                            else:
                                engine_speak("Invalid email address. Please try again.")
                                
                    else: 
                        engine_speak("Invalid email address. Please try again.")
                    
                else:
                    engine_speak("then what should i say")
                    content = record_audio(timeout=15)
                    engine_speak(content)
                    engine_speak("whom should i send")
                    # to = input()  
                    to = record_audio(timeout=20) 
                    engine_speak(to)
                    engine_speak("is the mail id correct")
                    ans = record_audio(timeout=5)
                    if ans =='yes' or ans == 'yes it is':
                        sendEmail(to+"@gmail.com", content)
                        engine_speak("Email has been sent !")
                    else:
                        engine_speak("whom should i send")
                        to = record_audio(timeout=15)
                        sendEmail(to, content)
                        engine_speak("Email has been sent !")
            except Exception as e:
                print(e)
                engine_speak("I am not able to send this email")
            wait()
    
    #18 get news
    if there_exists(['news']) :
        NewsFromBBC()
        wait()

    # 19 get map 
    if there_exists(['map to']) :
        location= text.replace("map to",'')
        # response = requests.get('https://api.ipdata.co?api-key=6041bc33705b86d28bd988d16ef62ac5ad7c7ec9b0ccea22207c0f0b')
        # data = response.json()
        current_location = get_current_location()

        # Calculate distance
        destination_location = geocoder.osm(location).latlng
        distance = geodesic(current_location, destination_location).kilometers
        
        # travel mode
        engine_speak("bike or car")
        travel=record_audio(timeout=10)
        if travel.lower()=="bike":
            travel="bicycling"
        else:
            travel = "driving"

        # Construct the URL for Google Maps directions
        url = f'https://www.google.com/maps/dir/{current_location[0]},{current_location[1]}/{location}?travelmode={travel}'
        # Open Google Maps with directions
        webbrowser.get().open(url)

        # Print distance
        print(f"The distance from the current location to {location} is approximately {distance:.2f} kilometers.")
        engine_speak(f"The distance from the current location to {location} is approximately {distance:.2f} kilometers.")
        wait()

    #20 say joke
    if there_exists(['joke']) :  
        joke = pyjokes.get_joke()
        print(joke)
        engine_speak(joke)
        wait()
    #21 send whatsapp message
    if there_exists(['send a message', 'send message', 'send a WhatsApp message','message']):
        try:
            engine_speak("What should I say?")
            message = record_audio(timeout=10) 
            engine_speak(f"{message} is this what u wanted to send ")
            ans = record_audio(timeout=10)
            if 'yes' or 'it is' in text: 
                engine_speak("To whom should I send the message?")
                phone_number = record_audio()
                send_whatsapp_message(phone_number, message,)
            else :
                engine_speak("What should I say?")
                message = record_audio(timeout=10)
                engine_speak("To whom should I send the message?")
                phone_number = record_audio()
                send_whatsapp_message(phone_number, message,) 
            
        except Exception as e:
            print("An error occurred:", str(e))
        wait()
        
    # saying bye and all the formality fun stuff
    if there_exists(['what can you do']):
        engine_speak("i can send messages, takes notes, send a mail,make a joke,give directions ,take a screenshot,get any information, play songs,play a particular video, give news,give a definition, tell time,give your current location, calculate , play a game , toss a coin ")
    if there_exists(['who are you ']) :
        engine_speak("i am" + asis_obj.name + "Your 24 7 virtual assistant. if you are bored i can tell you a joke, i can play youtube videos for you, and blah blah and i am awesome.")

    if there_exists(['i love you','love you']) :
        engine_speak("why would i love you, hah just kidding love you too")

    if there_exists(['thank you','thanks']) :
        engine_speak('Your welcome. Anything else you want me to do ?')
        
    if there_exists(['stop','goodbye', 'good bye', 'tata','bubye', 'bye','shutdown']):
        engine_speak("goodbye, had a good time helping you!")
        print("goodbye")
        exit()

    # 22 taking notes
    notes_file_path = 'notes.json'

# Load existing notes from the file
    notes = load_notes_from_file(notes_file_path)
    if there_exists(['take a note', 'write down']):
        try:
            engine_speak("Sure, please say the title of the note.")
            note_title = record_audio(timeout=10)  # Set timeout to 10 seconds
            engine_speak("Please say the content of the note.")
            note_content = record_audio(timeout=20)  # Set timeout to 20 seconds
            # Save the note with title to the dictionary
            notes[note_title] = note_content
            save_notes_to_file(notes, notes_file_path)
            engine_speak("Note saved successfully.")
        except Exception as e:
            print("An error occurred:", str(e))
        wait()
    # 23 Reading notes
    if there_exists(['read note', 'read note by title', 'read the note', 'read a note']):
        try:
            engine_speak("Sure, please say the title of the note you want to read.")
            note_title = record_audio(timeout=15)  # Set timeout to 15 seconds
            note_content = search_note_by_title(notes, note_title)
            if note_content != "Note not found":
                engine_speak(f"The content of the note titled '{note_title}' is:")
                # Split the content into lines and read each line separately
                lines = note_content.split('\n')
                for line in lines:
                    engine_speak(line,rate =100)
            else:
                engine_speak(f"No note found with the title '{note_title}'. Would you like to list all note titles?")
                response = record_audio(timeout=10)
                if response.lower() in ['yes', 'yeah', 'sure']:
                    engine_speak("Here are the titles of your notes:")
                    for title in notes:
                        engine_speak(title)
                        engine_speak("which content do you want me to say")
                        note_title = record_audio(timeout=15)  # Set timeout to 15 seconds
                        note_content = search_note_by_title(notes, note_title)
                        if note_content != "Note not found":
                            engine_speak(f"The content of the note titled '{note_title}' is:")
                            # Split the content into lines and read each line separately
                            lines = note_content.split('\n')
                            for line in lines:
                                engine_speak(line, rate=100)
                            else:
                                engine_speak(f"No note found with the title '{note_title}'. Would you like to list all note titles?")

                else:
                    engine_speak("Okay, let me know if you need anything else.")
        except Exception as e:
            print("An error occurred:", str(e))
        wait()
    #  24 calling a person
    if there_exists(['phone']):
        try:
            engine_speak("Sure, please say the contact name you want to call.")
            phone_number = record_audio(timeout=10)  # Set timeout to 10 seconds
            if phone_number in contact_numbers:
                contact_number = contact_numbers[phone_number]
                make_phone_call(contact_number)
        except Exception as e:
            print("An error occurred:", str(e))
        wait()
    
    # 25 novel suggestions :
    if there_exists(["novel","suggest novels"]) :    
           engine_speak("choose a genre fiction , nonfiction ,mystery, thriller, romance, science fiction, fantasy ")
           genre=record_audio(timeout=10)
           suggestions = get_novel(genre)
           if suggestions :
               print(f"Here are some novel suggestions in the {genre} genre:")
               for novels in suggestions:
                    print(novels)
                    if novels!='':
                        print("not found")
                    wait()
    
    # 26 medication remainder :
    if there_exists(["medicine reminder",'medicines reminder']):
        set_medication_reminder()
    
    

    
def set_medication_reminder():
    # Take user input for tablet name
    engine_speak("Please enter the name of the tablet for your medication reminder")
    tablet_name = record_audio(timeout=10)
    
    # Take user input for medication reminder time
    engine_speak("Please enter the time for your medication reminder (e.g., 2 am, 2.05 am)")
    reminder_time_str = input()
    
    try:
        # Parse the user input for reminder time
        match = re.match(r'(\d+)(?:\.(\d+))?\s*([ap]m)', reminder_time_str, re.I)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2) or 0)
            period = match.group(3).lower()
            
            if period == 'pm' and hour != 12:
                hour += 12
            
            reminder_time = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # Save tablet name and reminder time in a JSON file
            reminder_data = {"tablet_name": tablet_name, "reminder_time": reminder_time.strftime("%H:%M")}
            with open("medication_reminder.json", "w") as reminder_file:
                json.dump(reminder_data, reminder_file)
            
            # Function to display the medication reminder message with tablet name
            def display_medication_reminder():
                print(f"It's time to take your {tablet_name}!")
            
            # Schedule the medication reminder using threading.Timer
            current_time = datetime.now()
            if reminder_time < current_time:
                reminder_time = reminder_time + timedelta(days=1)  # Set reminder for the next day if time has passed
            
            reminder_timer = threading.Timer((reminder_time - current_time).total_seconds(), display_medication_reminder)
            reminder_timer.start()
        
        else:
            print("Invalid time format. Please enter the time in a valid format like '2 am' or '2.05 am'.")
    
    except ValueError:
        print("Invalid time format. Please enter the time in a valid format like '2 am' or '2.05 am'.")

# function for novel suggestions
def get_novel(genre):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&maxResults=5"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        suggestions = []
        for item in data.get('items', []):
            title = item.get('volumeInfo', {}).get('title', 'Unknown Title')
            author = ", ".join(item.get('volumeInfo', {}).get('authors', ['Unknown Author']))
            suggestions.append(f"{title} by {author}")
        engine_speak(suggestions)
        print(suggestions)
        engine_speak("if you want pdf of a paticular novel then mention its number from 0 to 4")
        ans = int(word_to_numeric(record_audio(timeout=10)))
        engine_speak(ans)
        if ans < 5:
            name = suggestions.__getitem__(f"{title}", [])[ans]
            pdf_url = name.get('accessInfo', {}).get('pdf', {}).get('downloadLink')
            print(f"Opening novel PDF in Google Chrome...")
            webbrowser.get('chrome').open_new_tab(pdf_url)
        else:
            engine_speak("ok hope you are satisfied")
        wait()


        
        
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
word_to_number = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}
def word_to_numeric(word):
    return word_to_number.get(word.lower())
# function skip add
def skipadd(self):
          # Wait for the ad to become skippable
        skip_ad_button = pyautogui.locateOnScreen('skip.jpg')
        if skip_ad_button:
            pyautogui.click(skip_ad_button)
        else:
            print("Ad skip button not found")

# function  get current location 
def get_current_location():
    try:
        # Request IP information
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        if 'loc' in data:
            # Extract latitude and longitude from the response
            latitude, longitude = map(float, data['loc'].split(','))
            return latitude, longitude
        else:
            print("Unable to retrieve location information.")
            return None
    except Exception as e:
        print("An error occurred while fetching location:", e)
        return None
    
# function wait
def wait():
    engine_speak("say harmony for me to wake up")
    while True:
        text = record_audio(timeout=10)  # Continuously listen for the wake word
        if "harmony" in text.lower():  # Check if the wake word is detected
            print("Wake word detected!")
            engine_speak("Yes, how can I help you?")  # Respond to the wake word
            return True
                
                    
account_sid = 'add you sid'
auth_token = 'add your auth token'
twilio_phone_number = 'add your phone number'


# function to make call
def make_phone_call(contact_number):
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Make the phone call
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',  # TwiML URL for the call
            to=contact_number,
            from_=twilio_phone_number
        )
        
        print("Phone call initiated. Call SID:", call.sid)
    except Exception as e:
        print("An error occurred:", str(e))


contact_numbers = {
//add contact  numbers
}  


# function to send message
def send_whatsapp_message(phone_number, message):
    current_time = datetime.now()
    send_time = current_time + timedelta(minutes=1)  # Send the message 1 minute from now

    # Ensure send time is in the future
    if send_time <= current_time:
        send_time = current_time + timedelta(minutes=1)  # Adjust send time if it's in the past

    try:
        if phone_number in contact_numbers:
            contact_number = contact_numbers[phone_number]
            pywhatkit.sendwhatmsg(f"+{contact_number}", message, send_time.hour, send_time.minute)
            print("Message sent successfully!")
            engine_speak("message sent successfully")
            press_enter()
            delete_pywhatkit_db()
        else:
            print("Contact not found")
    except Exception as e:
        print("An error occurred:", str(e))
# def send_whatsapp_message(phone_number, message):
#     current_time = datetime.now()
#     try:
#         if phone_number in contact_numbers:
#             contact_number = contact_numbers[phone_number]
#             pywhatkit.sendwhatmsg(f"+{contact_number}", message, current_time.hour, current_time.minute + 1)
#             print("Message sent successfully!")
#             engine_speak("message sent successfully")
#             press_enter()
#             delete_pywhatkit_db()
#         else:
#             print("contact not found")
#     except Exception as e:
#         print("An error occurred:", str(e))



# Function to load notes from a file
def load_notes_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

# Function to save notes to a file
def save_notes_to_file(notes, file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump(notes, file)


# Function to search for a note by title
def search_note_by_title(notes, title):
    if title in notes:
        return notes[title]
    return "Note not found"
  


# function to press enter
def press_enter():
    pyautogui.hotkey('enter')


#  function to delete msgdb
def delete_pywhatkit_db():
    try:
        os.remove('PyWhatKit_DB.txt')
        print("pywhatkit.db file deleted successfully.")
    except Exception as e:
        print("An error occurred while deleting pywhatkit.db file:", str(e))

#  function to read news
def NewsFromBBC():
     
                # BBC news api
                # following query parameters are used
                # source, sortBy and apiKey
    query_params = {
    "source": "bbc-news",
    "sortBy": "top",
    "apiKey": "2acfcce9b33342f5bda639f2ccebdda5"
    }
    main_url = " https://newsapi.org/v1/articles"

                # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
                # getting all articles in a string article
    article = open_bbc_page["articles"]
 
                # empty list which will
                # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
        
                # printing all trending news
        print(i+1, results[i])
 
                #to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)

# function for there_exists
def there_exists(terms):
    for term in terms:
        if term in text:
            return True
        


# function for engine_speak
def engine_speak(text, rate = 150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    text = str(text)
    engine.say(text)            
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask="", timeout=10):
    with sr.Microphone() as source: 
        if ask:
            engine_speak(ask)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=timeout) 
        print("Done Listening")
        text = ''
        try:
            text = r.recognize_google(audio)  
            print(">>", text.lower())
        except sr.UnknownValueError:
            print('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') 
        return text.lower()


# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10) 
    
    pygame.mixer.quit()  
    os.remove(audio_file)  

    print(asis_obj.name + ":", audio_string)


# function to send mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('samira03522@gmail.com', 'gudn zbsz pkpe yeaw')
    server.sendmail('samira03522@gmail.com', to, content)
    server.close()
# function for object detection
def find_object():
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # Open webcam
    cap = cv2.VideoCapture(0)  # Change 0 to another number if your webcam is not the default one

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame from the webcam.")
            break

        height, width, channels = frame.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                print(f"Detected: {label}")
                engine_speak(f"Detected: {label}")

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, label, (x, y + 30), font, 3, (0, 255, 0), 3)

        # Convert image from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame using matplotlib
        plt.imshow(frame_rgb)
        plt.axis('off')
        plt.show()

        # Exit loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
# get weather
def get_weather(city):
        try:
            observation = owm.weather_manager().weather_at_place(str(city))
            w = observation.weather
            temp = w.temperature('celsius')['temp']
            desc = w.detailed_status
            response = f"The temperature in {city} is {temp} degrees Celsius and the sky is {desc}."
        except pyowm.exceptions.api_call_error.APICallError:
            response = "Sorry, I could not retrieve the weather information for that city."
        
        engine = pyttsx3.init()
        engine.say(response)
        

time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'harmony'
person_obj.name = ""
engine = pyttsx3.init()
pygame.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) 
engine_speak("hi this is " + asis_obj.name + " how can i help you" )
owm = pyowm.OWM("dcc11c58d0c15bdbb7479dadebeebb83") 

# def listen_for_wake_word():
#     while True:
#         text = record_audio()  # Listen for user's voice input
#         if "harmony" in text.lower():  # Check if the wake word is detected
#             print("Wake word detected!")
#             engine_speak("Yes, how can I help you?")  # Respond to the wake word
#             return True

while(1):
    # if listen_for_wake_word():
    text = record_audio("Listening", timeout=10)
    print("Done")
    print("Q:", text)
    respond(text) 
    

   
