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

folder = 'C:/Users/Mi/Documents/GitHub/Audio_Speech/Code' 

def handle_allAudio(): #обрботка всех аудиофайлов файлов в папке
    for audio_data in os.listdir(folder):
        if audio_data.endswith('.wav') and os.path.isfile(os.path.join(folder, audio_data)):
            def diagramPlot(): #построение диаграмм
                
                y, sr = librosa.load(audio_data)
                y_harmonic = librosa.effects.harmonic(y)
                audio_name = os.path.splitext(audio_data)[0]

                #Построение аудиограммы
                plt.figure(figsize=(14, 5))
                librosa.display.waveshow(y, sr=sr)
                ipd.Audio(audio_data)
                plt.savefig(audio_name + '_Audiogram.png')

                #Построение спектрограммы
                plt.figure(figsize=(14, 5))
                X = librosa.stft(y)
                Xdb = librosa.amplitude_to_db(abs(X))
                librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
                plt.colorbar()
                plt.savefig(audio_name + '_Spectrogram.png')

                #Построение мел-спектрограммы
                plt.figure(figsize=(14, 5))
                X = librosa.feature.melspectrogram(y)
                Xdb = librosa.amplitude_to_db(abs(X))
                librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='mel')
                plt.savefig(audio_name + '_MelSpectrogram.png')

                #Chroma Energy Normalized (CENS)
                chroma=librosa.feature.chroma_cens(y=y, sr=sr)
                plt.figure(figsize=(15,5))
                librosa.display.specshow(chroma,y_axis='chroma', x_axis='time')
                plt.colorbar()
                plt.savefig(audio_name + '_CENS.png')

                # Spectral Contrast
                contrast=librosa.feature.spectral_contrast(y=y_harmonic,sr=sr)
                plt.figure(figsize=(15,5))
                librosa.display.specshow(contrast, x_axis='time')
                plt.colorbar()
                plt.ylabel('Frequency bands')
                plt.title('Spectral contrast')
                plt.savefig(audio_name + '_SpectContrast.png')

                # Calculate MFCCs
                mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=20)
                plt.figure(figsize=(15, 5))
                librosa.display.specshow(mfccs, x_axis='time')
                plt.colorbar()
                plt.title('MFCC')
                plt.savefig(audio_name + '_MFCC')

            diagramPlot()


if __name__ == '__main__':
    handle_allAudio()