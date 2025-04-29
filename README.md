# Class Generator - Final Project

## Overview

This project implements a simple Domain Specific Language (DSL) that takes a text command describing a class definition and generates Python class code.

## Members

- Aunaje' Caldwell, D'Metrius Herring

## How to Run

1. Open `class_parser.py`.
2. Run in terminal or IDE (e.g., Visual Studio Code) using: `python3 class_parser.py`.
3. Enter your command when prompted (example below).

## Example

**Input:**
```
Create a class called Student with fields name, GPA, age
```

**Output:**
```python
class Student:
    def __init__(self, name, GPA, age):
        self.name = name
        self.GPA = GPA
        self.age = age
```
Also, the output is automatically saved to a new file named `Student.py`.

## Files

- `class_parser.py` — main program
- `grammar.txt` — grammar definition (EBNF)
- `parse_tree.txt` — simple parse tree drawing
- `README.md` — project overview and instructions

## Bonus Features

- **Error Recovery**: If the user enters an invalid input, the program displays an error message and asks again instead of crashing.
- **Save-to-File**: Automatically saves generated Python code into a `.py` file based on the class name.