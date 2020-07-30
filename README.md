# Guitar Training Remote

I write this Python application for my own bass guitar practice needs. It can be
used with any instrument though. The name is inspired by the [Jedi Training Remote](https://www.starwars.com/databank/training-remote), seen
on Star Wars.

![GTR](/screenshot.png?raw=true "GTR")

## Installation

### Python

Python is needed to run this application. If you don't have it, [download](https://www.python.org/downloads/) and install Python.

### Program files

Create a new folder on your computer; presumably called GTR.

Download all files in this repository to that directory.

### Virtual environment creation

Open a terminal window, go to folder GTR and install a Python virtual environment by typing:

```
python3 -m venv venv
```

### Virtual environment activation

Now activate the virtual environment. On Windows, you need to type: 

```
venv/bin/activate.bat
```

On Mac and Linux, you need to type:

```
venv/bin/activate
```

### Prerequisite installation

While your virtual environment is active, install Kivy and Vibhaga by typing:

```
pip install kivy
pip install git+http://github.com/keremkoseoglu/vibhaga.git
```

Note that Kivy installation might be a little trickier than it seems. Check [installation notes](https://kivy.org) in case you need help.

## Starting

After activating the virtual environment (as described above), run the application by typing:

```
python3 main.py
```

To customize the practices, you can edit **/config.json** .

## How it works

This application will build a random set of practices (found in the package
**practice**), and display them in a sequence. Practice every day will 
hopefully improve your skills over time.

You will notice that the content of some practices will be random as
well, such as the chord or notes you need to work on.

## Modifying configuration

You can modify the current configuration by editing **config.json** . You can 
modify or add new instruments, chords, modes, arpeggions, improvs, etc.

GTR is integrated with [FlukeBox](https://github.com/keremkoseoglu/flukebox)! If you have a FlukeBox playlist containing your backing tracks, every time the Improv exercise starts, your backing track playlist will open as well. Just make sure that the "flukebox" section of **config.json** contains the right path and playlist values. 

## Adding new practice classes

The application builds the practice set completely automatically, based on
what is found in the package **practice**. The assumptions are;
* Every practice must have its own file, and every file must include a
single class
* Every practice must be derived from abstract_practice.AbstractPractice

Optionally, classes may also get advantage of built-in helpers; such as:
* Calling URL's
* Controlling the metronome

Just check a few classes under **/practice**, and see how easily you can add your own 
practices. If you would like to contribute, feel free to contact me.

## Adding new workout factories

Current active workout factory can be found in **factory.some_practices** .
Others can be found under **factory**. 

If you want to change the workout factory, implement a new factory class
under **factory** , and change the factory definition in **gui.face**.

You may want to exclude some practices completely, for instance.

## Architectural

This application proudly demonstrates dynamic object creation in Python.
**practice/toolkit** includes methods to dynamically return class names / 
objects from within the given package name.

This technique would be particularly useful if you want your application
to support plug-ins. Just put a new external **.py** file under the 
package folder, and there you go!
