# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
AttributeError: 'dict' object has no attribute 'append'


### 2. What I thought it meant
Cannot use the append method for a dictionary

### 3. What it actually meant
Dictionaries does not have append.

### 4. The fix
Change the variable intialization from a dictionary to a list.

## Entry 2

### 1. Error message
TypeError: string indices must be integers, not 'str'

### 2. What I thought it meant
My code calls a string instead of the integer.

### 3. What it actually meant
It was trying to compare a string to an integer, causing the error.

### 4. The fix
Updating the code to actually look for the integer and not the string.