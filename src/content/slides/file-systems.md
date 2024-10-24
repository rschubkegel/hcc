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

--

### Floating Point Numbers

_sign field_ | _exponent field_ | _significand field_

```py
  1 # 0 01111111 00000000000000000000000
100 # 0 10000101 10010000000000000000000
255 # 0 10000110 11111110000000000000000
```

---

## Storing Files

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnVpbjFhcHJ6bjEwdWRpZ2J6bncyZm95NWFwNHdyczV0azE1dmdiZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/aeqpymkqoW3BAiqboo/giphy.webp) <!-- .element: style="height:400px" -->

--

### Text Files (.txt)

![](/2024/fall/computer-science/images/text-file-hex.png)

--

### Image Files (.png)

<!-- ![](https://media4.giphy.com/media/l3vRgqJIdbRp7Exfa/giphy.webp?cid=ecf05e47a34t62sv5yvah3uezolo0suywz2vy0mqbc0typyd&ep=v1_gifs_search&rid=giphy.webp&ct=g) -->

![](/2024/fall/computer-science/images/image-file-hex.png) <!-- .element: style="height:400px" -->

--

## Image Files

![](https://www.ionos.com/digitalguide/fileadmin/_processed_/0/6/csm_what-is-a-pixel-the-arrangement-of-subpixels_3fe7466f5f.webp) <!-- .element: style="height:400px" -->

NOTES:
- If all three primary colors have the maximum value of 255, white appears
- The values in between allow around 16.7 million shades of color (2563) to be displayed

<!-- https://www.ionos.com/digitalguide/websites/web-design/what-is-a-pixel/ -->

---

## File Systems

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTViaWo3N2IxdWxsdTZjMTh5dXRrMXFpYzZhNXA0cTJ3dHJmd3FkeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SuEFqeWxlLcvm/giphy.webp) <!-- .element: style="height:400px" -->

NOTES: in a previous quiz, you were asked how you would organize a library. This is the difficult question behind file systems.

--

### Considerations

- Performance
- Integrity
- Scalability
- Compatibility
- Security

NOTES:
- Faster w/large files or many small files?
- Checksums or redundancy?
- What happens when you add more storage?
- Not all computers use the same
- Encryption, permissions, etc.

<!-- https://hivo.co/blog/a-tour-of-file-system-types-choosing-the-right-fit-for-your-needs -->

--

### Common Types

- FAT (File Allocation Table)
- NTFS (New Technology File System)
- ext4 (Fourth Extended File System)
- APFS (Apple File System)

NOTES:
- NTFS most common for Windows
- APFS most common for macOS
- ext4 most common for Linux

--

### Types of Files

- File (data)
- Directory (folder)

--

### Paths

Windows: `C:\Users\Rylan`

Unix: `/Users/Rylan`

--

### Fragmentation

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2F0QUvYwNaeFs%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=ca2485f480a020fb7204a36fee820836bdfcfb29145f5fe914a09d880f02a9c0&ipo=images) <!-- .element: style="height:400px" -->

NOTES:
- _Spatial_ (reference) locality is how close files are
- Takes longer to get to your aunt's house than your friend's
- Keep it closer to keep it fast
- Defragmentation re-organizes to keep common stuff close
- Other options include _temperal_ locality

--

### Review

Are all file systems the same? _No!_ <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

What are some considerations when picking a file system? _Performance, integrity, scalability, compatibility, security._ <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

What is a file path? _All folders plus the file name._ <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

What is fragmentation and why is it bad? _Separation of files, slows down R/W operations._ <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

---

## Now for Some Coding... <!-- .element: class="r-fit-text" -->

[Python: Reading/Writing Files](/2024/fall/computer-science/slides/python-files)
