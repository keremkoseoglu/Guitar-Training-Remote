# Guitar Training Remote

I write this Python application for my own bass guitar practice needs. It can be
used with any instrument though. The name is inspired by the [Jedi Training Remote](https://www.starwars.com/databank/training-remote), seen
on Star Wars.

Simply run main.py to start the application.

## How it works

This application will build a random set of practices (found in the package
**practice**), and display them in a sequence. Practice every day will 
hopefully improve your skills over time.

You will notice that the content of some practices will be random as
well, such as the chord or notes you need to work on.

## Adding new practices

The application builds the practice set completely automatically, based on
what is found in the package **practice**. The assumptions are;
* Every practice must have its own file, and every file must include a
single class
* Every practice must be derived from abstract_practice.AbstractPractice

Just check any class under practice, and see how easily you can add your own 
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

## Future plans

I will probably be adding new practices over time, depending on my
own practice needs.

Having mobile in mind, the GUI was developed with Kivy. However;
Kivy doesn't support mobile publishing for Python 3.6 at this time.
When it does, I have the intention to publish this application on
the mobile platforms.

It would be neat if the application included its own metronome, or if
it could play the given chord progressions. That would decrease the need
for external support in a practice session.
