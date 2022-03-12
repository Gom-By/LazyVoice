import speech_recognition as sr
import open_files as of
import manage_settings as ms

DATA = ms.config()

def record():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source: # DATA["microphone"]
            if DATA["adjust_noise"] == "on":
                r.adjust_for_ambient_noise(source)
            
            print("Say something :")
            audio = r.listen(source)
            
            try:
                text = r.recognize_google(audio, language=DATA["language"])
                print("You said: " + text)
            except Exception as e:
                print("A problem has occured.")
                print("Error:"+ str(e))
                return ''

            return text
    except OSError as e:
        print('Make sure the microphone is active.')
        print("Error:"+ str(e))
        return ''

if __name__=="__main__":
    text = record()
    if text!='':
        of.exec(text)
