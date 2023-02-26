---
date: 2016-11-09T06:00:00+06:00
lastmod: 2016-11-09T17:30:00+06:00
title: "Being Charles Darwin"
authors: ["david"]
categories:
  - features
tags:
  - history
slug: darwin
cover:
  image: https://media.licdn.com/media/AAEAAQAAAAAAAA2SAAAAJDc5OWUyMDdhLWE0N2UtNDQwYi05NDJmLWRiODhlZjMxYjhmYw.png
  style: normal
---

https://www.facebook.com/TheBeagleVoyage/

https://twitter.com/cdarwin?lang=en


In 2009 I commemorated the 200th anniversary of Charles Darwin's birth by creating a Twitter feed that published excerpts every day from the diary he kept on board the Beagle, as he sailed around the world. The idea was that on June 21st - say - here, it'd be June 21st back in 1832, and the Twitter stream would display whatever Charles had written on that day.

Although Darwin's diary is out of copyright and available online, as is the book he published about the voyage, as are the letters he wrote back home, there wasn't a conveniently prepared repository of tweets. That's where the work came in.

I created a database to hold the content, and then created a Twitter App to push the Tweets to the @cdarwin twitter account. Over the next five years I kept ahead of the voyage by sitting down on a Saturday morning and sorting through the diary and the letters to extract that single sub-140 letter phrase that might amuse, entertain or educate.

It seemed to go down well - I had around 22,000 followers on Twitter - and after finishing the voyage I decided to go round again with it. After a while, though, the fun palled. So I decided to publish the voyage in real time to Facebook instead. This time, the setup was a little more sophisticated.

I wrote a REST API sitting in front of the database. Then I created an AWS Lambda using Python that queries the REST API and sends an update confirming that content was received. Then it pushes that content into Facebook, using FB's API.

So now Charles is off again. As I write it's the 14th February 1832 and he hasn't quite reached the coast of Brazil yet. His voyage around the world lies ahead of him.