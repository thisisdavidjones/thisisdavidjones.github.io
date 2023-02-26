---
date: 2018-03-08T21:00:00+06:00
lastmod: 2018-03-08T21:30:00+06:00
title: "Estimation the simple, old-fashioned way"
categories:
  - work
tags:
  - work
  - estimation
slug: simpleold
---

So to begin with let's look at a very common way of producing estimates -- with a little twist -- and then think about how it can be improved.

{{< figure src="https://c1.staticflickr.com/5/4781/38893798600_05e1d4b963_z.jpg"  
link="https://c1.staticflickr.com/5/4781/38893798600_05e1d4b963_z.jpg"  
caption="Chand Baori step well, Rajasthan. Lots of small steps"
 class="figimg"
>}}



First, break the project up into features and then into  **small** tasks. Your tasks should be  a matter of *hours*  long, not days or, god forbid, weeks. If your tasks are too long you it suggests you haven't thought about what's really involved in programming them. Also, the act of decomposing features into smal tasks is the beginning of designing the solution.

You don't need to use any fancy software. Google Sheets or Microsoft Excel will do. 


{{< figure src="https://c1.staticflickr.com/5/4792/26832623288_6ae176bcbd_z.jpg"  
link="https://c1.staticflickr.com/5/4792/26832623288_6ae176bcbd_z.jpg"  
caption="Use a simple spreadhseet to keep track of progress on tasks"
 class="figimg"
>}}


Only the developer doing the work should estimate the effort. **This is important**. Individual developers are not fungible, swappable units. Any business that has one person produce the estimate and another person do the coding will be much less successful at estimating than one in which the estimation is produced by the developer.

This can be a difficult thing to organise. Perhaps the developers who will be creating the code have not yet been assigned to the project. But for an effective estimate it really is advisable.

It's important to keep track of the initial estimate and the revised estimate as work proceeds. Estimates *will* change, this is a fact of software development. As long as the information about that is clear, project managers and the business as a whole can take steps to accommodate it. If you're keeping a revised estimate as you proceed your spreasheet should be giving you the best current estimated schedule of delivery, even if that has changed substantially from the initial estimate.

{{% blocktext %}}
I'll talk about *why* software projects are so difficult to estimate a little later but the fact of the matter is that they *are*. Any company that wants to succeed in software development has to acknowledge this fact and manage it.  
{{% /blocktext %}}


Do not forget to add time for integration, testing, deployment, QA and so on. 

Now the little twist I mentioned: **Do not let a manager reduce the estimate**.

Managers revise estimates or lean on developers to reduce them because they do not understand the difference between an [**estimate**, a **committment** and a **target**](/estimation/estimate_target_commit/). Sometimes they want the estimate to meet a target and think they can achieve that magically by fiddling numbers in the *estimate* spreadsheet rather than by *managing* the project. Sometimes they think they can motivate software developers by giving them challenging targets (and of course confuse estimate and target).  

This is just inept management. 

Here's a way it worked for me a long time ago in a software house in London. Developers would produce estimates using an in-house and very effective process. The numbers would be handed to the sales team. If the sales team thought the estimate was too high for the amount of money the potential client as willing to spend then they had some leeway to *reduce the daily cost* of a developer. It was understood that a committment and an estimate were two very different things and that an estimate was useful and thoughtfully-produced data that shouldn't be ignored or overwritten.

You *can* force a higher work-rate from a team. For a while. Then they'll leave for other jobs that allow them to get home to see their families. If you need to cut the schedule you will have to *drop features*. 

So: this is one way of producing estimates. It's a little simple and a little old-fashioned now. Next up: Monte Carlo Simulation.

