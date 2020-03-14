def clearFileContent(fileName):
    """
      Clear the content of the file
      Post: the given file exist and is empty
    """
    f = open(fileName, "w")
    f.close()
    
def transferDate(name_fisier1,name_fisier2):
        '''
        Functia care transfera toate datele dintr-un fisier in altul
        Input: name_fisier1,name_fisier2
        Preconditii: name_fisier1 - este un string si resprezinta numele fisierului din care se copiaza datele
                     name_fisier2 - este un strin si reprezinta numele fisierului in care se vor copia datele din fisierul1
                     
        '''
        g=open(name_fisier2,'a')
        with open(name_fisier1) as f:
            for line in f:
                if line.strip()=='':
                    continue
                g.write(line)
                g.write('\n')
        g.close()