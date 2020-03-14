from operator import itemgetter
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
        return cmp(op1, op2)
    return not cmp(op1,op2)

def inegal_compare(op1,op2):
    '''
    Modalitate de comparare a doi operanzi
    Input: op1,op2
    Preconditii: op1- primul operand
                 op2-al doilea operand
    Returneaza True daca inegalitatea este adevarata si false in caz contrar
    '''
    if op1<op2:
        return True
    return False

def insertSort(lista,*, key=lambda x:x, reverse=False, cmp=inegal_compare):
    '''
    Programul sorteaza o lista de elemente utilizand metoda Insertion Sort
    Input: lista, key, reverse, cmp
    Preconditii: lista-lista care trebuie ordonata
                 key- criteriul dupa care se face ordonarea; este o functie care returneazaoperanzii care se vor compara pentru fiecare element al listei
                 reverse- True/False =Descrescator/Crescator
                 cmp= modalitatea dupa care se realizaeaza compararea <,>,<=,>= etc. este o functie care returneaza true sau false
    Functia returneaza lista ordonata in functie de criteriile cerute
    '''
    for i in range(1,len(lista)):
        ind=i-1
        val=lista[i]
        while ind>=0 and compare(key(val),key(lista[ind]),reverse,cmp):
            lista[ind+1]=lista[ind]
            ind=ind-1
        lista[ind+1]=val
    return lista

def testSortare():
    l=[9,-20,13,89,56,1]
    assert insertSort(l)==[-20,1,9,13,56,89]
    assert insertSort(l, reverse=True)==[89,56,13,9,1,-20]
    l=[(987,-5),(-9,291),(19,123)]
    assert insertSort(l, key=itemgetter(1))==[(987,-5),(19,123),(-9,291)]
    assert insertSort(l, key=itemgetter(0))==[(-9,291),(19,123),(987,-5)]
    assert insertSort(l, key=itemgetter(1), reverse=True)==[(-9,291),(19,123),(987,-5)]
    
testSortare()
        
