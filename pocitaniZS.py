#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:52:08 2019

@author: spu35165
"""
import tkinter as tk
from tkinter import Label, Entry, Radiobutton, Button, END
import random

hlavni= tk.Tk()
#column = sloupec, row= řádek, columnspan= přesahuje do více sloupců
Label(hlavni, text=u"Operace: ").grid(row=0, column=0, columnspan=1)


znamenko=tk.StringVar()
def vyberznamenka():
    selection=str(znamenko.get())
    Znak.config(text=selection)

znamenko=tk.StringVar()    
def novypriklad():
    cisloA= random.randint(1,10)
    cisloB= random.randint(1,10)
    cisloAentry.delete(0, END)
    cisloAentry.insert(0, str(cisloA))
    cisloBentry.delete(0, END)
    cisloBentry.insert(0,str(cisloB))
    
    
###########  R A D I O   MENU  ###########X
radioplus=Radiobutton(hlavni, text="+", value="+", variable=znamenko, command=vyberznamenka)
radioplus.grid(row=0, column=1)

radiominus=Radiobutton(hlavni, text="-", value="-", variable=znamenko, command=vyberznamenka)
radiominus.grid(row=0, column=2)

radionasob=Radiobutton(hlavni, text="*", value="*", variable=znamenko, command=vyberznamenka)
radionasob.grid(row=0, column=3)

radiodel=Radiobutton(hlavni, text="/", value="/", variable=znamenko, command=vyberznamenka)
radiodel.grid(row=0, column=4)

newpriklad=Button(hlavni, text="Nový příklad", command=novypriklad)
newpriklad.grid(row=0, column=5)


#############   CISLA   #################


cisloAentry= Entry(hlavni, width=5)
cisloAentry.grid(row=1, column=0)


Znak= Label(hlavni, text="?")
Znak.grid(row=1, column=1)

cisloBentry= Entry(hlavni, width=5)
cisloBentry.grid(row=1, column=2)

rovnase= Label(hlavni, text="=", width=5)
rovnase.grid(row=1, column=3)

Vysledek= Entry(hlavni, width=5)
Vysledek.grid(row=1, column=4)



    
hlavni.mainloop()