#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import os.path
import csv
import time
from functools import reduce
import re
#import json
from os import path
from colorama import Back, Fore, init, Style
from time import sleep
from tqdm import tqdm
#from tabulate import tabulate
from prettytable import PrettyTable



def almacenardatos():
    """a=''
    print('')
    return a"""
    init()
    print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
    init()
    print(Fore.RED + "Coincidencias de (port) o puertos encontrados "+Fore.GREEN+" **************************************")
    print ("")
    RED = '\033[1;31m'
    NOCOLOR = '\033[0;0m'

    palabras4 = ['tcp', '.com', 'n/a']

    palabra4 = 'tcp'
    ocurrencias4 = []
    with open('doc.txt') as lineas:
        for linea in lineas:
            if palabra4 in linea:
                ocurrencias4.append(linea)

    
        #print(aImprimir4)
    return ocurrencias4

def crear_archivo():
    if path.exists('prueba1.txt'):
        print('El archivo ya existe')
        file=open("prueba1.txt", "a")
    else:
        file=open("prueba1.txt", "a")
        print('El archivo fue creado')

        pass    

def menu():

    """
Inicio logo         ###################################################################
    """
#Color de texto inicio  ################################################################
#Color de texto fin  ###################################################################
print ("")
print ("")
print ("")
init()
print(Fore.RED + "          Software link "+Fore.GREEN+" : https://github.com/davenisc")
init()
print(Fore.RED + "          Description "+Fore.GREEN+"   : SCRIPT FOR RAPID SOFTWARE ANALYSIS")
init()
print(Fore.RED + "          Contact Mail "+Fore.GREEN+"  : info@davenisc.com")

#Color de texto inicio ###################################################################

#Color de texto fin    ###################################################################
init()
print(Fore.WHITE + "________________________________________________________________________  ")
print ("                                                                                      ")
init()
print(Fore.CYAN + "   ███████╗ ██████╗ ███████╗████████╗██╗    ██╗ █████╗ ██████╗ ███████╗    ")
init()   
print(Fore.CYAN + "   ██╔════╝██╔═══██╗██╔════╝╚══██╔══╝██║    ██║██╔══██╗██╔══██╗██╔════╝    ")
init()
print(Fore.CYAN + "   ███████╗██║   ██║█████╗     ██║   ██║ █╗ ██║███████║██████╔╝█████╗      ")
init()
print(Fore.CYAN + "   ╚════██║██║   ██║██╔══╝     ██║   ██║███╗██║██╔══██║██╔══██╗██╔══╝      ")
init()
print(Fore.CYAN + "   ███████║╚██████╔╝██║        ██║   ╚███╔███╔╝██║  ██║██║  ██║███████╗    ")
init()
print(Fore.CYAN + "   ╚══════╝ ╚═════╝ ╚═╝        ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ")
init()                
print(Fore.GREEN + "                                          _             _ _               ")
init()
print(Fore.GREEN + "                                         /_\  _ _  __ _| (_)______ _ _    ")
init()
print(Fore.GREEN + "                                        / _ \| ' \/ _` | | |_ / -_) '_|   ")
init()
print(Fore.GREEN + "                                       /_/ \_\_||_\__,_|_|_/__\___|_|     ")
init()
print(Fore.RED + "                 +-------------------------------------------+              ")
init()
print(Fore.RED + "                 | @DaveNISC |              |  @whitepadawan |              ")
init()
print(Fore.RED + "                 +-------------------------------------------+              ")
init()
print (Fore.GREEN +"                            By davenisc.com  | v 1.2.0                    ")
init()
print (Fore.WHITE +"________________________________________________________________________\n")
 
def pedirNumeroEntero():
    init()
    print(Fore.WHITE + "")
   
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Enter an option: "))
            correcto=True
        except ValueError:
            print('Error, enter an option')
            print ("")
     
    return num
 
salir = False
opcion = 0

