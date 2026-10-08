"""Seira Askhsewn 2."""


def sum_sequence(n, term):
    """A8roisma arxikwn orwn akolou8ias

    n -- deikths teleutaiou orou (deikths prwtou = 1)
    term -- synarthsh: term(i) einai o i-ostos oros

    Epistrefei tin timi term(1) + term(2) + ... + term(n).
    """
    i, sum = 2, term(1)
    while i <= n:
        sum += term(i)
        i += 1
    return sum


#>>>>>>>>>>>>>>>>>>>>> Askhsh 1 <<<<<<<<<<<<<<<

def digit_sum(x):
    """Ypologizei to a8roisma twn (dekadikwn) pshfiwn tou x

    x -- 8etikos akeraios

    >>> digit_sum(10000)
    1
    >>> digit_sum(615)
    12
    >>> digit_sum(23) == 5
    True
    """
    s = 0
    while x!=0:
        s = s+x%10
        x //= 10

    return s



#>>>>>>>>>>>>>>>>>>>>> Askhsh 2 <<<<<<<<<<<<<<<

def count_digit(x, i):
    """Ypologizei to plh8os twn emfanisewn enos pshfiou

    x -- 8etikos akeraios
    i -- pshfio (1 = 1o pshfio apo dexia, 2 = 2o apo dexia, ktl.)

    >>> count_digit(1000, 1)
    3
    >>> count_digit(12944342, 2)
    3
    >>> count_digit(121,1) == 2
    True
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW """
    temp=x // 10**(i-1)
    digit=temp % 10
    n = 0
    while x!=0:
        if x % 10 == digit:
            n += 1
        x = x//10
    return n


#>>>>>>>>>>>>>>>>>>>>> Askhsh 3 <<<<<<<<<<<<<<<

def paei_pi(n):
    """A8roisma n orwn tis akoloy8ias 
              4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, ... ktl.

    n -- 8etikos akeraios >= 1

    Epistrefei to a8roisma twn orwn 1 ews kai n.

    Paradeigmata:
    >>> paei_pi(1)
    4.0
    >>> paei_pi(2)
    2.666666666666667
    >>> paei_pi(3)
    3.466666666666667
    >>> paei_pi(1000)
    3.140592653839794
    >>> paei_pi(10000)
    3.1414926535900345
    """
    def term(n):
        return 4/ ((2*n-1) * (-1)**(n+1))

    return sum_sequence(n, term)



#>>>>>>>>>>>>>>>>>>>>> Askhsh 4 <<<<<<<<<<<<<<<

def stars_horizontal(n):
    """String asteriwn topo8etimena orizontiws.

    n -- akeraios >= 1
    
    Epistrefei string me n xaraktires '*'.

    Paradeigmata:
    >>> stars_horizontal(1)
    '*'
    >>> stars_horizontal(5)
    '*****'
    >>> print(stars_horizontal(5))
    *****
    """
    def star(i):
        return '*'
    return sum_sequence(n , star)



#>>>>>>>>>>>>>>>>>>>>> Askhsh 5 <<<<<<<<<<<<<<<

def reverse_args(f):
    """ Antistrefei ta orismata.

    -- f synartisi 2 orismatwn

    Epistrefei synartisi g opou i klisi g(x, y) exei idia timi me tin f(y, x).

    Paradeigmata:
    >>> pow(2, 3)
    8
    >>> pow(3, 2)
    9
    >>> wop = reverse_args(pow)
    >>> wop(2, 3)
    9
    >>> wop(3, 2)
    8
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW """
    def g(x,y):
        return f(y,x)
    return g


#>>>>>>>>>>>>>>>>>>>>> Askhsh 6 <<<<<<<<<<<<<<<

def askisi6():
    """Ypologismoi gewmetrikwn sximatwn.

    >>> askisi6()
    Perifereies kyklwn me aktina 1 ews 10
    6.283185307179586
    12.566370614359172
    18.84955592153876
    25.132741228718345
    31.41592653589793
    37.69911184307752
    43.982297150257104
    50.26548245743669
    56.548667764616276
    62.83185307179586
    Emvada tetragwnwn me pleura 1 ews 8
    1
    4
    9
    16
    25
    36
    49
    64
    Emvado kyklou aktinas 1 = 3.141592653589793
    Emvado kyklou aktinas 2 = 12.566370614359172
    Emvado kyklou aktinas 3 = 28.274333882308138
    Emvado kyklou aktinas 4 = 50.26548245743669
    Emvado kyklou aktinas 5 = 78.53981633974483
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW, APOFEYGONTAS
    TIN EPANALIPSI PAROMOIWN ENTOLWN """
    from math import pi
    """def perifereia_kyklou(r):
        return 2*pi*r
        
    def emvado_tetragonou(a):
        return a**2
        
    def emvado_kyklou(r):
        s='Emvado kyklou aktinas ' + str(r) + ' = ' + str(pi*r**2)
        return s
        
    def ektypose(apo, eos, synartisi):
        while apo<=eos:
            print(synartisi(apo))
            apo+=1
    
    print('Perifereies kyklwn me aktina 1 ews 10')
    ektypose(1,10,perifereia_kyklou);
    
    print('Emvada tetragwnwn me pleura 1 ews 8')
    ektypose(1,8,emvado_tetragonou)
    
    ektypose(1,5,emvado_kyklou)"""

    print('Perifereies kyklwn me aktina 1 ews 10')
    for i in range(1,26):
        if i<11:
            print(2*pi*i)
        elif i==11:
            print('Emvada tetragwnwn me pleura 1 ews 8')
        elif i<20:
            print ((i-11)**2)
        else:
            k=abs(20-i)
            if k!=0:
                print('Emvado kyklou aktinas',k,'=',pi*k**2)
    
        
#>>>>>>>>>>>>>>>>>>>>> Askhsh 7 <<<<<<<<<<<<<<<

def make_quadratic(a, b, c):
    """Polywnymo 2ou ba8mou.

    a, b, c -- ari8moi

    Epistrefei thn tetragwnikh synarthsh f(x) = a*x*x+b*x+c.

    Paradeigmata:
    >>> f = make_quadratic(1, 2, 1.0)
    >>> f(0)
    1.0
    >>> f(-1)
    0.0
    >>> f(1)
    4.0
    >>> f(1.5)
    6.25
    """
    return lambda x: a*x*x+b*x+c



#>>>>>>>>>>>>>>>>>>>>> Askhsh 8 <<<<<<<<<<<<<<<

def abacize(op):
    """Ekdoxh abaka (ari8mhthri) enos telesti.

    op -- synartisi dyo akeraiwn orismatwn
          pou epistrefei akeraia timi

    Epistrefetai nea synartisi pou dexetai ta
    ari8mitika orismata tis op kai epistrefei ta apotelesma tis
    xrhsimopoiwntas anaparastasi me xandres ari8mitiriou.

    Paradeigmata:
    >>> from operator import *
    >>> baby_add = abacize(add)
    >>> baby_add('o', 'o')
    'oo'
    >>> baby_add('oo', 'ooo')
    'ooooo'
    >>> baby_mul = abacize(mul)
    >>> baby_mul('oo', 'ooo')
    'oooooo'
    >>> abacize(max)('oo', 'ooo')
    'ooo'
    >>> abacize(pow)('oo', 'ooo')
    'oooooooo'
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW """
    def result(x, y):
        z=op(len(x),len(y))
        ap=z * 'o'
        return ap
    return result
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
     
    
    
