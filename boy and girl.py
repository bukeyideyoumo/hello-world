# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:34:24 2017

@author: Xiaoyaole
"""

girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
letterGirls={}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print ([b+'+'+g for b in boys for g in letterGirls[b[0]]])
"""
boys = ['chris', 'arnold', 'bob']
girls and boys are two lists

`letterGirls = {}` 
letterGirls is a dictionary

setdefault() method will set dict_var[key]=default if key is not already in dict_var (in your case dict_var is letterGirls )

dict_var.setdefault() usage

dict-var.setdefault(somekey,[]).append(somevalue)
In your code

letterGirls.setdefault(girl[0], []).append(girl)
will make a dictionary of the form

{'c': ['clarice'], 'b': ['bernice'], 'a': ['alice']}
key is girl[0] ie the first letter of name.

There was an indentation problem with your script.Other wise it will cause Key error .

It should be

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)   
print ([b+'+'+g for b in boys for g in letterGirls[b[0]]])
your output

['chris+clarice', 'arnold+alice', 'bob+bernice']
is obatined by taking each item in boys list and finding girl name with same first letter from dictionary letterGirls
""""""