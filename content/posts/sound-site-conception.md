---
title: "Sound Site Conception"
date: 2021-11-06T22:45:44+08:00
slug: 1636209944
tags: ["Audio", "Web"]
comments:
  mastodon:
    instance: "mastodon.social"
    statusId: 114079220050561504
---

[Sound site](https://github.com/Yi-Jiahe/soundsite), (read: sound sight), is a small project I worked on a bit in late June, exploring the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API). The idea was to make a easily accessible way for people to visualize sound and explore the effects of audio effects on the waveform.

The basic idea of the Web Audio API is an Audio Routing Graph, which lives within an Audio Context. The graph is formed of individual Audio Nodes, of which there are three types, Sources or Inputs, Effects and Destinations or Outputs. Sources can be Oscillators which basically produce notes, Audio Recordings like files and Microphones. The Ouputs are basically the device speakers. Effects nodes can be compared to guitar effects pedals such as the DelayNode, DynamicsCompressorNode and GainNode. They do however, also provide functions like data analysis with the AnalyserNodes and other functions such as merging and splitting channels with the ChannelSplitterNode, ChannelMergerNode and audio spatialization.

Sound site makes use of the Web Audio API to build an Audio Graph starting from the device microphone, and ending with the device speakers. After the source node and before the destination are AnalyserNodes, which provide the FFT and waveform of the input and output waves to visualize the effects of the effects on the waveform.

While I have put the project on hold due to limited interactivity making it difficult for users to influence the audio graph, the next goal when I return to the project will be to work on the front end to allow users to touch their sound on top of seeing it.
