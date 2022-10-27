Эта программа написана для личного использования с целью автоматизации анализа и рассчета основных параметров звука(голоса человека) на основе аудиозаписи (например, частота основного тона, частоты формант, джиттер, шиммер, высоту звука, mel- и mfcc- коэффициенты и др.). 
Суть работы программы: в коде вводится путь к папке, в которой хранятся исходные материалы (аудиозаписи), и путь к папке для сохранения результатов обработки; программа анализирует каждую .waw запись из указанной папки, строит графики и создает .arff файл с числовыми коэффициентами. Реализация таких функций выполнена посредством использования библиотек librosa и OpenSmile.

Чтобы запустить файл main.py и все работало верно, необходимо выполнить следующие шаги:

1. Установите на компьютер OpenSmile (ссылка на сайт: https://github.com/audeering/opensmile/releases) 
   и убедитесь, что он работает. Для этого введите в консоль "SMILExtract -h". Если вывелась справка с командами, то все работает
2. Откройте файл main.py в Visual Studio Code.
3. Установите все используемые библиотеки.
4. Посмотрите на строку 12 в коде. Введите путь к вашей папке с аудиозаписями.
5. В строке 13 введите путь к папке, куда вы хотите сохранять результаты работы.
6. В строке 116 введите путь к папке, где лежит SMILExtract.exe (находится там, куда вы установили OpenSmile)
7. Запустите код и проверьте папку с результатами

_________________________________________________________________________________
ENGLISH VERSION

This code was written for personal purposes to automate the analysis and calculation of the main parameters of sound (human voice) based on an audio recording (for example tone, formants, jitter, shimmer, pitch, mel- and mfcc-coefficients, etc.).
How it works: you need to write the path to the folder whith source materials (audio recordings) and to the folder, where results are supposed to be saved; the program analyzes each .waw record from the specified folder, builds graphs and creates an .arff file with numerical coefficients. The implementation of such functions is done through the use of the librosa and OpenSmile libraries.

Steps to run main.py correctly:
1. Install OpenSmile (link: https://github.com/audeering/opensmile/releases) and then try to write in the console "SMILExtract -h" (it suppose to return some usage information). So you will check if it works and was correctly installed or not.
2. Open main.py in Visual Studio Code.
3. Install libraries through the terminal.
4. Look at 12 line. Enter the path to the folder, where records are stored.
5. Look at 13 line. Enter the path to the folder, where are results supposed to be stored.
6. Look at 116 line. Enter the path to the folder, where is file SMILExtract.exe (place where you installed OpenSmile).
7. Run the programm, wait utill the end and then check your folder with results.
