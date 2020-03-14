class Inchiriere(object):
    '''
        Tip de data abstract pentru inchiriere
    '''
    
    def __init__(self,__film,__client,__returnare):
        '''
            Initializeaza un obiect de tip
            __film-obiect tip film
            __client-obiect tip client
            __returnare-string sub forma de data zz/ll/aaaa
        '''
        self.__client=__client
        self.__film=__film
        self.__returnare=__returnare

    def set_client(self, value):
        '''
        Schimba valoarea clientului
        value-obiect de tip client
        '''
        self.__client = value


    def set_film(self, value):
        '''
        Schimba valoarea filmului
        value-obiect de tip film 
        '''
        self.__film = value


    def get_client(self):
        '''
        Returneaza un obiect de tip client
        '''
        return self.__client


    def get_film(self):
        '''
        Returneaza un obiect de tip film
        '''
        return self.__film


    def get_returnare(self):
        '''
        Returneaza o data de returnare
        Returneaza un string
        '''
        return self.__returnare


    def set_returnare(self, value):
        '''
        Schibma stringul returnare cu un alt string value
        '''
        self.__returnare = value

    def __eq__(self,other):
        return self.__film==other.__film and self.__client==other.__client
    
    def __str__(self):
        return str(self.__film)+' '+str(self.__client)+' '+self.__returnare
    
    client = property(get_client, None, None, None)
    film = property(get_film, None, None, None)
    returnare = property(get_returnare, set_returnare, None, None)
    client = property(None, set_client, None, None)
    film = property(None, set_film, None, None)
    
  


    
        


