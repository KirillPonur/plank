import numpy as np
from functions import parsing
import matplotlib.pyplot as plt 
name='rec\\n2.tsv'

l,I=parsing(name,0,1)
#из графика для ртутной лампы по 4 точкам соотнесли градусы на шкале с длинами волн

def f(x): #x-- градусы
    p1 =-3.672*10**(-7)
    p2=-9.204*10**(-5)
    p3 =7.457
    f = p1*x**2 + p2*x + p3
    return 6.28*f


c=299792458
freq=f(l)
plt.figure('Задание 5.2')
plt.plot(freq,I,'b')
plt.plot(freq,I,'ro')
plt.ylabel('$I_ф$,мА',fontsize=12) 
plt.xlabel('$\\nu,10^{14}$Гц',fontsize=12)# 
plt.yticks([i for i in range(0,50,4)]) 
plt.grid () 
plt.show()