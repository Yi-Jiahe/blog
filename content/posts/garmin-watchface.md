---
title: "Garmin Watchface"
date: 2022-08-23T22:29:08+08:00
slug: 1661264948
draft: false
---

At the end of May I got a new running watch, specifically the Garmin Forerunner 55 since I had started running a couple of weeks before to prepare for my IPPT and I didn't want to run with my phone and the GPS tracking was also quite bad. Having gotten a new fitness tracker, the first thing I did was of course to find out how to develop on it.

Garmin makes it quite easy to start developing for their devices, just download the Connect SDK and the Monkey C extension for VS code and you're ready to build and run applications on their emulator or an actual device.

The week prior to beginning I had been using a data field heavy watch face with 8 fields and the time, so I knew that I wanted something which could make the most of the sensors of the watch. I also wanted something subtle but with a strong theme so I decided to go for a analog face based on our [Warden of Time](https://www.youtube.com/c/OuroKroniiCh).

I started off by implementing the watch face using drawing primitives such as arcs and lines and closed polygons combined with trigonometry, fixed points and transformations. The first obstacles where a matter of the screen resolution and colour space. The low resolution meant that lines didn't look too great at all angles and graphics scaled down too much didn't render quite the way they were supposed to. The memory-in-pixel (MIP) display meant that only 8 colours were avaliabe, again limiting how closely I could match the intended design. Ultimately with some tweaking I got the watch face to look something like what I was imagining.

At this point I think it is worth noting that a digital watch face is much simpler to implement, especially with the layouts and partial refreshes, since it doesn't have hands that necessitate a full refresh every minute, hour and 12 hours respectively. As a compromise, in low power mode the screen is only refreshed every minute and the second hand is not drawn.

The data screens were quite fun to implement as it was rather exciting to figure out how much I could fit on the screen. Again, another challenge was the limited screen space, meaning that the design had elements fighting for space. In the end, I'm quite happy with the layout I settled which which fits the second, minute and hour hands, date and time, battery indicator, activity ring alongside up to three additional data fields (only three less than the 8 data field face I was using before). My enjoyment in this part of the project was reading through the documentation and examples to figure out what data was available and how to acquire it, such as heart rate and the user's heart rate zones, as well as their daily steps and distance which can also be used to fill up the activity ring.

This foray into developing on the Garmin platform gave me the opportunity to draw on a low resolution display with graphical primitives as well as pull sensor data from the platform. On top of that, I have also been left with a unique, for better or worse, watch face that I've been using for close to 3 months now. I can say that the data fields have been more than adequate and I'm very satisfied with the outcome.

If you own a Garmin Forerunner, find the watch face on the Connect IQ store [here](https://apps.garmin.com/ja-JP/apps/6d184728-2c8d-4517-818a-3b1d75dc8bc6), or the source at https://github.com/Yi-Jiahe/Kronii.

---

On a less technical note, I have continued to run about twice a week even after my IPPT and have somehow also been doing statics almost every other day. Was it the watch? Maybe, I make it a point to track runs, walks (routine ones of sufficient length such as to and from work) and statics. I haven't been looking too much at the stress and body battery given that the latter just bottoms out at 5 at the end of every day anyway. Will I continue? Hopefully.