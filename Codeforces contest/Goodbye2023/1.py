t = int(input())
while t:
    n, k= map(int, input().split())
    l1 = list(map(int, input().split()[:n]))
    l2 = []
    multi = 1
    for i in l1:
        multi *= i
    if 2023 % multi != 0:
        print("NO")
    else:
        if multi == 2023:
            print("YES")
            print(1)
        elif multi != 2023 and k == 1:
            print("YES")
            print(2023//multi)
        elif multi != 2023:
            print("YES")
            if multi == 1:
                if k == 1:
                    print(2023)
                elif k == 2:
                    print(7, 289)
                elif k == 3:
                    print(7, 17, 17)
                elif k >= 4:
                    nums = [7,17,17]
                    k1 = [1]*(k-3)
                    nu = nums + k1 
                    print(*nu)
            elif multi == 7:
                if k == 1:
                    print(289)
                elif k == 2:
                    print(17,17)
                elif k >= 3:
                    nums = [7,17]
                    k1 = [1]*(k-2)
                    nu = nums + k1
                    print(*nu)
            elif multi == 17:
                if k == 1:
                    print(119)
                elif k >= 2:
                    nums = [119]
                    k1 = [1]*(k-1)
                    nu = nums + k1
                    print(*nu)
            elif multi == 119:
                if k == 1:
                    print(17)
                elif k >= 2:
                    nums = [17]
                    k1 = [1]*(k-1)
                    nu = nums + k1
                    print(*nu)
            elif multi == 289:
                if k == 1:
                    print(7)
                elif k >=2:
                    nums = [7]
                    k1 = [1]*(k-1)
                    nu = nums + k1
                    print(*nu)
    t -= 1