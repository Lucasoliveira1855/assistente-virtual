import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('Ola, eu sou a Elisabeth')
maquina.say('Como posso ajudar-lo?')
maquina.runAndWait()

try:
    with sr.Microphone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'Elisabeth' in comando:
            print(comando)

except:
    print('Microfone nao esta ok')