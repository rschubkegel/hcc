---
title: 'CS - File Systems'
date: 2024-10-31
---

# Reading & Writing Files <!-- .element: class="r-fit-text" -->

Week 9

---

## Review

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3c0YmhoMm9tcjRmZzlvaWdydWI4enAyZWltMGcwbHlobjM4NzBweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/777Aby0ZetYE8/giphy.webp) <!-- .element: style="height:400px" -->

--

### How Does a Computer Store Information? <!-- .element: class="r-fit-text" -->

It represents all data with **binary** numbers and organizes it into **files**.
<!-- .element: class="fragment" -->

--

### Storage vs. Memory

**Storage** is _persistent_, **memory** is _volatile_.
<!-- .element: class="fragment" -->

---

## Bits and Bytes

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmQxMjc5eHRkOXF0MmxocmswdXBqaXEwM3IyMDFsemgwbWt1bHZwOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZBtlT7yNCDCrD0mqVm/giphy.webp) <!-- .element: style="height:400px" -->

--

### Bits

A bit is a single binary digit: either 0 or 1.

--

### Bytes

A byte is 8 bits.

`00000000` is 0 in decimal
<!-- .element: class="fragment" -->

`11111111` is 255 in decimal
<!-- .element: class="fragment" -->

NOTES: why 8? because it's a power of 2 (2^3)

--

### Bigger Numbers

- B = byte
- KB = kilobyte (1000 B)
- MB = megabyte (1000 MB)
- GB = gigabyte (1000 MB)
- TB = terabyte (1000 GB)

NOTES: there are higher numbers like petabyte but they aren't as common

--

### Kilobits vs. Kilobytes

8 kilobits = 1 kilobyte

1Kb = 1/8 KB = 0.125 KB

<!-- https://www.lifewire.com/what-is-a-megabit-2483412 -->

--

### Kibibytes vs. Kilobytes

A “kibibyte” (KiB) is equal to 1024, or 2^10, bytes

<!-- https://www.logicmonitor.com/blog/what-the-hell-is-a-kibibyte -->

--

### Review

How many bits in a byte? _8_ <!-- .element: class="fragment" -->

How many bytes in a kilobyte? _1000_ <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

Is Kb the same as KB? _No!_ <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

Is KiB the same as KB? _No!_ <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

---

## Storing Primitives

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmtiYWVtbWpmZGR4ZTB6MG9vcjBoeWtkdnRmaWRlYm95NGdlMzNnaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT9C25UNTwfZuk85WP/giphy.webp) <!-- .element: style="height:400px" -->

--

### Booleans

```py
True  # 1
False # 0
```

--

### Integers

```py
  1 # 00000001
100 # 01100100
255 # 11111111
```

What about negative numbers? <!-- .element: class="fragment" -->

--

### Signed Integers

```py
   1 # 00000001
 100 # 01100100
-100 # 10011100
-127 # 10000001
 127 # 01111111
```

---

## Text Files

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnVpbjFhcHJ6bjEwdWRpZ2J6bncyZm95NWFwNHdyczV0azE1dmdiZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/aeqpymkqoW3BAiqboo/giphy.webp) <!-- .element: style="height:400px" -->

<!-- TODO -->

---

## Image Files

![](https://media4.giphy.com/media/l3vRgqJIdbRp7Exfa/giphy.webp?cid=ecf05e47a34t62sv5yvah3uezolo0suywz2vy0mqbc0typyd&ep=v1_gifs_search&rid=giphy.webp&ct=g) <!-- .element: style="height:400px" -->

<!-- TODO -->

---

## File Systems

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTViaWo3N2IxdWxsdTZjMTh5dXRrMXFpYzZhNXA0cTJ3dHJmd3FkeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SuEFqeWxlLcvm/giphy.webp) <!-- .element: style="height:400px" -->

<!-- TODO -->
