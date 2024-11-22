---
title: 'CS - Operating Systems'
date: 2024-09-19
---

# Operating Systems & Python Basics <!-- .element: class="r-fit-text" -->

Week 3

NOTES:
- OS
- Storage
- Data Types
- Operators
- Loops

---

## WARNING: Today Will Cover a Lot <!-- .element: class="r-fit-text" -->

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDdmMm15dnFsYWxyNDQ0aTR1dnV0YW94NGt6NXVzNjdudjhmeDJjcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xULW8x4nFdoEntmTAI/giphy.webp) <!-- .element: style="height:400px" -->

NOTE: I fully expect you to revisit this slide deck for review

---

## What is an Operating System (OS)? <!-- .element: class="r-fit-text" -->

NOTE: Special piece of software that makes it easy for other software to communicate with hardware

--

### Device Drivers

- There is no universal language for hardware
- Device drivers allows reusable I/O code

--

### Multitasking

- Process scheduling
- Single core vs. multi-core

--

### User Management

- Developed from "Time-Sharing"
- Users and groups
- Privileges

--

### Memory Allocation

AKA "Virtual Memory"

- Simplifies memory management
- Prevent attacks like buffer overflow
- Allows some programs to have more memory

--

### File System

- Abstracts data to "files"
- Directory (folder) hierarchy
- File permissions

---

## Common Operating Systems <!-- .element: class="r-fit-text" -->

- Windows <!-- .element: class="fragment" -->
- MacOS <!-- .element: class="fragment" -->
- Linux <!-- .element: class="fragment" -->
- Android <!-- .element: class="fragment" -->
- iOS <!-- .element: class="fragment" -->

NOTES: Operating systems by market share:
- Android 45%
- Windows 25%
- iOS 18%
- macOS 5%
- Linux 1%
- Source: <a href="https://gs.statcounter.com/os-market-share/">gs.statcounter.com</a>

--

### Windows

![](https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/MSFT-PC-open-with-Start-menu-on-the-screen?scl=2) <!-- .element: style="height:400px" -->

NOTES:
- Made by Microsoft
- First version (Windows) 1985
- GUI on top of MS-DOS
- Versions:
  - Windows (for consumers)
  - Windows Server
  - Windows PE
  - Windows IoT

--

### macOS

