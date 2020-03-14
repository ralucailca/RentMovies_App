from operator import itemgetter

def compare(op1,op2,reverse):
    '''
    Functia care compara doi operanzi si decide modul de ordonare, crescaor sau descrescator
    Input: op1,op2,reverse
    Preconditii: op1-primul operand
                 op2-al doilea operand
                 reverse- True sau False (True pentru invers adica decrescator si False pentru crescator
    '''
    if reverse==False:
        return op1<op2
    else:
        return op1>op2

def mergeSort(lista, key=lambda x:x, reverse=False):
    '''
    Programul sorteaza o lista de elemente utilizand metoda Insertion Sort
    Input: lista, key, reverse, cmp
    Preconditii: lista-lista care trebuie ordonata
                 key- criteriul dupa care se face ordonarea; este o functie care returneazaoperanzii care se vor compara pentru fiecare element al listei
                 reverse- True/False =Descrescator/Crescator
                 cmp= modalitatea dupa care se realizaeaza compararea <,>,<=,>= etc. este o functie care returneaza true sau false
    Functia returneaza lista ordonata in functie de criteriile cerute
    best case=worst case= average case= O(n*log2n) (Big-theta)
    '''
    if len(lista)>1:
        mij = len(lista)//2
        s = lista[:mij]
        d = lista[mij:]
     
         
        mergeSort(s,key,reverse)
        mergeSort(d,key,reverse)
    
        i=0
        j=0
        k=0
    
        while i < len(s) and j < len(d):
            if compare(key(s[i]),key(d[j]),reverse):
                lista[k]=s[i]
                i=i+1
            else:
                lista[k]=d[j]
                j=j+1
            k=k+1
    
        while i < len(s):
            lista[k]=s[i]
            i=i+1
            k=k+1
    
        while j < len(d):
            lista[k]=d[j]
            j=j+1
            k=k+1
   

def testSortare():
    l=[9,-20,13,89,56,1]
    mergeSort(l)
    assert l==[-20,1,9,13,56,89]
    l=[9,-20,13,89,56,1]
    mergeSort(l, reverse=True)
    assert l==[89,56,13,9,1,-20]
    l=[(987,-5),(-9,291),(19,123)]
    mergeSort(l, key=itemgetter(1))
    assert l==[(987,-5),(19,123),(-9,291)]
    mergeSort(l, key=itemgetter(0))
    assert l==[(-9,291),(19,123),(987,-5)]
    mergeSort(l, key=itemgetter(1), reverse=True)
    assert l==[(-9,291),(19,123),(987,-5)]
    
testSortare()