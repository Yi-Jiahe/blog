---
title: "Hello World"
date: 2021-06-17T11:37:31+08:00
categories: ["Admin"]
tags: ["Meta"]
draft: false
---
Orignally I had only planned for one Hello World post but because getting the blog up and running posed more of a challenge than initially expected, I'll break it into two. This first post covers the process of creating the blog while the next will explain my rationale for creating the blog.

So, I started off looking at some popular options for webpage design and hosting like Wix and Wordpress, especially because I had heard things about how popular Wordpress was and figured it was a good skill to learn. I was quickly turned away by the monthly costs however and decided to look for something else as I'm still at that point in time where I have much more time than money. I turned to GitHub Pages because it's what I used for my portfolio, but I wanted to see if I could do a bit more.

Therefore, I took a look at static site generators starting from Jerkyll as it is supported by GitHub pages. Unfortunately it is not officially supported for Windows which is what I use on a day to day basis and I wanted to perform the builds on my side for testing and more transparency into the process I suppose. I decided to go with Hugo because it was one of the more popular options with supposedly really quick generation times as compared to options like Next.js which I deemed overkill for a blog. While not much of a challenge, looking for a theme which fit my tastes took quite a bit of time too, but I'm quite satisified with what I picked. I also had to install the extended version in order to run it but that wasn't too much trouble and I think it might pay off later on anyway.

With a quick google I found a GitHub workflow which built my source and uploaded it to the gh-pages branch and my blog was up. For easier access I then wanted to setup a custom domain name, but I had a lot of clarifications to be made about domains. A lot of trial and error, consulations and info dumps later, I had my subdomain, http://blog.jiahe.dev which you can use if you made it here by some other means, setup.

Long story short, there was quite a bit of configuration and messing around involved in the setup of this blog but I picked up a couple of new tools and learnt about domains, registries, DNS and DNS resolvers in the process.