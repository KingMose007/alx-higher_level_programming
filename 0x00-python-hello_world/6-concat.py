#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
_ = lambda *args: print(*args)
_(_(f"Welcome to {str1}"), str2 + "!")
