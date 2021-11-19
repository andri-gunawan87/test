p = []


for i in range(81):
    if i == 0:
        pass
    elif i%15==0:
        p.append("Frontend Backend")
    elif i%5==0:
        p.append("Backend")
    elif i%3==0:
        p.append("Frontend")       
    else:
        p.append(i)

t = ','.join(map(str, p))
print(t)