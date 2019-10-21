map_ = []
params = input("Введите параметры (ширина, высота, кол-во бомб): ").split()
weight = int(params[0])
height = int(params[1])
count_bombs = int(params[2])
if weight * height < count_bombs:
    mistake = True
    while mistake:
        count_bombs = int(input("Количество бомб больше, чем размер поля, введите другое: "))
        if weight * height >= count_bombs:
            mistake = False
for i in range(0, height):
    map_.append({})
    for j in range(0, weight):
        map_[i][j] = 0
for n in range(1, count_bombs + 1):
    location = input("Введите координаты бомбы номер " + str(n) + ": ").split()
    x = int(location[0]) - 1
    y = int(location[1]) - 1
    if x >= 0 and x < weight and y >= 0 and y < height and map_[x][y] != "💣":
        map_[x][y] = "💣"
    else:
        mistake = True
        while mistake:
            if x < 0 or x >= weight or y < 0 or y >= height:
                location = input("Этой точки нет на карте, выберите другую: ").split()
            else:
                location = input("На этой точке уже есть бомба, выберите другую: ").split()
            x = int(location[0]) - 1
            y = int(location[1]) - 1
            if x >=0 and x < weight and y>=0 and y < height and map_[x][y] != "💣":
                map_[x][y] = "💣"
                mistake = False
    for i in range(x - 1, x + 2):
        if i in range(0, height):
            for j in range(y - 1, y + 2):
                if j in range(0, weight) and map_[i][j] != "💣":
                    map_[i][j] += 1
for i in range(0, height):
    str_ = ""
    for j in range(0, weight):
        str_ += str(map_[i][j]) + " "
    print(str_)