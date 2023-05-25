# The Matrix: A DIY 8x8 64-bit Movie Pendant 🎬👾🚀

## Description

A cosmic concoction of circuits and cinema, "The Matrix" is an 8x8 64-bit digital pendant that you can carry wherever you go, perfect for your neighborhood Supervillain, or anyone with a penchant for the dramatic. 🎭

This DIY gadget puts a digital screen right around your neck, presenting mini movie masterpieces in an 8x8 LED matrix. Choose from pre-loaded pixel animations, or craft your own miniature epics with the linked Matrix Editor! 🖌️

This project was brought to you by Ampere Works (Kailash), Absurd Industries (Amit) and will soon be hosted by Supervillains.wtf.

Let's dive into the technicalities and get started with creating your own Matrix! 💡🔧

## Hardware Breakdown

Assemble your Matrix! Get these parts together,

- [ ] Waveshare Zero (RP2040)
- [ ] LiPo battery for portability
- [ ] Charging module
- [ ] Wires
- [ ] Soldering Iron

## TODO WIRING DIAGRAM AND ASSEMBLY INFORMATiON HERE 

## Setting up CircuitPython

1. Follow the [official guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) to install CircuitPython on your Waveshare Zero RP2040.
2. Connect your device to your computer.

## Load in code.py and /movies folder

1. Copy the `code.py` file to your CIRCUITPY drive.
2. Create a `/movies` directory on your CIRCUITPY drive and place the movie files (`.txt` format) inside it.
3. Change the movie being loaded-in by modifying FRAME_FILE_PATH (line 15) to your movie's txt file.

## Breakdown of code.py

This python script powers your Matrix movie magic, with main functionality including:

- Setup of SPI and the MAX7219 LED matrix display
- Reading and parsing movie files into frames with adjustable brightness
- Displaying each frame with a short delay to create the animation effect

It's worth delving into the code to understand how it works and how you can customize it!

## Create your own movie animations

Craft your own 8x8 pixel movie animations with the help of the [Matrix Editor](https://xantorohara.github.io/led-matrix-editor/). 

## Todo list

- [ ] Add videos/pictures of the Matrix in action
- [ ] Added /lib; need to add support for Circup and list the libraries being used (with why for each)
- [ ] Add 3D file for the case of The Matrix

## Coming Soon

Keep an eye on [Supervillains.wtf](https://www.supervillains.wtf/) for when The Matrix pendant becomes available.

## Community

Join the Absurd's [Discord channel](https://discord.gg/DUSUtguG2H) for further development discussions, chit-chat and more!

## /movies Folder

The `/movies` folder contains a variety of pre-loaded pixel animations. 

1. `1-the-waving-friend.txt` - Meet your new digital buddy who just can't stop waving!
2. `2-garfs.txt` - Garf is always happy to see you.
3. `3-space-man.txt` - Watch as this tiny superhero zooms across the cosmos.
4. `4-squares.txt` - A simple, mesmerizing, repeating animation loop of squares.
5. `5-heart.txt` - A tale of a heart that just won't stop beating.
5. `6-space-invader.txt` - A space invader decides to kick it up a notch.

Feel free to add, modify, or delete the animations in this directory. Go ahead and make your Matrix Movie! 🌟

## Licensing information

This project is licensed under the GPL 3.0. The Matrix is a collaboration between Ampere Works (https://ampere.works), Absurd Industries (https://absurd.industries), and Supervillains Studio (https://supervillains.wtf).