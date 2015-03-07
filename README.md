# psyduck
Encrypted voice chat application with GUI in Python and Qt (PyQt) 

## Requirements
* Python 3
* Qt 4
* PyQt 4 with Python 3
* Pyglet

## Basic Setup
Note: These instructions are for Ubuntu (Linux in general)

1. Python 3 is already available on Ubuntu. However, typing `python` on the terminal uses the Python 2.x version. To use Python 3.x, type `python3`

2. We will be using pip to install pyglet. Typing `pip` in the terminal invokes it corresponding to Python 2.x version. For Python 3, we will have to install pip for that. Type `sudo apt-get install python3-pip`

3. Install Qt4. Download Qt 4 from the website and install it.

4. Download PyQt4 with python 3 and install it. You can directly install it from the software center.

5. To install Pyglet, type `pip3 install pyglet`

## Testing Qt and Pyglet
The temporary test files are in psyduck directory. So first `cd` into the directory and then type:

1. `python3 gui_test.py`
   You should see a blank blank window pop up.

2. `python3 pyglet_test.py`
	You should hear the sound "Hello"