# psyduck
Encrypted voice chat application with GUI in Python and Qt (PyQt) 

## Requirements
* Python 2.x
* Qt4
* PyQt4 
* PyAudio

## Basic Setup
Note: These instructions are for Ubuntu (Linux in general)

1. Install Qt4. Download Qt 4 from the website and install it.

2. Download PyQt4 and install it. You can directly install it from the software center.

3. To install PyAudio, type `sudo apt-get install python-pyaudio`

## Testing Qt and Pyglet
The temporary test files are in psyduck directory. So first `cd` into the directory and then type:

1. `python gui_test.py`
   You should see a blank blank window pop up.

2. `python pyaudio_test.py`
	You should hear the sound "Hello"