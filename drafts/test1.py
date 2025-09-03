config1 = []

while True:
    vvod = input("введи символ: ")
    if vvod == "e" or vvod == "е":
        break
    if vvod == "0" or vvod == "1" or vvod == "q1":
        config1.append(vvod)
    else:
        print("Введите другое")

while True:
    print("текущий формат: δ(q¹, 0/1) = (0/1, R/L, q¹/q⁰)")
    w1 = input("введите, где стоит xxx: δ(q1, xxx) = (*, *, *): ")
    if w1 == "0" or w1 == "1":
        w2 = input(f"введите, где стоит xxx: δ(q1, {w1}) = (xxx, *, *): ")
        if w2 == "0" or w2 == "1":
            w3 = input(f"введите, где стоит xxx: δ(q1, {w1}) = ({w2}, xxx, *): ")
            if w3 == "R" or "r" or w3 == "L" or "l":
                w4 = input(f"введите, где стоит xxx: δ(q1, {w1}) = ({w2}, {w3}, xxx): ")
                if w4 == "q1" or w4 == "q0":
                    print(f"δ(q¹, {w1}) = ({w2}, {w3}, {w4})")
    break

print(config1)
