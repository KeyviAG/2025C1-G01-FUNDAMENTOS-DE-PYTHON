
import csv, os
import pandas as pd
def ingresar_ventas(lista_ventas):
    while True:
        try: 
            curso = input ('Íngrese el nombre del curso: ').upper()
            cantidad = int (input('Ingrese la cantidad de curso vendidos: '))
            fecha = input('Íngrese la fecha de la venta (AAAA-MM-DD): ')
            precio = float(input('Íngrese el precio del curso: '))
            cliente = input('Íngrese el nombre del cliente: ').upper()
        except ValueError:
            print('Entradas no validas, por favor intetenlo nuevamente!')
            continue
        
        venta = {
            'curso' : curso,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
            'cliente' : cliente
        }
        lista_ventas.append(venta)
        
        
        continuar = input('Desea ingresar otra venta s/n :').lower()
        if continuar == 's':
            print('\n---- Ingresando otra venta ----')
        elif continuar == 'n':
            break
        else: 
            print ('Opción no valida')



def guardar_ventas(ventas):
    if not ventas:
        print('No hay ventas que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #si el archivo existe agrego Append  'A'
            with open('ventas.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writerows(ventas)        
        else: #Si no existe abro en modo escritura 'W'
            with open('ventas.csv','w',newline='2',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso                
        ventas = []
        print('Datos guardados exitosamente!')
        
        
def analisis_ventas():
    df = pd.read_csv('ventas.csv')
    print('\n---- RESUMEN VENTAS---')
    df['subtotal'] = df['cantidad'] * df['precio']
    total_ingresos = df['subtotal'].sum()

    print (f'TOTAL de ventas {total_ingresos:.2f}')
    
    
    curso_1= df.grouphy('curso')['cantidad'].sum().idxmax()
    print(f'Curso mas vendido: ', curso_1)
    
    cliente_1 = df.grouphy('cliente')['cantidad'].sum().idxmax()
    print(f'Curso mas vendido: ', cliente_1)
    
    fechas_1 = df.grouphy('fechas')['cantidad'].sum().idxmax()
    print(f'Curso mas vendido: ', fechas_1 )