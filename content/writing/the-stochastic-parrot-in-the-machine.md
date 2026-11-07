---
date: 2026-11-07T18:00:00+00:00
lastmod: 2026-11-07T18:00:00+00:00
title: "The Stochastic Parrot in the Machine"
description: "What confabulation in human minds and large language models might reveal about the nature of cognition, and why our errors may be as revealing as our successes."
authors: ["david"]
draft: false
categories:
  - articles
tags:
  - artificial intelligence
  - large language models
  - cognition
  - cognitive science
  - psychology
  - confabulation
  - philosophy of mind
topics:
  - Technology and computing
  - Society and ideas
slug: the-stochastic-parrot-in-the-machine
---

{{% pagedescription %}}
Large language models have become remarkably capable, and their achievements can be measured without any settled understanding of how those capabilities arise. They write software, translate languages, solve problems and produce sustained arguments with a competence that would have seemed improbable only a few years ago. Their success is established through performance, independently of any claim that they think as humans do. Indeed, there is good reason to be cautious about making such a claim.
{{% / pagedescription %}}


The history of psychology is littered with attempts to explain the human mind through the most sophisticated machinery of the age. Descartes employed hydraulic mechanisms to account for bodily and nervous functions. The nineteenth century supplied steam engines and models of energy and pressure, which found their way into theories of mental activity. In the twentieth century, the digital computer furnished cognitive science with the concepts of information processing, storage and computation. Some of these analogies proved remarkably productive, but their history should make us wary of assuming that the latest technological achievement has finally disclosed the principles of human thought.

There is a further reason for caution. We understand how language models are constructed and trained, yet our understanding of the processes underlying their particular capabilities remains incomplete. Their extraordinary performance has not depended upon establishing a functional correspondence with the human brain. We can recognise intelligence in their outputs, or at least capabilities traditionally associated with intelligence, without first settling how those capabilities are produced. Yet an unexpected resemblance emerges when we turn from their successes to their failures.

One of the characteristic defects of language models is hallucination: the production of plausible, fluent and sometimes elaborate falsehoods. More interesting for present purposes is their tendency to confabulate, constructing convincing explanations for answers whose actual causes those explanations fail to identify. There are well-documented parallels in human psychology, and some of the most revealing come from experiments in which the causes of behaviour have been deliberately concealed from the person producing it.

In the 1970s, Michael Gazzaniga and Joseph LeDoux investigated patients whose cerebral hemispheres had been surgically disconnected to treat severe epilepsy. In one celebrated experiment, a patient was shown a chicken claw in one visual field and a snowy landscape in the other, so that each hemisphere received different information. Asked to select related pictures, the patient chose a chicken with one hand and a shovel with the other. Both selections were entirely appropriate. But when asked to explain them, the speaking left hemisphere, which had seen the chicken claw but had no access to the snowy landscape, explained that the shovel was needed to clean out the chicken shed.

The explanation was coherent, immediate and false. Gazzaniga proposed the existence of a left-hemisphere *interpreter*, which constructs intelligible accounts of behaviour from whatever information is available to it. The experiment exposed a distinction between the processes that produce an action and those that subsequently explain it. [1]

Related phenomena have been investigated through post-hypnotic suggestion. Participants can be given suggestions intended to influence their subsequent behaviour or experience, sometimes accompanied by instructions to forget the source of the suggestion. In a 1993 experiment, Philip Zimbardo, Stephen LaBerge and Lynn Butler induced physiological arousal through post-hypnotic suggestions. Highly hypnotisable participants who experienced the arousal without remembering its suggested origin sometimes misattributed its cause. [2]

Subsequent work by Rochelle Cox and Amanda Barnier demonstrated that hypnotically suggested amnesia could also induce confabulation about autobiographical information. [3] The mechanisms of hypnosis remain contested, and responses vary considerably between individuals. Nevertheless, these experiments provide controlled examples of people constructing interpretations or memories when relevant causal or autobiographical information is inaccessible.

The parallel with language models becomes more specific when they are asked to explain their own reasoning. In 2023, Miles Turpin and colleagues demonstrated that introducing biases into a model's prompt could systematically influence its answers without those influences appearing in its subsequent explanations. The models frequently supplied plausible reasoning that rationalised the resulting answers. [4]

