#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:52:08 2019

@author: spu35165
"""
import tkinter as tk
from tkinter import Label, Entry, Radiobutton, Button, END, LabelFrame

import random

hlavni= tk.Tk()
hlavni.title("Počítání pro základní školy")
#column = sloupec, row= řádek, columnspan= přesahuje do více sloupců
prikladg = LabelFrame(hlavni, text="Příklad", padx=5, pady=5)
prikladg.grid(row=2)
menug = LabelFrame(hlavni, text="Vyber znaménko", padx=5, pady=5)
menug.grid(row=1)
stkog = LabelFrame(hlavni, text="Statistika", padx=5, pady=5)
stkog.grid(row=1, column=4, rowspan=2)

znamenko=tk.StringVar()
def vyberznamenka():
    selection=str(znamenko.get())
    Znak.config(text=selection)
    newpriklad.invoke()

znamenko=tk.StringVar()    
def start():
    if Znak['text'] == "+":
        cisloA=random.randint(1,50)
        cisloB= random.randint(1,50)
    if Znak['text'] == "-":
        cisloA=random.randint(1,50)
        cisloB= random.randint(1,cisloA)
    if Znak['text'] == "*":
        cisloA=random.randint(1,9)
        cisloB= random.randint(1,9)
    if Znak['text'] == "/":
        cisloB=random.randint(1,9)
        vysledek=random.randint(1,9)
        cisloA=vysledek*cisloB
    cisloAentry.delete(0, END)
    cisloAentry.insert(0, str(cisloA))
    cisloBentry.delete(0, END)
    cisloBentry.insert(0,str(cisloB))   
    vysledekEntry.delete(0,END)

   
dobre=0
celkem=0
vysledek=0
def zkontroluj(x):
    global dobre
    global celkem
    a = int(cisloAentry.get())
    b = int(cisloBentry.get())
    vys = vysledekEntry.get()
    if Znak['text'] == "+":
        vysledek = a+b
    if Znak['text'] == "-":
        vysledek = a-b
    if Znak['text'] == "*":
        vysledek = a*b
    if Znak['text'] == "/":
        vysledek = a/b
    try:
        if vysledek == int(vys):
            dobre+=1
            celkem+=1
            newpriklad.invoke()
            vysledekEntry.delete(0)
            hlavni.title("Počítání pro základní školy")
        if vysledek != int(vys):
            celkem+=1
            newpriklad.invoke()
            vysledekEntry.delete(0)
            hlavni.title("Počítání pro základní školy")
    except:
        hlavni.title("Ty jsi chobot")
        celkem+=1
        newpriklad.invoke()
    stats.config(text='{0}/{1}'.format(dobre,celkem))
    
        
###########  R A D I O   MENU  ###########
stats = Label(stkog, text="?")
stats.grid(row=0)

radioplus=Radiobutton(menug, text="+", value="+", variable=znamenko, command=vyberznamenka)
radioplus.grid(row=0, column=1)

radiominus=Radiobutton(menug, text="-", value="-", variable=znamenko, command=vyberznamenka)
radiominus.grid(row=0, column=2)

radionasob=Radiobutton(menug, text="*", value="*", variable=znamenko, command=vyberznamenka)
radionasob.grid(row=0, column=3)

radiodel=Radiobutton(menug, text="/", value="/", variable=znamenko, command=vyberznamenka)
radiodel.grid(row=0, column=4)


newpriklad=Button(stkog, text="START", command=start, width=10)


kontrola= Button(stkog, text="Zkontroluj", command=zkontroluj, width=10)
kontrola.grid(row=1)


#############   CISLA   #################


cisloAentry= Entry(prikladg, width=5)
cisloAentry.grid(column=0, row=0)


Znak= Label(prikladg, text="?")
Znak.grid(column=1, row=0)

cisloBentry= Entry(prikladg, width=5)
cisloBentry.grid(column=2,row=0)

rovnase= Label(prikladg, text="=", width=5)
rovnase.grid(column=3,row=0)

vysledekEntry= Entry(prikladg, width=5)
vysledekEntry.grid(column=4,row=0)

vysledekEntry.bind("<Return>",zkontroluj)

    
hlavni.mainloop()