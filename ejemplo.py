#Ejemplo de union
A = {1, 2, 3, 4}
B= {3,4,5,6}
C={'manzana', 'banana', 'pera', 'uva'}
D={'banana','kiwi','uva','mango'}
E = {3,5,6,7,8,9}
union= A.union (B)
union1= C.union (D)
union2= A.union(C)
union3= A.union (D)
union4= A|B
union5= C|B
union6= A.union(B,C)
union7= A|B|C
print("La union del conjunto A y B es", union)
print("La union del conjunto C y D es", union1)
print("La union del conjunto A y C es", union2)
print("La union del conjunto A y D es", union3)
print("La union del conjunto A y B es", union4)
print("La union del conjunto C y B es", union5)
print("La union del conjunto A, B y C es", union6)
print("La union del conjunto A, B y C es", union7)
#Ejemplo de interseccion
cruce= A.intersection(B)
cruce1= B.intersection (A)
cruce2= A&B
cruce3= A&B&C
cruce4= A.intersection(B,E)
print("La interseccion del conjunto A y B es", cruce)
print("La interseccion del conjunto A y D es", cruce1)
print("La interseccion del conjunto A y B es", cruce2)
print("La interseccion del conjunto A, B y C es", cruce3)
print("La interseccion del conjunto A, B y E es", cruce4)

x={'rojo', 'azul', 'amarillo', 'verde', 'negro', 'blanco'}
y={'sol', 'luna','estrella'}

cruce5=x&y
print("La interseccion de z,y es", cruce5)

union8=x|y
print("la union de x y y es", union8)