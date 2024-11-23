---
title: 'Hello World'
date: 2024-09-12
---

# Computer Science

Fall 2024

Rylan Schubkegel

---

## About Me

⬇️⬇️⬇️

--

### Education

- Homeschooled <!-- .element: class="fragment" -->
- Skagit Valley College <!-- .element: class="fragment" -->
- George Fox University <!-- .element: class="fragment" -->

NOTES:
- Homeschooling expeiences included:
  - First Class Co-op (Friday School)
  - Skagit Defenders Speech & Debate
- I attended Skagit Valley College through Running Start.
- I got my BS in Computer Science from GFU in 2022.

--

### Interests

- Game Development <!-- .element: class="fragment" -->
- Dancing <!-- .element: class="fragment" -->
- Townball <!-- .element: class="fragment" -->

---

## About _You_

- Education
- Interests
- Why are you taking this class?

NOTES:
- Were you always homeschooled?
- What do you like to do _outside of school_?
- Did you sign up on your own accord?

---

## About This Course

⬇️⬇️⬇️

--

### Resources

[Course Site](/2024/fall/computer-science/)

NOTES:
- Course resources are generic to the whole course
- Weekly resources are specific to each week

--

### Syllabus Review

[Syllabus](/2024/fall/computer-science/syllabus)

NOTE:
- Course goals are _not_ just programming
- **Make sure to emphasize assignment expectations**

---

## Enough of the boring stuff...

![](https://i.giphy.com/lSxpaFCtsOUpfiBYUV.webp) <!-- .element: style="height:400px" -->

---

## What is a Computer?

⬇️⬇️⬇️

NOTE: if there are no guesses, encourage "wrong answers only"

--

All computers have four roles:

- Input <!-- .element: class="fragment" -->
- Storage <!-- .element: class="fragment" -->
- Processing <!-- .element: class="fragment" -->
- Output <!-- .element: class="fragment" -->

NOTE: Have students give examples of each

--

Computers are **general purpose**

NOTES: Not ell electronics are computers; for example:
- Power tools
- Traffic lights
- Ultrasound machines

--

Digital computers have **hardware** and **software**

--

Computers are **fast**

<div class="r-stack">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/ENIAC_Penn1.jpg/2560px-ENIAC_Penn1.jpg" alt="" height="400" class="fragment current-visible">
  <img src="http://www.columbia.edu/cu/computinghistory/608.jpg" alt="" height="400" class="fragment current-visible">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/be/Deep_Blue.jpg" alt="" height="400" class="fragment current-visible">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/IPhone_First_Generation_8GB_%283677961514%29.jpg" alt="" height="400" class="fragment current-visible">
  <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.4gamers.com.tw%2Fckfinder%2Ffiles%2FElvis%2FReview%2FIntel-Core-i9-13900K-and-i5-13600K%2F09.jpg&f=1&nofb=1&ipt=785ddb2ac1553a4c55302bcb1fee3c97e6b790a53666d0062f5e0ec7cd0272b2&ipo=images" alt="" height="400" class="fragment current-visible">
</div>

How many instructions can be executed per second?

NOTES:
- ENIAC (1945): 5,000
- IBM 608 (1957): 4,500
- Deep Blue (IBM, 1997): 120,000,000 (per CPU)
- iPhone 1 (2007): 620,000,000
- Intel Core i9 (2024): 6,200,000,000

--

Moore's Law

The number of transistors on a microchip doubles approximately every two years.

![](/2024/fall/computer-science/images/moores-law-graph.jpg) <!-- .element: style="height:400px" -->

NOTES:
Proposed by Gordon Moore, co-founder of Intel, in 1965.
This has been true for around 50 years (up to ~2015).

---

## Instructing a Computer

⬇️⬇️⬇️

--

Computers are **dumb**

NOTE: They do not think for themselves; they do exactly what they are told

--

Exercise: Tie a Shoe

NOTES:
- Have students "write a program" to tie a shoe.
- Demonstrate that the program needs _very specific_ instructions.

--

The Language of Computers

Binary <!-- .element: class="fragment" -->

NOTES:
- As opposed to:
  - Decimal
  - Hexadecimal

--

Exercise: Binary Arithmetic

NOTE: Demonstrate counting, adding, and subtracting

--

Levels of Abstraction

- Machine code <!-- .element: class="fragment" -->
- Assembly language <!-- .element: class="fragment" -->
- Low-level <!-- .element: class="fragment" -->
- High-level <!-- .element: class="fragment" -->

NOTES:
- Binary
- x86, ARM, MIPS
- C, Rust
- Python, JavaScript, C#, Swift

--

Machine Code (binary)

```
0110 1000 0010 0001 0000 1010 0000 0000
1010 0011 0000 1101 0000 0000 0000 0110
0110 1000 0110 1111 0111 0010 0110 1100 0110 0100
1010 0011 0000 1000 0000 0000 0000 0110
0110 1000 0110 1111 0010 1100 0010 1000 0101 0111
1010 0011 0000 0100 0000 0000 0000 0110
0110 1000 0100 1000 0110 0101 0110 1100 0110 1100
1010 0011 0000 0000 0000 0000 0000 0110
1011 0000 0000 0000 0000 0000 0000 0110
1011 0000 0000 0000 0000 0000 0000 0000
1011 0000 0000 0000 0000 0000 0000 0001
0110 1000 0000 0100 0000 0000 0000 0000
1100 1101 1000 0000
0110 1000 0000 0001 0000 0000 0000 0000
1100 1101 1000 0000
```

--

Assembly (RISC)

```asm
.data
hello:
    .asciiz "Hello, World!\n"

.text
main:
    li a0, 4
    la a0, hello
    li a7, 4
    ecall
    li a7, 10
    ecall
```

--

Low-Level Language (C)

```c
int main() {
  printf("Hello, World!\n");
  return 0;
}
```

--

High-Level Language (Python)

```py
print("Hello, World!")
```

---

## Coming Up...

⬇️⬇️⬇️

--

### Homework

- Videos <!-- .element: class="fragment" -->
- Quiz <!-- .element: class="fragment" -->
- Projects <!-- .element: class="fragment" -->

--

### Next Class

Online

NOTES:
- Platform determined by what students responded to in intro survey
- Check out Chromebook and meet in student center, or join from home!

--

## Have a good week!