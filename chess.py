figure = input('Тип фігури:\n')
x1,y1 = int(input('Позиція фігури на даний момент:\n' )), int(input())

x2,y2 = int(input('Допустимий хід:\n')), int(input())


def Chess(user):
    if user == 'пішка': 
        return abs(y1 - y2) <= 1 and x1 == x2

    if user == 'король': 
        return -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1

    if user == 'тура': 
        return x1 == x2 or y1 == y2  

    if user == 'слон': 
        return  abs(x1 - x2) == abs(y1 - y2) 

    if user == 'кінь': 
        return 1 <= abs(x1 - x2) <= 2  and 1 <= abs(y1 - y2) <= 2

    if user == 'ферзь': 
        return abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2   

    raise ValueError('неправильний хід : {}'.format(user))

print(Chess(figure))
