# coding=utf-8
import os
import random
import codecs
import sys
import inspect
import subprocess
import RPi.GPIO as GPIO
import time
 

#determine the asshole fucking path of the cocksucker source files shit, and the fucking result fuck
script_dir = os.path.dirname(__file__)
rel_path = "/home/pi/Desktop/gyalazo-v5/src/"
dictionarypath = os.path.join(script_dir, rel_path)

script_dir = os.path.dirname(__file__)
rel_path = "/home/pi/Desktop/gyalazo-v5/res/"
resultpath = os.path.join(script_dir, rel_path) 

#put the fucking dictionary files to shit arrays
dictnum=0
dictionaryfiles = []
for r, d, f in os.walk(dictionarypath):
    for file in f:
        if '.txt' in file:   
            dictname=(file[0:-4])
            dictionaryfiles.append(dictname)

            #get the asshole words from files and put them into the dick arrays, with names by dicts    
            dictfile = dictionarypath + dictionaryfiles[dictnum] + '.txt'

            with codecs.open(dictfile, encoding='latin1') as fp:
                
                line = fp.readline()
                vars()[dictname]=[] #set this fuck to empty first
                while line:
                    vars()[dictname].append(line.strip())
                    line = fp.readline()
            dictnum=dictnum+1   

#this fucker function is random-sentence (rstc), the motherfucker "pos" means part-of-speech
def rstc(pos): 
    
        uppercase=0
        space=0
         
        speakout=[]
        wordtype=[]
        
        protectedwordtypes=["byname", "cm", "conj", "conjand", "gly", "ijt", "pnoun", "qm", "qone", "qthree", "qtwo"]   #protected word type is for not to delete from that dictionary, because no much of it, and we can use it multiple times
        needcapitalize=["gly","qm"] #after this pissed of types, the next letter will be uppercase
        needspace=["cm","gly","qm"] #afther this asshole word types the next character will be space
        vowels=["a","á","o","ó","u","ú","e","é","i","í","ö","o","ü","u"]    #just for specific countries
        
        for x in range(len(pos)):
            actdictname=pos[x] #name of the fucking type of word
            actdictlen=len(eval(pos[x])) #the actual dictionary's bitching length
            actdictarrname=eval(pos[x])
       
            wordtype.append(actdictname)
            
            if actdictlen > 0:
                gennum=random.randrange(0, actdictlen, 1)
                actdictval=eval(pos[x])[gennum] #the cockfucker word

                speakout.append(actdictval)
 
                if actdictname not in protectedwordtypes:
                    actdictarrname.remove(actdictval)
 
        f=open("/home/pi/Desktop/gyalazo-v5/res/result.txt","w")    #opening result.txt for writing. this is because we cannot speak out realtime with espeak some kind of lagging shit... so we will store the whole sentence, and speak it out after it generated
        
        for z in range(len(speakout)):  #here we do a couple of shit, determining do we need a space or an uppercase letter
            uppercase=0
            space=0
            
            if z==0 or wordtype[z-1] in needcapitalize:
                uppercase=1
            if z!=0:
                if wordtype[z] not in needspace:
                    space=1
            # lets start to fucking determine the next first shit character to decide which assfucker 
            if wordtype[z]=="byname":
                nextw=speakout[z+1][:1]
                
                if str(nextw.encode('utf-8').strip()) in vowels:    #if the next word begins with a vowel
                    speakout[z]=byname[1]   #article1 before word
                else:
                    speakout[z]=byname[0]   #article2 before word
                
            if space==1:
                f.write(str(" "))   #we need a space
                space=0    
            
            if uppercase==0:    #do we need an uppercase letter?
                f.write(str(speakout[z].encode('utf-8').strip()))   #no
                 
            if uppercase==1:
                f.write(str(speakout[z].encode('utf-8').capitalize().strip()))  #yes
                uppercase=0
            
        f=open("/home/pi/Desktop/gyalazo-v5/res/result.txt","r")    #our result is ready to read
        contents=f.read()   #read out to the contents variable
     
        print(contents) #print that shit!
        subprocess.check_output('espeak -vhu+m1 -f /home/pi/Desktop/gyalazo-v5/res/result.txt -p30 -s200 -a100 ', shell=True)   #speak that shit! (with a command executed in the terminal
        f.close()   #close that shit!
              
#-------- sucker sentence examples: --------#
# Mi a kurva anyádat nézel te faszkalap? Szájbabaszlak te buzi köcsög! Na takarodj a büdös picsába!
# Mit bámulsz buzigyerek? Szétbaszom a nyűves pofádat te cigány. Húzz a picsába, mert szétfejellek te köcsög.
# Kinek ugatsz te faszkalap? Anyádon rúglak, véged köcsög. Szopd le a faszomat és húzzd el a beled de geci gyorsan, mielőtt szétbaszlak.

#-------- fucking hungarian help: --------#
# adj       - melleknev
# byname    - nevelo (a, az) ------ [protected]
# cm        - comma (,) ----------- [protected]
# conj      - conjunction (mert) -- [protected]
# conjand   - conjuction and (és) - [protected]                    
# gly       - irasjel (. !) ------- [protected]
# ijt       - indulatszo (na) ----- [protected]
# noun      - fonev
# nounverb  - fonevi igenev
# pnoun     - nevmas (te) --------- [protected]
# pverb     - igekoto ige
# qm        - kerdojel (?) -------- [protected]
# qone      - kerdoszo1 (mi) ------ [protected]
# qthree    - kerdoszo3 (kinek) --- [protected]
# qtwo      - kerdoszo2 (mit) ----- [protected]
# subj      - targy
# subjto    - noun to
# verb      - ige                   


gennum=random.randrange(0, 8, 1)    #generating the sentence structure, the range is depends on how many predefined structure is here. the more you have, the less it will be unnatural

if gennum==0:
    rstc(["byname","adj","adj","subj","subj","noun","cm","nounverb","pnoun","subj","gly"]) #shark1

if gennum==1:
    rstc(["qtwo","verb","pnoun","adj","adj","subj","qm","pverb","pnoun","adj","adj","subj","gly"]) #shark2

if gennum==2:
    rstc(["pnoun","adj","adj","subj","cm","pverb","conjand","pverb","pnoun","adj","adj","subj","subj","gly"]) #bnsgt1

if gennum==3:
    rstc(["qtwo","verb","subj","cm","nounverb","byname","subj","subj","subjto","gly"]) #bnsgt2

if gennum==4:
    rstc(["pverb","pnoun","adj","subj","cm","conj","nounverb","pnoun","subj","gly"]) #niga1    

if gennum==5:
    rstc(["ijt","pnoun","subj","gly","qone","byname","noun","verb","pnoun","adj","subj","gly"]) #niga2    

if gennum==6:
    rstc(["nounverb","pnoun","subj","subj","subj","gly"]) #gandi1    
    
if gennum==7:
    rstc(["qtwo","verb","pnoun","adj","adj","subj","qm"]) #gandi2    

    
fout = open("/home/pi/Desktop/gyalazo-v5/log/log.txt", "a")     #open log for appending
fout.write("ver: " + str(gennum) + " | ")       #write the sentence version. In that case my friends helped me, so I want to know which sentence was which guy 
fout.close()    #close that shit!











