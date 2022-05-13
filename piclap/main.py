import numpy
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plot

fileName = 'myclap'
fileExtension = 'wav'
fs = 44100  # Sample rate
delta = 0.3


def listenForClap():
    seconds = 3  # Duration of recording

    print("Recording started")
    myRecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Recording ended")

    return myRecording


def saveNewClap():
    write(fileName + '.' + fileExtension, fs, listenForClap())


def doOnClapDetected(data, fs1):
    print("playing playback data...")
    sd.play(data, fs1)
    sd.wait()
    print("done playing playback data...")


def detectClap(recording, baseline, data, fs1):
    maxRec = max(recording)
    maxBase = max(baseline)
    if maxBase - delta*maxBase <= maxRec <= maxBase + delta*maxBase:
        doOnClapDetected(data, fs1)


def main():

    print("preparing playback data...")
    data, fs1 = sf.read("clap.wav", dtype='float32')
    rawBaseline = read("clap.wav")
    baseline = numpy.array(rawBaseline[1], dtype=np.float32)
    baselineNormal = []
    baselineLow = []
    baselineHigh = []
    for item in baseline:
        baselineNormal.append(item[1])
        baselineLow.append(item[1] - delta*item[1])
        baselineHigh.append(item[1] + delta*item[1])
    xBase = np.arange(1, len(baseline) + 1)
    plot.plot(xBase, baselineHigh, color='red')
    plot.plot(xBase, baselineNormal, color='green')
    plot.plot(xBase, baselineLow, color='blue')
    plot.show()

    while True:
        saveNewClap()
        rawRecording = read(fileName + "." + fileExtension)

        recording = numpy.array(rawRecording[1], dtype=np.float32)

        recBig = []
        for item in recording:
            recBig.append(item * 2 * 1e9)

        xRec = np.arange(1, len(recording) + 1)
        plot.plot(xRec, recBig, color='red')
        plot.show()

        detectClap(recBig, baselineHigh, data, fs1)


main()
