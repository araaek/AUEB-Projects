from math import *
def newton(func, funcderiv, x, m, ef):
    """
    func:       είναι η συνάρτηση της οποίας θέλουμε να υπολογίσουμε την ρίζα
    funcderiv:  είναι η παράγωγος της συνάρτησης
    x0:         είναι το αρχικό σημείο όπου υπολογίζεται η τιμή της συνάρτησης και της παραγώγου της
    m:          είναι το μέγιστο πλήθος επαναλήψεων
    ef:         είναι η ανοχή στην τιμή της συνάρτησης

    ΠΑΡΑΔΕΙΓΜΑ για τον υπολογισμό ρίζας της συνάρτησης x-cos(x) με αρχικό σημείο το 0, 
    με μέγιστο πλήθος επαναλήψεων 10 και ανοχή στην τιμή της συνάρτησης 0.000000000001
    
    newton('x-cos(x)','1+sin(x)',0,10,1e-12)
    """    

    def f(x):
        f=eval(func)
        return f

    def df(x):
        df=eval(funcderiv)
        return df
    
    n=0  
    print('n\txn\t\tf(xn)\t\tdf(xn)')

    while n<m and abs(f(x))>ef and abs(df(x))>0:
        s=str(n)+'\t'+"{:.8f}".format(x)+'\t'+"{:.8f}".format(f(x))+'\t'+"{:.8f}".format(df(x))
        print(s)
        x=x-f(x)/df(x)
        n+=1

        
    print('Εκτίμηση για την ρίζα:',x)
    

