# Raspberry Pi Clapper

## Overview

This program will use a USB microphone to detect claps and play a clap back through the speakers if it detects one. It has 2 recurring phases: 1 when it listens for claps for 3 seconds via the microphone and 1 that processes the input to detect claps. If it detects a clap, then it entern another phase, when it plays a clap sound through the default sound output device.

## Demo

The program works in the following way:
<ul>
  <li>
    It first needs to initialize the all the data that does not concern the part of the program that deals with microphone input and clap detection
  </li>
  <li>
    At this point, you will also see a graph appear on your screen. This is the graph of the clap it uses as a baseline to compare the input to and of the interval the input needs to be in to be recognized as a clap.
    <ul>
      <li>
        Red = the maximum value a sound needs to have to be recognized as a clap
      </li>
      <li>
        Green = the actual value of the baseline recording
      </li>
      <li>
        Blue = the minimum value a sound needs to have to be recognized as a clap
      </li>
    </ul>
  </li>
  <li>
    Then it starts the recording phase. The user will be notified about the start of this phase via a message in the console
  </li>
  <li>
    At the end of the recording phase, the program will display a message in the console, notifying the user the this phase has ended, it will process the input and display a graph of the recorded audio
  </li>
  <li>
    if the data in the recording sounds like a clap (a very short sound with a high pitch), then it will display a message to notify the user that a clap was detected and, eventually, play a clap sound
  </li>
</ul>

[Demo video](https://drive.google.com/file/d/15e6pFKUBUOGSAMBRIkujVEeyaV_vNnaT/view?usp=sharing)


## Demo photos

![Initializtion Image](https://github.com/tikiana22/Android-Things/blob/main/Screenshot19.jpg)
![Baseline Graph](https://github.com/tikiana22/Android-Things/blob/main/Screenshot20.jpg)
![Recording Stop and Graph](https://github.com/tikiana22/Android-Things/blob/main/Screenshot22.jpg)
![Clap detection success](https://github.com/tikiana22/Android-Things/blob/main/Screenshot24.jpg)

## Diagram

![Diagram](https://github.com/tikiana22/Android-Things/blob/main/RaspberryPiDiagram-01.jpg)


