# Milorad Karalic 5247
# DZ #01

def multiply_a_b_(a,b):
    return a * b

def area_a_b(a,b):
    if a <= 0 or b <= 0:
        return('Stranice moraju biti brojevi veci od nule')
    return multiply_a_b_(a,b)

print(area_a_b(2,8))
print(area_a_b(-5, 7))