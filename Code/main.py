import librosa
import librosa.display
import IPython
import pandas as pd
import scipy
import seaborn as sns
import IPython.display as ipd
import matplotlib.pyplot as plt 
import numpy as np
import os

folder = 'C:/Users/Mi/Desktop/openSMILE/bin/Audio/Wav' 

def handle_allAudio(): #обрботка всех аудиофайлов файлов в папке
    for audio_data in os.listdir(folder):
        if audio_data.endswith('.wav') and os.path.isfile(os.path.join(folder, audio_data)):
            def diagramPlot(): #построение спектрограмм и графиков
                y, sr = librosa.load(audio_data)
                print(type(y), type(sr))
                plt.figure(figsize=(14, 5))

                #Построение аудиограммы
                librosa.display.waveshow(y, sr=sr)
                ipd.Audio(audio_data)

                #Построение спектрограммы
                X = librosa.stft(y)
                Xdb = librosa.amplitude_to_db(abs(X))
                librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
                plt.colorbar()
                plt.savefig(folder + audio_data + '.png')

                #Построение мел-спектрограммы
                librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='mel')
                plt.colorbar()
                plt.savefig('Note_A_3_MelSpec.png')