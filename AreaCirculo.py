import math
%matplotlib inline
import matplotlib.pyplot as plt


nu=int(input("Numero de valores: "))
def randux(cnu): #Mixto Univac
    xo=4
    gen1=[]
    for i in range(cnu):
        mod =(515*xo+1)%(2**35)
        div=float(mod)/(2**35)
        xo=mod
        gen1.append(div)
    return gen1

def randuy(cnu): #Multiplicativo con C=1
    xo=51
    gen2=[]
    for i in range(cnu):
        mod =(3*xo+1)%100
        div=float(mod)/100
        xo=mod
        gen2.append(div)
    return gen2

gen1=randux(nu)
gen2=randuy(nu)

c=0
N=nu
plt.ion()
axi=plt.gca()

for i in range(nu):
    gen1[i]=(12)*gen1[i]-6
for j in range(nu):
    gen2[j]=(12)*gen2[j]-6


for i in range(nu):
    if(6**2>=((gen1[i]*gen1[i])+(gen2[i]*gen2[i]))):
        c=c+1
        d=1/(N*100)
        d=d+d
        axi.plot(gen1[i],gen2[i],'b.')
    else:
        axi.plot(gen1[i],gen2[i],'r.')
    if i%120==0:
        plt.draw()

ar=c*d
print "Area Teorica: ", math.pi*25
print "Area Estimada: ", ar
print "Valores dentro: ", c
