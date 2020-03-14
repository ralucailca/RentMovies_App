from repo.FileRepository import FilmFileRepo, ClientFileRepo, InchiriereFileRepo
from valid.Validare import ValidatorInchiriere
from business.Controllers import ControllerInchiriere
import unittest
from model.Film import Film
from model.Inchiriere import Inchiriere
from model.Client import Client
from file.fileUtils import clearFileContent

class TestCaseInchirieriController(unittest.TestCase):
    def setUp(self):
        clearFileContent('testFilm1.txt')
        clearFileContent('testClienti1.txt')
        clearFileContent('testInchirieri1.txt')
        repof=FilmFileRepo('testFilm1.txt')
        repoc=ClientFileRepo('testClienti1.txt')
        repoi=InchiriereFileRepo('testInchirieri1.txt')
        validator=ValidatorInchiriere()
        self.contr=ControllerInchiriere(repoi,validator,repof,repoc)
        self.f1=Film(10,'Titanic','1997','romantic')
        self.f2=Film(11,'Divergent','2017','actiune')
        self.c1=Client(10,'Diana','2990806123456')
        self.c2=Client(12,'Valentin','1921012123456')
        repof.adauga(self.f1)
        repof.adauga(self.f2)
        repoc.adauga(self.c1)
        repoc.adauga(self.c2)
        self.contr.adaugaInchiriere(10, 10, '12/12/2019')
        self.contr.adaugaInchiriere(11, 12, '13/01/2020')
        self.contr.adaugaInchiriere(10, 12, '13/12/2019')
        
    def tearDown(self):         
        #cleanup code executed after every testMethod 
        pass
        
    def test_topFilme(self):
        self.assertTrue(self.contr.TopFilme()==[self.f1])
        
    def test_topGenuri(self):
        self.assertTrue(self.contr.topGenuri()==[['romantic',2], ['actiune',1]])
                        
    def test_ordonareNumar(self):
        self.assertTrue(self.contr.ordonareNumar()==[self.c1, self.c2])
        
    def test_ordonareNume(self):
        self.assertTrue(self.contr.ordonareNume()==[self.c1, self.c2])
        
    def test_topClienti(self):
        self.assertTrue(self.contr.topClienti()==[])
        
if __name__ == '__main__':     
    unittest.main()
        