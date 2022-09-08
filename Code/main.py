import librosa
import librosa.display
import pandas as pd
import seaborn as sns
import IPython.display as ipd
import matplotlib.pyplot as plt 
import numpy as np
import os
import subprocess


folder = 'C:/Users/Mi/Desktop/Audio/' #введите путь к папке, где хранятся аудиозаписи
result_folder = 'C:/Users/Mi/Desktop/Results/' #введите путь к папке, где вы хотите сохранять результат работы

def handle_allAudio(): #функция обработки всех аудиофайлов файлов в папке
    for audio_data in os.listdir(folder): #перебор всех файлов в выбранной папке
        if audio_data.endswith('.wav') and os.path.isfile(os.path.join(folder, audio_data)): #проверка формата (.wav) и существование такого файла
            
            def diagramPlot(): #функция построения графиков
                
                #определение переменных
                y, sr = librosa.load(folder + audio_data) # y - временной ряд, sr - частота дискретизации
                y_harmonic = librosa.effects.harmonic(y) #отбор только гармонических элементов
                audio_name = os.path.splitext(audio_data)[0] #название аудио без расшиерния

                #Audiogram
                plt.figure(figsize=(14, 5)) #задать размеры поля
                librosa.display.waveshow(y, sr=sr) #отображение аудиограммы в поле
                plt.savefig(result_folder + audio_name + '_Audiogram.png') #сохранение графика в папку

                #Spectrogram
                plt.figure(figsize=(14, 5))
                X = librosa.stft(y) #функция построения спктрограммы
                Xdb = librosa.amplitude_to_db(abs(X)) #конвертация амплитуды в ДБ
                librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz') #отображение спектрограммы в поле и задание осей
                plt.colorbar() #шкала цвета
                plt.savefig(result_folder + audio_name + '_Spectrogram.png')

                #Mel-Spectrogram
                plt.figure(figsize=(14, 5))
                X = librosa.feature.melspectrogram(y) #функция построения мел-спектрограммы
                Xdb = librosa.amplitude_to_db(abs(X))
                librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='mel')
                plt.colorbar()
                plt.savefig(result_folder + audio_name + '_MelSpectrogram.png')

                #Chroma Energy Normalized (CENS)
                chroma=librosa.feature.chroma_cens(y=y, sr=sr) #функция цветности
                plt.figure(figsize=(15,5))
                librosa.display.specshow(chroma,y_axis='chroma', x_axis='time')
                plt.colorbar()
                plt.savefig(result_folder + audio_name + '_CENS.png')

                # Spectral Contrast
                contrast=librosa.feature.spectral_contrast(y=y_harmonic,sr=sr)
                plt.figure(figsize=(15,5))
                librosa.display.specshow(contrast, x_axis='time')
                plt.colorbar()
                plt.ylabel('Frequency bands') #название переменной
                plt.title('Spectral contrast') #название графика
                plt.savefig(result_folder + audio_name + '_SpectContrast.png')

                # Spectral Centroid
                cent = librosa.feature.spectral_centroid(y=y, sr=sr)
                plt.figure(figsize=(15,5))
                plt.subplot(1, 1, 1) #добавление нескольких графиков в одно поле
                plt.semilogy(cent.T, label='Spectral centroid') #все графики в одном масштабе
                plt.ylabel('Hz')
                plt.xticks([]) #отображение каждого временного интервала на оси
                plt.xlim([0, cent.shape[-1]]) #определение границ оси
                plt.legend()
                plt.savefig(result_folder + audio_name + '_SpectCentroid.png')

                # Spectral Rolloff
                rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
                plt.figure(figsize=(15,5))
                plt.semilogy(rolloff.T, label='Roll-off frequency')
                plt.ylabel('Hz')
                plt.xticks([])
                plt.xlim([0, rolloff.shape[-1]])
                plt.legend()
                plt.savefig(result_folder + audio_name + '_SpectRolloff.png')

                # Spectral Bandwidth
                spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(y+0.01, sr=sr)[0] #график спектральной ширины с отклонением (p)
                spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(y+0.01, sr=sr, p=3)[0]
                spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(y+0.01, sr=sr, p=4)[0]
                plt.figure(figsize=(15, 9))
                plt.plot(spectral_bandwidth_2, color='r')
                plt.plot(spectral_bandwidth_3, color='g')
                plt.plot(spectral_bandwidth_4, color='y')
                plt.legend(('p = 2', 'p = 3', 'p = 4'))
                plt.savefig(result_folder + audio_name + '_SpectBandwidth.png')

                # Zero Crossing Rate
                zrate=librosa.feature.zero_crossing_rate(y_harmonic)
                plt.figure(figsize=(14,5))
                plt.semilogy(zrate.T, label='Fraction')
                plt.ylabel('Fraction per Frame')
                plt.xticks([])
                plt.xlim([0, rolloff.shape[-1]])
                plt.legend()
                plt.savefig(result_folder + audio_name + '_ZCR.png')

                # Calculate MFCCs
                mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=20) #рассчет 20 коэффициентов
                plt.figure(figsize=(15, 5))
                librosa.display.specshow(mfccs, x_axis='time')
                plt.colorbar()
                plt.title('MFCC')
                plt.savefig(result_folder + audio_name + '_MFCC')

                #OpenSmile
                #Ввод консольной команды согласно синтиксису приложения OpenSmile
                work_directory = os.getcwd() #сохранения пути текущей директории
                os.chdir('C:/Users/Mi/Desktop/openSMILE/bin') #введите путь, где у вас хранится OpenSMILE (а именно файл SMILExtract.exe)
                file_name = audio_name + '.arff'   
                args = ["SMILExtract", "-C", "config/gemaps/v01a/GeMAPSv01a.conf", "-I", folder + audio_data, "-O", result_folder + file_name]
                process = subprocess.Popen(args, stdout=subprocess.PIPE)
                data = process.communicate()
                os.chdir(work_directory)
            diagramPlot() #вызов функции построения графиков


#вызов функции обработки аудиозаписей
if __name__ == '__main__':
    handle_allAudio()