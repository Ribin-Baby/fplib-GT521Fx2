# > `Python Library for GT-521Fx2 fingerprint sensor module`
---
* we have support for both python3 and MicroPython.
* **`Tested python-version: [ "3.6.9" ]`**

[![python](https://raw.githubusercontent.com/Ribin-Baby/fplib-GT521Fx2/main/junks/python-logo-generic.svg)](https://www.python.org/)   [![micropython](https://raw.githubusercontent.com/Ribin-Baby/fplib-GT521Fx2/main/junks/MicroPython_logo_400x400.jpg)](https://micropython.org/)

# >> introduction to GT-521Fx2
---
Our code is specially developed for  [**GT-521F32**](https://www.sparkfun.com/products/14518) and [**GT-521F52**](https://www.sparkfun.com/products/14585) series of sparkfun fingerprint sensors.
[
![sensor](https://raw.githubusercontent.com/Ribin-Baby/fplib-GT521Fx2/main/junks/14585-Fingerprint_Scanner_-_TTL__GT-521F52_-01.jpg)](https://learn.sparkfun.com/tutorials/fingerprint-scanner-gt-521fxx-hookup-guide)

This fingerprint scanner has the ability to:

- Enroll a Fingerprint
- Identify a Fingerprint
- Capable of 360° Recognition

While the input voltage is between **3.3V and 6V**, the UART's logic level is only **3.3V**. You will need a [logic level converter](https://www.sparkfun.com/products/12009) or [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers) to safely communicate with a 5V device.

#### Pinout:
[
![sensor](https://raw.githubusercontent.com/Ribin-Baby/fplib-GT521Fx2/main/junks/14518-04SerialPowerConnectorLabel.png)](https://learn.sparkfun.com/tutorials/fingerprint-scanner-gt-521fxx-hookup-guide)

* A Quick testing tool by [sparkfun](https://www.sparkfun.com/) for windows is available to download from [here](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/3/20171129-SDK_Demo_Ver1.9.zip).
 
 [![SDK_demo](https://raw.githubusercontent.com/Ribin-Baby/fplib-GT521Fx2/main/junks/FingerprintScannerConnectSDK.png)](https://learn.sparkfun.com/tutorials/fingerprint-scanner-gt-521fxx-hookup-guide)
 <p align = "center">  
<i>Fig.1 -  SDK_DEMO.exe quick testing tool for windows.</i>
</p>

* The `SDK_DEMO.exe` software tool is owned by [sparkfun](https://www.sparkfun.com/).

# >> intro to our [repository](https://github.com/Ribin-Baby/fplib-GT521Fx2)
---
Directory structure:

```
fplib-GT521Fx2
______________
│
│   README.md
│   LICENSE    
│   fplibMicro.py
│   test.py
│ 
└───fplib
│   │
│   │   __init__.py 
│   │   fpmain.py
│  
└───documents
│   │
│   │   GT-521F52_Programming_guide_V10_20161001.pdf
│   │   GT-521FX2_datasheet_V1.1__003_.pdf
│   
└───junks
    │
    │   14518-04SerialPowerConnectorLabel.png
    │   MicroPython_logo_400x400.jpg
    │   ...
    │   python-logo-generic.svg
   ```

### 1. [`fplib`](https://github.com/Ribin-Baby/fplib-GT521Fx2/tree/main/fplib) folder
* This folder contains the python3 version of sensor library code.
* We have written the code in [**fpmain.py**](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/fplib/fpmain.py) file.
* This code is developed by reffering [**programming guide**](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/documents/GT-521F52_Programming_guide_V10_20161001.pdf) for GT-521fxx fingerprint sensor, the **pdf** version of the guide is given in [**documents**](https://github.com/Ribin-Baby/fplib-GT521Fx2/tree/main/documents) folder.
### 2. [`documents`](https://github.com/Ribin-Baby/fplib-GT521Fx2/tree/main/documents) folder
* This folder contains 2 **pdf** files, a [**programming guide**](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/documents/GT-521F52_Programming_guide_V10_20161001.pdf)  and a [**datasheet**](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/documents/GT-521FX2_datasheet_V1.1__003_.pdf) of the sensor we use.
* These 2 files are very important to get a better understanding about the working of the sensor and how to use them.
### 3.  [`junks`](https://github.com/Ribin-Baby/fplib-GT521Fx2/tree/main/junks) folder
* This folder contains many image files that we used in [**README.md**](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/README.md) file of this project/Repo.
### 4. [`fplibMicro.py`](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/fplibMicro.py) file
* This is the implementation of sensor code specially written for MicroPyhton supported devices, such as [**raspberry pi pico**](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) , [**esp32**](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-devkitc.html) e.t.c.. . I have tested the code on both the board and it works fine.
### 5. [`test.py`](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/test.py) file
* In this file i have done testing of different functionalities that is supported by the sensor.
* You can look onto it, and get a better idea on how to use this library for your needs.

# >> intro to the library code and its testing.
---
### 1. initializing communication with the sensor.
* First of all connect the device to your computer and make a note of the communication port allocated to the device.

[
![img1](https://raw.githubusercontent.com/Ribin-Baby/fplib-GT521Fx2/main/junks/IMG_20220621_142706-01.jpeg)](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/junks/IMG_20220621_142706-01.jpeg)

<p align = "center">  
<i>Fig.2 - Sensor connected to a raspberry pi pico microcontroller.</i>
</p>

* now we are importing the library to our python code.
```python
from fplib import fplib
```
* after calling the library we need to initialize communication with the device using the port id.
```python
# fingerprint module variables
fp = fplib(port=0, baud=115200, timeout=3)

# module initializing
init = fp.init()
print("is initialized :", init) 
```
OUTPUT:
> **`is initialized : True`**
* so if the output is `True` then the communication with the sensor is initialized successfully.

### 2. Turning sensor LED - ON and OFF.
* To turn on the LED:
```python
led = fp.set_led(True)
print("LED status :", led) 
```
* To turn off the LED:
```python
led = fp.set_led(False)
print("LED status :", led) 
```
* for both the cases, if the sensor executes the instruction successfully will return `True` as output.

[
![img1](https://raw.githubusercontent.com/Ribin-Baby/fplib-GT521Fx2/main/junks/IMG_20220621_142801.JPG)](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/junks/IMG_20220621_142801.JPG)

<p align = "center">  
<i>Fig.3 - Sensor LED in ON state.</i>
</p>

OUTPUT:
> **`LED status : True`**

### 3. Checking if finger is pressed on the sensor or not.
* It is required to check if finger is pressed or not before enrolling or collecting templates, so to do this:
```python
pressed = fp.is_finger_pressed()
print("is finger pressed :", pressed)
```
* if someone pressed on the surface of the sensor then the output will be `True`.

OUTPUT:
> **`is finger pressed : True`**

### 4. Fetching fingerprint template from the sensor.
* We can collect fingerprint datas from different users using the following lines of code.
```python
data, downloadstat =fp.MakeTemplate()
print(f"Is template fetched :", downloadstat)
img_arr = []
if downloadstat:
   data = bytearray(data)
   # converting bytes to integer
   for ch in data:
       img_arr.append(ch)
print("fetched template data: ", img_arr)
```
* if the fetching process succeed then we will get `downloadstat as True` .
*  And we will get a template data of length `502` data points.
*  We can use this data to upload it to the sensor memory.

OUTPUT:
> **`Is template fetched : True`**

> **`fetched template data: [1, 0, 4, 16, 100, 0, .... , 0, 0, 106, 68, 24, 70]`**

### 5. setting the fetched template to sensor memory.
* we can upload back the fetched template data to the device memory, so that the sensor can use this template to identify a user.
```python
# the data should be of lenght 502 .
DATA = [1, 0, 4, 16, 100, 0, .... , 0, 0, 106, 68, 24, 70]
# idx -> is the id where we need to set the template.
fp.delete(idx=4)
status = fp.setTemplate(idx=4, data=DATA)
print("set template status :", status)
```
OUTPUT:
> **`set template status : True`**
* if we get a status `True` then the template is set on specified index (here it is 4).
* So after setting the template we can identify the user .

### 6. identify a user.
* after collecting many templates using `MakeTemplate()` and setting those templates to sensor memory using `setTemplate()` method we can use the sensor for identifyong users using the below code.
```python
id = fp.identify()
print("identified id:", id)
```
* This code will return the `id` if a match was found.

OUTPUT:
> **`identified id: 4`**


# Conclusion :
---
* More functionalities are added to the library, you can find it in the code.

* some of the functionalities are:
	- - get fingerprint image
	- - enroll new users
	- - verifying users
	- - recognizing users 
	- - e.t.c ..,
* Arduino code for this fingerprint sensor is available in official sparkfun repository : [click here](https://github.com/sparkfun/Fingerprint_Scanner-TTL)

## License Information :
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

*  [MIT](https://github.com/Ribin-Baby/fplib-GT521Fx2/blob/main/LICENSE)

### THE END
___
