from math import *
def bisection():
    def f(x):
        return 2*cos(x)-x
    
    a=float(input('Κάτω όριο του διαστήματος '))
    b=float(input('Πάνω όριο του διαστήματος '))
    ex=float(input('Μέγιστο επιτρεπτό σφάλμα στη θέση της ρίζας '))
    ef=float(input('Μέγιστη επιτρεπτή απόλυτη τιμή της συνάρτησης στο σημείο που επιστρέφεται ως εκτίμηση της ρίζας '))
    m=(a+b)/2
    n=1
    
    
    print('n\ta\tb\tm\tf(a)\tf(b)\tf(m)')
    s=str(n)+'\t'+str(round(a,4))+'\t'+str(round(b,4))+'\t'+str(round(m,4))+'\t'+str(round(f(a),4))+'\t'+str(round(f(b),4))+'\t'+str(round(f(m),4))
    print(s)
    while (b-a)/2>ex and abs(f(m))>ef:
        n+=1
        if f(m)*f(a)<0:
            b=m
        elif f(m)*f(b)<0:
            a=m
        m=(a+b)/2
        s=str(n)+'\t'+str(round(a,4))+'\t'+str(round(b,4))+'\t'+str(round(m,4))+'\t'+str(round(f(a),4))+'\t'+str(round(f(b),4))+'\t'+str(round(f(m),4))
        print(s)
    print('Εκτίμηση για την ρίζα:',m)
    