while not salir:

    
    init()
    print(Fore.CYAN + "Menu Software Analizer"+Fore.CYAN+"                Menu RegShot Filter \n\n")
 
    init()
    print(Fore.RED + "1. "+Fore.WHITE+" Analyze software "  +Fore.RED+ "                   5.  " +Fore.WHITE+ "Filter and create logs")
    init()
    print(Fore.RED + "2. "+Fore.WHITE+" See result       "  +Fore.RED+ "                   6.  "  +Fore.WHITE+ "Show URLs found")
    init()
    print(Fore.RED + "3. "+Fore.WHITE+" ¿What is software analyzer?" +Fore.RED+ "         7.  " +Fore.WHITE+ "Analyze URLs")
    init()
    print(Fore.RED + "4. "+Fore.WHITE+" ¿How to use analyzer software?" +Fore.RED+ "      8.  " +Fore.YELLOW+ "Exit")
    print ("") 
    print ("")
    print ("") 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:

        ############################################################################################################
        
        print ("")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Analyze software\n\n")
        soft_a = raw_input('Drag the software to be analyzed here\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("")    

        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" We will start the analysis of this software " +Fore.GREEN+ " please wait! " +Fore.WHITE+ "<*>\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Better go and have a coffee while the information collection process finishes, the script will go back to the main menu when the scan finishes. " +Fore.GREEN+ "" +Fore.WHITE+ "")
        print("")
        init()
        print(Fore.RED + "   ( ( "+Fore.WHITE+"")
        init()
        print(Fore.RED + "    ) ) "+Fore.WHITE+"")
        init()
        print(Fore.RED + "  ........"+Fore.WHITE+"")
        init()
        print(Fore.RED + "  |      |]"+Fore.WHITE+"  go!! ")
        init()
        print(Fore.RED + "  \      / "+Fore.WHITE+"  and have   ")
        init()
        print(Fore.RED + "   `----'"+Fore.WHITE+"    a coffee   ")
        print("")

        
        #os.system("gnome-terminal -e 'ping 8.8.8.8'")
        #command = '  nslookup ' + url_analyze +  ' > scan_ip.txt '

        #os.system(command)


        ###################################################################################### buscando MD5

        command = '''  md5sum  ''' + soft_a +  ''' |awk '{print $1}' > log_hash.txt '''

        os.system(command)

        search_hash = open('hash.txt','w')

        regex = '[A-Za-z-0-9]{32,32}'


        datos2 = open('log_hash.txt')
        for line2 in datos2:
            line2 = line2.rstrip()
            y = re.findall('[A-Za-z-0-9]{32,32}', line2)
            if len(y) > 0 :
                search_hash.write(str(y[0]+ "\n"))
                #print (y[0])

        search_hash = open('hash.txt','w')


        lines = [line.strip() for line in open('log_hash.txt', 'r')]
        for x in lines:
            found_h = re.search('[A-Za-z-0-9]{32,32}', x)
            if found_h:
                search_hash.write(x + "\n")

        var = os.getcwd()

        ###################################################################################### buscando sha256

        command = '''  sha256sum  ''' + soft_a +  ''' |awk '{print $1}' > log_sha256.txt '''

        os.system(command)

        search_hash256 = open('hash256.txt','w')

        regex = '[A-Za-z-0-9]{64,64}'


        datos3 = open('log_sha256.txt')
        for line3 in datos3:
            line3 = line3.rstrip()
            sha256 = re.findall('[[A-Za-z-0-9]{64,64}', line3)
            if len(sha256) > 0 :
                search_hash256.write(str(sha256[0]+ "\n"))
                #print (y[0])

        search_hash256 = open('hash256.txt','w')


        lines = [line.strip() for line in open('log_sha256.txt', 'r')]
        for b in lines:
            found_h = re.search('[[A-Za-z-0-9]{64,64}', b)
            if found_h:
                search_hash256.write(b + "\n")

        var = os.getcwd()

        ###################################################################################### buscando sha1

        command = '''  sha1sum  ''' + soft_a +  ''' |awk '{print $1}' > log_sha1.txt '''

        os.system(command)

        search_hash1 = open('hash1.txt','w')

        regex = '[A-Za-z-0-9]{40,40}'


        datos4 = open('log_sha1.txt')
        for line4 in datos4:
            line4 = line4.rstrip()
            sha1 = re.findall('[[A-Za-z-0-9]{40,40}', line4)
            if len(sha1) > 0 :
                search_hash1.write(str(sha1[0]+ "\n"))
                #print (y[0])

        search_hash1 = open('hash1.txt','w')


        lines = [line.strip() for line in open('log_sha1.txt', 'r')]
        for c in lines:
            found_h = re.search('[[A-Za-z-0-9]{40,40}', c)
            if found_h:
                search_hash1.write(c + "\n")

        var = os.getcwd()


        #####################################################################################################


        command = '  automater  ' + var+'/hash.txt' +  ' > log_scan.txt '
        os.system(command)

        command = '  file  ' + soft_a +  ' > log_format.txt '
        os.system(command)

        command = '  string  ' + soft_a +  ' > log_strings.txt '
        os.system(command)

        command = '  exiftool  ' + soft_a +  ' > log_metadata.txt '
        os.system(command)
    
        for i in tqdm(range(100)):
            sleep(0.02) 
        print("") 

        init()
        print(Fore.RED + "[*]"+Fore.GREEN+" Finished analysis }:) \n\n")
        print ("")
        time.sleep(5)
        os.system('clear')
        
    elif opcion == 2:

        ######################################################################################## mostrando hash MD5
        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.GREEN+" Hash found (MD5)\n")

        init()
        print (Fore.WHITE +"")

        print_hash = open('hash.txt','r')

    

        regex = '[A-Za-z-0-9]{32,32}'

        list_hash = []

        for line2 in print_hash:
            line2 = line2.rstrip()
            y = re.findall('[A-Za-z-0-9]{32,32}', line2)
            if len(y) > 0 :
                if y[0] not in list_hash:
                    list_hash.append(y[0])
                    print (y[0])

        ############################################################################## mostrando sha256

        print ("") 

        print(Fore.RED + "[*]"+Fore.GREEN+" Hash found (sha256)\n")

        init()
        print (Fore.WHITE +"")

        print_hash = open('hash256.txt','r')

    

        regex = '[A-Za-z-0-9]{64,64}'

        list_hash = []

        for line3 in print_hash:
            line3 = line3.rstrip()
            x = re.findall('[A-Za-z-0-9]{64,64}', line3)
            if len(x) > 0 :
                if x[0] not in list_hash:
                    list_hash.append(x[0])
                    print (x[0])



        ############################################################################## mostrando sha256

        print ("") 

        print(Fore.RED + "[*]"+Fore.GREEN+" Hash found (sha1)\n")

        init()
        print (Fore.WHITE +"")

        print_hash = open('hash1.txt','r')

    

        regex = '[A-Za-z-0-9]{40,40}'

        list_hash = []

        for line4 in print_hash:
            line4 = line4.rstrip()
            z = re.findall('[A-Za-z-0-9]{40,40}', line4)
            if len(z) > 0 :
                if z[0] not in list_hash:
                    list_hash.append(z[0])
                    print (z[0])



                    
        #init()
        #print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        ######################################################################################## mostrando metadata

        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.GREEN+" Data found (Metadata)\n")

        init()
        print (Fore.WHITE +"")

        print_data = open('log_metadata.txt','r')

        #[for].[0-9]+.[0-9]+.[0-9]+.[0-9]+ IP del server
        #[0-9].+[a-z]\s*[a-z]+\s\s[a-z]+ puerto 

        regex = '[\w].+'

        list_data = []

        for line3 in print_data:
            line3 = line3.rstrip()
            b = re.findall('[\w].+', line3)
            if len(b) > 0 :
                if b[0] not in list_data:
                    list_data.append(b[0])
                    print (b[0])
        #init()
        #print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        
        #######################################################################################################


        ######################################################################################## mostrando formato y tipo

        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.GREEN+" file type and format found (type/format)\n")

        init()
        print (Fore.WHITE +"")

        print_data = open('log_format.txt','r')

        regex = '([A].+)\w+'

        list_data = []

        for line14 in print_data:
            line14 = line14.rstrip()
            b = re.findall('([A].+)\w+', line14)
            if len(b) > 0 :
                if b[0] not in list_data:
                    list_data.append(b[0])
                    print (b[0])
        #init()
        #print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        

        ######################################################################################## mostrando strings de binario

        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.RED+" String results found (IP/URL/DLL) this function will be added soon \n")

        print_data = open('log_strings.txt','r')

        regex = '[\w].+'

        list_data = []

        for line3 in print_data:
            line3 = line3.rstrip()
            b = re.findall('[\w].+', line3)
            if len(b) > 0 :
                if b[0] not in list_data:
                    list_data.append(b[0])
                    print (b[0])
        #init()
        #print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        ########################################################################################### mostrando resultados antivirus

        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.GREEN+"  Malware analysis result (AV)\n")

        init()
        print (Fore.WHITE +"")
        
        print_data = open('log_scan.txt','r')

        regex = '([BitDefender]{11,11}....+)'

        list_data = []

        for line3 in print_data:
            line3 = line3.rstrip()
            b = re.findall('([BitDefender]{11,11}....+)', line3)
            if len(b) > 0 :
                if b[0] not in list_data:
                    list_data.append(b[0])
                    #init()
                    #print (Fore.RED +b[0])
                    t = PrettyTable(['(*)', 'Malware Name'])
                    t.add_row(['(*)', b])
                    print t

        print_data1 = open('log_scan.txt','r')

        regex = '([McAfee]{6,6}....+)'

        list_data1 = []

        for line4 in print_data1:
            line4 = line4.rstrip()
            c = re.findall('([McAfee]{6,6}....+)', line4)
            if len(c) > 0 :
                if c[0] not in list_data1:
                    list_data1.append(c[0])
                    #init()
                    #print (Fore.RED +c[0])
                    t = PrettyTable(['(*)', c])
                    print t    

        print_data2 = open('log_scan.txt','r')

        regex = '([Symantec]{8,8}....+)'

        list_data2 = []

        for line5 in print_data2:
            line5 = line5.rstrip()
            d = re.findall('([Symantec]{8,8}....+)', line5)
            if len(d) > 0 :
                if d[0] not in list_data2:
                    list_data2.append(d[0])
                    #init()
                    #print (Fore.RED +k[0])
                    t = PrettyTable(['(*)', d])
                    print t

        print_data3 = open('log_scan.txt','r')

        regex = '([Kaspersky]{8,8}....+)'

        list_data3 = []

        for line6 in print_data3:
            line6 = line6.rstrip()
            f = re.findall('([Kaspersky]{8,8}....+)', line6)
            if len(f) > 0 :
                if f[0] not in list_data3:
                    list_data3.append(f[0])
                    #init()
                    #print (Fore.RED +f[0])
                    t = PrettyTable(['(*)', f])
                    print t

        print_data4 = open('log_scan.txt','r')

        regex = '([TrendMicro]{10,10}....+)'

        list_data4 = []

        for line7 in print_data4:
            line7 = line7.rstrip()
            g = re.findall('([TrendMicro]{10,10}....+)', line7)
            if len(g) > 0 :
                if g[0] not in list_data4:
                    list_data4.append(g[0])
                    #init()
                    #print (Fore.RED +g[0])
                    t = PrettyTable(['(*)', g])
                    print t 

        print_data5 = open('log_scan.txt','r')

        regex = '([Microsoft]{9,9}....+)'

        list_data5 = []

        for line8 in print_data5:
            line8 = line8.rstrip()
            h = re.findall('([Microsoft]{9,9}....+)', line8)
            if len(h) > 0 :
                if h[0] not in list_data5:
                    list_data5.append(h[0])
                    #init()
                    #print (Fore.RED +h[0])
                    t = PrettyTable(['(*)', h])
                    print t

        print_data6 = open('log_scan.txt','r')

        regex = '([Fortinet]{8,8}....+)'

        list_data6 = []

        for line9 in print_data6:
            line9 = line9.rstrip()
            j = re.findall('([Fortinet]{8,8}....+)', line9)
            if len(j) > 0 :
                if j[0] not in list_data6:
                    list_data6.append(j[0])
                    #init()
                    #print (Fore.RED +j[0])
                    t = PrettyTable(['(*)', j])
                    print t

        print_data7 = open('log_scan.txt','r')

        regex = '([Avast]{5,5}....+)'

        list_data7 = []

        for line10 in print_data7:
            line10 = line10.rstrip()
            k = re.findall('([Avast]{5,5}....+)', line10)
            if len(k) > 0 :
                if k[0] not in list_data7:
                    list_data7.append(k[0])
                    #init()
                    #print (Fore.RED +k[0])
                    t = PrettyTable(['(*)', k])
                    print t

        print_data8 = open('log_scan.txt','r')

        regex = '([Sophos]{6,6}....+)'

        list_data8 = []

        for line11 in print_data8:
            line11 = line11.rstrip()
            l = re.findall('([Sophos]{6,6}....+)', line11)
            if len(l) > 0 :
                if l[0] not in list_data8:
                    list_data8.append(l[0])
                    #init()
                    #print (Fore.RED +l[0])
                    t = PrettyTable(['(*)', l])
                    print t

        print_data9 = open('log_scan.txt','r')

        regex = '([Avira]{5,5}....+)'

        list_data9 = []

        for line12 in print_data9:
            line12 = line12.rstrip()
            m = re.findall('([Avira]{5,5}....+)', line12)
            if len(m) > 0 :
                if m[0] not in list_data9:
                    list_data9.append(m[0])
                    #init()
                    #print (Fore.RED +m[0])
                    
                    t = PrettyTable(['(*)', m])
                    #t.add_row(['2', m])
                    print t

        print_data10 = open('log_scan.txt','r')

        regex = '([Malwarebytes]{12,12}....+)'

        list_data10 = []

        for line13 in print_data10:
            line13 = line13.rstrip()
            p = re.findall('([Malwarebytes]{12,12}....+)', line13)
            if len(p) > 0 :
                if p[0] not in list_data10:
                    list_data10.append(p[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', p])
                    print t  


        print_data20 = open('log_scan.txt','r')

        regex = '([FireEye]{7,7}....+)'

        list_data20 = []

        for line20 in print_data20:
            line20 = line20.rstrip()
            q = re.findall('([FireEye]{7,7}....+)', line20)
            if len(q) > 0 :
                if q[0] not in list_data20:
                    list_data20.append(q[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', q])
                    print t    


        print_data30 = open('log_scan.txt','r')

        regex = '([AegisLab]{8,8}....+)'

        list_data30 = []

        for line30 in print_data30:
            line30 = line30.rstrip()
            r = re.findall('([AegisLab]{8,8}....+)', line30)
            if len(r) > 0 :
                if r[0] not in list_data30:
                    list_data30.append(r[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', r])
                    print t       



        print_data32 = open('log_scan.txt','r')

        regex = '([ALYac]{5,5}....+)'

        list_data32 = []

        for line32 in print_data32:
            line32 = line32.rstrip()
            w = re.findall('([ALYac]{5,5}....+)', line32)
            if len(w) > 0 :
                if w[0] not in list_data32:
                    list_data32.append(w[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', w])
                    print t         


        print_data29 = open('log_scan.txt','r')

        regex = '([Arcabit]{7,7}....+)'

        list_data29 = []

        for line29 in print_data29:
            line29 = line29.rstrip()
            o = re.findall('([Arcabit]{7,7}....+)', line29)
            if len(o) > 0 :
                if o[0] not in list_data29:
                    list_data29.append(o[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', o])
                    print t         
                         

        print_data28 = open('log_scan.txt','r')

        regex = '([Cyren]{5,5}....+)'

        list_data28 = []

        for line28 in print_data28:
            line28 = line28.rstrip()
            n = re.findall('([Cyren]{5,5}....+)', line28)
            if len(n) > 0 :
                if n[0] not in list_data28:
                    list_data28.append(n[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', n])
                    print t      




        print_data27 = open('log_scan.txt','r')

        regex = '([DrWeb]{5,5}....+)'

        list_data27 = []

        for line27 in print_data27:
            line27 = line27.rstrip()
            e = re.findall('([DrWeb]{5,5}....+)', line27)
            if len(e) > 0 :
                if e[0] not in list_data27:
                    list_data27.append(e[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', e])
                    print t    



        print_data26 = open('log_scan.txt','r')

        regex = '([F-Secure]{8,8}....+)'

        list_data26 = []

        for line26 in print_data26:
            line26 = line26.rstrip()
            a = re.findall('([F-Secure]{8,8}....+)', line26)
            if len(a) > 0 :
                if a[0] not in list_data26:
                    list_data26.append(a[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', a])
                    print t      



        print_data25 = open('log_scan.txt','r')

        regex = '([Comodo]{6,6}....+)'

        list_data25 = []

        for line25 in print_data25:
            line25 = line25.rstrip()
            i = re.findall('([Comodo]{6,6}....+)', line25)
            if len(i) > 0 :
                if i[0] not in list_data25:
                    list_data25.append(i[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', i])
                    print t      


        print_data24 = open('log_scan.txt','r')

        regex = '([Emsisoft]{8,8}....+)'

        list_data24 = []

        for line24 in print_data24:
            line24 = line24.rstrip()
            z = re.findall('([Emsisoft]{8,8}....+)', line24)
            if len(z) > 0 :
                if z[0] not in list_data24:
                    list_data24.append(z[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', z])
                    print t      




        print_data22 = open('log_scan.txt','r')

        regex = 'ESET-NOD32....+'

        list_data22 = []

        for line22 in print_data22:
            line22 = line22.rstrip()
            uu = re.findall('ESET-NOD32....+', line22)
            if len(uu) > 0 :
                if uu[0] not in list_data22:
                    list_data22.append(uu[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', uu])
                    print t    


        print_data23 = open('log_scan.txt','r')

        regex = 'Ad-Aware....+'

        list_data23 = []

        for line23 in print_data23:
            line23 = line23.rstrip()
            x = re.findall('Ad-Aware....+', line23)
            if len(x) > 0 :
                if x[0] not in list_data23:
                    list_data23.append(x[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', x])
                    print t    



        print_data31 = open('log_scan.txt','r')

        regex = 'AhnLab-V3....+'

        list_data31 = []

        for line31 in print_data31:
            line31 = line31.rstrip()
            v = re.findall('AhnLab-V3....+', line31)
            if len(v) > 0 :
               if v[0] not in list_data31:
                   list_data31.append(v[0])
                   #init()
                   #print (Fore.RED +p[0])
                   t = PrettyTable(['(*)', v])
                   print t    



        print_data21 = open('log_scan.txt','r')

        regex = 'CAT-QuickHeal....+'

        list_data21 = []

        for line21 in print_data21:
            line21 = line21.rstrip()
            sa = re.findall('CAT-QuickHeal....+', line21)
            if len(sa) > 0 :
                if sa[0] not in list_data21:
                    list_data21.append(sa[0])
                    #init()
                    #print (Fore.RED +p[0])
                    t = PrettyTable(['(*)', sa])
                    print t              

           




        #init()
        #print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")



    elif opcion == 3:

        ############################################################################################################
        
        print ("")
        init()  
        print(Fore.RED + "[*]"+Fore.WHITE+"    Hello and welcome to " +Fore.GREEN+ "Software_analizer (**)\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   With this script you can optimize your time, do a quick analysis before analyzing ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   with other tools that may take a little  more time to give you a result. ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   This tool will show a series of results such as metadata, hash and malware analysis")
        init()
        print(Fore.RED + "[!]"+Fore.WHITE+"   This script makes use of and depends on the following tools for its operation " +Fore.GREEN+ ":\n")
        init()
        print(Fore.CYAN + "[1]"+Fore.WHITE+"       Md5sum V 8.28")
        init()
        print(Fore.CYAN + "[2]"+Fore.WHITE+"       Automater ")
        init()
        print(Fore.CYAN + "[2]"+Fore.WHITE+"       File type ")
        init()
        print(Fore.CYAN + "[2]"+Fore.WHITE+"       String ")
        init()
        print(Fore.CYAN + "[3]"+Fore.WHITE+"       Exiftool V 10.80\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   In the same way, Software_analizer.py makes use of regular expressions to filter the ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   data that we need,use of the libraries (os, time, re, time, color, tqdm and sleep)\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   It is important to keep in mind that if you are going to use Kali linux you  ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   should only install the tqdm librarybut if you are going to use Windows you")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   must install all the libraries with the option pip install \n\n")

        ########################################################################################
    


    elif opcion == 4:

        ############################################################################################################
        
        print ("")
        init()  
        print(Fore.RED + "[*]"+Fore.WHITE+"    Hello and welcome to " +Fore.GREEN+ "Software_analizer (**)\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   This is a small guide to how Software Analyzer is used \n")
        init()
        print(Fore.CYAN + "[1]"+Fore.WHITE+"   Use the Software Analyzer menu, choose the option (1) drag the software to the Terminal window")
        init()
        print(Fore.CYAN + "[2]"+Fore.WHITE+"   Use the Software Analyzer menu, choose the ocpion (2) to visualize the results\n")
        init()
        print(Fore.RED + "[!]"+Fore.WHITE+"    If you want to analyze the software a little more, use the RegShot Filter menu, for this you must follow the following steps: " +Fore.GREEN+ ":\n")
        init()
        print(Fore.CYAN + "[1]"+Fore.WHITE+"   Download and install RegShot on a Windows virtual machine")
        init()
        print(Fore.CYAN + "[2]"+Fore.WHITE+"   Run RegShot Filter to have a first capture of the system")
        init()
        print(Fore.CYAN + "[3]"+Fore.WHITE+"   Install the software to analyze in the Windows virtual machine to have a second capture of the system")
        init()
        print(Fore.CYAN + "[4]"+Fore.WHITE+"   Compare the two captures with RegShot, this will generate a file (TXT)")
        init()
        print(Fore.CYAN + "[5]"+Fore.WHITE+"   Save that result (log) in a file called (doc.txt) and paste it in the Software_Analizer.py folder")
        init()
        print(Fore.CYAN + "[6]"+Fore.WHITE+"   Make use of the RegShot filter menu and extract the results\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   :)\n")
        

        ########################################################################################

    elif opcion == 5:
        
        #data = os.system('netstat -ano')
        #os.system('netstat -ano > c:\escaneo1.txt')
        print ("")
        """
        time.sleep(5)"""
        ############################################################################################################################################ inicio
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Coincidences of (port) or ports found")
        init()
        print (Fore.WHITE + "")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras1 = ['port', 'n/a', 'n/a']
        palabra1 = 'port'
        ocurrencias = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra1 in linea:
                    ocurrencias.append(linea)

        for frase in ocurrencias:
            aImprimir1 = frase
            for palabra1 in palabras1:
                if palabra1 in frase:
                    aImprimir1 = re.sub(r'(%s)' % palabra1, r'%s\1%s' % (RED, NOCOLOR), frase)

                    url06 = frase
                    f1 = open ('port.txt','a')
                    f1.write(url06)
                    f1.flush()
                    break
                    
            print(aImprimir1) 
            
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")    
        #print (ocurrencias)
        ############################################################################################################################################## fin
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Coincidences of (.exe) or executables found")
        print ("")
        print ("")
        init()
        print (Fore.WHITE + "")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'
        palabras = ['.exe', 'n/a', 'n/a']
        palabra = '.exe'
        ocurrencias1 = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra in linea:
                    ocurrencias1.append(linea)            
        #print (ocurrencias1)
        for frase in ocurrencias1:
            aImprimir = frase
            for palabra in palabras:
                if palabra in frase:
                    aImprimir = re.sub(r'(%s)' % palabra, r'%s\1%s' % (RED, NOCOLOR), frase)
                    

                    url02 = frase
                    f1 = open ('exe.txt','a')
                    f1.write(url02)
                    f1.flush()
                    break
            print(aImprimir)

            
        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        #print (len(ocurrencias1))
        ############################################################################################################################################ inicio
        #os.system("gnome-terminal -e 'sudo apt-get update'")

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Matches of (www) or URL found ")
        print ("")
        init()
        print (Fore.WHITE + "")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras2 = ['www', 'n/a']
        palabra2 = 'www'
        ocurrencias2 = []
        lista02 = []
        comillas = '""'
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra2 in linea:
                    ocurrencias2.append(linea)

                           
        for frase in ocurrencias2:
            aImprimir2 = frase
            for palabra2 in palabras2:
                if palabra2 in frase:
                    aImprimir2 = re.sub(r'(%s)' % palabra2, r'%s\1%s' % (RED, NOCOLOR), frase)

                    url01 = frase
                    f1 = open ('www.txt','a')
                    f1.write(url01)
                    f1.flush()
                    break

            print(aImprimir2)            
        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("") 
        ############################################################################################################################################ fin

        ############################################################################################################################################ inicio
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Matches of (http) or URL found")
        print ("")
        init()
        print (Fore.WHITE + "")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras3 = ['http', '.com', 'n/a']

        palabra3 = 'http'
        ocurrencias3 = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra3 in linea:
                    ocurrencias3.append(linea)

        for frase in ocurrencias3:
            aImprimir3 = frase
            for palabra3 in palabras3:
                if palabra3 in frase:
                    aImprimir3 = re.sub(r'(%s)' % palabra3, r'%s\1%s' % (RED, NOCOLOR), frase)
                    
                    url03 = frase
                    f1 = open ('http.txt','a')
                    f1.write(url03)
                    f1.flush()
                    break
            print(aImprimir3)
        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("") 
        ############################################################################################################################################ fin


        ############################################################################################################################################ inicio
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Coincidences of (TCP) or protocol found ")
        print ("")
        init()
        print (Fore.WHITE + "")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras4 = ['tcp', '.com', 'n/a']

        palabra4 = 'tcp'
        ocurrencias4 = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra4 in linea:
                    ocurrencias4.append(linea)

        for frase in ocurrencias4:
            aImprimir4 = frase
            for palabra4 in palabras4:
                if palabra4 in frase:
                    aImprimir4 = re.sub(r'(%s)' % palabra4, r'%s\1%s' % (RED, NOCOLOR), frase)
                    
                    url04 = frase
                    f1 = open ('tcp.txt','a')
                    f1.write(url04)
                    f1.flush()
                    break
            print(aImprimir4)

        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("") 
    elif opcion == 6:
        
        print ("")
       
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Found URLs")
        print ("")
        init()
        print (Fore.WHITE + "")

        #########################################################################################
        
        """input = ('ingrese su nombre')
        text = 'URLs son www.prueba.com'
        match_pattern = re.search(r'www.prueba.com', text)
        print (match_pattern.group(0))"""

        #########################################################################################

        analizar_url = open('url.txt','w')

        regex = '[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]'


        datos2 = open('www.txt')
        for line2 in datos2:
            line2 = line2.rstrip()
            y = re.findall('[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]', line2)
            if len(y) > 0 :
                analizar_url.write(str(y[0]+ "\n"))
                print (y[0])

        analizar_url = open('url.txt','w')


        lines = [line.strip() for line in open('www.txt', 'r')]
        for x in lines:
            found_h = re.search('[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]+', x)
            if found_h:
                analizar_url.write(x + "\n")
                
        """datos2 = open('usuario.txt')
        for line2 in datos2:
            line2 = line2.rstrip()
            y = re.findall('.*?Validation,(\w+).*', line2)
            if len(y) > 0 :
                print (y[0])"""

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        ########################################################################################

        #########################################################################################
    elif opcion == 7:
        
        print ("")    

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Analysis of URLs found")
        print ("")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Starting Analysis, this may take several minutes, please wait ")
        print ("")

        for i in tqdm(range(100)):
            sleep(0.02)

        
        ruta_carpeta = os.path.dirname(os.path.realpath(__file__))
        ruta_log = ruta_carpeta+'/url.txt'
        os.system("automater"+" " +ruta_log)

        #ruta_log = os.path.dirname(os.path.realpath(__file__))

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(3)
        print ("")
    elif opcion == 8:
        salir = True
    else:
        print ("Enter a number between 1 and 8")
print ("") 
print ("********Finished script***********")
print ("")

#comandos error

"""ping 
 apt-cache show nmap
 apt-cache search nmap
 sudo apt-get install python-nmap
 sudo apt-get install python3-nmap

"""

#paginas de consulta
#https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/
#http://www.poketcode.com/es/python/archivos_csv/index.html
#http://python-para-impacientes.blogspot.com/2014/02/ejecutar-un-comando-externo.html




#######################################################################################
# Fuentes
# https://www.solvetic.com/tutoriales/article/3871-como-guardar-resultado-comando-en-archivo-texto-linux/
# https://caminosdigitales.es/ejecutar-systeminfo-y-guardar-en-archivo-con-python/
# https://lapertenencia.wordpress.com/2014/08/16/python-guardando-resultado-comandos-linux-en-una-variable/