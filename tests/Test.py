from model.Film import Film
from model.Client import Client
from model.Inchiriere import Inchiriere
from valid.Validare import ValidatorClient,ValidatorFilm,ValidatorInchiriere 
from repo.Repository import *
from business.Controllers import ControllerFilm, ControllerClient, ControllerInchiriere
from file.fileUtils import clearFileContent
from repo.FileRepository import *


class Test(object):
    
    def __init__(self):
        self.__idf=2
        self.__titlu='Titanic'
        self.__an='1997'
        self.__gen='romantic'
        self.__film=Film(self.__idf,self.__titlu,self.__an,self.__gen)
        self.__bidf=-23
        self.__btitlu=''
        self.__ban='2398'
        self.__bgen=''
        self.__bfilm=Film(self.__bidf,self.__btitlu,self.__ban,self.__bgen)
        self.__idc=5
        self.__nume='Mihai'
        self.__CNP='1990212113344'
        self.__client=Client(self.__idc,self.__nume,self.__CNP)
        self.__bidc=-5
        self.__bnume=''
        self.__bCNP='9995067113342'
        self.__bclient=Client(self.__bidc,self.__bnume,self.__bCNP)
        self.__validatorf=ValidatorFilm()
        self.__validatorc=ValidatorClient()
        #self.__filmRepo=FilmRepository()
        #self.__clientRepo=ClientRepository()
        #self.__contrFilm=ControllerFilm(self.__filmRepo,self.__validatorf)
        #self.__contrClient=ControllerClient(self.__clientRepo,self.__validatorc)
        self.__returnare='27/12/2020'
        self.__inchiriere=Inchiriere(self.__film,self.__client,self.__returnare)
        self.__breturnare='12/13/2015'
        self.__binchiriere=Inchiriere(self.__bfilm,self.__bclient,self.__breturnare)
        self.__validatorir=ValidatorInchiriere()
        #self.__inchiriereRepo=InchiriereRepository()
        #self.__contrInchiriere=ControllerInchiriere(self.__inchiriereRepo,self.__validatorir,self.__filmRepo,self.__clientRepo)
        self.__filename='test.txt'
        self.__filenamec='testClienti.txt'
        self.__filenamei='testInchirieri.txt'
        clearFileContent(self.__filename)
        clearFileContent(self.__filenamec)
        clearFileContent(self.__filenamei)
        self.__fileRepof=FilmFileRepo('test.txt')
        self.__fileRepoc=ClientFileRepo(self.__filenamec)
        self.__fileRepoi=InchiriereFileRepo(self.__filenamei)
        self.__filmRepo=FilmFileRepo('test.txt')
        self.__clientRepo=ClientFileRepo(self.__filenamec)
        self.__inchiriereRepo=InchiriereFileRepo(self.__filenamei)
        self.__contrFilm=ControllerFilm(self.__filmRepo,self.__validatorf)
        self.__contrClient=ControllerClient(self.__clientRepo,self.__validatorc)
        self.__contrInchiriere=ControllerInchiriere(self.__inchiriereRepo,self.__validatorir,self.__filmRepo,self.__clientRepo)
        
        
    def __testModel(self):
        assert self.__film.get_idf()==self.__idf
        assert self.__film.get_titlu()==self.__titlu
        assert self.__film.get_an()==self.__an
        assert self.__film.get_gen()==self.__gen
        assert self.__client.get_idc()==self.__idc
        assert self.__client.get_nume()==self.__nume
        assert self.__client.get_cnp()==self.__CNP
        assert str(self.__film)=='2 Titanic 1997 romantic'
        assert str(self.__client)=='5 Mihai 1990212113344'
        self.__client.set_nume('Alin')
        assert self.__client.get_nume()=='Alin'
        assert self.__inchiriere.get_client()==self.__client
        assert self.__inchiriere.get_film()==self.__film
        assert self.__inchiriere.get_returnare()==self.__returnare
        self.__inchiriere.set_returnare('17/11/2020')
        assert self.__inchiriere.get_returnare()=='17/11/2020'
    
        
    def __testValidare(self):
        try:
            self.__validatorf.ValidareFilm(self.__film)
            assert True
        except ValueError:
            assert False  
        
        try:
            self.__validatorf.ValidareFilm(self.__bfilm)
            assert False
        except ValueError as er:
            assert str(er)=='id negativ!\ntitlu invalid!\nan invalid!\ngen invalid!\n'
            
        try:
            self.__validatorc.ValidareClient(self.__client)
            assert True
        except ValueError:
            assert False
        
        try:
            self.__validatorc.ValidareClient(self.__bclient)
            assert False 
        except ValueError as ev:
            assert str(ev)=='id negativ!\nnume invalid!\nCNP invalid!\n'
        try:
            self.__validatorir.ValidareInchiriere(self.__inchiriere)
            assert True
        except ValueError as er:
            assert False
        try:
            self.__validatorir.ValidareInchiriere(self.__binchiriere)
            assert False
        except ValueError as er:
            assert str(er)=='Data returnare invalida\n'
   
    def __testRepo(self):
        assert len(self.__filmRepo)==0
        assert len(self.__clientRepo)==0
        self.__filmRepo.adauga(self.__film)
        assert len(self.__filmRepo)==1
        try:
            self.__filmRepo.adauga(self.__film)
        except ValueError as er:
            assert str(er)=='Element existent!'
        try:
            self.__filmRepo.cauta(self.__bfilm)
        except ValueError as er:
            assert str(er)=='Element inexistent!'
        keyFilm=Film(self.__idf,None,None,None)
        assert self.__filmRepo.cauta(keyFilm)==self.__film
        self.__filmRepo.adauga(self.__bfilm)
        assert self.__filmRepo.getAll()==[self.__film, self.__bfilm]
        newFilm=Film(self.__bidf,'AmericanPie','2013','comedie')
        self.__filmRepo.update(newFilm)
        assert self.__filmRepo.getAll()==[self.__film,newFilm]
        self.__filmRepo.sterge(self.__film)
        assert self.__filmRepo.getAll()==[newFilm]
        removeElem=Film(self.__bidf,None,None,None)
        self.__filmRepo.sterge(removeElem)
        try:
            self.__filmRepo.update(removeElem)
        except ValueError as er:
            assert str(er)=='Element inexistent!'
        assert self.__filmRepo.getAll()==[]
   
            
    def __testController(self):
        assert self.__contrFilm.getAllF()==[]
        self.__contrFilm.adaugaFilm(self.__idf,self.__titlu,self.__an,self.__gen)
        assert self.__contrFilm.getAllF()==[self.__film]
        newFilm=Film(7,'MazeRunner','2017','actiune')
        self.__contrFilm.adaugaFilm(7,'MazeRunner','2017','actiune')
        assert self.__contrFilm.getAllF()==[self.__film,newFilm]
        try:
            self.__contrFilm.adaugaFilm(self.__bidf,self.__btitlu,self.__ban,self.__bgen)
            assert False
        except ValueError as er:
            assert str(er)=='id negativ!\ntitlu invalid!\nan invalid!\ngen invalid!\n'
        assert self.__contrFilm.getAllF()==[self.__film,newFilm]
        assert self.__contrClient.getAllC()==[]
        self.__contrClient.adaugaClient(self.__idc,self.__nume,self.__CNP)
        assert self.__contrClient.getAllC()==[self.__client]
        newClient=Client(19,'Mihaela','2931229111335')
        self.__contrClient.adaugaClient(19,'Mihaela','2931229111335')
        assert self.__contrClient.getAllC()==[self.__client,newClient]
        try:
            self.__contrClient.adaugaClient(self.__bidc,self.__bnume,self.__bCNP)
        except ValueError as er:
            assert str(er)=='id negativ!\nnume invalid!\nCNP invalid!\n'
        assert self.__contrClient.getAllC()==[self.__client,newClient]
        self.__contrFilm.stergeFilm(self.__idf)
        assert self.__contrFilm.getAllF()==[newFilm]
        try:
            self.__contrFilm.stergeFilm(self.__idf)
        except ValueError as er:
            assert str(er)=='Element inexistent!'
        upFilm=Film(7,'MazeRunner3','2018','actiune')
        self.__contrFilm.modificaFilm(7,'MazeRunner3','2018','actiune')
        assert self.__contrFilm.getAllF()==[upFilm]
        assert self.__contrFilm.cautaFilm(7)==upFilm
        assert self.__contrClient.cautaClient(self.__idc)==self.__client
        try:
            self.__contrFilm.cautaFilm(self.__idf)
            assert False
        except ValueError as er:
            assert str(er)=='Element inexistent!'
            
        self.__contrFilm.adaugaFilm(self.__idf,self.__titlu,self.__an,self.__gen)
            
        assert self.__contrInchiriere.getAllI()==[]
      
        self.__contrInchiriere.adaugaInchiriere(self.__idf,self.__idc,self.__returnare)
        assert self.__contrInchiriere.getAllI()==[self.__inchiriere]
        try:
            self.__contrInchiriere.adaugaInchiriere(self.__bidf,self.__bidc,self.__breturnare)
            assert False
        except ValueError as er:
            assert str(er)=='Element inexistent!'
        try:
            self.__contrInchiriere.modificaInchiriere(self.__bidf,self.__idc,'12/10/2020')
            assert False
        except ValueError as er:
            assert str(er)=='Element inexistent!'
        self.__contrInchiriere.modificaInchiriere(self.__idf,self.__idc,'12/10/2020')
        newInchiriere=Inchiriere(self.__film,self.__client,'12/10/2020')
        assert self.__contrInchiriere.getAllI()==[newInchiriere]
        try:
            self.__contrInchiriere.stergeInchiriere(self.__bidf,self.__idc)
            assert False
        except ValueError as er:
            assert str(er)=='Element inexistent!' 
        assert self.__contrInchiriere.cautaInchiriere(self.__idf,self.__idc)==newInchiriere
        try:
            self.__contrInchiriere.cautaInchiriere(self.__idf,self.__bidc)
            assert False
        except ValueError as er:
            assert str(er)=='Element inexistent!' 
        self.__contrInchiriere.stergeInchiriere(self.__idf,self.__idc)
        assert self.__contrInchiriere.getAllI()==[]
    
    def runTests(self):
        self.__testModel()
        self.__testValidare()
        self.__testRepo()
        self.__testController()
        #self.__testFileRepo()
        
       


