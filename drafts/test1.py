config = []
w1 = ""
w2 = ""
w3 = ""
w4 = ""

print("ввод конфигурации по одному символу")

while True:
    vvod = input("введи символ: ")
    if vvod == "e" or vvod == "е":
        break
    if vvod == "0" or vvod == "1" or vvod == "q1":
        config.append(vvod)
    else:
        print("Введите другое")

print(config)

def enter_rule(t1, t2, t3, t4):
    print("текущий формат: δ(q, a) = (b, D, p)")
    print("допустимые значения: δ(q¹, 0/1) = (0/1, R/L, q¹/q⁰)")
    t1 = input("введите, где стоит xxx: δ(q1, xxx) = (*, *, *): ")
    if t1 == "0" or t1 == "1":
        t2 = input(f"введите, где стоит xxx: δ(q1, {t1}) = (xxx, *, *): ")
        if t2 == "0" or t2 == "1":
            t3 = input(f"введите, где стоит xxx: δ(q1, {t1}) = ({t2}, xxx, *): ")
            t3 = t3.lower()
            if t3 == "r" or t3 == "l":
                t4 = input(f"введите, где стоит xxx: δ(q1, {t1}) = ({t2}, {t3}, xxx): ")
                if t4 == "q1" or t4 == "q0":
                    print(f"δ(q¹, {t1}) = ({t2}, {t3}, {t4})")
                    return t1, t2, t3, t4

def check_config():
    if "q1" not in config:
        print("в конфигурации нет q1")
        return

def check_rule(w1):
    q1_index = config.index("q1")
    if q1_index + 1 >= len(config):
        print("нет символа справа от q1")
        return
    if config[q1_index + 1] != w1:
        print("справа от q1: ", config[q1_index + 1])
        print("значение w1: ", w1)
        print("символ справа не соответствует 'a'")
        return

def apply_rule(cfg):
    q1_index = cfg.index("q1")
    cfg[q1_index+1] = w2
    if w3 == "r":
        cfg[q1_index], cfg[q1_index+1] = cfg[q1_index+1], cfg[q1_index]
        if w4 == "q0":
            pass
    elif w3 == "l":
        cfg[q1_index], cfg[q1_index - 1] = cfg[q1_index - 1], cfg[q1_index]
        if w4 == "q0":
            pass

check_config()
w1, w2, w3, w4 = enter_rule(t1=w1, t2=w2, t3=w3, t4=w4)
check_rule(w1)
apply_rule(config)

print(config)
