import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
duration = 5  # секунды записи
sample_rate = 44100
q = int(input('Какую программу запустить? 1 - Голосовой переводчик, 2 - Тренировка'))
if q==1:
    print('-' * 50)
    lang = input('Введите код языка для перевода (ru - Русский, en - Английский, es - Испанский, pt - Португальский, id - Индонезийский, pl - Польский, it - Итальянский, tr - Турецкий)')
    print("Говори...")
    recording = sd.rec(
    int(duration * sample_rate), # длительность записи в сэмплах
    samplerate=sample_rate,      # частота дискретизации
    channels=1,                  # 1 — это моно
    dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи
    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")
    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)
    try: 
        text = recognizer.recognize_google(audio, language="ru-RU")    
        print("Ты сказал:", text)
    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")

    translator = Translator()
    translated = translator.translate(text, dest=lang)  # здесь 'en' — это английский
    print("Перевод на", lang, ':', translated.text)
    print('-' * 50)
elif q==2:
    err = 0
    if err==3:
        print('Игра окончена! Вы ошиблись три раза')
    words_by_level = {
    "легко": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "средне": ["банан", "школа", "друг", "окно", "жёлтый"],
    "сложно": ["технология", "университет", "информация", "произношение", "воображение"]}
    dif = input('Введите урокень сложности - легко, средне, сложно')
    word =random.choice(words_by_level[dif])
    print(word)
    print("Говори...")
    recording = sd.rec(
    int(duration * sample_rate), # длительность записи в сэмплах
    samplerate=sample_rate,      # частота дискретизации
    channels=1,                  # 1 — это моно
    dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи
    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")
    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)  
    try: 
        text = recognizer.recognize_google(audio, language="en-US").lower()    
        print("Ты сказал:", text)
        translator = Translator()
        translated = translator.translate(text, dest='ru').text.lower()
        if word==translated:
            print('Верно')
        else:
            print('Неверно')
            err + 1
    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")
else:
    print('branch test')
    
    
