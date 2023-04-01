import openai
import speech_recognition as sr
import pyttsx3
import pyaudio



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()
def take_command():
    try:
        with sr.Microphone() as source:
            
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("▶️   "+command)
            return command
    except:
        pass

# Authenticate with your OpenAI API key
openai.api_key = "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"

def generate_response(command):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= command,
        max_tokens=800,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]




# Define the prompt that you want to send to GPT-3
prompt = "discribe with a poem how you might imagine earth in 2100 "
def run_gpt():
    command = take_command()
    gpt_answer = generate_response(command)
    print(gpt_answer)
    talk(gpt_answer)




while True:
    run_gpt()
