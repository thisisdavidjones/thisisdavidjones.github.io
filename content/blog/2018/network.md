---
date: 2018-04-12T06:00:00+06:00
lastmod: 2018-04-12T17:30:00+06:00
title: "A little network issue"
authors: ["david"]
categories:
  - blog
tags:
  - computing
  - network
slug: network

---

I'm experimenting with cheap-and-cheerful voice control of my music system. I have a NAS with tens of thousands of ripped music files and I'd like to play them, easily, on my Sonos speakers and/or my Echo Dots. 

{{< figure src="https://c1.staticflickr.com/1/785/41384732332_d8c12601f5_z.jpg"  
link="https://c1.staticflickr.com/1/785/41384732332_d8c12601f5_z.jpg"  
caption="The salient bits of my home network"
 class="figimg"
>}}

Now I could upload them to some subscription service, and use the streaming capabilities - but it seems to me a bad idea for three reasons:

 * it seems overkill for my requirements
 * it's an additional expense
 * it's not as much fun as rolling my own solution
 
 I'm much more enthusiastic about voice control than I thought I'd be. I have a couple of Echo Dots and a Google Home Mini and the convenience makes me think there's a real future to this. 

  Just an aside - I have already managed to issue commands to the Echo to play my own music files on my Sonos speakers. I installed Plex on a Raspberry Pi 3, did a scan of my NAS-based music libraries, and installed the Sonos app on the Echo Dot. Hey presto, it just worked.

 But it's a bit clunky, and besides, I wanted to write my own AWS lambda for control. I've written a couple of Alexa Skills just to investigate what's involved and I have a fair amount of experience with lambdas so I'm pretty confident I can get that bit working. The part I'm a little hazy on at the moment is the callback from the lambda to Plex on my home network. I'll need to investigate the Plex API, and see what's involved in securely opening a port for inbound lambda calls.

 Ideally, I'd like to be able to issue commands such as :

  * *Alexa*  ***mymusic*** *play {track name}*
  * *Alexa*  ***mymusic*** *play {artist}*
  * *Alexa*  ***mymusic*** *play {playlist}*

And so on. If it works I'll opensource it.