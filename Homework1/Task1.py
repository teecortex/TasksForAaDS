def isPrime(n):
    k = 0
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            k += 1
    if k == 0:
        return True

def naive(s):
    u = 1
    while u < len(s):
        mass[int(s[u - 1: u + 1]) - 10] += 1
        u += 1

def rabin_carp(s):
    def Hash(s):
        alphabet = 10
        return int(s[0]) * alphabet + int(s[1])
    for i in range(10, 100):
        h = Hash(str(i))
        j = 2
        while j < len(s):
            if (Hash(s[j-1:j+1]) == h) and (s[j-1:j+1] == str(i)):
                mass[int(s[j-1:j+1]) - 10] += 1
            j += 1

def Hash(s):
    alphabet = 10
    return int(s[0]) * alphabet + int(s[1])

def boyer_murr(s):
    for i in range(10, 100):
        image = str(i)
        symbol_nums = {}
        set_of_symbols = set()
        m = len(image)
        for i in range(m - 2, -1, -1):
            if image[i] not in set_of_symbols:
                set_of_symbols.add(image[i])
                symbol_nums[image[i]] = m - i - 1

        if image[m - 1] not in set_of_symbols:
            symbol_nums[image[m - 1]] = m
            set_of_symbols.add(image[m - 1])

        i = m - 1
        while i < len(s):
            k = 0
            for j in range(m - 1, -1, -1):
                if s[i - k] != image[j]:
                    if j == m - 1:
                        off = symbol_nums[s[i]] if symbol_nums.get(s[i], False) else m
                    else:
                        off = symbol_nums[image[j]]
                    i += off
                    break
                k += 1
            if (j == 0) and (k == m):
                mass[int(image) - 10] += 1
                i += 1


def KMP(s):
    for i in range(10, 100):
        image = str(i)
        if s[0] == s[1]:
            image_arr = [0, 1]
        else:
            image_arr = [0, 0]
        j = 0
        while j < len(s) - 1:
            for k in range(len(image)):
                if (s[j + k] != image[k]):
                    j += ((image_arr[k - 1] + 1) if k == 1 else 1)
                    break
            else:
                mass[int(image) - 10] += 1
                j += 1


s = ""
k = 0
n = 2
while k < 500:
    if (isPrime(n)):
        s += str(n)
        k += 1
    n += 1

mass = [0 for i in range(10, 100)]
naive(s)
print(max(mass))
mass = [0 for i in range(10, 100)]
rabin_carp(s)
print(max(mass))
mass = [0 for i in range(10, 100)]
boyer_murr(s)
print(max(mass))
mass = [0 for i in range(10, 100)]
KMP(s)
print(max(mass))




