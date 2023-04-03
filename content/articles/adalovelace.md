---
date: 2023-04-03T08:00:00
lastmod: 2024-03-23T08:00:00
title: "The noble lie of Ada Lovelace"
authors: ["david"]
categories:
  - articles
tags:
  - technology
  - programming
  - history
  - philosophy
slug: adalovelace
---

{{% pagedescription %}}
Despite [Ada Lovelace Day](https://findingada.com/), the [Ada Lovelace Institute](https://www.adalovelaceinstitute.org/), the [Ada Lovelace Award](https://en.wikipedia.org/wiki/Ada_Lovelace_Award) and Wikipedia's confirmation that Ada Lovelace is ['often regarded as the first computer  programmer'](https://en.wikipedia.org/wiki/Ada_Lovelace), Lovelace was not the first programmer and she had no hand in the creation of the Babbage Difference Engine and Analytic Engine. Does the exaggeration of her contribution matter? Is it a noble lie?
{{% / pagedescription %}}

{{% section %}}
  {{% sidenote %}}
    {{% blockquote src="Allan G. Bromley," cite="Difference and Analytical Engines" extra="1990" %}}
Not only is there no evidence that Lovelace ever prepared a program for the Analytical Engine, but her correspondence with Babbage shows that she did not have the knowledge to do so.
    {{% /blockquote %}}
  {{% /sidenote %}}




Ada Lovelace first met Charles Babbage at a party in 1833 when she was 17 and he was  42. Babbage,  the Lucasian Professor of Mathematics at Cambridge, a prestigious position previously held by Newton and later by Dirac and Hawking, invited Lovelace and her mother, Baroness Wentworth,  to see his recently constructed Difference Engine. He was forever seeking funding for his projects and such well-connected supporters would have been useful to him. The Baroness was impressed, calling the device 'a thinking machine'.


The **Difference Engine** was a mechanical calculating device that used the method of 'finite  difference' to create tables of numbers that represented the values of polynomial functions. Many significant mathematical functions in engineering and science can be approximated from such polynomials, so a machine that automated their calculation could prove extremely valuable


{{% / section %}}


{{% section %}}
## Lovelace and mathematics
Lovelace maintained contact with Babbage and the encounter with the Difference Engine seems to have sparked in her an interest in mathematics  though she didn't pursue it deeply or seriously for several years. But in 1839, after marriage and three children, Lovelace  asked Babbage if he could find her a maths instructor. Babbage introduced her to [Augustus De Morgan](https://en.wikipedia.org/wiki/Augustus_De_Morgan) at UCL. 

Lovelace appeared to show some aptitude and De Morgan once wrote of her:

> Had any young [male]  beginner, about to go to Cambridge, shewn the same power[s], I should have prophesied ... that they would have certainly made him an original mathematical investigator, perhaps of first rate eminence

Although, in contrast, one of her biographers, Dorothy Stein, wrote that the errors she made -  'many elementary'  -- and the questions she asked of De Morgan and others were 

{{% blockquote src="Dorothy Stein" cite="['The Lovelace–De Morgan mathematical correspondence: A critical re-appraisal'](https://www.sciencedirect.com/science/article/pii/S0315086017300319#br0450))" extra="pp. 84, 89–91" %}}
evidence of the tenuousness with which she grasped the subject of mathematics
{{% / blockquote %}}

{{% / section %}}



{{% section %}}
  

## The Analytical Engine
Meanwhile, Babbage had conceived the **Analytical Engine**. This was to be a general purpose computer rather than the 'simple' mechanical calculator that was its predecessor. It included an ALU, conditional branching and loops, an integrated memory, and a punched card system for controlling computation steps. It could be 'programmed' using a punch-card system. Technically, it was 'Turing Complete'.

{{% sidenote %}}'Turing Complete' is a term used to describe a set of data manipulation rules that can in principle simulate a Turing Machine{{% / sidenote %}}

No prototype of this new Engine was ever built, but Babbage described it in notes and diagrams. When the British government decided to terminate funding for his projects he turned elsewhere for support. He gave a talk in Turin, where notes where taken by an army engineer called Luigi Menabrea (who later became the prime minister of Italy). Menabrea published a paper (in French) based on his notes of Babbage's talk, and Ada decided to translate it into English. She added a number of extended appendices, which were called 'Notes', including one - 'Note G' - that is the note said to contain the very first 'program'
{{% / section %}}



{{% section %}}
  ## Note G
{{% sidenote %}}
{{% blockquote src="Doron Swade" cite="[BBC Radio 4 - In Our Time, Ada Lovelace](https://www.bbc.co.uk/programmes/b0092j0x)"%}}
Lovelace published the first thing we would now recognise as an algorithm but the work was Babbage's. The principle of a program was Babbage's
{{%/ blockquote %}}
{{% / sidenote %}}  
Notes to the translation were co-authored by Babbage and Lovelace.  There is only one 'program' in the notes and that we know to have been written by *Babbage* and not Lovelace. Note G contains a description of how the Analytic Engine could be used to generate ['Bernoulli Numbers'](https://en.wikipedia.org/wiki/Bernoulli_number). This isn't a program as we now understand it but a sketch of an algorithm. And it was prepared for Lovelace *by Babbage* (although Lovelace did spot an error in it). Babbage had already created such algorithms or 'programs' for the Analytical Engine more than 5 years earlier:

{{% blockquote src="Doron Swade" cite="quoted in ['Ada Lovelace: Original and Visionary, but No Programmer'](https://www.bbvaopenmind.com/en/technology/visionaries/ada-lovelace-original-and-visionary-but-no-programmer/))" extra="09&nbsp;December&nbsp;2015" %}}
The manuscript evidence clearly shows that Babbage wrote ‘programs’ for his Analytical Engine in 1836-7 i.e. 6-7 years before the publication of Lovelace’s article in 1843. There are about 24 of such ‘programs’ and they have the identical features of the Lovelace’s famous ‘program’ ... [they] do not support, indeed they contradict the claim that Lovelace was the ‘first programme

{{% / blockquote %}}

This really shouldn't come as a surprise. It would have been exceedingly odd for Babbage to have conceived of a general purpose programmable calculator without sketching out a few algorithms for it.
{{% /section %}}



{{% section %}}
  ## Vision for the Analytical Engine
{{% sidenote %}}

  {{% blockquote src="Helen Joyce" cite="['Review of 'The Cogwheel Brain'](https://plus.maths.org/reviews/book3/2pdf/index.html/op.pdf)" extra="September 2000" %}}
although Swade is sympathetic to the situation and aspirations of Ada Lovelace, daughter of Byron, who translated and annotated a paper describing the Analytical Engine, he is very clear that the widespead modern conception of her as a serious collaborator on Babbage’s work is incorrect
 {{% / blockquote %}}
{{% /sidenote %}}


Swade says that the effort to claim Lovelace as 'the first programmer' obscures her *real* contribution:
    {{% blockquote src="Javier Yanes" cite="[Ada Lovelace: Original and Visionary, but No Programmer](https://www.bbvaopenmind.com/en/technology/visionaries/ada-lovelace-original-and-visionary-but-no-programmer/)" extra="OpenMind BBVA, 1990" %}}
&hellip;Swade stresses that this in no way undermines the figure of Lovelace and the value of her contribution. In fact, according to the historian, “the obsession with the Bernoulli ‘program’ by those wishing to promote Lovelace has so obscured the much more significant contribution that she made.” And what was it? In the words of Swade, “an original understanding of where the power and potential of computers lay.”
    {{% / blockquote %}}

Ada's reputation as more than an amateur enthusiast for Babbage's work rests on her vision for the future of the Analytic Engine, and to what extent it advanced beyond Babbage's own conception of it.

We should be wary of exaggerated claims here, having read so much  hyperbole that views Lovelace, who died of (probably) cervical cancer in 1852, as a genius whose original groundbreaking work was thwarted by a patriarchal society. Lovelace was ***not*** a Lise Meitner, or a Jocelyn Bell Burnell, both of whose recognition *was* obscured and denied by the sexist cultures in which they worked.

Lovelace did suggest that the Analytical Engine could operate on more than mathemtical symbols, and this seems to be the first *published* statmement to that effect. She had a vision that went beyond anything Babbage himself clearly stated, though there are hints that he understood  the Engine's broader potential - and it would be odd if he didn't. 

{{% section %}}

  ## Recap

To summarise so far:


* Lovelace had no part in the design and prototyping of the Difference Engine
* She had no part in the conception and design of the Analytic Engine
* She did not write the first algorithms for the Analytic Engine
* She was not the sole author of 'Note G' 
* Babbage prepared the Note G algorithm for calculating Bernoulli numbers



But:

* Lovelace *did* spot an error in Babbage's algorithm
* She *was* a keen publicist of Babbage's work
* She *did* suggest the Analytic Engine could manipulate more than numbers
{{% / section %}}

## Noble Lies

In the Republic, Plato argues that a just society can only be achieved if individuals are properly educated and that the best way to ensure this is through a system of strict social classes.

To maintain this system, Plato proposed the idea of a "noble lie," a falsehood told by the ruling class to the rest of society to justify the social order and to prevent social unrest. The lie would be that each individual in society was born into a certain class based on their inherent qualities and abilities, rather than by chance or circumstances. This would provide the justification for the social hierarchy and discourage individuals from challenging the status quo.

Plato believed that the "noble lie" was necessary for the stability of society and the happiness of its citizens. He argued that the ruling class would have a duty to deceive the rest of society for the greater good.

Plato suggested the  "noble lie" would  create a stable society where everyone knows their place and *is content with it*. It could  help prevent social unrest, which might occur if people perceived the social order as unjust. The lie would then  promote social harmony and unity, with everyone believing they had an allocated role to play in society.

The noble lie, though, assumes that the ruling class knows what is best for society, in a disinterested way. Powerful myths that sustain a social order may be acitvely damaging if and when the myths are understood to be just that.

## Ada Lovelace as a Noble Lie

The myth of Ada Lovelace as the "first computer programmer," could, charitably,  be considered a "noble lie". It presents Lovelace as a pioneer in computer science, despite her negligible contributions being grossly overstated, to serve as an inspiration for women in science and technology and encourages them to pursue careers in these fields. But others argue that the myth distorts the history of computer science and perpetuates a false narrative about the contributions of women in the field -- and obscures the real oppression of women.

[Virginia Woolf,  in 'A Room of One's Own'](https://www.d.umn.edu/~tbacig/cst1010/chs/woolfe.html), imagined a fictious sister of Shakespeare, observing that that a woman with his talents would have been denied the opportunity to develop. This is the point about the historic oppression of women - they have been refused education and the possibility of careers -- and everybody else has been denied the benefits of their genius.  

Inventing a myth of Lovelace as a noble lie hides this  historic subjugation of women. There simply are not hundreds of great female contributions to STEM felds from the past whose histories are waiting for the expertise and dedication of unblinkered scholoars to reveal. This is a tradgedy of our past - the millions of lives unfulfilled and potential talent wasted. It would be as well to remember that.

There are other women whose work in STEM fields we could use instead to encourage girls and women without needing to tell a lie, and while preserving the true history of women's oppression by men. Here are a few of my suggestions:

* Emmy Noether
* Lise Meitner
* Curie (of course)
* Jocelyn Bell Burnell
* Cecilia Payne-Gaposchkin

and if you don't know about them, go and read and be enthused at how they broke through *despite* the restrictions of their culture.


{{% / section %}}

{{%  section %}}
## Timeline of events

* 1804: Punch-card controlled Jacquard Loom patented
* 1815: Lovelace born
* 1822: Difference Engine #0 completed by Babbage
* 1832: Babbage and Clement produce a prototype of Difference Engine #1
* 1833: Babbage meets Lovelace; Babbage demonstrates the Difference Engine prototype to Lovelace
* 1836-7: Babbage writes the first 'programs' for the Analytical Engine
* 1842: Menabrea publishes a paper on the Analytical Engine based on Babbage's lectures
* 1843: Lovelace translates Menabrea's description, annotated with notes inc. Note G
* 1852: Lovelace dies
* 1871: Babbage dies
{{% / section %}}


{{% section %}}
## Bibliography

* Bromley, Allan G. (1990). "[Difference and Analytical Engines"](https://ed-thelen.org/comp-hist/CBC-Ch-02.pdf). In Aspray, William (ed.). Computing Before Computers. Ames: Iowa State University Press. ISBN 978-0-8138-0047-9.

* Dorothy Stein [Ada A Life and a Legacy ](https://monoskop.org/images/e/e7/Stein_Dorothy_Ada_A_Life_and_a_Legacy.pdf) 1985 ISBN 0-262-19242-X 

* Christopher Hollings, Ursula Martin, Adrian Rice [The Lovelace–De Morgan mathematical correspondence: A critical re-appraisal](https://www.sciencedirect.com/science/article/pii/S0315086017300319#br0310), Historia Mathematica Volume 44, Issue 3, August 2017, Pages 202-231

* The Renaissance Mathematicus [Charles not Ada, Charles not Charles and Ada, just Charles…](https://thonyc.wordpress.com/2021/01/01/charles-not-ada-charles-not-charles-and-ada-just-charles/)

* [Babbage’s Calculating Engines: Being a Collection of Papers Relating to Them; Their History and Construction](https://thonyc.wordpress.com/2021/01/01/charles-not-ada-charles-not-charles-and-ada-just-charles/#:~:text=Babbage%E2%80%99s%20Calculating%20Engines%3A%20Being%20a%20Collection%20of%20Papers%20Relating%20to%20Them%3B%20Their%20History%20and%20Construction%2C)

* Virginia Woolf, ['A Room of  One's Own'](https://www.amazon.co.uk/Room-Ones-Penguin-Modern-Classics/dp/0241436281)


{{% / section %}}
