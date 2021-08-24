def main():
    #escribe tu código abajo de esta línea
    e= int(input('Ingresa tu edad: '))
    a= e >=18
    b = e>0

    if a and b :
        id= str(input('¿Tienes identificación oficial? (s/n): '))
        if id== 's':
            print ('Trámite de licencia concedido')

        elif id == 'n':
            print('No cumples requisitos')

        else:
            print('Respuesta incorrecta')      
    if not a and b:
        print('No cumples requisitos')
    if not b:
        print('Respuesta incorrecta')    

if __name__=='__main__':
    main()

