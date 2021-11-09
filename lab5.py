hours=int(input(   'години: '))
minuts=int(input("хвилини: "))

b=(hours*60,minuts*60)
if hours<=24:
    print(b,"хвилин","секунд")
elif hours>=25:
    print("erorr")