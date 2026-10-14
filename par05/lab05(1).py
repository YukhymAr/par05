#1
def fsize(width, height):
    vid = width * height
    print(vid)
    return vid

def triple(width, height):
    vid = width * height / 2
    print(vid)
    return vid

def sircle(width, height):
    vid = 2 * 3.14 * (width + height) / 4
    print(vid)
    return vid



print("Виберіть Трикутник , Квадрат чи Коло")
Sv = input("Яку фігуру треба обчислити: ")
width = float(input("Width: "))
height = float(input("Height: "))

if Sv == "трикутник":
    triple(width, height)
elif Sv == "квадрат":
    fsize(width, height)
elif Sv == "коло":
    sircle(width, height)
else:
    print("Невідома фігура!!!")



#2
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def divisors(n):
    result = []
    for i in range(1 , n + 1):
        if n % i == 0:
            result.append(i)
    return result

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def main():
    n = int(input("Введіть натуральне число N: "))

    if is_prime(n):
        print("Просте число: так")
    else:
        print("Просте число: ні")

    print("Дільники:", divisors(n))
    print("Сума цифр:", digit_sum(n))
main()


#3
def average(gs):
    cnt = 0
    tot = 0
    for g in gs:
        tot += g / n
        cnt += 1
    if cnt == 0:
        return 0

    return tot
    return cnt

def minimum(gs):
    if not gs:
        return None

    min_val = gs[0]
    for g in gs:
        if g < min_val:
            min_val = g
    return min_val

def maximum(gs):
    max_val = gs[0]
    if not gs:
        return None

    for g in gs:
        if g > max_val:
            max_val = g
    return max_val

def count_above(gs, val):
    cnt = 0
    for g in gs:
        if g > val:
            cnt += 1
    return cnt
n = int(input("Скільки у вас оцінок? "))

gs = []
for i in range(n):
    g = int(input(f"Введіть оцінку №{i + 1}: "))
    gs.append(g)

porig = int(input("Введіть поріг: "))

# Виведення результату
print("Середній бал:", average(gs))
print("Мінімальна:", minimum(gs))
print("Максимальна:", maximum(gs))
print(f"Вище {porig}:", count_above(gs, porig))

