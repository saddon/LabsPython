# TODO Найдите количество книг, которое можно разместить на дискете

S = 1.44*1024*1024
res = int(S // (4*25*50*100))

print("Количество книг, помещающихся на дискету:", res)
