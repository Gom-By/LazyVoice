import speech_recognition as sr
import open_files as of

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something :")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio, language="fr-FR")
            print("You said: \n " + text)
        except Exception as e:
            print("A problem has occured.")
            print("Error:"+ str(e))

        # return text
        with open("record.txt", 'w', encoding="utf-8") as f:
            f.write(text)

if __name__=="__main__":
    main()
    of.exec()
