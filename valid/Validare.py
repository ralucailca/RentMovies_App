import time
from datetime import date

class ValidatorFilm(object):
    def __init__(self):
        pass
    
    def ValidareFilm(self,film):
        '''
        Functia care valideaza un film
        Input: self,film
        Preconditii: film-obiect din clasa Film
        Arunca eroare daca id-ul este negativ, titlul sau genul filmului este vid si daca anul de aparitie al filmului este mai mare decat anul curent 2018
        '''
        er=''
        if film.get_idf()<0:
            er+='id negativ!\n'
        if film.get_titlu()=='':
            er+='titlu invalid!\n'
        if film.get_an()>'2019' or film.get_an()<'1900':
            er+='an invalid!\n'
        if film.get_gen()=='':
            er+='gen invalid!\n'
        if len(er)>0:
            raise ValueError(er)
        
class ValidatorClient(object):
    def __init__(self):
        pass
     
    def ValidareClient(self,client):
        '''
        Functia care valideaza un client
        Input: self,client
        Preconditii: client- obiect din clasa client 
        Arunca erorare daca id-ul e negativ, numele este inexistent sau cnp-ul nu e valid
        CNP-ul nu e valid daca:
                -are numar de cifre diferit de 13
                -nu exista luna
                -nu exista ziua in luna respectiva
                -nu are cifrele de inceput una dintre urmatoarele:1,2,5,6
        '''
        er=''
        if client.get_idc()<0:
            er+='id negativ!\n'
        if client.get_nume()=='':
            er+='nume invalid!\n'
        else:
            ok=1
            nume=client.get_nume()
            if nume[0]<'A' or nume[0]>'Z':
                ok=0
            for i in range(1,len(nume)):
                if nume[i]<'a' or nume[i]>'z':
                    ok=0
            if ok==0:
                er+='nume invalid!\n'
                
        cnp=client.get_cnp()
        ok=1
        if len(cnp)!=13:
            ok=0
        else:
            cif='0123456789'
            for i in range(len(cnp)):
                if cnp[i] not in cif:
                    ok=0
            else:
                s='1256'
                if cnp[0] not in s:
                    ok=0
    
                zile={'01': 31, '02': 29, '03': 31, '04': 30, '05':31, '06': 30, '07': 31, '08': 31,
                      '09': 30, '10': 31, '11': 30, '12': 31}
                zi=int(cnp[5:7])
                an=int(cnp[1:3])
                luna=cnp[3:5]
                if luna not in zile:
                    ok=0
                else:
                    if zi>zile[luna]:
                        ok=0
                    if luna=='02':
                        if an==0 or an%4!=0: #verificam daca anul nu este bisect
                            if zi>28:
                                ok=0
        if ok==0:
            er+='CNP invalid!\n' 
        if len(er)>0:
            raise ValueError(er)

class ValidatorInchiriere(object):
    def __init__(self):
        pass
    
    def ValidareInchiriere(self,inchiriere):
        '''
        Functia care valideaza un obiect de tip inchiriere
        Verifica daca clientul exista sau nu in lista de clienti
        Verifica daca clientul exista sau nu in lista de filme 
        Verifica daca data este valida
        '''
        er=''
        returnare=inchiriere.get_returnare()
        if self.__validareDataReturnare(returnare)==False:
            er+='Data returnare invalida\n'
        if len(er)>0:
            raise ValueError(er)

          
    def __validareDataReturnare(self,returnare):
        '''
        Functia care verifica daca data este valida in functie de data curenta
        Inpu: returnare
        Preconditii: returnare= data returnarii sub forma zz/ll/aaaa (z-zi,l-luna,a-an)
        Returneaza True daca data este considerata valida si False in caz contrar
        Verifica ca data returnarii sa fie dupa data curenta din ziua crearii inchirierii respective
        Verifica sa exista numarul de zile in luna respectiva si sa existe luna 
        '''
        dret=returnare.split('/')
        datac=str(date.today())
        datac=datac.split('-')
        ok=True
        num='0123456789/'
        if len(returnare)!=10:
            return False
        elif len(returnare)==10:
            for i in range(0,10):
                if returnare[i] not in num:
                    return False
                if ok:
                    anc=int(datac[0])
                    lc=datac[1]
                    zc=int(datac[2])
                    anr=int(dret[2])
                    lr=dret[1]
                    zr=int(dret[0])
            
                    if anc>anr: #daca anul curent mai mic decat anul returnarii
                        return False
                    if anc==anr and lr<lc: #daca anul curent egal cu cel al returnarii, dar luna returnarii este in urma celei curente
                        return False
                    if anc==anr and lr==lc and zr<zc: #daca anul si luna curenta sunt egale cu cele ale returnarii, dar ziua returnarii este in urma celei curente
                        return False
                    zile={'01': 31, '02': 29, '03': 31, '04': 30, '05':31, '06': 30, '07': 31, '08': 31,
                                  '09': 30, '10': 31, '11': 30, '12': 31}
                    if lr not in zile:
                        return False
                    else:
                        if zr>zile[lr]:
                            return False
                        if lr=='02':
                            if anr==0 or anr%4!=0: #verificam daca anul nu este bisect
                                if zr>28:
                                    return False
        return True                        
        
        
