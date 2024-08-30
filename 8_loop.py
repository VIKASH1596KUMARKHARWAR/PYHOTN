l = [1, 2, 3, 4, 5, 5, "sudha", "kumar", "coourse"]
# place str and int in diff list
l_num = []
l_str = []

for i in l:
    if type(i) == int or type(i) == float:
        l_num.append(i)
    else:
        l_str.append(i)

print(l_num)
print(l_str)
