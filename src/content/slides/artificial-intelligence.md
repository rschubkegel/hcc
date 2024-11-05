---
title: 'CS - Artificial Intelligence'
date: 2024-10-10
---

# Artificial Intelligence <!-- .element: class="r-fit-text" -->

Week 6

---

## Review

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzE0d2dsZGltMmdjaGFmN2NhMHZmYWY0a2o1eXJ3czJtcG54MXR1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wvt3tpE4FAKZcGJnkR/giphy.webp) <!-- .element: style="height:400px" -->

--

### Can any computer be a server?

Yes!
<!-- .element: class="fragment" -->

A server is just a **role**.
<!-- .element: class="fragment" style="opacity:0.75;font-size:0.8em;" -->

--

A server is a computer that _provides_ resources over a network.
<!-- .element: style="opacity:0.75;font-size:0.8em;" -->

### What _consumes_ the server resources?

A **client**.
<!-- .element: class="fragment" -->

--

### Is the cloud the same as a server?

No!
<!-- .element: class="fragment" -->

The cloud is a _collection of servers_.
<!-- .element: class="fragment" style="opacity:0.75;font-size:0.8em;" -->

--

### Does the cloud need WiFi?

No!
<!-- .element: class="fragment" -->

It does need an internet connection, but not necessarily a WiFi connection.
<!-- .element: class="fragment" style="opacity:0.75;font-size:0.8em;" -->

---

## ~~Artificial~~ Intelligence

![](https://i.giphy.com/d3mlE7uhX8KFgEmY.webp) <!-- .element: style="height:400px" -->

--

### What is Intelligence?

It's hard to define.
<!-- .element: class="fragment" -->

Intelligence is a _suitcase word_.
<!-- .element: class="fragment" style="opacity:0.75;font-size:0.8em;" -->

--

> A word that "contain a variety of meanings packed into them."

<cite hidden>https://alexvermeer.com/unpacking-suitcase-words/</cite>

Coined by Marvin Minsky in _The Emotion Machine_.
<!-- .element: class="fragment" style="opacity:0.75;font-size:0.8em;" -->

--

Examples of suitcase words:

- Consciousness <!-- .element: class="fragment" -->
- Experience <!-- .element: class="fragment" -->
- Conscience <!-- .element: class="fragment" -->
- Thinking <!-- .element: class="fragment" -->
- Intelligence <!-- .element: class="fragment" -->

--

### Dimensions of Intelligence

- Logical <!-- .element: class="fragment" -->
- Verbal <!-- .element: class="fragment" -->
- Social <!-- .element: class="fragment" -->
- Emotional <!-- .element: class="fragment" -->

--

### Characteristics of Intelligence

- Understanding <!-- .element: class="fragment" -->
- Thinking <!-- .element: class="fragment" -->
- Interaction <!-- .element: class="fragment" -->

--

### For Our Purposes...

> Intelligent _agents_ precieve, reason, and act.

---

## Artificial Intelligence

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjRrNWs2YWNiaTF3NDBzYno5YW84MTZremRuZnZ3a2dnOHlpNThjYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y4PkFXkfTeEKqGBBsC/giphy.webp) <!-- .element: style="height:400px" -->

--

### Types of AI

- Symbolic <!-- .element: class="fragment" -->
- Neural Networks <!-- .element: class="fragment" -->

NOTES:
- Symbolic example: ruleset for medical diagnosis with reasoning.
- Most AI we interact with today is a neural network, including
  Large Language Models (LLM),
  Generative Adversarial Networks (GAN),
  and Convolutional Neural Networks (CNNs).

--

### Machine Learning

- Reinforcement Learning <!-- .element: class="fragment" -->
- Supervised Learning <!-- .element: class="fragment" -->

NOTES:
- Just like children, machine learning involes _teaching_.
- Learning involves repeition with rewards or penalties.
- To train computer vision models, hundreds of thousands of images must be labeled.

--

### Side Note: CAPTCHA

![](https://upload.wikimedia.org/wikipedia/en/8/80/Images_Recaptcha.png) <!-- .element: style="height:400px" -->

NOTES:
- CAPTCHA stands for Completely Automated Public Turing test to tell Computers and Humans Apart.
- Google's reCAPTCHA is a CAPTCHA that provides tons of free testing data.

--

### Large Language Models (LLMs)

- GPT <!-- .element: class="fragment" -->
- Gemini <!-- .element: class="fragment" -->
- Llama <!-- .element: class="fragment" -->

NOTES:
- LLMs are trained on vast amounts of data.
  They are very impressive and can beat humans at many tasks,
  including ranking in 90th percentile of bar exam (GPT-4).
  However, they are simply predicting what comes next
  based on patterns they've learned during training.
- OpenAI, Multimodal, Chatbot & API
- Google, Multimodal, Chatbot & API
- Meta, Just text, Open Source

---

## The Morality of AI

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3lzdnB5cjZsajlob3U0bjR4YXhtdWhjdnZ4eGVnZmNncWh6OHR0ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/h8UBzPFeCaTaXfheAz/giphy.webp) <!-- .element: style="height:400px" -->

--

### <span style="color:lightcoral">Immoral</span> Uses of AI

- Inappropriate Content <!-- .element: class="fragment" -->
- Phishing <!-- .element: class="fragment" -->
- Plagiarism <!-- .element: class="fragment" -->
- Impersonation <!-- .element: class="fragment" -->
- Fake News <!-- .element: class="fragment" -->

NOTE: AI is just a tool; in that sense it is amoral. The same code of conduct of other tools applies.

--

### <span style="color:lightgreen">Moral</span> Uses of AI

