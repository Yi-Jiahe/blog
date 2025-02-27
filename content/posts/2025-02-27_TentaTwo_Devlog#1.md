---
title: "TentaTwo Devlog #1"
date: 2025-02-27T09:05:39+08:00
tags:
 - TentaTwo
 - Devlog
---

Having used the TentaOne for almost half a year now, I have come to believe that a new design would be more appropriate than a revision. 
With that, I decided to mark the start of development on the TentaTwo.

## Learning points fron the TentaOne

To understand the design choices made with the TentaTwo, it is important to understand the pain points from the TentaOne which motivated them.

### Keymap is difficult to remember

A macropad allows the collection of highly varied actions onto a single device.
When designing the TentaOne, I figured that the most important thing was to provide enough keys such that there would be room to add as many macros one desired.
I believed that the layout could be improved over time and learnt with practice.

After half a year, I found myself only using ~4 button actions and 3 sets of encoder actions regularly.
While I do find myself wanting to use some of the other macros stored on the device, I did not manage to remember which layer button combination they were on.

I think that the diverse nature of macros means that there is a trade-off between ease of use and logically assigning actions to layers.
Putting the most used actions on the top layer means mixing a variety of actions onto different layers, making it difficult to remember what is one which layer.
Grouping actions on layers means that commonly used actions might end up scattered across different layers, making them difficult to access.

### Shortcuts specific to a single application

Another unique trait of macros is that they can be complex key combinations meant to simplify performing specific actions in a specific workflow.
This means that outside of the specific application the macro was designed for, it is either useless or results in unexpected consequences when pressed accidentally.

### Rotary encoder not as inituitve as expected

The main motivation behind the TentaOne was to introduce a rotary encoder into my workflow to provide a more suitable control for actions such as rotating the canvas, zooming and changing brush size.
In practice, I found that it didn't work as well as I had hoped.

Firstly, the sensitivities required for each action were different, meaning that while zooming felt too sensitive, rotation felt too slow.
Secondly, actions on certain layers were difficult to use because of the hand position required to hold the layer and rotate the knob.
Thirdly, the encoder click required an uncomfortable amount of force to actuate. 

## Key design changes

To address these issues, I plan to make large changes to the TentaTwo

### More different inputs, less keys

Taking inspiration from the Tourbox, I hypothesize that input diversity is more important than quantity.

I intend on adding a second encoder in the form of a scroll wheel, allowing for a different dimension of input, more suitable for incrementing and decrementing values, with muscle memory from zooming on a mouse.

I also intend on adding the joystick that I failed to introduce in the TentaOne for use with radial menus.
As I primarily intend on using the TentaTwo to complient a tablet workflow, mouse control is not needed, thus the directional input from the joystick would not be necessary for that purpose.
Instead, I find radial menus in games very convinent ways to access tools and actions and would like to explore them in productivity applications.

To add on the encoders and joystick, I intend on adding an additional button wired in paralell with the click on these inputs.
This would allow an alternative button to access the hard to use click inputs on these devices.

Another input I would like to explore is a 5 directional button, which appears to be a D-pad in the form of a small joystick.
This is mainly to get a feel of how well it would work as a pointing device on a keyboard, like a trackpoint.
Nevertheless I thnk it might be a differernt option to a D-pad.

On the layers side, I feel that I still want to keep at least 3 layers/modifier keys to offer more actions on the special input devices.
To allow multiple modifiers keys to be pressed easily by a single finger, I am thinking to explore a key layout similar to a stenograph, where keys share an edge, allowing for both to be depressed at the same time.

### Software macro translation

To provide greater flexibility, I have once again taken inspiration from Tourbox, this time from their console application.
In doing so, I will be able to store different configurations for different applications, allowing the device to remain relevent accross contexts.

Another benefit is that I will be able to introduce additional tools like context menus and visual cues.

The trade-off is that additional software would be required to use the macropad, making less plug and play, also making it unlikely to work on mobile devices.
That said, I'm not sure the same macros would have worked on mobile anyway, so it might not be a issue.
