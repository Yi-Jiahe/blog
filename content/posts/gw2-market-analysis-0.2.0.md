---
title: "Gw2 Market Analysis 0.2.0"
date: 2021-11-06T23:21:24+08:00
tags: ["Web App", "Java", "Order Book"]
draft: false
---
Financial Data is difficult to get. Its often rate limited, or charged by the number of API calls. On top of that, one needs to be on top of things to understand what they mean. In order to get my toes wet, I decided to explore the GW2 API and the BLTC, or in-game aution house to get some practical experience on how quantitative analysis and markets work.

[GW2 Market Analysis](https://github.com/Yi-Jiahe/gw2-market-analysis) is a Java application which scrapes the market every 12 hours to avoid aliasing, assuming that there exists periodic market fluctations with a period of one day. v0.1.0 of the application was completed in late August/ early September and implemented the scraper and database, such that there would be data for me to work with in the future. I set up a Lightsail instance to host the database and used a Systemd timer and service to schedule the scraper to run and store its results. I made use of the JDBC API to interact with my MySQL database on the machine.

In late October/ early November I returned to the project to implement the data visualization half of the project, after collating about 2 months of data. At this point I switched over to Spring Boot and overhauled the project making use of Spring Boot and JPA/Hibernate for persistence and made use of their ORM for retrieving the database entries. I also setup a CI/CD pipeline with GitHub Actions to build the lastest version of the project, deploy it to the instance and restart the Systemd service resposible for serving the page. The page itself made use of an earlier project I worked on to visualize the rest of the non-time series data from the API.
