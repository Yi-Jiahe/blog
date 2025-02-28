---
title: "Ttgo T5 V2 3"
date: 2023-07-30T21:05:01+08:00
slug: 1690722301
tags: ["Embedded"]
comments:
  mastodon:
    instance: "mastodon.social"
    statusId: 114079242568403120
---

## Motivation

I found a new toy after being inspired by a post I saw about image generation AI model being run on a Raspberry Pi. One of the suggestions was to hook up the output to an eInk display because of the slow generation rate, with a link to some Raspberry Pi eInk display combos for ~100 pounds.

After a bit of searching and I found an esp32 connected 4.7" 540x960 eInk display for about 50SGD plus shipping.

## Experimentation

After playing around with the provided examples for a bit, I decided to implement an image of the day programme, which would allow me to choose between a few images from Pixiv to have displayed on my device.

Unfortunately, the TTGO T5 v2.3 is a bit short on buttons mounted on the board itself, so I made do with using the single programmable button to refresh the image.

The main difficulty I had with getting the images to be displayed on the device was figuring out that the framebuffer stored two pixels per byte at 4-bit grayscale and figuring out how to retrieve it from the esp32.

The rest of the time I spent yak-shaving, trying to architect an automated terraform managed platform to cache the Pixiv rankings and image results, serving them my device in a secure fashion. Unfortunately this was taking more time than I had intended, so I settled with manually uploading the the processed image onto an S3 bucket. 

## Results

While there is still much to build on, I now have a manual workflow for transforming images into a binary blob which can be downloaded by the esp32 and displayed on the screen.

The 4-bit grayscale display does leave quite a bit to be desired, so maybe I'll move away from displaying illustrations on it.

## What's next

Downloading preprocessed images onto the esp32 is actually a surprisingly promising workflow in my opinion. Sure, it does lose out the ability to do partial refreshes and requires a larger bandwidth than just transmitting the data required to make UI updates, but I believe neither are very big issues.

From the demo sketch that came pre-loaded on the device, the partial refreshes left an unpleasant looking black rectangle in the refreshed section. If the device was constantly refreshing sections of the screen, I could imagine it might look quite messy.

The device also doesn't make mobile data, and a full screen refresh takes a couple of seconds anyway, so downloading ~254kb (according to my filesystem) every so often isn't really a big deal.

Offloading the image preparation also frees me from having to work with on the device itself, allowing for much more flexibility in what I can do. To be honest, that's more than enough reason to convince me that it's the way to go for a personal hobby device.

Perhaps the next thing I shall work on is something more information focused, like a schedule, calendar or dashboard.

Check out the follow up [post](https://blog.jiahe.dev/posts/1691644449/) on generating information dashboards.
