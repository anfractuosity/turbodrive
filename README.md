# turbodrive

A portable floppy disk based music player.

To improve the quality of the .stl file generated, do the following:

```
Preferences > Part Design > Max deviation to: 0.0100mm
```

Alas the case did slightly split when inserting the drive, so for the next print I will need to increase the internal dimensions by around 2mm (this 
can be simply fixed in my Python code).

# Render from FreeCAD

![CAD](/images/cad.png)

# 3D print

![3D print](/images/print.jpg)

# Electronics

* Raspberry Pi Zero
* USB floppy adapter
* USB panel mount - https://thepihut.com/products/adafruit-panel-mount-extension-usb-cable-micro-b-male-to-micro-b-female
* 3.5mm panel mount socket - https://uk.farnell.com/lumberg/1502-02/socket-3-5mm-jack-4way/dp/1368639
* 18650 to USB board, for powering the pi and the floppy drive - https://www.youtube.com/watch?v=joAkJ9QA2bw 
* I2S module for providing audio output - https://learn.adafruit.com/adafruit-i2s-stereo-decoder-uda1334a
* Buttons - probably of the capacitive type, connected to the Pi with thin magnet wire
