---
title: 'CS - Computer Graphics'
date: 2024-12-05
---

# Computer Graphics <!-- .element: class="r-fit-text" -->

Week 13

---

## Screens and Pixels

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDRtN3piOG10dnh3Z3ZqdWhnZWFoZGE5cnRwYnJtM2V4dGs0N3Q2dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPGcIho4Ca3QP90sg/giphy.webp) <!-- .element: style="height:400px" -->

--

### Coordinates

![](https://inventwithpython.com/invent4thed/images/00013.jpeg) <!-- .element: style="height:400px" -->

--

### Why Inverted?

Computer coordinates are often inverted

(y-axis pointing downwards)

NOTES:
- First graphics terminals used origin at the top-left corner of the screen due (largely) to the way CRT monitors scanned the image from top to bottom
- Using a coordinate system with the y-axis pointing downwards makes it easier to **render text** correctly.

--

### Resolution

Resolution is the number of pixels in each dimension

Written as "w x h" or "w / h"

### Common Resolutions

- 720p / HD: 1280×720 px
- 1080p / FHD: 1920x1080 px
- 1440p / QHD: 2560×1440 px
- 2160p / UHD: 3840×2160 px
- 4K: 4096×2160 px
- 8K: 7680×4320 px

NOTE:
- HD = High Definition
- FHD = Full HD
- QHD = Quad HD
- UHD = Ultra HD
- Total number of pixels in 720p is 921,600 px while 1080p is 2,073,600 px
- Total number of pixels in 4K is 8,847,360 px and 8K is 33,177,600 px

---

## Colors

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW5kaHJrZWI2YTM3ZTMzeDdnc2wydWI4eWVvamI5NGs1eXdsd2h0ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xThuWcaa4U4XZQDgvm/giphy.webp) <!-- .element: style="height:400px" -->

--

### RGB

Red, Green, Blue

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.ZTm2jZXrmUvQnTlnv2MLtQHaHA%26pid%3DApi&f=1&ipt=81607bcb78cdf7e34a6efd1befe363a4c7a7d3090a6b389c86243deff0304a8f&ipo=images) <!-- .element: style="height:400px" -->

NOTE: these are called "channels"

--

### Example Values

- Red: (255, 0, 0)
- Green: (0, 255, 0)
- Blue: (0, 0, 255)
- White: (255, 255, 255) <!-- .element: class="fragment" -->
- Black: (0, 0, 0) <!-- .element: class="fragment" -->

--

### Bits and Bytes

- How many bits in a byte? _8_ <!-- .element: class="fragment" -->
- How many numbers in a byte? _256_ <!-- .element: class="fragment" -->

--

### Hexadecimal

Hexadecimal is a base-16 number system

0 = 0
9 = 9
10 = A
15 = F

--

### Colors in Hex

- Red: #FF0000
- Green: #00FF00
- Blue: #0000FF

--

### Transparency

- RGBA (Red, Green, Blue, Alpha)
- Alpha: 0 = transparent, 255 = opaque

- Red (RGBA): (255, 0, 0, 255)
- Red (Hex): #FF0000FF

---

## Review

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTY2YjdrYzd1OGJxZHZvZHY4Ymtmc295OTdpMDJnNWFkdzk3MGV4MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eKaX6IsR3z5Rev2E8A/giphy.webp) <!-- .element: style="height:400px" -->

--

### Where is the origin?

Top-left corner (0, 0) <!-- .element: class="fragment" -->

--

### What is "resolution"?

Resolution is the number of pixels in each dimension <!-- .element: class="fragment" -->

--

### What are the primary colors of light?

RGB (Red, Green, Blue) <!-- .element: class="fragment" -->

--

### How can you represent white in hex?

#FFFFFF <!-- .element: class="fragment" -->

--

### What does the "alpha" channel represent?

Transparency <!-- .element: class="fragment" -->

---

## Now for Some Coding... <!-- .element: class="r-fit-text" -->

[Intro to Pygame](/2024/fall/computer-science/slides/pygame)
