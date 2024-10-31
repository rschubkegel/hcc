---
title: 'CS - Databases'
date: 2024-11-07
---

# Databases <!-- .element: class="r-fit-text" -->

Week 10

---

## Review

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzBwZGN3cTZpMWt3czd2NDN6ejVsb2Q3enhieGp1bGJ6cGk1OWppYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/n4A8i9oVJDIOY/200.webp) <!-- .element: style="height:400px" -->

--

### All Files Are Just What?

Binary <!-- .element: class="fragment" -->

--

### How Many Bits in a Byte?

8 <!-- .element: class="fragment" -->

--

### How Many Bytes in a Gigabyte?

1,000,000,000 <!-- .element: class="fragment" -->

--

### What is a File Path?

All folders plus a file name. <!-- .element: class="fragment" -->

`C:\Users\Rylan\notes.txt` <!-- .element: class="fragment" -->

---

## Databases

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpnghq.com%2Fwp-content%2Fuploads%2Fred-database-icon-transparent-background.png&f=1&nofb=1&ipt=21b4c61fc6e5ed747458b911e978ce48cbf0f9723be8c462a640a9d0bbdad5c3&ipo=images) <!-- .element: style="height:400px" -->

--

### What is a Database?

> An organized collection of structured information
<!-- .element: class="fragment" -->

--

### Why Not Use Files?

- 🤔 Hard to organize <!-- .element: class="fragment" -->
- 🐢 Too slow <!-- .element: class="fragment" -->
- 💔 No relationships <!-- .element: class="fragment" -->

--

### Example Database

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fermodelexample.com%2Fwp-content%2Fuploads%2F2020%2F11%2Fmore-on-entity-relationship-diagrams-david-tsai-medium-1.png&f=1&nofb=1&ipt=16d1489dde6e6019ac1964eb542b1b5286a211a0f60a8311444db15ebe0135cf&ipo=images) <!-- .element: style="height:400px" -->

--

### Databases vs. File Systems

- Structured data model (usually relational) <!-- .element: class="fragment" -->
- Database files not readable in a text editor <!-- .element: class="fragment" -->
- Databases require a DBMS... <!-- .element: class="fragment" -->

--

A database management system (DBMS) is a special program that allows you to interact with a database.

--

### How Do You Interact With Them?

- Structured query language (SQL)
- Used to modify data and _ask questions_ about it
- SQL is a domain specific language (DSL) (not programming language)

--

### Where Are Databases Used?

Everywhere! <!-- .element: class="fragment" -->

NOTE: Every cloud app, every online account... they all use databases.

--

### Why Use a Database?

Fast, reliable, structured. <!-- .element: class="fragment" -->

--

### Why Use a File System?

User-friendly, no DBMS, better for BLOBs. <!-- .element: class="fragment" -->

---

## Review

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWQycjg1aTdtaGtsOGs4am00ZWIwZmpkcmhlNGY5MzI0eG41eTU2biZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3H4YmeYZ6sx3rbvO9r/100.webp) <!-- .element: style="height:400px" -->

--

### What is a Database?

An organized collection of structured information. <!-- .element: class="fragment" -->

--

### Benefits of a Database?

Speed, relationships. <!-- .element: class="fragment" -->

--

### Benefits of a File System?

User-friendly, no DBMS required, good for unstructured data. <!-- .element: class="fragment" -->

--

### Does Google Store User Data in Regular Files?

No\*, it uses databases. <!-- .element: class="fragment" -->

\*But databases use regular files... so kinda. <!-- .element: class="fragment" -->

---

## Now for Some Coding... <!-- .element: class="r-fit-text" -->

[Python: Pandas Module](/2024/fall/computer-science/slides/python-pandas)
