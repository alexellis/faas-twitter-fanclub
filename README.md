# faas-twitter-fanclub
Twitter Fanclub for OpenFaaS 

Dependencies:

* [OpenFaaS](https://github.com/openfaas/faas)
* Minio
* Redis (optional for rate limiting)
* Minio-db https://github.com/alexellis/minio-db

Functions:
* Functions in stack.yml
* get-avatar via https://github.com/alexellis/faas-dockercon
* Polaroid function - https://github.com/faas-and-furious/faas-contributor-stamp/tree/master/polaroid

Twitter API tokens need to go into a `twitter_secrets.yml` file.

Example:

![](https://pbs.twimg.com/media/DKgmEYoXoAku90i.jpg)

![](https://pbs.twimg.com/media/DKg1EJ6WsAAqAN0.png)

https://twitter.com/alexellisuk_bot/status/912020783337279488
