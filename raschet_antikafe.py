# Расчёт стоимости посещения антикафе «Ход конём»
# Будни: 3 руб/мин, выходные: 4 руб/мин, стоп-чек 900 руб в день

def stoimost(minuty, vyhodnoy):
    cena = 4 if vyhodnoy else 3
    summa = minuty * cena
    if summa > 900:
        summa = 900
    return summa


minuty = int(input("Сколько минут вы были в антикафе? "))
otvet = input("Сегодня выходной? (да/нет) ")
print("К оплате:", stoimost(minuty, otvet.lower() == "да"), "руб.")
