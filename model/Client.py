class Client(object):
    '''
        Tip de data abstract pentru clienti 
    '''
    def __init__(self,__idc,__nume,__CNP):
        '''
        Initializeaza un client
        idc-int
        nume-string
        cnp-string, 13 cifre
        '''
        self.__idc=__idc
        self.__nume=__nume
        self.__CNP=__CNP
        
    def __str__(self):
        '''
        Functia care treansforma un obiect de tipul client in string
        Returneaza un string format din instantele obiectului
        '''
        return str(self.__idc)+' '+self.__nume+' '+self.__CNP
    
    def __eq__(self,other):
        '''
        Functai care verifica daca doua obiecte de tipul client sunt egale
        Verificaea se face dupa id
        Functia returneaza True daca obiectele au acelasi id si False in caz contrar
        '''
        return self.__idc==other.__idc

    def get_idc(self):
        '''
        Functia care returneaza id-ul clientului
        '''
        return self.__idc


    def get_nume(self):
        '''
        Functia care returneaza id-ul clientului
        '''
        return self.__nume


    def get_cnp(self):
        '''
        Functia care returneaza cnp-ul clientului
        '''
        return self.__CNP


    def set_nume(self, value):
        '''
        Functia care modifica numele unui client
        '''
        self.__nume = value


    def set_cnp(self, value):
        '''
        Functia care modifica cnp-ul unui client
        '''
        self.__CNP = value

    idc = property(get_idc, None, None, None)
    nume = property(get_nume, set_nume, None, None)
    CNP = property(get_cnp, set_cnp, None, None)
    
        


