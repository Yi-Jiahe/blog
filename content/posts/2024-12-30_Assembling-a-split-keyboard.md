---
title: "Assembling a Split Keyboard"
date: 2024-12-30T10:33:41+08:00
draft: true
---

## Recap

Previously on the series, I prepared the layout and PCB of the Palette 58 with Ergogen and Kicad. Since then, I have gotten the design manufactured and assembled.

## Setbacks

My original deisgn had a couple of untested designs, which unfortuntately did not quite work out as planned.

The first issue was the RGB LEDs. While I had successfully implemented the power delivery and signal lines on a macropad, the Tenta One, there were several differences on the Palette 58. On the Tenta One, I left out the decoupling capacitors because I wasn't aware of what they were. This time, having learnt about them and reviewing the LED specs, I decided to include them. Since the capacitors were a basic part from the manufacterer, I figured there was no reason not to follow the specs sheet and place on per LED. The number of LEDs were also more than doubled on the Palette 58 (29) than the Tenta One (11), resulting in a much higher current draw. On top of that I received multiple advises against the power plane I was using for power delivery. Compounded, the result was that the VCC and grounds on the board were shorted when the microcontroller was powered, resulting in issues booting up the keyboard. Due to the complexity of the issue, I chose to cut the LEDs from the project so as to not delay it.

As a postmortem however, a couple of changes I had planned were to change to an RGB LED with a lower power consumption or single colour LEDs just to serve as a backlight. Given that most designs do not use decoupling capacitors, I also indented on removing them to avoid shorts due to non-critical component failure. A change I did implemnt on the next iteration was to remove the power plane and replace it with a second ground plane.

The second issue was that the battery diode meant to allow charging while cutting off battery power was not working, and the voltage from the battery was read accross the microcontroller regardless of the switch position. I had thought I had chosen a suitable diode but it appeared to have broken down. Following more advice that it was doing nothing but draining power, I decided to remove it.

Removing these extra features simplified the PCB significantly, allowing me to route most of the signal traces on the top layer and keep large undisrupted ground planes.

Assembling the original board, I found that I needed to avoid using pin headers with the spacers to keep the height of the controller and screen in-line with the keycaps. In order to reduce the height of the controller, I decided to test a method of using diode legs as pin headers. This was a terrible mistake however, as the diode legs led to poor contact and I needed to prepare another controller with proper headers for testing.

## Assembly

Before assembling the second design, I decided to salvage the parts from the failed board. Reusing the hotswap sockets was relatively simple, I heated up one side while lifting it up, repeating it on the other. The diode leg controller wasn't too difficult either as the pins were all separate and came out easily. The main issue I faced was cleaning out the solder from the holes, which took multiple attemps.

Having utilized the surface mount assembly during the PCB manufacturing, the assembly was relativley straightforward and simply involved soldering the sockets.


