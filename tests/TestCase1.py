import unittest
from valid.Validare import ValidatorFilm
from business.Controllers import ControllerFilm
from model.Film import Film
from repo.FileRepository import FilmFileRepo
from file.fileUtils import clearFileContent


class TestCaseFilmController(unittest.TestCase):
    
    def setUp(self):
        val=ValidatorFilm()
        clearFileContent('testunitf.txt')
        repo=FilmFileRepo('testunitf.txt')
        self.contr=ControllerFilm(repo, val)
        self.contr.adaugaFilm(20,'Titanic','1997','romantic')
        self.f=Film(20,'Titanic','1997','romantic')
     
    def tearDown(self):         
        #cleanup code executed after every testMethod 
        pass
       
    def test_Adauga(self):
        self.assertTrue(self.contr.getAllF()==[self.f])
        self.assertRaises(ValueError,self.contr.adaugaFilm,-10, "", "1200", '')
        self.assertRaises(ValueError,self.contr.adaugaFilm,20,'Divergent','2017','actiune')
       
    def test_Cauta(self):
        self.assertTrue(self.contr.cautaFilm(20)==self.f)
        self.assertRaises(ValueError,self.contr.cautaFilm,2)
     
    def test_Modifica(self):
        self.contr.modificaFilm(20,'TitanicNew','2000','drama')
        self.assertTrue(self.contr.getAllF()==[Film(20,'TitanicNew','2000','drama')])
        self.assertRaises(ValueError,self.contr.modificaFilm,2,'TitanicNew','2000','drama')
        
    def test_Remove(self):
        self.assertRaises(ValueError,self.contr.stergeFilm,9)
        self.assertTrue(self.contr.getAllF()==[self.f])
        self.contr.stergeFilm(20)
        self.assertTrue(self.contr.getAllF()==[])
        self.assertEquals(self.f.get_idf(),20) 
        self.assertTrue(self.f.get_titlu()=="Titanic")         
        self.assertTrue(self.f.get_an()=="1997")  
        self.assertTrue(self.f.get_gen()=="romantic")
        
if __name__ == '__main__':     
    unittest.main()
          