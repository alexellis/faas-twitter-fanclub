# faas-twitter-fanclub

This is a set of Serverless functions for OpenFaaS that make a "Fanclub":

Here's how it works:

* Star a GitHub repository (configured by placing a webhook in your settings page)
* twitterfanclub function receives the JSON, downloads the user's avatar and posts it to S3
* twitterstargazer is called with the path in S3 - invokes a polaroid function with the image and Tweets it

This is an example of function chaining and use of external storage for persistence. This is important because functions are stateless and ephermeral.

See also: [Function Chaining](https://github.com/openfaas/faas/blob/master/guide/chaining_functions.md)

Dependencies:

* [OpenFaaS](https://github.com/openfaas/faas)
* Minio
* Redis (optional for rate limiting)
* Minio-db https://github.com/alexellis/minio-db

Functions:
* Functions in stack.yml
 * twitterfanclub
 * twitterstargazer
* get-avatar via https://github.com/alexellis/faas-dockercon
* Polaroid function - https://github.com/faas-and-furious/faas-contributor-stamp/tree/master/polaroid

Your Twitter API tokens need to go into a `twitter_secrets.yml` file.

Example polaroids shared by [alexellisuk_bot](https://twitter.com/alexellisuk_bot):

![](https://pbs.twimg.com/media/DKgmEYoXoAku90i.jpg)

![](https://pbs.twimg.com/media/DKg1EJ6WsAAqAN0.png)

https://twitter.com/alexellisuk_bot/status/912020783337279488

* Got questions or want to find out more?

Send an email over to alex@openfaas.com or try out the integration by clicking "Star" on [OpenFaaS](https://github.com/openfaas/faas)
