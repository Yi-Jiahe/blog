---
title: "SQLite3 and Go"
date: 2023-08-10T03:33:04Z
slug: 1691638384
---

# The issue

Using SQLite with go using using the mattn/go-sqlite3 module requires cgo which in turn requires gcc and complicates cross-compliation.

If developing on Windows, gcc needs to be installed which can be quite the ordeal.

If using multistage builds in Docker, care needs to be taken to ensure that the architecture matches the final stage. I encounted an issue when using the default golang image which is a Debian image to build for a final Alpine image. 

At first I tried adding `apk add --no-cache libc6-compat` to my final image as suggesteed by https://stackoverflow.com/questions/51508150/standard-init-linux-go190-exec-user-process-caused-no-such-file-or-directory#comment117747592_62123648. 
However this resulted in `fcntl64: symbol not found`.
Unfortunately, I was unable to find a resolution for this issue.

What I decided to do, was to download the go and gcc toolchain into an alpine build image to build for alpine, as suggested by https://megamorf.gitlab.io/2019/09/08/alpine-go-builds-with-cgo-enabled/.

# Sqlite3 in Go

There exists a cgo-free port of SQLite in Go, modernc.org/sqlite which can be used to avoid this issue.

One of the comparisions between the two is in speed as tested by https://datastation.multiprocess.io/blog/2022-05-12-sqlite-in-go-with-and-without-cgo.html.
But given my intended usage of the database, I'm not particularly worried about the performance.