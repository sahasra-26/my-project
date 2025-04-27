import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import wikipedia
import pyjokes

#speech to text

def convert():
    r = sr.Recognizer()
    with sr.Microphone() as audio:
        print("I am listening")
        r.pause_threshold= 0.9
        spoke = r.listen(audio)

        try:
            q = r.recognize_google(spoke,language="en")
            print(f"{q}")
            return q
        except sr.UnknownValueError:
            print("Sorry,I did not understand")
            return "Please speak,I am listening"
        except sr.RequestError:
            print("Sorry,service is unavailable")
            return "Please speak,I am listening"
        except:
            return "Please speak,I am listening"
        
convert()

#speaking 

def talking(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#talking("hello I am hebo your virtual assistant")

#greeting

def greet():
    talking('''Hello, I am HEBO your virtual assistant, How can I help you?''')

greet()

#date 

def tell_day():
    day = datetime.date.today()
    day_name = day.strftime("%A")
    formatted_day = day.strftime("%d %B %Y")
    print(f"today is {day_name},and the date is {formatted_day}")
    talking(f"today is {day_name} and the date is {formatted_day}")

tell_day()

#time

def tell_time():
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    print(f"The current time is {time}")
    talking(f"The current time is {time}")

tell_time()

#the main file part

def ask():
    greet()
    start = True
    while(start):
        q = convert().lower()
        if "date" in q or "day" in q:
            tell_day()
            continue
        elif "time" in q:
            tell_time()
            continue
        elif "youtube" in q:
            talking("Loading YouTube in a moment")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "google" in q:
            talking("Loading Google in a moment")
            webbrowser.open("https://www.google.com")
            continue
        
        elif "name" in q:
            talking("I am HEBO, your virtual assistant")
            print("I am HEBO, your virtual assistant")
            continue
        elif "play" in q:
            song = q.split("play",1)[-1].strip()
            talking(f'now playing{song}')
            pywhatkit.playonyt(song)
            print(f'now playing {song}')
            continue
        elif "help" in q or "how to use" in q:
            talking('''I am HEBO your virtual assistant, here to help you with your queries like day,date,time, opening youtube and google, and search in wikipedia ''')
            print('''I am HEBO your virtual assistant, here to help you with your queries like day,date,time, opening youtube and google, and search in wikipedia ''')
            continue
        
        elif "from wikipedia" in q:
            talking("searching wikipedia now")
            q = q.replace("wikipedia","").strip()
            try:
                answer = wikipedia.summary(q,sentences=3)
                talking("The answer is as follows")
                print(answer)
                talking(answer)
            except wikipedia.exceptions.DisambiguationError:
                talking("please give a more specific query")
                print("could not understand. please be more specific")
            except wikipedia.exceptions.PageError: 
                talking("sorry,could not find the information on that topic")
                print("sorry,could not find the information on that topic")   
            continue

        elif "joke" in q or "funny" in q or "entertain" in q:
            joke = pyjokes.get_joke()
            print(joke)
            talking(joke)
            continue
        elif "stop" in q or "enough" in q or "end" in q:
            talking("I will stop now,delighted to have helped you!")
            print("I will stop now,delighted to have helped you!")
            break

ask()
