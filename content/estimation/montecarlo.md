---
date: 2018-03-11T01:00:00+06:00
lastmod: 2018-03-11T01:30:00+06:00
title: "Monte Carlo Simulation"
categories:
  - work
tags:
  - work
  - estimation
  - montecarlo
slug: montecarlo
---

In the [last item about simple estimation](/estimation/simpleold/)  the final 'estimate' was a single number with  no mention of the likelihood of achieving it -- and I've already warned that's more like a *target* than an estimate. No estimate can be 100% certain. So how can we calculate and express that certainty?

{{< figure src="https://c2.staticflickr.com/4/3877/14396523136_6c5e0f785c_z.jpg"  
link="https://c2.staticflickr.com/4/3877/14396523136_6c5e0f785c_z.jpg"  
caption="Airport baggage carousel, Venice. Fortuna Imperatrix Mundi"
 class="figimg"
>}}

We're going to run simulations, that's how. 

##### Monte Carlo Simulation #####

The Monte Carlo method uses a large number of random or pseudo-random numbers generated between some interval with some distribution. It was invented by Stanislaw Ulam, quickly taken up by the polymathic genius, John von Neumann, and was kept under wraps for a few years because they were both working on the Manhatten Project at the time. The idea is fairly simple - instead of struggling with advanced combinatorial calculations you use a computer to generate a large number of simulations and *observe* the result.


##### Monte Carlo in estimation #####

In the case of task  estimation the spread could be decided upon by using the single-point estimate as the mean of a normal distribution, and choosing a likely standard deviation (this does raise the question as to whether actual task times vary from estimates according to a normal distribtion but we'll keep things simple for now).

Or, we could enhance the estimation process by asking the estimator to supply a *worst case*, a *best case* and a *most likely case*.

Either way, we're going run a large number of simulations and use the resulting spread of numbers to give us a cumulative probability distriubtion.


The simulations can be run in Excel, which I've used in the past. I'm going to try using **R** just because I'm teaching myself a little more about **R** and **RStudio**. 

##### Who wants to know #####

Why are we doing this again?

It's because, when developers supply single-point 'estimates', the developers themselves are tacitly deciding upon the appropriate level of risk to be accepted in a project. But that is **not** appropriate - no business should be content with unquantified project risk being obscured in this way.

The amount of risk to be accepted on a project is a **business** decision, not a **developer** decision and pretending otherwise is bad project management, bad business decision-making, and bad estimation practice. I think it happens for two reasons: managers often don't *understand* this point; and very poor managers actively *want* the decision to be made by someone else because they're so accustomed to projects missing targets by substantial amounts that their working practice is to start by identifying  people to blame.

Next: an worked example of a Monte Carlo simulation on project task estimates





