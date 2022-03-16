# In[33]:
#Dette er en alternativ version af LIX-udregneren, hvor der kommer en pop-up box
#så man kan indlæse andre filer en den éne herman bang tekst

    
#tkinter importeres
import tkinter as tk

#funktionen filedialog, der åbner stifinder, importeres
from tkinter import filedialog
from tkinter import *

#der defineres en funktion: at vælge filen 
#resultatet af funktionen er et stinavn, der vælges i stifinder
def choose_file():
    global selected_file
    selected_file = filedialog.askopenfile()
    
def CloseWindow():  root_window.destroy()


#popup-vinduet defineres 
root_window = tk.Tk()
root_window.geometry('200x100')
frame = Frame(root_window)
frame.pack()

#der sættes tekst i vinduet med tk.Label funktionen
label = tk.Label(root_window, text="Velkommen til LIX-Udregneren")
label.pack(side=TOP)
#Der defineres en knap
knap = tk.Button(root_window, text="Vælg din tekst", width = 10, command = lambda: ([choose_file()], [CloseWindow()]))
knap.pack(side= BOTTOM)

root_window.mainloop()

Tekst = selected_file.read()



# In[9]:


#For at finde antal ord definerer vi en funktion, der fjerner tegnsætning og store bogstaver og deler teksten op ved mellemrum, så den bliver delt op i ord (strings)
def rens_ord(text_0):
    text_1 = text_0.replace("\n"," ")
    text_2 = text_1.replace("."," ")
    text_3 = text_2.replace(","," ")
    text_4 = text_3.replace(":"," ")
    text_5 = text_4.replace("*"," ")
    text_6 = text_5.replace("–"," ")
    text_7 = text_6.replace("'"," ")
    text_8 = text_7.replace("”"," ")
    text_ren = text_8.replace("-"," ")
    text_lav = text_ren.lower()
    text_token = text_lav.split()
    return text_token


# In[55]:


#funktionen køres på Herman Bang teksten
rensettekst = rens_ord(Tekst)

#Vi regner så ud hvor mange ord der er i teksten
#printer antallet af ord i det hele
AntalOrd = len(rensettekst)
print ("Antallet af ord i teksten er "+ str(len(rensettekst)))


# In[53]:


#for at udregne LIX tal tæller man alle ord over 7 bogstaver som lange ord
#Alle ord på eller over 7 bogstaver bliver tilføjet til listen langeOrd.
langeOrd = []           
for ord in rensettekst:           
    if len(ord) >= 7:   
        langeOrd.append(ord) 

#printer antallet af lange ord
print("Antallet af lange ord i teksten er " + str(len(langeOrd)))


# In[58]:


#Udregner procentdel
AntalLangeOrd = len(langeOrd)
Andel = (AntalLangeOrd / AntalOrd)
ProcentAndel = Andel * 100
#printer en tekststreng ("Det er") plus procentandelen omformet til en streng
print("Procentandelen af lange ord i teksten er " + str(ProcentAndel) + " procent.")   


# In[51]:


#Nu mangler vi bare at beregne antal punktummer
AntalPunktummer = Tekst.count(".")
print("Antallet af punktummer i teksten er " + str(AntalPunktummer) )


# In[62]:


#Vi er nu klar til at udregne LIX-tallet
#LIX = (antal ord/antal punktummer) + (lange ord * 100/antal ord)
if AntalLangeOrd == 0 or AntalPunktummer == 0:
    print("Der er 0 lange ord og/eller 0 punktummer, så LIX-tallet udregnes ikke, så man ikke dividerer med 0")
    LIX = 0

else:
    LIX = (AntalOrd / AntalPunktummer) + (AntalLangeOrd*100/AntalOrd) 
    print("LIX-tallet for teksten er " + str(LIX))


# In[77]:


if LIX > 54:
    print("Teksten er meget svær")
elif LIX >= 45:
    print("Teksten er svær")
elif LIX >= 35:
    print("Teksten er middel")
elif LIX >=25:
    print("Teksten er let for øvede læsere")
else:
    print ("Teksten er let")