![](https://www.apple.com/newsroom/images/2024/09/macos-sequoia-is-available-today/article/Apple-macOS-Sequoia-hero_big.jpg.large_2x.jpg) <!-- .element: style="height:400px" -->

NOTES:
- Made by Apple
- First version (Mac OS) 1984
- "Deliberately sought to minimize the user's awareness of the operating system" ([Wikipedia](https://en.wikipedia.org/wiki/Classic_Mac_OS))
- Uses different file system than Windows

--

### Linux

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.ubuntushop.be%2Fimages%2F751ubufront.png&f=1&nofb=1&ipt=964c9bf0d1bf902df6e3f1d7d94d4f5e75838c4f7a99beb96dd9b5e316c90e5c&ipo=images) <!-- .element: style="height:400px" -->

NOTES:
- Family of open-source OSs
- Some popular distributions (distros):
  - Ubuntu
  - Mint
  - Debian
  - Fedora
  - Arch
- Linux kernel used by Android and ChromeOS

---

## Persistent vs. Volatile Storage <!-- .element: class="r-fit-text" -->

--

### Persistent Storage

- AKA "permanent" storage
- Retained when computer is off <!-- .element: class="fragment" -->
- Cheap 💲 <!-- .element: class="fragment" -->
- Slow 🐢 <!-- .element: class="fragment" -->

--

### Common Types

<div class="r-stack">
  <img src="https://heirloom.cloud/cdn/shop/articles/64ee4ce0479e7649341854f3_rsz_18in_-_525_in_-_35_in_floppy_disks_adobestock_169862513_c644b2da-09d8-4259-8157-d7ae1e5b4623.jpg?v=1709917997&width=1200" alt="" height="400" class="fragment current-visible">
  <img src="https://www.findlight.net/blog/wp-content/uploads/2018/05/cant-eject-cd-laptop.jpg" alt="" height="400" class="fragment current-visible">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Laptop-hard-drive-exposed.jpg/800px-Laptop-hard-drive-exposed.jpg" alt="" height="400" class="fragment current-visible">
  <img src="https://www.backblaze.com/blog/wp-content/uploads/2016/03/blog-ssd-inside.jpg" alt="" height="400" class="fragment current-visible">
</div>

NOTES:
- Floppy disks (magnetic material) - ~500 KB/s
- Optical discs (use a physical medium with pits and lands) - ~72 MB/s (Blu-ray)
- Hard disk drives (HDD - magnetic) - ~300 MB/s
- Solid state drives (SSD - electrical charges and floating-gate transistors) - ~5000 MB/s

--

### Volatile Storage

- Temporary; lost when computer is turned off
- RAM is the most common volatile storage <!-- .element: class="fragment" -->
- Expensive 💲💲💲 <!-- .element: class="fragment" -->
- Fast 🐇 <!-- .element: class="fragment" -->

--

![](https://static.tvtropes.org/pmwiki/pub/images/812368b15a632ebc5ebd21fbb23a3689.jpg) <!-- .element: style="height:400px" -->

NOTES:
- DDR1 (Double Data Rate) released in 1998 - ~1.6 GB/s
- DDR5 (5th Generation) released in 2020 - ~51.2 GB/s

---

## Data Types

<ul class="fragment">
  <li>Primitive Data Types</li>
  <li>Compound Data Types</li>
</ul>

--

### Primitive Data Types

- Integer (int) <!-- .element: class="fragment" -->
- Floating Point Number (float) <!-- .element: class="fragment" -->
- String (str) <!-- .element: class="fragment" -->
- Boolean (bool) <!-- .element: class="fragment" -->
- NoneType (None) <!-- .element: class="fragment" -->

--

### Example

```py
100             # integer
3.14            # float
"Hello, World!" # string
True            # bool
None            # None
```

--

### Compound Data Types

- Lists <!-- .element: class="fragment" -->
- Tuples <!-- .element: class="fragment" -->
- Dictionaries <!-- .element: class="fragment" -->
- Sets <!-- .element: class="fragment" -->
- Objects (will revisit) <!-- .element: class="fragment" -->

--

### Example

```py
[1, 2, 3]             # list
(1, 2, 3)             # tuple
&lbrace;"one": 1, "two": 2&rbrace;  # dictionary
&lbrace;1, 2, 3&rbrace;             # set
```

---

## Operators

--

### Arithmetic Operators

```py
10 + 5 # 15
10 - 5 # 5
10 * 5 # 50
10 / 3 # 3.333
10 % 3 # 1
10 ** 5 # 100000
10 // 3 # 3
```

NOTES:
- Addition
- Subtraction
- Multiplication
- Division
- Modulus (remainder)
- Exponentiation
- Floor division

--

### Assignment Operators

```py
x = 5 # x = 5
x += 3 # x = x + 3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x %= 3 # x = x % 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3
```

NOTE: There are more for bitwise operators

--

### Comparison Operators

```py
10 == 5 # False
10 != 5 # True
10 &gt; 5 # True
10 &lt; 5 # False
10 &gt;= 5 # True
10 &lt;= 5 # False
```

NOTES:
- Equals
- Not equals
- Greater than
- Less than
- Greater than or equal to
- Less than or equal to

--

### Logical Operators

```py
total_minutes = 100
hours = total_minutes // 60
minutes = total_minutes % 60
seconds = total_minutes * 60
```

--

### Example

```py
number = 5
if number % 2 == 0:
    print("5 is even")
else:
    print("5 is odd")
```

--

### Example

```py
rylan_is_awesome = False
ava_is_awesome = True
if rylan_is_awesome and ava_is_awesome:
    print("Everyone is awesome!")
if ryan_is_awesome or ava_is_awesome:
    print("Someone is awesome!")
if not rylan_is_awesome:
    print("Ryan is not awesome 🥲")
```

---

## Loops

NOTES:
- Your "make a quiz" assignment was tedious.
- What if you were required to have 100+ questions?
- What if you could jump to another line of code to repeat it?

--

### GOTO

AKA "jump" statement

--

#### MIPS Example

```mips
loop_len:
  add     $t1, $t0, $a0        # calculate character address
  lb      $t2, 0($t1)          # load character from memory
  beq     $t2, $zero, exit_len # found null-terminating character
  addi    $t0, $t0, 1          # increment counter
  j       loop_len             # loop again
```

--

#### C Example

```c
void checkEvenOrNot(int num) 
&lbrace;
    if (num % 2 == 0)
        goto even;
    else
        goto odd;
even:
    printf("%d is even", num);
    return;
odd:
    printf("%d is odd", num);
&rbrace;
```

--

#### What Could Go Wrong?

- Code readability <!-- .element: class="fragment" -->
- Infinite loops <!-- .element: class="fragment" -->
- Security issues <!-- .element: class="fragment" -->

NOTE: Modern languages only use loops

--

### `while` Loops

- Anatomy:
  - Condition
  - Body

NOTE: Most basic type. All other loops based on this.

--

### Python Example

```py
answer = 0
guess = -1
while guess != answer:
    guess = int(input("Guess a number: "))
print("You got it!")
```

--

### Infinite Loop

```py
print("Hello, World!")
while True:
    print("Hello again!")
```

--

### `break` Statement

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDNzejVvZWtzdXcwZmFuZ2cyMW55YjA0MHoydWE3YTBrbzhjMGN2YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uHcghH7mo1LW9fFFEB/giphy.webp) <!-- .element: style="height:400px" -->

--

### Loop Until `q` Pressed

```py
print("Hello, World!")
while True:
    if input("Press q to quit ") == "q":
        break
    print("Hello again!")
```

NOTE: Good practice to avoid `break` statements

--

### Loop Until `q` Pressed

```py
print("Hello, World!")
should_continue = True
while should_continue:
    if input("Press q to quit ") == "q":
        should_continue = False
    print("Hello again!")
```

--

### `for` Loops

- Use with lists
- Syntactic sugar for `while` loops

--

### Example

```py
for student in ["Kylan", "Nash", "Micah"]:
    print("Hello, " + student)
```

--

### Example

```py
students = ["Kylan", "Nash", "Micah"]
index = 0
while index &lt; 3:
    print("Hello, " + students[index])
    index = index + 1
```

--

### Example

```py
for i in range(10):
    print(i)
```

---

## Blocks

- A group of statements <!-- .element: class="fragment" -->
- Lines must have same indentation <!-- .element: class="fragment" -->
- Can be nested <!-- .element: class="fragment" -->
- AKA "body" of a loop, function, class, etc. <!-- .element: class="fragment" -->

--

### Example

```py [1-7|4-7|5|7]
print("Hello, World!")
should_continue = True
while should_continue:
    if input("Press q to quit") == "q":
        should_continue = False
    else:
        print("Hello again!")
```

---

## Remember all that?

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmg4bHN4N2Z4OHN0NHh0OHhnZmk5cm95MndxenE1bmtmazIzdnRmOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gEvab1ilmJjA82FaSV/giphy.webp) <!-- .element: style="height:400px" -->

---

## Activity: Guess the Number <!-- .element: class="r-fit-text" -->

<a href="/2024/fall/computer-science/assignments/guess-the-number">Project Page</a>

NOTES:
- Make sure to go over basic list usage (see project page)
- Explain additional challenges
- Stop recording

---

## Have a great week 👋🏻 <!-- .element: class="r-fit-text" -->
