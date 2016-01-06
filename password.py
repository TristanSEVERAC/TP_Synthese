# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  #1 pwd est une variable qui récupère la valeur en entrée de password transformé en List: (abc) devient ['a', 'b', 'c']
    found = False
    i=len(pwd)-1
    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2 incrémente de 1 la valeur ascii du dernier caractère contenu dans pwd
           found = True             
        else:
           pwd[i] = chr(ord(pwd[i])- 25)
           i = i - 1
           if pwd[i] < 'z':
               pwd[i] = chr(ord(pwd[i])+1)
               found = True
    
    return ''.join(pwd) #3 convertie toutes les valeurs de la variable pwd en une seule chaine: a,b,c devient abc

# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
