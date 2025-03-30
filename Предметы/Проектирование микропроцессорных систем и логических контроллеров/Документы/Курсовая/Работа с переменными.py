def f1():
    i = 2

    for j in range(1,19,3):
        for k in range(8):
            print(f"B{i}:= %ID9.{j}.{k}.0; B{i}:= (B{i}-4) * (120/16) - 40;")
            i+=1
    print()
    i = 47
    for j in range(2,19,3):
        for k in range(8):
            print(f"B{i}:= %ID9.{j}.{k}.0; B{i}:= (B{i}-4) * (5000/16);")
            i+=1
    print()
    i = 1

    for j in range(3,19,3):
        for k in range(8):
            print(f"Co{i}:= %ID9.{j}.{k}.0;")
            i+=1
    print()

    
def f2():
    i = 1
    a = 1
    b = 1
    for j in range(19,25,1):
        for k in range(8):
            if b == 9:
                b = 1
                a+=1
            print(f"AT %ID9.{j}.{k}.0 := CF{a}.VAV{b};")
            i+=1
            b+=1
    print()
f1()
