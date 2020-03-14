from tests.Test import Test
from repo.Repository import *
from repo.FileRepository import *
from valid.Validare import ValidatorClient,ValidatorFilm,ValidatorInchiriere
from business.Controllers import ControllerFilm, ControllerClient, ControllerInchiriere
from ui.Console import Console

t=Test()
t.runTests()
#filmRepo=FilmRepository()
filmRepo=FilmFileRepo('filme.txt')
#clientRepo=ClientRepository()
clientRepo=ClientFileRepo('clienti.txt')
#inchiriereRepo=InchiriereRepository()
inchiriereRepo=InchiriereFileRepo('inchirieri.txt')
validatorf=ValidatorFilm()
validatorc=ValidatorClient()
validatorinch=ValidatorInchiriere()
contrFilm=ControllerFilm(filmRepo,validatorf)
contrClient=ControllerClient(clientRepo,validatorc)
contrInchiriere=ControllerInchiriere(inchiriereRepo,validatorinch,filmRepo,clientRepo)
consola=Console(contrFilm,contrClient,contrInchiriere)
consola.run()