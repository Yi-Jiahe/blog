---
title: "Developing Mobile Pages With Pillow"
date: 2023-08-10T05:14:09Z
slug: 1691644449
tags:
  - Cloud
  - Python
comments:
  mastodon:
    instance: "mastodon.social"
    statusId: 114079272481849387
---

This is a follow up post to the one I made about the [TTGO T5 v2.2](https://blog.jiahe.dev/posts/1690722301/). 
The aim was to prepare images and make them available for display.

## Background

At this point I had a Lambda function for converting image data to binary data directly usable by the epdiy Arduino library using Pillow.

I also explored taking screenshots of webpages using Puppeteer, uploading them to S3 and passing them through the Lambda function. 
However, I had a few concerns about this approach:

1) The response time of the endpoint would be dependent on how long it takes to render the page alongside the other network requests, which could be highly variable.

2) Web content is not suitable for low resolution 4-bit grayscale displays, resulting in a poorly optimised UI.

While these concerns could be alievated to some degree by hosting a local server serving custom designed pages, it is more moving parts.

## The solution

In order to reduce the complexity of the solution, I decided to implement the image generation with Pillow.

My first attempt with default system fonts and all text had a few flaws such as being unable to show non-Ascii characters such as Japanese and Emojis, not presenting the information in an easy to digest manner and overall not looking too great.

From there I decided to take inspiration from a website I visited at the desired resolution. The main takeaways I adapted where a card view with thumbnail, title and subtitle, as well as more subtle elements like padding.

Combined with a cleaner font and some adjustments such as larger thumbnails at the cost of padding to cater to the smaller screen with no colours made for a much better presentation.

## Takeaways

Laying out elements without a framework is a little tedious because elements and their content need to be manually placed and styles need to be manually applied.

Dynamically generating the layout based on variable style properties such as font sizes, paddings etc. also requires math and extra lines of code, but its quite satisfying to experiment with different values.

## What's next

While it was a learning experience, if I had to make more screens, I might be more inclined to using a UI framework to develop them as suggested above.

Perhaps if its not too much trouble, a toy framework might be interesting to develop for Pillow and Python.
