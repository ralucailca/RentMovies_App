class Film(object):
    '''
        Tip de data abstract pentru filme
    '''

    def __init__(self,__idf,__titlu,__an,__gen):
        '''
             Initializeaza un film
             idf-int
             titlu-string
             an-strin, 4 cifre
             gen-string
        '''
        self.__idf=__idf
        self.__titlu=__titlu
        self.__an=__an
        self.__gen=__gen
        
    def __str__(self):
        '''
        Functia care treansforma un obiect de tipul film in string
        Returneaza un string format din instantele obiectului
        '''
        return str(self.__idf)+' '+self.__titlu+' '+self.__an+' '+self.__gen
    
    def __eq__(self,other):
        '''
        Functai care verifica daca doua obiecte de tipul film sunt egale
        Verificaea se face dupa id
        Functia returneaza True daca obiectele au acelasi id si False in caz contrar
        '''
        return self.__idf==other.__idf
    
    def get_idf(self):
        '''
        Functia care returneaza id-ul filmului
        '''
        return self.__idf


    def get_titlu(self):
        '''
        Functia care returneaza titlul filmului
        '''
        return self.__titlu


    def get_an(self):
        '''
        Functia care returneaza anul filmului
        '''
        return self.__an


    def get_gen(self):
        '''
        Functia care returneaza genul filmului
        '''
        return self.__gen


    def set_titlu(self, value):
        '''
        Functia care modifica titlul filmului
        '''
        self.__titlu = value


    def set_an(self, value):
        '''
        Functia care modifica anul filmului
        '''
        self.__an = value


    def set_gen(self, value):
        '''
        Functia care modifica genul filmului
        '''
        self.__gen = value

    
    idf = property(get_idf, None, None, None)
    titlu = property(get_titlu, set_titlu, None, None)
    an = property(get_an, set_an, None, None)
    gen = property(get_gen, set_gen, None, None)
    
    


