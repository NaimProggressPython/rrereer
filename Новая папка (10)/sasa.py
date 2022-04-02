import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
print ("Скажите что-нибудь...")
audio = r.listen(source)

query = r.recongnize_google(audio, Language="ru-RU")
print("Вы сказали: " + query.lower())