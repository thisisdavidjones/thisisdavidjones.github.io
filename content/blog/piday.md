---
date: 2018-03-14T06:00:00+06:00
lastmod: 2018-03-14T12:30:00+06:00
title: "Pi Day: estimating pi with Monte Carlo simulations"
authors: ["david"]
categories:
  - blog
tags:
  - R
  - data
  - visualisation
slug: piday
---



It's Pi Day (because of the weird American date convention of m.d.y  the date is 3.14 in the US). So for Pi Day I've been looking at Monte Carlo simulations in R. Here's the result of a simple simulation of pi. 



{{< figure src="https://c1.staticflickr.com/5/4783/26935809968_780bd8b61b_z.jpg"  
link="https://c1.staticflickr.com/5/4783/26935809968_780bd8b61b_z.jpg"  
caption="Four simulation runs to estimate pi with an increasing number of iterations"
 class="figimg"
>}}


Four runs, the first with 1,000 iterations; the second with 10,000; the third with 100,000, the fourth with 1,000,000. Finally got a value for pi of 3.141144 (it's really 3.14159....etc).

It works by generating a number of vectors (1,000, 10,000, 100,000, 1,000,000) representing points between 0 and 1; and then working out the proportion that lie within a quadrant of unit radius

The R code is very simple -  [piday on github here](https://github.com/thisisdavidjones/piday):

```
set.seed()
iter=1000

x=runif(iter)
y=runif(iter)
z=sqrt(x^2+y^2)

piest = length(which(z<=1))*4/length(z)

options(scipen = 9999999)
title=paste("Monte Carlo for Pi Day. ", iter, " iterations, pi= ",piest)

plot(x[which(z<=1)],y[which(z<=1)],xlab="X",ylab="Y",main=title)
points(x[which(z>1)],y[which(z>1)],col='blue')

```

#### A note on π ####

At school you might have used 22/7 as an approximation of π and you were told  -- I hope -- that it was an approximation. The decimal expansion of π doesn't just go on forever. π is an *irrational* number and a *transcendental* number.

**Irrational**  means that the number can't be expressed as a *ratio* of two numbers - like 22/7, for example. Irrational numbers annoyed the Ancient Greeks terribly but we're comfortable with them.

A **transcendental** number is one that is not a root of a non-zero polynomial (with integer or rational coefficients). That might be a bit more of a stumbling block for some people so to explain: 

You can think of a *polynomial* as an algebraic equation, like:

x<sup>2</sup> − 4x + 7 = 0

It has a more technical definition that you can look up but it'll do for now. You might remember *solving* equations like these and (in the case of these sort of equations) getting two 'solutions'. Those were the *roots* of the equation.

So a *transcendental* number is one that's never a root of any equation like that. Not all irrational numbers are transcendental. For example, the square root of 2 is famously irrational, and famously upset the Greeks, but it isn't transcendental because it is a root of  x<sup>2</sup> − 2 = 0.

 The set of transcendental numbers is uncountably infinite. That's a *bigger* infinity than the set of all natural numbers, the ordinary counting numbers. And, yes, some infinities are bigger than other. 