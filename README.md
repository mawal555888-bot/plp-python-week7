# Week 7 Assignment: Shopping List Manager

- `list_warmup.py`: practises list basics: reading items by index, `.append()`, `.remove()`, and `len()`.
- `shopping_list.py`: a menu-driven shopping list manager with add, remove, show, and done options.
- `list_report.py`: prints a numbered list, counts names longer than 4 letters, and finds the longest name using a loop.

It is safer to check `in` before calling `.remove()` because `.remove()` raises a `ValueError` and crashes the program if the item is not on the list. Checking first lets the program print a friendly message and keep running instead.