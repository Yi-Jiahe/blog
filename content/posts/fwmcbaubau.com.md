---
title: "fwmcbaubau.com"
date: 2024-03-04T05:58:23Z
tags: ["Web", "Cloud"]
---

Before we begin, check out the site at [fwmcbaubau.com](fwmcbaubau.com)!

In case you didn't visit the site or came from a future where the site is no longer live, here's a brief description.

fwmcbaubau.com is a website where users contribute to a global click count by clicking on a button which also plays an animation and audio.

# Architecture

Now that we're on the same page, I'll share the architecture of the site. The site itself is statically hosted, with the assets coming from a CDN.

The counter itself is backed by a redis instance which stores the count which is just incremented whenever the button is pressed.

There's a server which sits in front of the redis instance, which also performs aggregations, rate-limiting and metric reporting.

You might have noticed that there are two buttons but only one count. In fact, there are two counts being tracked, but they are combined before being exposed.

In an attempt to deter bots, the server also features a rate limiter. 
To ensure actual users are not negatively impacted, the rate limiter is not particularly strict and is not difficult to circumvent.
All that's left is an appeal for people to not abuse the counter.

There is a time series of the counters and other useful metrics, making use of a prometheus server which was already running.
With it, I am able to get an idea of how the count is growing, as well as spot unusually behavior.

# Prototype

The counter was originally implemented as a serverless solution, using Redis Cloud and AWS Lambda.
However, the free tier of Redis Cloud has no concurrency and cloud not handle the development traffic (just me).
As a result, I made use of a shared self-hosted Kubernetes cluster to host the Redis instance. 
To prevent exposing the Redis instance, I refactored the Lambda endpoint into a webserver hosted in the cluster.