Here, then, are biological and artificial systems which, under certain conditions, produce convincing explanations that misrepresent the processes responsible for their outputs. Given their profoundly different architectures, why should their failures exhibit this resemblance?

There is a further observation available through ordinary introspection. In spontaneous conversation, particularly when arguing or responding rapidly to someone else's remarks, thoughts and sentences seem simply to arrive. We may know what we intend to communicate, but we seldom experience ourselves consciously assembling the sequence of words through which the thought is expressed. The processes that produce fluent speech are largely hidden from us.

This limitation is familiar in experimental psychology. In their influential 1977 paper, *Telling More Than We Can Know*, Richard Nisbett and Timothy Wilson argued that people often lack direct introspective access to the higher-order processes influencing their judgements. Asked to explain their responses, they may draw upon plausible causal theories rather than knowledge of the processes actually involved. [5]

Perhaps, then, the significance of confabulation extends beyond the unusual circumstances in which it can be demonstrated experimentally. It may expose a process that contributes to ordinary, successful cognition: the generation of coherent interpretations from learned relationships, contextual information and incomplete knowledge. When the available information corresponds sufficiently well to the causes of an action, the resulting explanation may be accurate. When crucial information is missing, the same capacity may produce an invention.

This raises the possibility of reversing the familiar comparison between artificial intelligence and the human brain. Instead of asking whether language models reproduce the processes of human cognition, we might ask whether significant aspects of human cognition operate in ways resembling those of language models.

Such a hypothesis would require considerably more evidence to establish shared computational mechanisms. Similar behaviour can arise from different processes. Nor does the suggestion attempt to account for consciousness, subjective experience or the entirety of cognition. Its scope is the generation of thought, language and explanation, particularly where access to their underlying causes is limited.

In 2021, Emily Bender and her colleagues published *On the Dangers of Stochastic Parrots*, questioning the attribution of meaning and understanding to language models trained to generate statistically plausible sequences of words. [6] The phrase became a memorable expression of scepticism about machine intelligence. Yet the performance of increasingly large models, developed through extensive training and iterative refinement, has demonstrated how much sophisticated behaviour can arise from processes of statistical learning and generation.

We began with good reasons to resist the temptation to explain the brain through the latest fashionable technology. Those reasons remain. But the unexpected similarities in confabulation, together with the limited access we possess to the origins of our own thoughts, invite a different speculation. Perhaps some substantial part of human cognition operates through processes more closely resembling statistical generation than we have supposed.

If so, the stochastic parrot may eventually prove as revealing a description of something in ourselves as it was intended to be a criticism of artificial intelligence.

## References

1. Gazzaniga, M. S., and LeDoux, J. E. (1978). *The Integrated Mind*. Plenum Press. See also Gazzaniga, M. S. (2000), [Cerebral specialization and interhemispheric communication: Does the corpus callosum enable the human condition?](https://doi.org/10.1093/brain/123.7.1293), *Brain*, 123(7), 1293–1326.
2. Zimbardo, P. G., LaBerge, S., and Butler, L. D. (1993). [Psychophysiological consequences of unexplained arousal: A posthypnotic suggestion paradigm](https://doi.org/10.1037/0021-843X.102.3.466). *Journal of Abnormal Psychology*, 102(3), 466–473.
3. Cox, R. E., and Barnier, A. J. (2015). [A hypnotic analogue of clinical confabulation](https://doi.org/10.1080/00207144.2015.1031037). *International Journal of Clinical and Experimental Hypnosis*, 63(3), 249–273.
4. Turpin, M., Michael, J., Perez, E., and Bowman, S. R. (2023). [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html). *Advances in Neural Information Processing Systems*, 36.
5. Nisbett, R. E., and Wilson, T. D. (1977). [Telling More Than We Can Know: Verbal Reports on Mental Processes](https://doi.org/10.1037/0033-295X.84.3.231). *Psychological Review*, 84(3), 231–259.
6. Bender, E. M., Gebru, T., McMillan-Major, A., and Shmitchell, S. (2021). [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://doi.org/10.1145/3442188.3445922). *Proceedings of ACM FAccT 2021*, 610–623.
