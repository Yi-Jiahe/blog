---
title: "[Opinion] My State of Rust Wasm Q1 2024"
date: 2024-03-06T20:33:20+08:00
---

WASM and rust is something I have been excited about for a couple of years now.
The ability to write a program in a language other than Javascript (or Typescript which admittedly is pretty good) and have it also compile for the web seemed like such a good idea.
I suppose its similar to how you can use Nodejs to use Javascript for things other than the web.

Anyway, I've followed it on and off over the past two years and I felt that now's a good time to share my opinion of it, inspired by this [post](https://www.reddit.com/r/rust/comments/17jptxp/state_of_rust_and_webassembly_in_2023/) on Reddit.

Before I go any further, I want to mention that my experience with the web and rust is just as a hobby, and this is an opinion piece on my experiences with the technologies and not an informational piece.

Now that that's cleared up, let's continue.

The top results you get when you search for Rust and WASM together are wasm-pack and wasm-bindgen, and its been that way since I first searched it a couple of years ago.
My main issue with this as someone who wants to try it out, is that the Rust and WebAssembly tutorial is outdated and will not work if you just follow the steps provided.
As someone who wants to figure out how to get started with it, it makes for a very steep learning curve.

The wasm-pack default bundler target is tricky to get working, with most of the resources I have found advising using the web target which I feel isn't as clean.
It doesn't help that I'm not very familiar with web technologies either, but at least the Webpack side of things was easier to follow and understand. 

The fact that the tutorial (and the accompanying template) is outdated, makes me wary of the fact that the wasm-pack repository hasn't been updated for four months at the time of writing, with most of the recent commits being fixes. 
Similarly, the WasmPackPlugin on the wasm-bindgen tutorial hasn't been updated for at least a year.

Perhaps they're both stable and in maintenance mode, but unfortunately I don't think I'll be finding out anytime soon.

The reason I got into this is because I wanted to use the same codeset for a game, with a single player mode being handled by the browser and the multiplayer mode calling the server.
However, my conclusion from this exploration is that perhaps it would be faster to just have the client be for visualization and delegate all the game function to the server.
