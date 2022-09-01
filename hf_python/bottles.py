word = "бутылок"
for bear_num in range(99, 0, -1):
    print(bear_num, word, "пива на стене.")
    print(bear_num, word, "пива.")
    print("Возьми одну.")
    print("Пусти по кругу.")
    if bear_num == 1:
        print("Нет бутылок пива на стене!")
        print("Нет бутылок пива!")
        print("Пойди в магазин и купи еще...")
    else:
        new_num = bear_num - 1
        if 11 <= new_num <= 19:
            word = "бутылок"
        else:
            if new_num % 10 == 1:
                word = "бутылка"
            elif new_num % 10 in (2, 3, 4):
                word = "бутылки"
            else:
                word = "бутылок"
            print(new_num, word, "пива на стене.")
        print()
