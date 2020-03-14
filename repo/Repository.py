

class Repository(object):
    def __init__(self):
        self._elems=[]
        
    def __len__(self):
        '''
        Functai care returneaza lungimea unei liste oarecare a unui obiect din clasa repository
        '''
        return len(self._elems)
    
    def adauga(self,elem):
        '''
        Functia care adauga un element intr-o lista corespunzatoare obiectului de tip repository
        Input: elem
        Preconditii: elem- elemntul care trebuie adaugat
        In caz ca elementul deja este in lista atunci functia arunca o eroare
        '''
        if elem in self._elems:
            raise ValueError('Element existent!')
        self._elems.append(elem)
    
    def cauta(self,elem):
        '''
        Functia care cauta un element intr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie cautat
        Cautarea este realizata dupa id-ul obiectului
        Output: el
        Postconditii; el-obiect
        Returneaza elementul cautat 
        In caz ca elementul nu se afla in lista, functia arunca o eroare
        '''
        if elem not in self._elems:
            raise ValueError('Element inexistent!')
        for el in self._elems:
            if el==elem:
                return el
                
    def update(self,elem):
        '''
        Functia care modifica un element intr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie modificat
        Modificarea se face in functie de id-ul obiectului
        In caz ca elementul nu se afla in lista functia arunca o eroare
        '''
        if elem not in self._elems:
            raise ValueError('Element inexistent!')
        for i in range (len(self._elems)):
            if self._elems[i]==elem:
                self._elems[i]=elem
                return
            
    def sterge(self,elem):
        '''
        Functia care sterge un element dintr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie sters
        Stergerea se face in functie de id-ul obiectului
        Returneaza lista modificata
        In caz ca elementul nu se afla in lista functia arunca o eroare
        '''
        if elem not in self._elems:
            raise ValueError('Element inexistent!') 
        for i in range (0,len(self._elems)):
            if self._elems[i]==elem:
                del self._elems[i]
                return self._elems
            
    def getAll(self):
        '''
        Functia care returneaza toate elementele listei
        '''
        return self._elems[:]
    
class FilmRepository(object):
    
    def __init__(self):
        self.__elems=[]
        
    def __len__(self):
        '''
        Functai care returneaza lungimea unei liste oarecare a unui obiect din clasa repository
        '''
        return len(self.__elems)
    
    def adauga(self,elem):
        '''
        Functia care adauga un element intr-o lista corespunzatoare obiectului de tip repository
        Input: elem
        Preconditii: elem- elemntul care trebuie adaugat
        In caz ca elementul deja este in lista atunci functia arunca o eroare
        '''
        if elem in self.__elems:
            raise ValueError('Element existent!')
        self.__elems.append(elem)
    
    def cauta(self,elem):
        '''
        Functia care cauta un element intr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie cautat
        Cautarea este realizata dupa id-ul obiectului
        Output: el
        Postconditii; el-obiect
        Returneaza elementul cautat 
        In caz ca elementul nu se afla in lista, functia arunca o eroare
        '''  
        if elem not in self.__elems:
            raise ValueError('Element inexistent!')
        for el in self.__elems:
            if el==elem:
                return el
        
            
                
     
    def update(self,elem):
        if elem not in self.__elems:
                raise ValueError('Element inexistent!')
        for i in range (len(self.__elems)):
            if self.__elems[i]==elem:
                self.__elems[i].set_titlu(elem.get_titlu())
                self.__elems[i].set_an(elem.get_an())
                self.__elems[i].set_gen(elem.get_gen())
                return
            
    def sterge(self,elem):
        '''
        Functia care sterge un element dintr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie sters
        Stergerea se face in functie de id-ul obiectului
        Returneaza lista modificata
        In caz ca elementul nu se afla in lista functia arunca o eroare
        '''
        if elem not in self.__elems:
            raise ValueError('Element inexistent!') 
        for i in range (0,len(self.__elems)):
            if self.__elems[i]==elem:
                del self.__elems[i]
                return self.__elems
            
    def getAll(self):
        '''
        Functia care returneaza toate elementele listei
        '''
        return self.__elems[:]
   
            
