print("Введите коэффициенты для квадратного уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2-4*a*c

if D > 0:
    x1 = (-b + D**0.5)/(2 * a)
    x2 = (-b - D**0.5)/(2 * a)
    print("x1 = {x1} \nx2 = {x2}".format(x1=x1,x2=x2))
elif D == 0:
    x = (-b + D**0.5)/(2*a)
    print("Корень один \nx = {x}".format(x=x))
else:
    print("Корней нет")