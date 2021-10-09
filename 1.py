def newfunc():
    while True:
        try:
            x=float(input("Ваше число:"))
        except:
            False
        else:
            break
    return x
print("Введите вещественное число A:")
a=newfunc()
print("Введите вещественное число B:")
b=newfunc()
print("Введите вещественное число C:")
c=newfunc()
if (a<b) and (b<c):
    print("Да, A<B<C")
elif (a>b) and (b>c):
    print("Да, A>B>C")
else:
    print("Нет, ни одно из условий (A<B<C или A>B>C)не выполняется")

	
