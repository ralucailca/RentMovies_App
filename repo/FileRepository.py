
from repo.Repository import *
from model.Client import *
from model.Film import *
from model.Inchiriere import *
from file.fileUtils import clearFileContent, transferDate 


class FilmFileRepo(object):
    def __init__(self,filename):
        self.__filename=filename
        
    def __createFilmFromLine(self,line):
        '''
        Creaza un obiect de tip film dintr-o linie a fisierului data ca parametru
        Input: linie
        Preconditii: strin citit din fisier corespunzatoare unei linii (pana la enter)
        '''
        fields=line.split(' ')
        idf=int(fields[0])
        titlu=fields[1]
        an=fields[2]
        g=fields[3]
        gen=''
        n=len(g)
        for i in range(0,n-1):
            gen+=g[i]
        if g[n-1]!='\n':
            gen+=g[n-1]
        f=Film(idf,titlu,an,gen)
        return f
        
    def adauga(self,elem):
        '''
        Adauga un element in fisier
        '''
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue
                film=self.__createFilmFromLine(line)
                if film==elem:
                    raise ValueError('Element existent!')
                    return 
        f=open(self.__filename,'a')
        f.write('\n')
        f.write(str(elem))
        f.write('\n')
        f.close()
        
    def cauta(self,elem):
        '''
        Cauta si returneaza un element in fisier dupa id
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                film=self.__createFilmFromLine(line)
                if film==elem:
                    gasit=True
                    f=film
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
        return f
    
    def cauta_titlu(self,titlu):
        '''
        Cauta si returneaza filmele care contine un titlu cerut 
        Input: titlu
        Preconditii: titlu-string
        '''
        rez=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue
                film=self.__createFilmFromLine(line)
                if titlu in film.get_titlu():
                    rez.append(film)
        return rez
    
    def sterge(self,elem):
        '''
        Sterge un element din fisier
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                film=self.__createFilmFromLine(line)
                if film==elem:
                    gasit=True
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
        g=open('fisier_intermediar.txt','a')
        clearFileContent('fisier_intermediar.txt')
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='': 
                    continue
                film=self.__createFilmFromLine(line)
                if film!=elem:
                    g.write(str(film))
                    g.write('\n')
        g.close()
        clearFileContent(self.__filename)
        transferDate('fisier_intermediar.txt',self.__filename)
        
    def update(self,elem):
        '''
        Modifica un element existent in fisier
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                film=self.__createFilmFromLine(line)
                if film==elem:
                    gasit=True
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
        g=open('fisier_intermediar.txt','a')
        clearFileContent('fisier_intermediar.txt')
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='': 
                    continue
                film=self.__createFilmFromLine(line)
                if film!=elem:
                    g.write(str(film))
                    g.write('\n')
                elif film==elem:
                    g.write(str(elem))
                    g.write('\n')
        g.close()
        clearFileContent(self.__filename)
        transferDate('fisier_intermediar.txt',self.__filename)
        
    def getAll(self):
        '''
        Returneaza toate filmele din fisier
        '''
        allf=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue 
                film=self.__createFilmFromLine(line)
                allf.append(film)
        return allf
    
    def __len__(self):
        '''
        Returneaza lungimea fisierului, adica numarul de filme din fisier
        '''
        allf=self.getAll()
        return len(allf)
                    
   
class ClientFileRepo(object):
     
    def __init__(self,filename):
        self.__filename=filename
        
    def __createClientFromLine(self,line):
        '''
        Creeaza clinetul corespunzator unei linii din fisier
        Returneaza clientul
        '''
        fields=line.split(' ')
        idc=int(fields[0])
        nume=fields[1]
        c=fields[2]
        cnp=''
        for i in c:
            if i!='\n':
                cnp+=i
        client=Client(idc, nume, cnp)
        return client
         
    def adauga(self,elem):
        '''
        Adauga un element in fisier
        '''
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue
                client=self.__createClientFromLine(line)
                if client==elem:
                    raise ValueError('Element existent!')
                    return 
        f=open(self.__filename,'a')
        f.write('\n')
        f.write(str(elem))
        f.write('\n')
        f.close()
        
             
    def cauta(self,elem):
        '''
        Cauta si returneaza un element in fisier dupa id
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                client=self.__createClientFromLine(line)
                if client==elem:
                    gasit=True
                    c=client
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
        return c
    
    def cautaNume(self,nume):
        '''
        Cauta si returneaza toti clientii care au un anumit nume 
        Input: nume
        Preconditii: nume-string
        '''
        rez=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue
                client=self.__createClientFromLine(line)
                if nume in client.get_nume():
                    rez.append(client)
        return rez
       
    def sterge(self,elem):
        '''
        Sterge un element din fisier
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                client=self.__createClientFromLine(line)
                if client==elem:
                    gasit=True
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
        g=open('fisier_intermediar.txt','a')
        clearFileContent('fisier_intermediar.txt')
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='': 
                    continue
                client=self.__createClientFromLine(line)
                if client!=elem:
                    g.write(str(client))
                    g.write('\n')
        g.close()
        clearFileContent(self.__filename)
        transferDate('fisier_intermediar.txt',self.__filename) 
           
    def update(self,elem):
        '''
        Modifica un element existent in fisier
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                client=self.__createClientFromLine(line)
                if client==elem:
                    gasit=True
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
            
        g=open('fisier_intermediar.txt','a')
        clearFileContent('fisier_intermediar.txt')
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='': 
                    continue
                client=self.__createClientFromLine(line)
                if client!=elem:
                    g.write(str(client))
                    g.write('\n')
                elif client==elem:
                    g.write(str(elem))
                    g.write('\n')
        g.close()
        clearFileContent(self.__filename)
        transferDate('fisier_intermediar.txt',self.__filename)
        
    def getAll(self):
        '''
        Returneaza toti clientii din fisier
        '''
        allc=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue 
                client=self.__createClientFromLine(line)
                allc.append(client)
        return allc
    
    def __len__(self):
        '''
        Returneaza lungimea fisierului, adica numarul de filme din fisier
        '''
        allc=self.getAll()
        return len(allc)
        
    

        
    
