tecst = 'ввп ты Ужасен ,займись лучше ввп , а не этим '
my_li = tecst.split()

for i in my_li:
    if i == "ввп":
        my_li.remove(i)
print(my_li)
