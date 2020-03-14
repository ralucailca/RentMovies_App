from operator import itemgetter
def inegal_compare(op1,op2):
    '''
    Modalitate de comparare a doi operanzi, indica modul cum acestia se vor compara, adica cu < 
    Input: op1,op2
    Preconditii: op1- primul operand
                 op2-al doilea operand
    Returneaza True daca inegalitatea este adevarata si false in caz contrar
    '''
    if op1<op2:
        return True
    return False

def compare(op1,op2,reverse,cmp):
    '''
    Functia care compara doi operanzi utilizand un anumit criteriu de comparare si care decide modul de ordonare, crescaor sau descrescator
    Input: op1,op2,reverse,cmp
    Preconditii: op1-primul operand
                 op2-al doilea operand
                 reverse- True sau False (True pentru invers adica decrescator si False pentru crescator
                 cmp-functie care indica cum se vor compara operanzii
    '''
    if reverse==False:
        return not cmp(op1,op2)
    return cmp(op1,op2)

def getNextGap(gap):
    '''
    Functia care calculeaza urmatorul gap folosint shrink factor=1.3
    Se imparte la shrink factor, iar rezultatul trebuie sa fie numar intreg, adica se ia in considerare dpoar catul impartirii
    Daca rezultatul este mai mic decat 1 atunci se returneaza 1, altfel se returneaza valoarea calculata
    '''
    gap=(gap*10)//13
    if gap<1:
        return 1
    return gap

def comboSort(lista,*, key=lambda x:x, reverse=False, cmp=inegal_compare):
    '''
    Programul sorteaza o lista de elemente utilizand metoda Combo Sort
    Input: lista, key, reverse, cmp
    Preconditii: lista-lista care trebuie ordonata
                 key- criteriul dupa care se face ordonarea; este o functie care returneazaoperanzii care se vor compara pentru fiecare element al listei
                 reverse- True/False =Descrescator/Crescator
                 cmp= modalitatea dupa care se realizaeaza compararea <,>,<=,>= etc. este o functie care returneaza true sau false
    Functia returneaza lista ordonata in functie de criteriile cerute
    '''
    n=len(lista)
    gap=n
    swapped=True
    while gap!=1 or swapped==True:
        gap=getNextGap(gap)
        swapped=False
        #comparam toate elementele cu spatiul lipsa curent (current gap)
        for i in range(0,n-gap):
            if compare(key(lista[i]),key(lista[i+gap]),reverse,cmp):
                lista[i], lista[i+gap]=lista[i+gap],lista[i]
                swapped=True
    return lista


def testSortare():
    l=[9,-20,13,89,56,1]
    assert comboSort(l)==[-20,1,9,13,56,89]
    assert comboSort(l, reverse=True)==[89,56,13,9,1,-20]
    l=[(987,-5),(-9,291),(19,123)]
    assert comboSort(l, key=itemgetter(1))==[(987,-5),(19,123),(-9,291)]
    assert comboSort(l, key=itemgetter(0))==[(-9,291),(19,123),(987,-5)]
    assert comboSort(l, key=itemgetter(1), reverse=True)==[(-9,291),(19,123),(987,-5)]
    
testSortare()