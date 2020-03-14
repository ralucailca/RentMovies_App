from model.Film import Film
from model.Client import Client
from model.Inchiriere import Inchiriere
from operator import itemgetter 
from sortari.insertSort import *
from sortari.comboSort import *
from file.fileUtils import clearFileContent

 
class ControllerFilm(object):
    
    def __init__(self, __filmRepo,__validatorf):
        self.__filmRepo=__filmRepo
        self.__validatorf=__validatorf
        
    def adaugaFilm(self,idf,titlu,an,gen):
        '''
        Functia care adauga un element in lista de filme
        Input: idf,titlu,an,gen
        Preconditii: idf-id-ul filmului-
                     titlu-titlul filmului
                     an-anul de aparitie al filmului
                     gen-genul filmului
        Functia valideaza obiectul
        '''
        f=Film(idf,titlu,an,gen)
        self.__validatorf.ValidareFilm(f)
        self.__filmRepo.adauga(f)
        
    def getAllF(self):
        '''
        Fnctia care returneaza toate elementele din lista cu filme
        '''
        return self.__filmRepo.getAll()
    
    def stergeFilm(self,idf):
        '''
        Functia care sterge un element din lista cu filme
        Input: idf-id-ul filmului care trebuie sters
        '''
        f=Film(idf,None,None,None)
        self.__filmRepo.sterge(f)
        
    def modificaFilm(self,idf,titlu,an,gen):
        '''
        Functia care modifica un film in fucntie de id
        Input: idf,titlu,an,gen
        Preconditii: idf-id-ul filmului care trebuie inlocuit
                     titlu-titlul filmului nou
                     an-anul de aparitie al filmului nou
                     gen-genul filmului nou
        Functia valideaza obiectul
        '''
        f=Film(idf,titlu,an,gen)
        self.__validatorf.ValidareFilm(f)
        self.__filmRepo.update(f)
        
    def cautaFilm(self,idf):
        '''
        Functia care cauta un film in lista cu filme dupa id
        Input: idf
        Preconditii: idf-id-ul filmului care trebuie cautat
        Returneaza obiectul tip film cu id-ul cerut
        '''
        f=Film(idf,None,None,None)
        return self.__filmRepo.cauta(f)
    
    def cautaTitlu(self,titlu):
        '''
        Functia care returneaza toate filmele care contin un titlu
        '''
        rez=self.__filmRepo.cauta_titlu(titlu)
        return rez


class ControllerClient(object):

    def __init__(self,__clientRepo,__validatorc):
        self.__clientRepo=__clientRepo
        self.__validatorc=__validatorc
        
    def adaugaClient(self,idc,nume,CNP):
        '''
        Functia care adauga un element in lista de clienti
        Input: idc,nume,CNP
        Preconditii: idc-id client
                     nume- numele clientului
                     CNP-cnp-ul clientului
        Functia valideaza obiectul
        '''
        c=Client(idc,nume,CNP)
        self.__validatorc.ValidareClient(c)
        self.__clientRepo.adauga(c)
        
    def getAllC(self):
        '''
        Functia care returneaza toti clientii din lista
        '''
        return self.__clientRepo.getAll()
    
    def stergeClient(self,idc):
        '''
        Functia care sterege un client din lista de clienti
        Input: idc
        Preconditii: idc- id client care trebuie sters
        '''
        c=Client(idc,None,None)
        self.__clientRepo.sterge(c)
        
    def modificaClient(self,idc,nume,CNP):
        '''
        Fucntia care modifica un client din lista de clienti
        Input: idc,nume,CNP
        Preconditii: idc-id client care trebuie modificat
                     nume- numele clientului nou
                     CNP-cnp-ul clientului nou
        Functia valideaza obiectul
        '''
        c=Client(idc,nume,CNP)
        self.__validatorc.ValidareClient(c)
        self.__clientRepo.update(c)
        
    def cautaClient(self,idc):
        '''
        Functia care cauta in functie de id un client in lista de clienti
        Input: idc
        Preconditii: idc-id clientului
        Returneaza un obiect tip client
        '''
        c=Client(idc,None,None)
        return self.__clientRepo.cauta(c)
    
    def cautaNume(self, nume):
        '''
        Cauta si returneaza toti clientii care au un anumit nume 
        Input: nume
        Preconditii: nume-string
        '''
        rez=self.__clientRepo.cautaNume(nume)
        return rez


