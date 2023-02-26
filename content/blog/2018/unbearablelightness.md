---
date: 2018-04-15T06:00:00+06:00
lastmod: 2018-04-15T17:30:00+06:00
title: "The Unbearable Lightness of Being on Social Media"
authors: ["david"]
categories:
  - blog
tags:
  - computing
slug: unbearablelightness
kindle: 
  - book: 'The Unbearable Lightness of Being'
    asin:  '0571135390'
    linkid: '789d5f3af5bd25b644beede46e3362e2'
  - book: 'Nausea'
    asin: '014118549X'
    linkid: '5a6c8db19d2a68e5c766410a39b41082'
---

{{%poetry attr="Eliot, 'Rhapsody on a Windy Night'"%}}
The memory throws up high and dry  
A crowd of twisted things;  
{{%/poetry%}}


Vicky Lai's recent blog post about [deleting older tweets](https://vickylai.com/verbose/delete-old-tweets-ephemeral/), using an AWS lambda, struck a deep chord with me and I've implemented her *ephemeral* solution. Description of technical fix [over at Vicky's blog](https://vickylai.com/verbose/delete-old-tweets-ephemeral/) and my take on it [below](#lambda).


Vicky believes that social media imposes a view of identity that's new -- and innacurate. She writes that your social media interactions, being preserved forever, give an impression of you *now* that's not who you happen to be *now*. Instead, Vicky embraces change and impermanence  -- in this case using a clever little technical fix -- in a manner that I think is deeply true, although counter to most people's view of their lives and themselves. 


I'm *suspicious* of memories, I'm *suspicious* of claims of identity-as-narrative. For years I avoided taking photographs of occasions - parties, events - because I believed the act of taking the photo interfered with the occasion and the frozen moment of the photo *becomes* the inauthentic memory. 

In Sartre's '*Nausea'*, the protagonist, Roquentin, is wary about recalling memories, too. Sartre writes that bringing past events to mind is like exposing an old and valuable tapestry to the light. You have to do it from time to time else there'd be no point having it, but every time you do, the light damages it a little, and you repair it each time with a stitch or two, until the entire tapestry consists of only patches and mendings. There is nothing left of the original memory. The description of the dynamic reconsitution of memory has received support in recent times from the [ingenious work of Elizabeth Loftus](https://en.wikipedia.org/wiki/Elizabeth_Loftus).

Like Vicky, I'm wary of constructing an identity through a narrative of past, ephemeral remarks and interactions. More than wary: I think it's a positively misleading thing to do. The injuction to constitute ourselves through narrative is a misstep in contemporary psychology and  *weltanschauung*  that should be resisted. 

[William Blattner](https://sites.google.com/a/georgetown.edu/prof-william-blattner/) says that the temporal structure  of our lives does not have a narrative form; that our lives are not, even metaphorically, works of literature: 'We are not texts'. And still less are we tweets. 

Milan Kundera was barking up the same tree in, '*The Unbearable Lightness of Being*', where he writes about the meaningless of a life lived only once, where the 'lightness' of the title refers to a life lived with no oppressive weight of consequential decisions, in contrast to Nietzsche's thought experiment of eternal recurrence, which posited the same life lived over and over again *ad infinitum*.

{{%blocktext%}}

*Einmal ist keinmal* ... what happens but once might as well not have happened at all. 


“Human life occurs only once, and the reason we cannot determine which of our decisions are good and which bad is that in a given situation we can make only one decision; we are not granted a second, third, or fourth life in which to compare various decisions.” 

{{%/blocktext%}}

A long historical personal trace represented as the *present self* is a denial of these facts of lightness, of the fleeting nature of each moment. So, thanks to Vicky, I've created my own Lambda to ruthlessly expunge older tweets.

<a id="lambda"></a>
[Vicky's blog post](https://vickylai.com/verbose/delete-old-tweets-ephemeral/) gives you just about everything you need if you want to do it yourself -- she also links to an earlier post that describes [setting up Lambdas from scratch](https://vickylai.com/verbose/aws-lambda/). 

Just a word for Windows users: the Lambda is written in Go so you'll need to [download the Windows msi](https://golang.org/dl/) if you haven't already. You'll need to get (**go** get ...) three packages Vicky's code uses, and then to build the compiled .zip, set the correct permissions, and expose the **main** function.  I advise using the tools and following the instructions here: [https://github.com/aws/aws-lambda-go#for-developers-on-windows](https://github.com/aws/aws-lambda-go#for-developers-on-windows).

