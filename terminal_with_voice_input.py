import speech_recognition as sr
#import json

def start_terminal_with_voice_input(func):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        #recognizer.adjust_for_ambient_noise(source)
        while(True):
            user_input = input("\nUser: ")
            if (user_input.lower() == "exit"):
                break
            if (user_input.lower() == ""):
                print("Listening for 5 seconds...")
                audio_data = recognizer.listen(source, phrase_time_limit=5)
                print("Recognizing......")
                try:
                    # Recognize the speech
                    # whisper
                    text = recognizer.recognize_whisper(audio_data)
                    # vosk
                    #text = recognizer.recognize_vosk(audio_data)
                    # text = json.loads(transcription)["text"] #for vosk

                    print("Recognized speech: ", text)
                    if(text.lower() == "exit"):
                        break
                    user_input = text
                    print("User (via voice): ", end="")
                    print(user_input)
                except sr.UnknownValueError:
                    user_input = None
                    print("Speech recognition could not understand the audio.")
                except sr.RequestError as e:
                    user_input = None
                    print(f"Could not request results from service; {e}")
                except:
                    user_input = None
                    print("Speech recognition failed.")

            if(user_input):
                response = func(user_input)
                print("Assistant: ", end="")
                print(response)

