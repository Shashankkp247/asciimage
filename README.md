# ASCIIMAGE
#### Video Demo:  todo
#### Description:
Hello, I am Shashank and this is my project named Asciimage which is a **cli tool** that uses a library called **ascii_to_image** to convert to an image into ascii format where it creates a text file with the ascii image which has the same name as the image given to.<br>

**NOTE : This tool requires Python 3 and image file format must be .jpg**<br>
***Usage:***<br>
**project.py [-h] [--img IMG] [--res {LOW,MEDIUM,HIGH}]**
<br>
*Flags:
<br>
Here **-h** flag shows the above help message
And **--img** is a required flag after which should be prepended with the image file path and name of the file.
<br>
**NOTE that the tool only accepts iage files with jpg format**
<br>
Lastly **--res** which is optional and the default input for it is MEDIUM,
but this behaviour can be overrided with ***--res*** flag followed with the choices of resolution {LOW, MEDIUM, HIGH},
***--res*** flag determines the quality at which the ascii image should be saved at in the text file.

*Example:

* **WINDOWS :**<br>

python project.py --img /test/naruto.jpg --res LOW

* **LINUX :**<br>

python3 project.py --img /test/naruto.jpg --res HIGH

*GETTING STARTED:

To get started git clone this repo.
then cd into the local version of this repo.
There after you can use the above example based on your os.
the jpg file mentioned is present in the test directory inside the asciimage directory.

***This repo also contains a test_project file which was made by me to carry out unit tests using the pytest library***
***Kindly ignore it, when encountered with it***

#### THANK YOU...
#### HOPE YOU LIKE THE TOOL..
##### ALL HAIL PYTHON!