class InchiriereFileRepo(object):  
    
    
    def __init__(self,filename):
        self.__filename=filename
         
    def __createInchFromLine(self,line):
        fields=line.split(' ')
        idf=int(fields[0])
        idc=int(fields[1])
        returnare=fields[2]
        f=Film(idf,None,None,None)
        c=Client(idc,None,None)
        i=Inchiriere(f,c,returnare)
        return i
    
    def adauga(self,elem):
        '''
        Adauga un element in fisier
        '''
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue
                i=self.__createInchFromLine(line)
                if i==elem:
                    raise ValueError('Element existent!')
                    return 
        f=open(self.__filename,'a')
        f.write('\n')
        line=str(elem.get_film().get_idf())+' '+str(elem.get_client().get_idc())+' '+elem.get_returnare()
        f.write(line)
        f.write('\n')
        f.close()
    
    def cauta(self,elem):
        '''
        Cauta si returneaza un element in fisier dupa id
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                i=self.__createInchFromLine(line)
                if i==elem:
                    gasit=True
                    inchiriere=i
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
        return inchiriere
    
    def sterge(self,elem):
        '''
        Sterge un element din fisier
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                i=self.__createInchFromLine(line)
                if i==elem:
                    gasit=True
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
        g=open('fisier_intermediar.txt','a')
        clearFileContent('fisier_intermediar.txt')
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='': 
                    continue
                i=self.__createInchFromLine(line)
                if i!=elem:
                    line=str(i.get_film().get_idf())+' '+str(i.get_client().get_idc())+' '+i.get_returnare()
                    g.write(line)
                    g.write('\n')
        g.close()
        clearFileContent(self.__filename)
        transferDate('fisier_intermediar.txt',self.__filename)
   
    def update(self,elem):
        '''
        Modifica un element existent in fisier
        '''
        with open(self.__filename) as f:
            gasit=False
            for line in f:
                if line.strip()=='':
                    continue
                i=self.__createInchFromLine(line)
                if i==elem:
                    gasit=True
            if gasit==False:
                raise ValueError('Element inexistent!')
                return 
            
        g=open('fisier_intermediar.txt','a')
        clearFileContent('fisier_intermediar.txt')
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='': 
                    continue
                i=self.__createInchFromLine(line)
                if i!=elem:
                    line=str(i.get_film().get_idf())+' '+str(i.get_client().get_idc())+' '+i.get_returnare()
                    g.write(line)
                    g.write('\n')
                elif i==elem:
                    line=str(elem.get_film().get_idf())+' '+str(elem.get_client().get_idc())+' '+elem.get_returnare()
                    g.write(line)
                    g.write('\n')
        g.close()
        clearFileContent(self.__filename)
        transferDate('fisier_intermediar.txt',self.__filename)
    
    def getAll(self):
        '''
        Returneaza toti clientii din fisier
        '''
        alli=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue 
                i=self.__createInchFromLine(line)
                alli.append(i)
        return alli
    
    def __len__(self):
        '''
        Returneaza lungimea fisierului, adica numarul de filme din fisier
        '''
        alli=self.getAll()
        return len(alli)
    
    def cauta_film(self,elem):
        '''
        Functia care returneaza toate inchirierile in care apare filmul cerut 
        Input:elem
        Preconditii: elem este un onicet de tipul film
        '''
        rez=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue
                i=self.__createInchFromLine(line)
                if i.get_film()==elem:
                    rez.append(i)
        return rez
    
    def cauta_client(self,elem):
        '''
        Functia care returneaza toate inchirierile in care apare clientul cerut
        Input: elem
        Preconditii: elem este un obiect de tipul client
        '''
        rez=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=='':
                    continue
                i=self.__createInchFromLine(line)
                if i.get_client()==elem:
                    rez.append(i)
        return rez
    