class ControllerInchiriere(object):
    
    def __init__(self,__inchiriereRepo,__validatorinch,__filmRepo,__clientRepo):
        self.__inchiriereRepo=__inchiriereRepo
        self.__validatorinch=__validatorinch
        self.__filmRepo=__filmRepo
        self.__clientRepo=__clientRepo
        self.__finalizareInchirieri()
        
    def __finalizareInchirieri(self):
        '''
        Functia finalizeaza o inchiriere din repository cu fisier prin adugarea clinetului si a filmului
        '''
        lista=self.__inchiriereRepo.getAll()
        for elem in lista:
            f=elem.get_film()
            c=elem.get_client()
            f=self.__filmRepo.cauta(f)
            c=self.__clientRepo.cauta(c)
            elem.set_film(f)
            elem.set_client(c)
  
    def adaugaInchiriere(self,idf,idc,returnare):
        '''
        Functia care adauga o inchiriere in lista de inchirieri
        Input: idf,idc,returnare
        Preconditii: idf-id-ul unui film deja adaugat in lista
                     idc-id-ul unui client deja adaugat in lista
                     returnare-data returnarii filmului
        '''
        f=Film(idf,None,None,None)
        c=Client(idc,None,None)
        film=self.__filmRepo.cauta(f)
        client=self.__clientRepo.cauta(c)
        i=Inchiriere(film,client,returnare)
        self.__validatorinch.ValidareInchiriere(i)
        self.__inchiriereRepo.adauga(i)
    
    def __completeaza_inchiriere(self,i):
        '''
            Functia care finalizeaza o inchiriere 
            Input: i-obiect tip inchiriere
        '''
        f=i.get_film()
        c=i.get_client()
        f=self.__filmRepo.cauta(f)
        c=self.__clientRepo.cauta(c)
        i.set_film(f)
        i.set_client(c)    
   
    def cautaInchTitlu(self,titlu):
        '''
        Functia care returneaza toate inchirirerile care contin un film cu un anumit titlu
        Returneaza o lista cu toate inchirierile in care filmul cu titlul cautat apare
        '''
        rez=[]
        filme=self.__filmRepo.cauta_titlu(titlu)
        for f in filme:
            i=self.__inchiriereRepo.cauta_film(f)
            for elem in i:
                self.__completeaza_inchiriere(elem)
            rez.append(i)
        return rez
    
    def cautaInchNume(self,nume):
        '''
        Functia care returneaza toate inchirirerile care contin un client cu un anumit nume
        Returneaza o lista cu toate inchirierile in care cleintul cu numele cautat apare
        '''
        rez=[]
        clienti=self.__clientRepo.cautaNume(nume)
        for c in clienti:
            i=self.__inchiriereRepo.cauta_client(c)
            for elem in i:
                self.__completeaza_inchiriere(elem)
            rez.append(i)
        return rez
        
                     
    def stergeInchiriere(self,idf,idc):
        '''
        Functia care sterge o inchiriere din lista de inchirieri
        Input: idf,idc
        Preconditii: idf-id-ul unui film deja adaugat in lista
                     idc-id-ul unui client deja adaugat in lista
        '''
        film=Film(idf,None,None,None)
        client=Client(idc,None,None)
        i=Inchiriere(film,client,None)
        self.__inchiriereRepo.sterge(i)
        
    def cautaInchiriere(self,idf,idc):
        '''
        Cauta in lista cu inchirieri inchirierea dupa id-ul filmului si cel al clientului
        Input: idf,idc
        Preconditii: idf-id-ul unui film deja adaugat in lista
                     idc-id-ul unui client deja adaugat in lista
        '''
        film=Film(idf,None,None,None)
        client=Client(idc,None,None)
        i=Inchiriere(film,client,None)
        i=self.__inchiriereRepo.cauta(i)
        film=self.__filmRepo.cauta(film)
        client=self.__clientRepo.cauta(client)
        i.set_client(client)
        i.set_film(film)
        return i
            
    
    def modificaInchiriere(self,idf,idc,returnare):
        '''
        Functia care modifica data inchirierii
        Input: idf,idc,returnare
        Preconditii: idf-id-ul unui film deja adaugat in lista
                     idc-id-ul unui client deja adaugat in lista
                     returnare-data returnarii filmului
        
        '''
        f=Film(idf,None,None,None)
        c=Client(idc,None,None)
        film=self.__filmRepo.cauta(f)
        client=self.__clientRepo.cauta(c)
        i=Inchiriere(film,client,returnare)
        self.__validatorinch.ValidareInchiriere(i)
        self.__inchiriereRepo.update(i)

    def getAllI(self):
        '''
        Functia care returneaza toate inchirierile din lista 
        '''
        lista=self.__inchiriereRepo.getAll()
        for elem in lista:
            self.__completeaza_inchiriere(elem)
        return lista

    
    def strInchiriere(self,idf,idc,returnare):
        '''
        Functia care returneaza un string care contine inchirierea
        '''
        f=Film(idf,None,None,None)
        c=Client(idc,None,None)
        film=self.__filmRepo.cauta(f)
        client=self.__clientRepo.cauta(c)
        return str(idf)+'-'+film.get_titlu()+' '+str(idc)+'-'+client.get_nume()+' '+returnare
    
    def __nrFilmeInchiriate(self,idc):
        '''
        Functia care calculeaza cate filme a inchiriat un singur client
        Input: idc
        Preconditii: idc- id-ul clientului 
        Returneaza numarul de filme inchiriate de catre clientul cu id-ul cerut
        '''
        nr=0
        listaInchirieri=self.getAllI()
        for i in listaInchirieri:
            client=i.get_client()
            if client.get_idc()==idc:
                nr+=1
        return nr
    
    def __nrFilmInchiriat(self,idf):
        '''
        Functia care caluleaza de cate ori a fost inchiriat un film
        Input: idf
        Preconditii: idf- id-ul filmului
        Returneaza numarul clientilor care a inchiriat acel film
        '''
        nr=0
        listaInchirieri=self.getAllI()
        for i in listaInchirieri:
            film=i.get_film()
            if film.get_idf()==idf:
                nr+=1
        return nr
    
    def TopFilme(self):
        '''
        Functia care returneaza cele mai inchiriate filme
        '''   
        max=0        
        listaFilme=self.__filmRepo.getAll()
        topFilme=[]
        for f in listaFilme:
            nr=self.__nrFilmInchiriat(f.get_idf())
            if nr>max:
                max=nr
        for f in listaFilme:
            nr=self.__nrFilmInchiriat(f.get_idf())
            if nr==max:
                topFilme.append(f)
        return topFilme    
    
    def cauta_client(self,idc):
        '''
        Functia care returneaza toate inchirierile in care apare clientul cerut
        Input: idc
        Preconditii: idc-id-ul clientului
        '''
        c=Client(idc,None,None)
        lista=self.__inchiriereRepo.cauta_client(c)
        for elem in lista:
            self.__completeaza_inchiriere(elem)
        return lista
        
    def ordonareNume(self):
        '''
        Functia care ordoneaza clientii care au inchiriat filme dupa numele lor
        '''
        inchirieri=self.getAllI()
        listaClienti=self.__clientRepo.getAll()
        clienti=[]
        for c in listaClienti:
            gasit=0
            for i in inchirieri:
                if c==i.get_client():
                    gasit=1
            if gasit==1 and c not in clienti:
                clienti.append(c)
        #clienti=sorted(clienti, key=lambda client: client.get_nume())
        clienti=insertSort(clienti, key=lambda client: client.get_nume())
        return clienti
    
    def ordonareNumar(self):
        '''
        Functia care ordoneaza clientii care au inchiriat filme dupa numarul de filme inchiriate
        '''
        inchirieri=self.getAllI()
        listaClienti=self.__clientRepo.getAll()
        clienti=[]
        nrFilme=[]
        for c in listaClienti:
            gasit=0
            for i in inchirieri:
                if c==i.get_client():
                    gasit=1
            if gasit==1:
                nr=self.__nrFilmeInchiriate(c.get_idc())
                el=(nr,c)
                if el not in nrFilme:
                    nrFilme.append(el)
        #nrFilme=sorted(nrFilme, key=itemgetter(0))
        nrFilme=insertSort(nrFilme, key=itemgetter(0))
        for el in nrFilme:
            clienti.append(el[1])
        return clienti
   
    def topClienti(self):
        '''
        Functia care calculeaza primii 30% clienti cu cele mai multe inchirieri
        Returneaza o lista care contine perechi cu:-clientul (obiect tip client)
                                                   -numarul de filme inchiriate
        '''
        c=self.__clientRepo.getAll()
        numarc=len(c)
        n=numarc
        clienti=self.ordonareNumar()
        if numarc!=len(clienti): #cazul in care avem clienti,dar acestia nu au inchiriat nimic. Ei trebuie adaugati la inceputul listei de clienti ordonati crescator
            nr0=[]
            for el in c:
                if el not in clienti:
                    nr0.append(el)
            clienti=nr0[:]+clienti[:]
        numarc=int((30*numarc)/100)   #30% din numarul total de clienti
        topc=[]
        for i in range(n-numarc,n):
            nr=self.__nrFilmeInchiriate(clienti[i].get_idc())
            topc.append((clienti[i],nr))   
        return topc
            
    def topGenuri(self):
        '''
        Functia care ordoneaza genurile filmelor in ordine descrascatoare in functie de numarul filmelor inchiriate cu genul respectiv
        Returneaza o lista care contine perechi cu:-genul de film
                                                   -numarul de filme cu genul respectiv inchiriate
        '''
        listaFilme=self.__filmRepo.getAll()
        listaGenuri=[]
        for f in listaFilme:
            if [f.get_gen(),0] not in listaGenuri:
                listaGenuri.append([f.get_gen(),0])
        listaInchirieri=self.getAllI()
        for i in listaInchirieri:
            film=i.get_film()
            for g in listaGenuri:
                if g[0]==film.get_gen():
                    g[1]+=1
        #listaGenuri=sorted(listaGenuri, key=itemgetter(1), reverse=True)
        #listaGenuri=insertSort(listaGenuri, key=itemgetter(1), reverse=True)
        listaGenuri=comboSort(listaGenuri, key=itemgetter(1), reverse=True)
        return listaGenuri
        
    def stergeDupaFilm(self,idf):
        '''
        Sterge toate inchirierile care contin filmul cu id-ul dat
        '''
        f=Film(idf,None,None,None)
        listaInchirieri=self.__inchiriereRepo.cauta_film(f)
        for el in listaInchirieri:
            self.__inchiriereRepo.sterge(el)
            
    def stergeDupaClient(self,idc):
        '''
        Sterge toate inchirierile care contin clientul cu id-ul dat
        '''
        c=Client(idc,None,None)
        listaInchirieri=self.__inchiriereRepo.cauta_client(c)    
        for el in listaInchirieri:
            self.__inchiriereRepo.sterge(el)
            
    def modificaDupaFilm(self, idf):
        '''
        Modifica toate inchirierile care au acelasi film
        '''
        f=Film(idf,None,None,None)
        film=self.__filmRepo.cauta(f)
        listaInchirieri=self.__inchiriereRepo.cauta_film(f)
        for el in listaInchirieri:
            i=Inchiriere(film,el.get_client(),el.get_returnare())
            self.__inchiriereRepo.update(i)
            
    def modificaDupaClient(self, idc):
        '''
        Modifica toate inchirierile care au acelasi cleint
        '''
        c=Client(idc,None,None)
        client=self.__clientRepo.cauta(c)
        listaInchirieri=self.__inchiriereRepo.cauta_client(c)
        for el in listaInchirieri:
            i=Inchiriere(el.get_film(),client,el.get_returnare())
            self.__inchiriereRepo.update(i)
        