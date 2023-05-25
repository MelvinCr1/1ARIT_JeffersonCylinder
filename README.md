# Jefferson cylinder - 1Arit

The goal of this mini-project is to implement the Jefferson cylinder in Python.<br>
The graphical interface will be created by necessarily using the Tkinter library.

## Features

soon

### Jefferson cylinder generality

Remember that this device is made up of a certain number of discs, 36 for the original, pivoting around an axis and on which are inscribed disorderly alphabets. The two correspondents have the same disks.<br>
Each disc is identifiable by a number. The key is the order in which the discs are inserted on the axle, so it is a series of numbers.<br>
To encrypt a message, the sender arranges the discs according to the key, then rotates them so that the message appears on the same line of the cylinder. The encrypted message will then be the content of the next sixth line (this last choice is only conventional, we could have made another one).<br>
To decrypt a message, the recipient of course also arranges the discs according to the key, then rotates them so that the encrypted message appears on the same line of the cylinder. The original message will then be the content of the previous sixth line.<br>
See https://en.wikipedia.org/wiki/Jefferson_disk for additions and a photograph of the original cylinder.

### Console version

Random draw of a character string made up of the 26 letters of the alphabet.<br>
Writing of n lines in a text file, n being a strictly positive integer parameter, each of them being generated according to the previous draw.<br>
Reading a text file in which each line contains a permutation of the 26 letters of the alphabet in uppercase and creating a dictionary whose keys are the integers between a 1 and the number of lines in the file, the value corresponding to a key i being the i-th line of the file.

## Built With

* [PyCharm] - The IDE used

## Authors

* **Melvin Cureau** - *Initial work* - [MelvinCureau](https://github.com/MelvinCureau)

See also the list of [contributors](https://github.com/MelvinCureau/jefferson_Cylinder/contributors) who participated in this project.
