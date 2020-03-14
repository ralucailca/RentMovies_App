from random import *
import string

class Console(object):
    def __init__(self,__contrFilm,__contrClient,__contrInchiriere):
        self.__contrFilm=__contrFilm
        self.__contrClient=__contrClient
        self.__contrInchiriere=__contrInchiriere
     
    '''    
    def __stringGenerator(self, size=randrange(6,10), chars=string.ascii_lowercase):
        return ''.join(choice(chars) for _ in range(size))
    '''
        
    def __construireString(self,r,size):
        '''
        Functia care contrsuieste recursiv un string de numere aleatoriu
        '''
        litere=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','v','x','y','z']
        if size!=1:
            r=self.__construireString(r,size-1)
        r+=choice(litere)
        return r
        
    def __uiGeneratorFilme(self,params):
        '''
        Functia care genereaza aleatoriu un numar cerut de filme pe care le adauga in lista
        Int: params
        Preconditii: lungimea listei params este de un element
                     contine numarul de filme care trebuie generate
        '''
        if len(params)!=1:
            print('Numar invalid de params!')
            return
        g=['romantic','drama','actiune','comedie']
        majuscule=['A','B','C','D','E','F','G','H','I','J','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        listid=[]
        for i in range(0,int(params[0])):
            id=randrange(0,1000000,1)
            if id not in listid:
                an=str(randrange(1900,2019,1))
                titlu=choice(majuscule)+self.__construireString('', randint(5,13))
                gen=choice(g)
                while True:
                    try:
                        self.__contrFilm.adaugaFilm(id,titlu,an,gen)
                        
                    except ValueError:
                        break
            listid.append(id)
                
                
    def __uiGeneratorClienti(self,params):
        '''
        Functia care genereaza aleatoriu un numar cerut de clienti pe care ii adauga in lista
        Int: params
        Preconditii: lungimea listei params este de un element
                     contine numarul de clineit care trebuie generati
        '''
        if len(params)!=1:
            print('Numar invalid de params!')
            return
        gen=['1','2','5','6']
        majuscule=['A','B','C','D','E','F','G','H','I','J','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        listid=[]
        for i in range(0,int(params[0])):
            id=randrange(0,1000000,1)
            if id not in listid:
                nume=choice(majuscule)+self.__construireString('', randint(5,10))
                CNP=str(choice(gen))+str(randint(10,99))+'0'+str(randint(1,9))+'0'+str(randint(1,9))+str(randint(100,999))+str(randint(100,999))
                while True:
                    try:
                        self.__contrClient.adaugaClient(id,nume,CNP)
                    except ValueError as er :
                        print(er)
                        break
            listid.append(id)
            
    def __uiAdaugaFilm(self,params):
        '''
        Functia care adauga un film in lista de filme
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari formarii obiectului
        '''
        if len(params)!=4:
            print('Numar de parametrii invalid!')
            return
        try:
            idf=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        titlu=params[1]
        an=params[2]
        gen=params[3]
        self.__contrFilm.adaugaFilm(idf,titlu,an,gen)
    
    def __uiAdaugaClient(self,params):
        '''
        Functia care adauga un client in lista de clienti
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari dormarii obiectului
        '''
        if len(params)!=3:
            print('Numar de parametrii invalid!')
            return
        try:
            idc=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        nume=params[1]
        CNP=params[2]
        self.__contrClient.adaugaClient(idc,nume,CNP)
    
    def __uiStergeFilm(self,params):
        '''
        Functia care sterge un film in lista de filme
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari dormarii obiectului
        '''
        if len(params)!=1:
            print('Numar invalid de parametrii!')
            return
        try:
            idf=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        self.__contrInchiriere.stergeDupaFilm(idf)
        self.__contrFilm.stergeFilm(idf)
    
    def __uiStergeClient(self,params):
        '''
        Functia care sterge un client in lista de clienti
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari dormarii obiectului
        '''
        if len(params)!=1:
            print('Numar invalid de parametrii!')
            return
        try:
            idc=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        self.__contrInchiriere.stergeDupaClient(idc)
        self.__contrClient.stergeClient(idc)
    
    def __uiModificaFilm(self,params):
        '''
        Functia care modifica un film in lista de filme
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari dormarii obiectului
        '''
        if len(params)!=4:
            print('Numar invalid de parametrii!')
            return
        try:
            idf=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        titlu=params[1]
        an=params[2]
        gen=params[3]
        self.__contrFilm.modificaFilm(idf,titlu,an,gen)
        self.__contrInchiriere.modificaDupaFilm(idf)
        
        
    
    def __uiModificaClient(self,params):
        '''
        Functia care modicica un client in lista de clienti
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari dormarii obiectului
        '''
        if len(params)!=3:
            print('Numar de parametrii invalid!')
            return
        try:
            idc=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        nume=params[1]
        CNP=params[2]
        self.__contrClient.modificaClient(idc,nume,CNP)
        self.__contrInchiriere.modificaDupaClient(idc)
    
    def __uiCautaFilm(self,params):
        '''
        Functia care cauta un film in lista de filme
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari dormarii obiectului
        '''
        if len(params)!=1:
            print('Numar invalid de parametrii!')
            return
        try:
            idf=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        film=self.__contrFilm.cautaFilm(idf)
        print(film)
    
    def __uiCautaClient(self,params):
        '''
        Functia care cauta un client in lista de clienti
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari dormarii obiectului
        '''
        if len(params)!=1:
            print('Numar invalid de parametrii!')
            return
        try:
            idc=int(params[0])
        except ValueError:
            print('Id-ul nu este numar intreg!')
            return
        client=self.__contrClient.cautaClient(idc)
        print(client)
        
    def __print_lista(self,l,n): #functie recursiva lab12
        '''
            Functia are afiseaza recursiv pe ecran o lista 
            Input: l
            l-lista de elemente
            n-numarul de elemente din lista
        '''
        if n>0:
            self.__print_lista(l,n-1)
            print(l[n-1])
    
    def __uiPrintFilme(self,params):
        '''
        Functia care tipareste lista de filme
        '''
        if len(params)!=0:
            print("Numar invalid de params!")
            return
        l=self.__contrFilm.getAllF()
        self.__print_lista(l,len(l))
    
    def __uiPrintClienti(self,params):
        '''
        Functia care tipareste lista de clienti
        
        '''
        if len(params)!=0:
            print("Numar invalid de params!")
            return
        l=self.__contrClient.getAllC()
        for el in l:
            print(el)
            
    def __uiAdaugaInchiriere(self,params):
        ''' 
        Functia care adauga o inchiriere in lista de inchirieri
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari formarii obiectului
                     3 parametrii neceasri- primul id-ul filmului
                                            al doilea id-ul clientului
                                            data returnarii sub forma zz/ll/aaaa (z-zi,l-luna,a-an)
        '''
        if len(params)!=3:
            print('Numar invalid de parametrii!')
            return
        idf=int(params[0])
        idc=int(params[1])
        returnare=params[2]
        self.__contrInchiriere.adaugaInchiriere(idf,idc,returnare)
        
    def __uiStergeInchiriere(self,params):
        '''
        Functia care sterge o inchiriere din lista
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari formarii obiectului
                     2 parametrii neceasri- primul id-ul filmului
                                            al doilea id-ul clientului
        '''
        if len(params)!=2:
            print('Numar invalid de parametrii!')
            return
        idf=int(params[0])
        idc=int(params[1])
        self.__contrInchiriere.stergeInchiriere(idf,idc)
    
    def __uiModificaInchiriere(self,params):
        '''
        Functia care modifica o inchiriere si anume data acesteia
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari formarii obiectului cu care se va modifica
                    3 parametrii neceasri- primul id-ul filmului
                                            al doilea id-ul clientului
                                            data returnarii sub forma zz/ll/aaaa (z-zi,l-luna,a-an) cea finala, cu care se va modifica cea initiala
        '''
        if len(params)!=3:
            print('Numar invalid de parametrii!')
            return
        idf=int(params[0])
        idc=int(params[1])
        returnare=params[2]
        self.__contrInchiriere.modificaInchiriere(idf,idc,returnare)
    
    def __uiCautaInchiriere(self,params):
        '''
        Functia care cauta o inchiriere in lista dupa id-ul clientului si cel al filmului
        Verifica daca utilizatorul a dat parametrii necesari
        Preconditii: params=lista de parametrii necesari formarii obiectului
                     2 parametrii neceasri- primul id-ul filmului
                                            al doilea id-ul clientului
        '''
        if len(params)!=2:
            print('Numar invalid de parametrii!')
            return
        idf=int(params[0])
        idc=int(params[1])
        inchiriere=self.__contrInchiriere.cautaInchiriere(idf,idc)
        print(inchiriere)
    
    def __uiPrintInchirieri(self,params):
        '''
        Functia care afiseaza toate inchirierile sub forma:
           id film-titlu film id client-nume client data returnarii
        Nu are parametrii
        '''
        if len(params)!=0:
            print('Numar invalid de parametrii!')
            return
        listaInchirieri=self.__contrInchiriere.getAllI()
        for el in listaInchirieri:
            print(el)
            
    def __uiTopFilme(self,params):
        '''
        Functia care afiseaza filmele cele mai inchiriate de catre clienti
        '''
        if len(params)!=0:
            print('Numar invalid de params')
            return
        topFilme=self.__contrInchiriere.TopFilme()
        for f in topFilme:
            print(f)
            
    def __uiOrdonareNume(self,params):
        '''
        Functia care afiseaza inchirierile ordonate dupa numele clientilor
        '''
        if len(params)!=0:
            print('Numar invalid de params')
            return
        clienti=self.__contrInchiriere.ordonareNume()
        for c in clienti:
            print(c)
            inchirieri=self.__contrInchiriere.cauta_client(c.get_idc())
            for i in inchirieri:
                print('      '+str(i.get_film())+' '+i.get_returnare())
                
    def __uiOrdonareNumar(self,params):
        '''
        Functia care afiseaza inchirierile ordonate dupa numele clientilor
        '''
        if len(params)!=0:
            print('Numar invalid de params')
            return
        clienti=self.__contrInchiriere.ordonareNumar()
        for c in clienti:
            print(c)
            inchirieri=self.__contrInchiriere.cauta_client(c.get_idc())
            for i in inchirieri:
                print('      '+str(i.get_film())+' '+i.get_returnare())
                
    def __uiTopClienti(self,params):
        '''
        Functia care afiseaza primi 30% clienti cu cele mai multe filme inchiriate
        '''
        if len(params)!=0:
            print('Numar invalid de params')
            return
        topClienti=self.__contrInchiriere.topClienti()
        for c in topClienti:
            print(c[0].get_nume()+' a inchiriat '+str(c[1])+' filme.')
            
    def __uiTopGenuri(self,params):
        '''
        Functia care afiseaza genurile filmelor in ordine descrescatoare dupa numarul de inchirieri al filmelor cu genul respectiv
        '''
        if len(params)!=0:
            print('Numar invalid de params')
            return
        topGenuri=self.__contrInchiriere.topGenuri()
        for g in topGenuri:
            print(g[0]+' cu un numar de '+str(g[1])+' inchirieri.')
            
    def __uiCautaTitlu(self,params):
        '''
        Fucntia care afiseaza toate filmele care contin un titlu
        '''
        if len(params)!=1:
            print('Numar invalid de params')
            return
        filme=self.__contrFilm.cautaTitlu(params[0])
        for f in filme:
            print(f)
            
    def __uiCautaInchTitlu(self,params):
        '''
        Functia care afiseaza filmele cu titlul cautat si toate inchirierile in care ele apar
        '''
        if len(params)!=1:
            print('Numar invalid de params')
            return
        rez=self.__contrInchiriere.cautaInchTitlu(params[0]) #returneaza o liste de liste, fiecare 
        for el in rez:
            print(str(el[0].get_film()))
            for i in el:
                print('    '+str(i.get_client())+' '+i.get_returnare())
                
    def __uiCautaNume(self,params):
        '''
        Functia care afiseaza toti clientii care contin un nume
        '''
        if len(params)!=1:
            print('Numar invalid de params')
            return
        clienti=self.__contrClient.cautaNume(params[0])
        for c in clienti:
            print(c)
            
    def __uiCautaInchNume(self,params):
        '''
        Functia care afiseaza clientii cu numele cautat si toate inchirierile in care acestia apar
        '''
        if len(params)!=1:
            print('Numar invalid de params')
            return
        rez=self.__contrInchiriere.cautaInchNume(params[0]) #returneaza o liste de liste, fiecare 
        for el in rez:
            print(str(el[0].get_client()))
            for i in el:
                print('    '+str(i.get_film())+' '+i.get_returnare())
                
    def __meniu(self):
        print('MENIU-COMENZI')
        print('Adauga film: adaugaFilm')
        print('Adauga client: adaugaClient')
        print('Sterge film: stergeFilm')
        print('Sterge client: stergeClient')
        print('Modifica film: modificaClient')
        print('Modifica client: modificaFilm')
        print('Cauta film: cautaFilm')
        print('Cauta client: cautaClient')
        print('Afiseaza lista de filme: printf')
        print('Afiseaza lista de clienti: printc')
        print('Adauga inchiriere: adaugaInchiriere')
        print('Sterge inchiriere: stergeinchiriere')
        print('Modifica inchiriere: modificaInchiriere')
        print('Cauta inchiriere: cautaInchiriere')
        print('Afiseaza toate inchirierile: printi')
        print('Genereaza filme: generareFilme')
        print('Genereaza clienti: generareClienti')
        print('Cele mai inchiriate filme: topFilme')
        print('Clientii cu filmele ordonate dupa numele clientilor: ordonareNume')
        print('Clienti cu filmele ordonate dupa numarul de filme inchiriate: ordonareNumar')
        print('Primi 30% clienti cu cele mai multe filme: topClienti ')
        print('Top cele mai preferate genuri de filme: topGenuri')
        print('Cauta filmele care contin un titlu: cautaTitlu')
        print('Cauta inchirieri care au un film ce contine un anumit titlu: cautaInchTitlu')
        print('Cauta cleintii care contin un nume: cautaNum')
        print('Cauta inchirieri care au un client ce contine un anumit nume: cautaInchNume')
    
    def run(self):
        '''
        Functia care apeleaza aplicatia, citeste comenzile de la tastatura date de utilizator si le executa, apeleaza corespunzator
        '''
        comenzi={'adaugaFilm':self.__uiAdaugaFilm, 'adaugaClient':self.__uiAdaugaClient,
                 'stergeFilm':self.__uiStergeFilm, 'stergeClient':self.__uiStergeClient,
                 'modificaFilm':self.__uiModificaFilm, 'modificaClient':self.__uiModificaClient,
                 'cautaFilm':self.__uiCautaFilm, 'cautaClient':self.__uiCautaClient,
                 'printf':self.__uiPrintFilme, 'printc':self.__uiPrintClienti,
                 'adaugaInchiriere':self.__uiAdaugaInchiriere, 'stergeInchiriere': self.__uiStergeInchiriere,
                 'modificaInchiriere':self.__uiModificaInchiriere,'cautaInchiriere':self.__uiCautaInchiriere,
                 'printi':self.__uiPrintInchirieri,
                 'generareFilme': self.__uiGeneratorFilme, 'generareClienti': self.__uiGeneratorClienti,
                 'topFilme':self.__uiTopFilme, 'ordonareNume':self.__uiOrdonareNume,
                 'ordonareNumar':self.__uiOrdonareNumar, 'topClienti':self.__uiTopClienti,
                 'topGenuri':self.__uiTopGenuri, 'cautaTitlu': self.__uiCautaTitlu, 'cautaInchTitlu': self.__uiCautaInchTitlu,
                 'cautaNume': self.__uiCautaNume, 'cautaInchNume': self.__uiCautaInchNume
                 }
        self.__meniu() 
        while True:
            cmd=input('>>')
            param=cmd.split(' ')
            if param[0]=='exit':
                return
            elif param[0] in comenzi:
                try:
                    comenzi[param[0]](param[1:])
                except ValueError as er:
                    print(er)
            elif param[0] not in comenzi and param[0]!='exit':
                print('Comanda invalida. Incercati alta comanda!')
                
        
        

