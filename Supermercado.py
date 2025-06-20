 #declarar variables y pedir datos si compra tres productos tiene descuento de 35%
 
print("ingrese los precios de los 3 productos")
producto1 =float (input("precio del primer producto")) #la variuable: tipo de dato (imput( "texto a pedir"))
producto2 =float (input("precio del segundo  producto"))
producto3 =float (input("precio del tercer producto"))


#formula 
total= producto1 + producto2 +producto3

descuento= total*0.35
totalpagar=total-descuento

#tambien se puede 
total*=0.65 #para que se genere de una vez el descuento

'''
En matematicas del 100 % de algo y se descuenta un porcentaje significa que se esta pagando
el restante, por ejemplo si se descuenta el 35% significa que se paga el 65% del precio original
en decimales el porcentaje se expresa en 0,65

asi que el total se multiplica por el valor que se esta pagando

''' 

print(f"el total a pagar es {total}")