x0=input("Ingrese la semilla: ");
n=input("Cantidad de numeros a generar ");
print " "
tam=len(str(x0));
band=1;
x0=x0**2;

while band<n+1:
    x0=str(x0);
    #print x0;
    if len(x0)%2==0 and len(x0)==(2*tam):
        num=x0[((2*tam)/4):((6*tam)/4)];
        print "Numero: "+num;
        band=band+1;
        num=int(num);
        x0=num**2;
        
    else:
        cero="";
        for i in range((2*tam)-len(str(x0))):
            cero=cero+"0";
        x0=str(x0);
        x0=cero+x0;