class ClientRepository(Repository):
    
    def __init__(self):
        self.__elems=[]
        
    def __len__(self):
        '''
        Functai care returneaza lungimea unei liste oarecare a unui obiect din clasa repository
        '''
        return len(self.__elems)
    
    def adauga(self,elem):
        '''
        Functia care adauga un element intr-o lista corespunzatoare obiectului de tip repository
        Input: elem
        Preconditii: elem- elemntul care trebuie adaugat
        In caz ca elementul deja este in lista atunci functia arunca o eroare
        '''
        if elem in self.__elems:
            raise ValueError('Element existent!')
        self.__elems.append(elem)
    
    def cauta(self,elem):
        '''
        Functia care cauta un element intr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie cautat
        Cautarea este realizata dupa id-ul obiectului
        Output: el
        Postconditii; el-obiect
        Returneaza elementul cautat 
        In caz ca elementul nu se afla in lista, functia arunca o eroare
        '''
        
        if elem not in self.__elems:
            raise ValueError('Element inexistent!')
        for el in self.__elems:
            if el==elem:
                return el
        
                
      
    def update(self,elem):
        
        if elem not in self.__elems:
                raise ValueError('Element inexistent!')
        for i in range (len(self.__elems)):
            if self.__elems[i]==elem:
                self.__elems[i].set_nume(elem.get_nume())
                self.__elems[i].set_cnp(elem.get_cnp())
                return
            
            
    def sterge(self,elem):
        '''
        Functia care sterge un element dintr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie sters
        Stergerea se face in functie de id-ul obiectului
        Returneaza lista modificata
        In caz ca elementul nu se afla in lista functia arunca o eroare
        '''
        
        if elem not in self.__elems:
            raise ValueError('Element inexistent!') 
        for i in range (0,len(self.__elems)):
            if self.__elems[i]==elem:
                del self.__elems[i]
                return self.__elems
        
            
    def getAll(self):
        '''
        Functia care returneaza toate elementele listei
        '''
        return self.__elems[:]
    
 
class InchiriereRepository(object):
    def __init__(self):
        self.__elems=[]
        
    def __len__(self):
        '''
        Functai care returneaza lungimea unei liste oarecare a unui obiect din clasa repository
        '''
        return len(self.__elems)
    
    def adauga(self,elem):
        '''
        Functia care adauga un element intr-o lista corespunzatoare obiectului de tip repository
        Input: elem
        Preconditii: elem- elemntul care trebuie adaugat
        In caz ca elementul deja este in lista atunci functia arunca o eroare
        '''
        if elem in self.__elems:
            raise ValueError('Element existent!')
        self.__elems.append(elem)
    
    def cauta(self,elem):
        '''
        Functia care cauta un element intr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie cautat
        Cautarea este realizata dupa id-ul obiectului
        Output: el
        Postconditii; el-obiect
        Returneaza elementul cautat 
        In caz ca elementul nu se afla in lista, functia arunca o eroare
        '''
        if elem not in self.__elems:
            raise ValueError('Element inexistent!')
        for el in self.__elems:
            if el==elem:
                return el
            
                 
    def update(self,elem):
        '''
        Functia care modifica un element intr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie modificat
        Modificarea se face in functie de id-ul obiectului
        In caz ca elementul nu se afla in lista functia arunca o eroare
        '''
        if elem not in self.__elems:
            raise ValueError('Element inexistent!')
        for i in range (len(self.__elems)):
            if self.__elems[i]==elem:
                self.__elems[i]=elem
                return
            
    def sterge(self,elem):
        '''
        Functia care sterge un element dintr-o lista 
        Input: elem
        Preconditii: elem- elemntul care trebuie sters
        Stergerea se face in functie de id-ul obiectului
        Returneaza lista modificata
        In caz ca elementul nu se afla in lista functia arunca o eroare
        '''
        if elem not in self.__elems:
            raise ValueError('Element inexistent!') 
        for i in range (0,len(self.__elems)):
            if self.__elems[i]==elem:
                del self.__elems[i]
                return self.__elems
            
    def getAll(self):
        '''
        Functia care returneaza toate elementele listei
        '''
        return self.__elems[:]
            
    def cauta_film(self,elem):
        '''
        Functia care returneaza toate inchirierile in care apare filmul cerut 
        Input:elem
        Preconditii: elem este un onicet de tipul film
        '''
        inchirieri=[]
        for el in self.__elems:
            film=el.get_film()
            if film==elem:
                inchirieri.append(el)
        return inchirieri
    
    def cauta_client(self,elem):
        '''
        Functia care returneaza toate inchirierile in care apare clientul cerut
        Input: elem
        Preconditii: elem este un obiect de tipul client
        '''
        inchirieri=[]
        for el in self.__elems:
            client=el.get_client()
            if client==elem:
                inchirieri.append(el)
        return inchirieri 
                
                
