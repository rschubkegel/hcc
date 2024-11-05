---
title: 'CS - More Files'
date: 2024-11-07
---

# Special Files <!-- .element: class="r-fit-text" -->

Week 10

---

## Review

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmcxeGozN2IweWt1enh1Z2c3Y2ViODBpYzY4eWY1c3FnbWgxaW8wbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MnL9Mu66fWdp7FgAuR/giphy.webp) <!-- .element: style="height:400px" -->

--

### Are all file systems the same?

No!
<!-- .element: class="fragment" -->

--

### What is a file path?

All folders plus the file name.
<!-- .element: class="fragment" -->

--

### What is a directory?

A folder (special type of file).
<!-- .element: class="fragment" -->

---

## File Paths

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExenl4NWY5ZGVnc28xaHEyZXQ5YnJ2cmo0a25vcDNnM20wanJmb2k5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ck5GjA4qC20pzxP6CP/200.webp) <!-- .element: style="height:400px" -->

--

### Relative vs. Absolute Paths

- Relative changes depending on your _current directory_
- Absolute is always the same

NOTE: **Relative** is like step-by-step map instructions: "turn left, walk two blocks" while **absolute** is like "one block south of Starbucks."

--

### Relative Paths

- `.` current directory
- `..` parent directory

👆🏻 **IMPORTANT TO REMEMBER** 👆🏻
<!-- .element: class="fragment" -->

--

### Absolute Paths (Windows)

- `C:`
  - Letter drive (default is C)
- `%USERPROFILE%`
  - User directory

NOTE: `%USERPROFILE%` is technically an environment variable that changes based on the user, but it is absolute because it does not change based on your current directory.

--

### Absolute Paths (Unix)

- `/` current drive
- `~` user directory

NOTE: The name "tilde" came into English from Spanish tilde, which in turn came from the Latin titulus, meaning 'title' or 'superscription'.

--

### Examples

`notes.txt` or `./notes.txt`
<!-- .element: class="fragment" -->

`../other_folder.txt`
<!-- .element: class="fragment" -->

`/c/Users/Rylan/Documents` or `C:\Users\Rylan`
<!-- .element: class="fragment" -->

`~/Documents` or `%USERPROFILE%/Documents`
<!-- .element: class="fragment" -->

NOTES:
- First two are **relative** paths to **files**
- Second two are **absolute** paths to **directories**

--

## Hidden Files

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWptMXVuNWV6NnN3OGw3enZscHJrcGprZGI4cTY4NmNjc3VzNWRtayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/COYGe9rZvfiaQ/giphy.webp) <!-- .element: style="height:400px" -->

--

### Show Hidden Files

![](/2024/fall/computer-science/images/explorer-hidden-files-toggle.png) <!-- .element: style="height:400px" -->

--

### Hide Files

![](/2024/fall/computer-science/images/file-properties.png) <!-- .element: style="height:400px" -->

--

### Dotfiles

Files with format `.*` are hidden by default on Linux

- `.env`
- `~/.bashrc`
- `.replit`

NOTE: Try it for yourself on Replit by typing `ls` and `ls -a` in the Shell!

---

## Special Files

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzk3ZzN6NGo1N20xbnpnOWJkYmYwanU2MWVnYWR5OGk3MGprYTJvMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEjHN4MtbSqEe4D8Q/giphy.webp) <!-- .element: style="height:400px" -->

--

### Lock Files

Used by some apps only while editing a file.

- `~CoolProject.krita`
- `NeatPhoto.affinity~lockfile~`

--

### Secret Windows Files

- `hiberfil.sys`
  - Used for hibernation
- `swapfile.sys` and `pagefile.sys`
  - Virtualized memory
  - Used when RAM overflows

--

### Linux `/dev` Directory

- Contains files that represent devices
- Used for I/O

NOTE: "it highlights the architecture of \*nix systems, which is 'everything is a file'"
<!-- https://www.baeldung.com/linux/dev-directory -->

---

## Review

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjBjemt5eW9yNWxmZHdjdWpkcmN3d2d6Z2d4bXdqdWZnNm90OTgzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/872o15eAXFBw66UfNl/giphy.webp) <!-- .element: style="height:400px" -->

--

### What Is a Relative File Path?

A **relative** file path changes destination based on your current directory.
<!-- .element: class="fragment" -->

Antonym: **absolute** file path.
<!-- .element: class="fragment" -->

--

### What Does `.` Represent?

The current directory.
<!-- .element: class="fragment" -->

--

### What Does `..` Represent?

The parent directory.
<!-- .element: class="fragment" -->

--

### Are All Files Visible by Default?

No!
<!-- .element: class="fragment" -->

---

## Now for Some Coding...

[Python: More on Files](/2024/fall/computer-science/slides/python-more-files)