- Phishing Detection <!-- .element: class="fragment" -->
- Accessibility (HCI) <!-- .element: class="fragment" -->
- Censorship?? <!-- .element: class="fragment" -->

> Finally, brothers and sisters, whatever is true, whatever is noble, whatever is right, whatever is pure, whatever is lovely, whatever is admirable—if anything is excellent or praiseworthy—think about such things.
> 
> \- Philippians 4:8

--

### <span style="color:lightcoral">Immoral</span> Training of AI

- Biased Data <!-- .element: class="fragment" -->
- Privacy Violations <!-- .element: class="fragment" -->
- Non-consentual Data Collection <!-- .element: class="fragment" -->

NOTES:
- If the data contains biases, the AI model can learn and perpetuate those biases.
- If this data is not properly anonymized or protected, it can be used to identify individuals and violate their privacy.
- In many cases, data is collected from a variety of sources, including social media, public records, and other online sources, without the knowledge or consent of the individuals involved.

--

### <span style="color:lightgreen">Moral</span> Training of AI

> The fear of the Lord is the beginning of wisdom, and knowledge of the Holy One is understanding.
> 
> \- Proverbs 9:10

NOTES:
- Careful selection of training data
- Careful supervision of reinforcement learning
- Respecting others' privacy and dignity as fellow image-bearers (love thy neighbor)

---

## The Philosophy of AI

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWhjZnJzZ3BkaDY4emNtZm1zaHk1NHRxMXphaTByOG5ic2RjZWphOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0ID5AW1SmPuG3u0/giphy.webp) <!-- .element: style="height:400px" -->

--

### Identity <span style="color:lightcoral">Crisis</span>

> The development of full artificial intelligence could spell the end of the human race.
>
> \- Stephen Hawking
<!-- .element: class="fragment" style="font-size:0.6em" -->

> With artificial intelligence we are summoning the demon.
>
> \- Elon Musk
<!-- .element: class="fragment" style="font-size:0.6em" -->

> By 2100, our destiny is to become like the gods we once worshipped and feared. But our tools will not be magic wands and potions but the science of computers, nanotechnology, artificial intelligence, biotechnology, and most of all, the quantum theory.
>
> \- Michio Kaku
<!-- .element: class="fragment" style="font-size:0.6em" -->

NOTES: In the eyes of the world, AI jeopardizes our humanity. Some even say could lead to the end of the human race. But where do find our identity?

--

### Identity <span style="color:lightgreen">Stability</span>

> Then God said, “Let us make man in our image, after our likeness.” ...
>
> \- Genesis 1:26
<!-- .element: class="fragment" style="font-size:0.8em" -->

> The fear of the Lord is the beginning of knowledge; fools despise wisdom and instruction.
>
> \- Proverbs 1:7
<!-- .element: class="fragment" style="font-size:0.8em" -->

NOTES:
We find our identity in the workmanship of God.
We are divine image-bearers.
What is true, noble, and right is a reflection of God's character.
We can know God experientially, not just cognitively.

--

### Characteristics of Intelligence

- Understanding <!-- .element: class="fragment" -->
- Thinking <!-- .element: class="fragment" -->
- Interaction <!-- .element: class="fragment" -->

NOTE: AI falls short in many ways; understanding is deeper than symbol matching.

--

### The Chinese Room Argument

> A computer executing a program cannot have a mind, understanding, or consciousness, regardless of how intelligently or human-like the program may make the computer behave.
<!-- .element: class="fragment" style="font-size: 0.8em" -->
<!-- https://en.wikipedia.org/wiki/Chinese_room -->

NOTES:
The thought experiment starts by placing a computer that can perfectly converse in Chinese in one room, and a human that only knows English in another, with a door separating them.
Chinese characters are written and placed on a piece of paper underneath the door, and the computer can reply fluently, slipping the reply underneath the door.
The human is then given English instructions which replicate the instructions and function of the computer program to converse in Chinese.
The human follows the instructions and the two rooms can perfectly communicate in Chinese, but the human still does not actually understand the characters, merely following instructions to converse.
Searle states that both the computer and human are doing identical tasks, following instructions without truly understanding or "thinking".

--

### A Final Verse...

> They show that the work of the law is written on their hearts, while their conscience also bears witness, and their conflicting thoughts accuse or even excuse them...
>
> \- Romans 2:15
<!-- .element: class="fragment" style="font-size: 0.8em" -->

NOTES:
We are not just rational beings, but we are moral beings.
God has given us minds and souls.
By the grace of God, those who believe in Christ are given a heart of flesh instead of a heart of stone.

---

### Review

![](https://i.giphy.com/yNs2a0jRkYxy6191B2.webp) <!-- .element: style="height:400px" -->

--

### What is intelligence?

Perception, reasoning, and action.
<!-- .element: class="fragment" -->

--

### How does a machine learn?

Reinforcement with rewards and penalties.
<!-- .element: class="fragment" -->

--

### What does LLM stand for?

Large Language Model.
<!-- .element: class="fragment" -->

--

### Is AI immoral?

No.
<!-- .element: class="fragment" -->

Though it is very powerful, it is just a tool.
<!-- .element: class="fragment" style="opacity:0.75;font-size:0.8em;" -->

--

### How must we be careful with AI?

Usage and training.
<!-- .element: class="fragment" -->

We must use and train AI in a way that brings glory to God.
<!-- .element: class="fragment" style="opacity:0.75;font-size:0.8em;" -->

--

### Does AI have understanding?

No!
<!-- .element: class="fragment" -->

---

## Now for some coding... <!-- .element: class="r-fit-text" -->

[Python Modules](/2024/fall/computer-science/slides/python-modules)