# По какой-то причине не работет. Думаю нужно сначало пройти class. Ещё Абдумлмалик сказал, что array и list - разные по принципу сохранения

def addTwoNumbers(l1: list, l2: list) -> list[int]:
    l1 = l1[::-1]
    for i in range(len(l1)):
        l1[i] = str(l1[i])
    l2 = l2[::-1]
    for i in range(len(l2)):
        l2[i] = str(l2[i])
    num_1 = int("".join(l1))
    num_2 = int("".join(l2))
    sum = num_1 + num_2
    lst = list(str(sum))
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst[::-1]

print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))