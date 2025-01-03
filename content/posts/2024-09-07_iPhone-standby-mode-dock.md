---
title: "iPhone Standby Mode Dock"
date: 2024-09-07T14:49:21+08:00
---

My brother shared this [iPhone Standby Mode Dock](https://www.youtube.com/watch?v=L3nWw8qSYgk) with me and asked me to print it. 
My printer, however, is seldom used and poorly maintained so I wanted to modify the model to increase the chances of it printing successfully.

## Design

Scott kindly shared the [models](https://makerworld.com/en/models/615378#profileId-538769) for non-commercial use.
Because the files were not in an easily editable format, I created a new editable CAD [document](https://cad.onshape.com/documents/088aba448095a55b0cefb778/w/61f07337c3a206c3a56a4a47/e/3ef5bf1044b6f81334bc4e6d).

The main thing I wanted to change was the amount of plastic required for the print.
While this detracted completely from the point of the original build, the original design didn't really appeal to me anyway.
To do so I shortened the dock and removed the enclosure, removing the need for all the infill.

The quick release mechanism was also removed together with the enclosure, which I did consider a loss.
However, as I fiddled with the design, I also couldn't see the phone coming out without pulling the charger out along with it.
I decided to go for a slide release instead, since that's how I usually remove the charger from my phone.
To do so, I removed the top and middle portion of the bottom bevel, allowing the phone to be slid out from the top.
This also allowed the side buttons to be accessible while in the dock.
I fixed the orientation allowed for the phone with a cutout for the speaker and charger because the dimensions I got from the charger did not make it symmetrical.

The channel for the charger cable was a little tricky to design because I wanted to angle it to have a gentle curve so as not to damage the cable.

## Print monitoring

Since the last time I used my printer, I acquired a Raspberry Pi 5 for my home server.
Conveniently it is located close enough to my printer, so I repurposed it and by webcam to monitor my printer.

My first attempt to steam the video feed was quite poor, with a resolution of 480p and a FPS of around 5.
Unfortunately, my first print attempt failed, and the stream didn't have the quality for me to notice that the extrusion had stopped.

A bit of debugging later, I made the filament feed smoother with some smooth plastic and restarted the print.
Together with the print, I also decided to adjust the stream settings to improve the quality.

An online search of my webcam revealed that it should be able to work at 1080p.
I confirmed this by running `v4l2-ctl --list-formats-ext` which revealed that there was 1080p 30 FPS MPEG format (I was originally running 480p YUYV).

```
ffmpeg -f v4l2 -input_format mjpeg -i /dev/video0 -video_size 1920x1080 -framerate 30 -f mpegts -codec:v libx264 -preset ultrafast -b:v 1000k -r 30 udp://{desktop-ip}:23000
```

I updated my stream to

- use MPEG `-f v4l2 -input_format mjpeg`
- from the webcam `-i /dev/video0`
- at 1080p `-video_size 1920x1080`
- and 30 FPS `-framerate 30`
- and 30 FPS on the output `-r 30`

I also updated the output codec to libx264 `-f mpegts -codec:v libx264` which seems to work fine for YouTube, plus some extra settings I was recommended by Perplexity `-preset ultrafast -b:v 1000k`.

Finally stream to my desktop by UDP `udp://{desktop-ip}:23000` at some random port with my desktop's IP on my TailScale network.

## Salvaging failed prints

Monitoring is all well and good, but it doesn't fix the problems inherent with my printer.

About a third of the way the first print, about 5 hours in, the filament got caught because it wasn't spooled right.
After the fact I remembered that I should probably have fixed the spooling before inserting the filament and starting the print.

The first third of the print wasn't quite enough to support the phone yet, so I sliced the model partway up and continued the print.

The second print failed again about another third in because the print wasn't securely attached to the print bed.
I destroyed my last print bed by having the extruder too close to the bed, so I choose to err on the side of further away this time, especially because my first print had already deformed the bed a little.
I had also gotten tired of recalibrating the print bed every print, so I eyeballed the bed leveling.
The first layer looked like it was alright, so I let the print be.
The print ended up detaching itself from the print bed before it was ready.

Not wanting to waste the time and plastic I had already invested, I whipped out my soldering iron with a flat head attachment and welded the two halves together.

## Conclusion

The "finished" product works well enough, if a little ugly and somewhat subpar.

Importantly for me was that:

1) It doesn't topple with a phone in it.
2) It's able to locate the charger and not have it get ripped out when removing he phone.
3) The one I was most worried about, the cable can be threaded through the guide.
