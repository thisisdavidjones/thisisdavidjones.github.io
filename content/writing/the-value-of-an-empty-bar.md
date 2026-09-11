---
date: 2026-09-10T08:00:00+01:00
lastmod: 2026-09-10T08:00:00+01:00
title: "The Value of an Empty Bar"
description: "Why deliberate reserve capacity helps transformation programmes respond to discoveries, manage uncertainty and keep work moving."
authors: ["david"]
draft: false
categories:
  - articles
tags:
  - business
  - transformation
  - capacity planning
  - queueing theory
  - architecture
topics:
  - Technology and computing
  - Society and ideas
slug: the-value-of-an-empty-bar
---

In music, a rest is written down. It begins at a particular point, lasts for a specified time and ends when the player is needed again. One instrument may be silent while the rest of the orchestra carries on. No conductor looks at a bar’s rest and wonders whether the oboe could be given a few extra notes to improve utilisation. The silence is part of the composition.

Put the equivalent into a transformation plan and it looks rather different. An unallocated week attracts attention; a specialist with a blank afternoon appears to be a resource awaiting better management. Before long, every box is coloured in and every available hour has somewhere to go. The plan looks impressively complete. It also assumes that doing the work won’t teach us much that we didn’t know when we planned it.

Consider a hypothetical migration rehearsal. Two systems that should produce the same balance don’t. The difference is small enough to have escaped earlier analysis and large enough to prevent sign-off. Finding the cause needs two people: a data specialist who understands the reconciliation rules and somebody who knows an old interface through which some of the records have passed.

The investigation might take half a day. Getting that half-day can take two weeks. Both specialists have been allocated efficiently elsewhere, and there’s no common slot before a decision that depends on their findings. The migration team can wait, reshuffle its work or carry on with an uncertainty that the rehearsal was designed to uncover.

There’s nothing pathological about this. Mature estates contain old interfaces, obscure dependencies and bits of business logic whose full consequences emerge only when systems are exercised together. A rehearsal that exposes one of them has succeeded. The question is whether the organisation has left itself any means of responding to what it has learned.

Queueing theory explains why a small piece of unexpected work can produce a much larger delay. When arrivals and task durations vary, a heavily loaded resource has little ability to absorb another demand. As utilisation approaches capacity, waiting times can rise very sharply. The familiar principle from roads, call centres and airport security applies just as readily to the one person who understands an elderly settlement interface.

That changes what we ought to measure. A scarce specialist who is busy 95 per cent of the time may look wonderfully productive on a resource report while several programmes spend days waiting for the remaining five per cent. Booking that person more thoroughly can improve the utilisation figure while making delivery slower.

Capacity is also stubbornly specific. Ten free architects don’t add up to one available data specialist when the problem lies in reconciliation logic. Spare development capacity doesn’t help much when what’s missing is a decision from the person authorised to accept a risk. Estate-wide averages conceal the shortages that matter. The useful questions concern particular skills and dependencies: how variable is demand for them, how readily can somebody substitute, and what happens elsewhere when they aren’t available?

Transformation makes this especially important because much of the work is designed to produce new information. We test, rehearse, profile data and review architectures because we expect to discover things, including that some of our assumptions were wrong.

Toyota’s *jidoka* principle joins detection to intervention: when an abnormality appears, the process can stop so the problem is dealt with rather than carried downstream. The parallel is useful because discovery alone isn’t much of a capability. If every important finding triggers a negotiation over whose existing commitment must be broken, the organisation has become better at seeing problems than at responding to them.

That suggests a better way to think about reserve capacity. It’s part of the organisation’s ability to use what it learns. Without it, discovery carries a penalty: investigate later, downgrade the issue, keep moving, or accept a workaround because the people required for the proper answer are elsewhere. Nobody needs to tell a team to suppress bad news. A sufficiently tight plan can create the incentive on its own.

The objection is obvious. Spare capacity costs money, and “contingency” can become a respectable name for work that hasn’t been thought through. Recurring operational demand belongs in the plan, as do dependency analysis, migration rehearsals and data profiling.

Engineering margins offer a more disciplined model for what remains uncertain. NASA explicitly carries allowances in cost, schedule and technical performance to account for uncertainty and risk, and manages them as knowledge develops. The important idea isn’t a particular percentage. It’s that the margin exists for a reason and doesn’t become ownerless empty space waiting to be colonised.

Capacity can be treated the same way. Keep reserve where uncertainty and dependency risk make additional work plausible. Be clear about what may call on it and who decides. Review its use, release it where understanding has improved and increase it where new risks appear. And don’t confuse capacity with schedule. Moving a milestone two weeks to the right doesn’t create two hours next Tuesday from the only person who understands the data model.

When I look at a transformation plan as an architect, I therefore want to know more than whether its milestones join up and its resource chart balances. Which people and decisions sit across several delivery paths? What happens when a rehearsal disproves an assumption? Where can unexpected work be absorbed, and how long do important findings wait before somebody can act on them?

There are useful measures here too. Alongside milestones and completion percentages, look at blocked time, the age of unresolved findings, queues around scarce specialists and repeated rework. Those tell you something a utilisation chart can’t: whether the organisation is making progress or merely keeping everybody busy while they wait for one another.

A rest in music isn’t unused time. It has a place, a duration and a purpose, while the composition continues around it. The empty spaces in a credible transformation plan should be just as deliberate.

So the useful question isn’t how much spare capacity a programme ought to have. It’s this: when the next important discovery arrives, where is the room to do something about it?

