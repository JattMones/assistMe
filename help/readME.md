# AssistMe Help Guide

## Getting started

### Installation and Setup
See the [readME]() for installation instructions.
### System Overview

### Video Tutorial/First Time Use
- [First Time Running Program and Basic Overview]()
- [Scheduling tasks]()
- [Recording Information]()

## AutoHotkey(AHK) Help

### AutoHotkey Docs
For anyone trying to develop your own ahk scripts, it is
necessary to read at least the introduction and quick-start
sections in the [AutoHotkey docs](https://autohotkey.com/docs/AutoHotkey.htm).
AutoHotkey is a very powerful scripting language on windows,
so it's important to fully understand the language if you're
writing scripts. Reading the entire docs is obviously not
required, but highly recommended.    

### AutoHotkey Community
The [AutoHotkey Community](https://autohotkey.com/board/) is
a great resource if you have specific questions about using
AutoHotkey. Many developers have already built simple tools
in ahk, and encountered problems similar to problems you may
be experiencing. Because of this, browsing and searching
this site often provides you with solutions quickly.   

### Quick Tips
- **Dependencies**</br>
It is important to recognize that AutoHotkey and Pulovers
Macro Creator are very good at mimicing raw user input.
Because of this, things such as mouse clicks can easily be
intended to click one thing, but fail because of a change in
window, window size, time to load, time to paint, etc.
Because of this, we recommend using things such has hotkeys
as frequently as possible in your recordings to limit the
variability of something like clicking a button. For
example, instead of clicking the maximize button, we
recommend pressing the windows key and up arrow. To see a
full list of useful hotkeys like this, see the [HotKey
section](). </br></br>
- **Quick Syntax**</br>
*Variables and Expressions:*
  1. The "=" symbol is used to assign unquoted literal
  strings or variables enclosed in percent signs (i.e.
  mostly used when storing strings or referencing string
  variables).
  2. The ":=" symbol is used to store numbers, quoted
  strings, and other types of expressions (i.e. most
  mathematical expressions/calculations should uses this
  symbol).
  3. When referencing a variable when using "=" the variable
  is only referenced when surrounded by %, like so %Var%.
  4.  When referencing a variable when using ":=" the
  variable is referenced without %.</br></br>
  5. We found the use of three built in variables:
  clipboard, A_SceenHeight, and A_ScreenWidth to be
  particularly useful.

  *Loops and Hotkeys:*
  1. Any loop starts with an open "{" and ends with a
  closing "}".
  2. Conditional statements are found to be false when = 0,
  and true at all other values.
  3. Types of loops include: If, While, Loop Until, For, etc.
  4. Create your own hotkeys with the :: symbol in ahk.
  </br></br>
- **Running an ahk script**</br>
*Is a script running?*</br>
To check if an AHK script is running, click the "show hidden
icons" arrow on your task bar, and any running AHK scripts
will be displayed there. Interact with these scripts by
right clicking the icon. You can also see if the AutoHotkey
program itself is running by checking the background
processes in the task manager.</br></br>
*Prevent a script from taking over*</br>
Since an AHK script can take control of your keyboard and
mouse, it's important to put in a safety measures to prevent
a script from "taking over your computer". The first video
on this [page](https://assist-me-download.netlify.com/surveypage/)
demonstrates how coding a "kill switch"
into your scripts could be helpful. Other programs are
available which can disable AutoHotkey from running until
you enable it after start-up. This would allow you to
restart you computer and the script would be disabled at
start-up.

### Video Tutorial
- [Quick Tips Video]()

## Contact
Contact assistMe developers through the [assistMe
website](https://assist-me-download.netlify.com/) or on
[github]().
