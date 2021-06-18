---
title: "Hello Blog"
date: 2021-06-18T11:37:24+08:00
categories: ["Admin"]
tags: ["Meta", "Audio", "Drone"]
draft: false
---
Till now, I have been sharing my successes and completed projects on my portfolio at https://www.jiahe.dev, which you may want to take a look at. However, projects are never smooth sailing and some ideas have never seen the light of day. This blog is made for such projects, to document their progress regardless and for me to share my thoughts.

On that note, a couple of long running projects I have had which I hope to showcase some time in the future are my audio effects platform and drone development and simulation project.

The audio effects platform aims to be a flexible hardware platform for implementing digital audio effects for electronic instruments, paired with some visualization tools. To date I have experimented with hardware filters like band-pass filters, a software effects suite built with PyAudio and TkInter. I hope to combine some hardware aspects (maybe not hardware effects becuase that would be hard to scale) with software in my latest project utilising an Orange Pi with a TFT LCD screen and speaker for interactivity and feedback.

The drone development and simuation project is more of an exploration into the toolchains and building a workflow utilizing them. I hope to create a simulation environment like the Drone Racing League Simulator which supposedly takes into account the aerodynamics of the drone but really, is just very cool. I started by building a drone simulator in Python so that I could implement the physics calcuations myself, but quickly moved to Unity to take advantage of its engine to work on the controls. I ended the project there after implementing some basic PID controllers, because I found that the Unity simulation was not as robust as I would have liked. After picking up some more controls experience with my FYP project, I switched my interest to ROS and Gazebo simulations because I figured that if it were good enough for researchers, it was good enough for me. After playing around with ROS, I found that Gazebo doesn't come with native support for multirotor simulation. I therefore looked into SITL simulation with popular Open Source flight controllers like Ardupilot and PixHawk, and got the Ardupilot simulator working with Gazebo. The challenges ahead are getting PixHawk's Gazebo integration to build, finding a way to run the simulations smoothly by getting around some hardware/software constraints of my system, and figuring out how to integrate higher level control into the simulations.

As you can see, I've got a few projects I'm excited about but I'm not too sure about how long they'll take given life and other concerns. Through this blog I hope to share some ideas I'm interested in regardless of how they go.