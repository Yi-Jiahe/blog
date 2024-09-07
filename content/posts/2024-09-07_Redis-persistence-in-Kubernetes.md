---
title: "Redis Persistence in Kubernetes"
date: 2024-09-07T16:07:02+08:00
---

Some time ago [fwmcbaubau.com](fwmcbaubau.com) experienced data loss multiple times in a short time span due to the lack of persistent storage.

The data was stored in a self-hosted Redis server because it was cheaper to provision a Redis server with extra resources rather than utilize the SaaS version.
When I first developed the feature I didn't provision any storage for the pod because of the added complexity and cost.
When the first data loss incident occurred, I looked into the costs of provisioning storage and concluded that it was reasonable.
However, restoring the data wasn't a big deal and enough time had passed that I didn't feel like modifying the deployment.
The recent incidents finally got me to take action because it took me a while to notice the first and the second one happened really soon after the first.

Actually provisioning the storage was surprisingly simple.
All I needed to do was add a volume claim template to the StatefulSet as per the [documentation](https://docs.digitalocean.com/products/kubernetes/how-to/add-volumes/) and Digital Ocean provisioned it automatically. 
On the Redis side, I followed the [image](https://hub.docker.com/_/redis) instructions to configure persistent storage and mount the volume at /data.

I verified the updates by restarting the Redis pod and confirming that the count did not reset.