edad = input(int("Ingrese su edad: "))
nombre = input(("Ingrese su nombre: "))
genre = input(("Ingrese su género: "))

edad_jubilatoria_men = 65
edad_jubilatoria_woman = 60

if edad >= edad_jubilatoria_men and edad <= edad_jubilatoria_woman:
    print(f"{nombre} es un jubilado")
else:
    print(f"{nombre} no es un jubilado")



