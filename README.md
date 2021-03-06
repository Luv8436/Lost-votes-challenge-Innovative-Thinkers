### Lost-votes-challenge-Innovative-Thinkers
# DragVote
<img src="dragvote.png" height=300px width=400px/>

# Project Overview
After drawing the nation’s attention on millions of votes lost due to migration, the DRAGVOTE is a setup for remote voting in which voter can vote for his constituency by casting his voting from the residing constituency without migrating into original one. This solves problems of crores of people in India and the government and also help the democracy to find approx 29 crores of Lost votes.

# Process of voting 
1 . Voters who want to vote from other constituencies needs to fill the form available both offline and online.<br><br>
2. After authenticating the details of voters , the data is stored into the database and the receipt is isssued to the voter containing details of the venue , date and approximate time of their visit to polling booth.<br><br>
3 . Few hours before voting starts , the voting machines are configured and setup so that polling officers can enter the details of the constituency in which the machine is deployed and connected to the network and the list of remote voters coming for voting to the constituency gets loaded and voting takes place without any network.<br><br>
4 . At the voting day , the voter visit to designated location with the issued slip and goes through biometric authentication.<br><br>
5 . After the successful authentication , the details of the voter is identified by the voting machine and the candidates standing from his constituency gets displayed on the voting machine.<br><br>
6. Then voters goes near voting machine and caste his vote for his preffered candidate and after casting the VVPAT connected to the machine activates and display the slip for few seconds for conformation.<br><br>
7 . After voting is over , the machine is connected to the network to send results to the database safely and the data stored inside machine is deleted permanently.
# DRAGVOTE EVM Architecture
<img src="setup.png" alt="setup of dragvote" >

# Tehnical details 
## Authentication <br>
### Fingerprint Biometric
<img src="fingerprint.jpg" height=300px widht=300px > 

Required Components:
1. Raspberry Pi
2. USB to Serial converter
3. Fingerprint Module
4. Push buttons
5. 16x2 LCD
6. 10k pot
7. Bread Board or PCB (ordered from JLCPCB)
8. Jumper wires
9. LED (optional)
10. Resistor 150 ohm -1 k ohm (optional)


## Connection of the Raspberry Pi Fingerprint Sensor

The USB adapter is labeled, but the fingerprint sensor cables are not. However, the cables have a clear color, which we can identify and connect to the USB converter. We only need four of the cables (if your fingerprint sensor has more, you can ignore the remaining colors):
* Red: Depending on the accepted voltage of the sensor (3.3V or 5V).
* White: RXD
* Green: TXD
* Black: GND
To check whether the cabling is correct and whether the sensor is detected, you can open your console and perform the following before and after connecting:
```
ls /dev/ttyUSB*
```
If no other serial devices are connected via USB, nothing should be displayed first and afterwards /dev/ttyUSB0. If the name differs (because, for example, other devices are connected), you have to adapt it accordingly in the following steps.

## Circuit Diagram  
<img src="circuit.png" height=400px width=400px >


## Installation of the Raspberry Pi Fingerprint Library

For some commands of the installation, root privileges are required. Therefore start a terminal session and type the following, which executes all the following commands as root:
### Step 1: To install this library, root privileges are required. So first we enter in root by given command:
```
sudo bash
```

### Step 2: Then download some required packages by using given commands:
Now add the necessary package sources :
```
wget -O - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | apt-key add -
wget http://apt.pm-codeworks.de/pm-codeworks.list -P /etc/apt/sources.list.d/
```

### Step 3: After this, we need to update the Raspberry pi and install the downloaded finger print sensor library:


We update the available packages and install the Python library:
```
apt-get update
apt-get install python-fingerprint --yes
```

### Step 4: After installing library now we need to check USB port on which your finger print sensor is connected, by using given the command:
If an error has occurred (in particular, that not all dependent packages have been installed), then execute the following:
```
apt-get -f install
```
To return to the normal shell (under the Pi user), type exit.


## Operation of Fingerprint Sensor with Raspberry Pi:
Now by putting a finger over fingerprint module, we can check whether our finger prints are already stored or not. If your fingerprint is stored then LCD will show the message with the storing position of fingerprint like ‘Fount at Pos:2’ otherwise it will show ‘No Match Found’.<br/><br/>
![fingerprint-setup](fingerprint-sensor.jpg)


# Iris Biometric Verification
## RaspberryPiOpenSourceIris
Official Repo for IJCB 2020 Paper:

Open Source Iris Recognition Hardware and Software with Presentation Attack Detection<br/>
*Zhaoyuan Fang, Adam Czajka<br/>*

<img src="Teaser.png" width="800" >

## Cite

If you find this repository useful for your research, please consider citing our work:

```
@article{fang2020osirishardsoft,
  title={Open Source Iris Recognition Hardware and Software with Presentation Attack Detection},
  author={Zhaoyuan Fang, Adam Czajka},
  journal={IEEE International Joint Conference on Biometrics (IJCB)},
  year={2020}
}
```

## Prerequisites
The code is written and tested with Python 3.5 and Raspberry Pi 3B+. The software can also be treated as an individual open-source method.<br/>
Required libraries: PyTorch, TensorFlow, OpenCV

## The NDIris3D Dataset
We are currently working on the release of this dataset.

## Software

### Iris Recognition
The iris recognition is adapted from [this paper](https://ieeexplore.ieee.org/abstract/document/8658238).

### OSPAD-2D and OSPAD-3D 
All source codes of the PAD methods are in the PAD folder. <br/>
References to the PAD methods can be found here: [OSPAD-2D](https://arxiv.org/abs/1809.10172) and [OSPAD-3D](https://arxiv.org/abs/1811.07252).

### CC-Net Segmentation
We apply [CC-Net](https://ieeexplore.ieee.org/abstract/document/8759448) for fast iris segmentation. All the codes are in the CCNet folder, as well as the segmentation model saved as a TensorFlow graph. Please check out CCNet/main.py for re-training / testing. The codes are straightforward to follow.

## Hardware Assembly Instructions
The required components include: Raspberry Pi (tested on 3B+), NIR-sensitive Pi-compatible camera, NIR filter, NIR LEDs, resistors and wires. The assembly steps are the following.<br/>
<ol>
<li/>Wire the left and right NIR LEDs to the output pins as specified in cfg/cfg.yaml. Connect them also with resistors to protect the circuit.</li>
<li/>Pile / assemble with a tube the NIR filter and camera. Place it in between the left and right LEDs.</li>
<li/>Adjust the angle of the LEDs; measure the updated angles and update in cfg/cfg.yaml OSPAD_3D settings.</li>
</ol>
