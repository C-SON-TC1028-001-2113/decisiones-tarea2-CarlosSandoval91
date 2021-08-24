def main():
    #escribe tu código abajo de esta línea
    L1=int(input('Ingresa la medida del lado 1: '))
    L2=int(input('Ingresa la medida del lado 2: '))
    L3=int(input('Ingresa la medida del lado 3: '))
    if L1>0 and L2>0 and L3>0:
        if L1+L2>L3 and L1+L3>L2 and L2+L3>L1 :
            if L1==L2 and L1==L3:
                print('ES UN TRIANGULO EQUILATERO')
            elif  L1==L2 or L1==L3 or L2==L3: 
                print('ES UN TRIANGULO ISOSCELES')  
            else: 
                print('ES UN TRIANGULO ESCALENO')      
        else:
            print('NO ES TRIANGULO')     
    else:
        print('NO ES TRIANGULO')    



if __name__=='__main__':
    main()
