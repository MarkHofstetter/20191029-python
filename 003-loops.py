j = 0
while j < 10:
    j += 2
    print("w: ", j)
else:
    print("while else:", j)

# es gibt keine schleifenlabel dh ein break verlaesst
# IMMER die innerste Schleife
while True:
    j -= 1
    print(j)
    if j <= 0:
        break

# print(list(range(5))
for i in range(5):
    if i == 3:
        continue
    print(i, end = '*')
else:
    print('else:', i)

    
        