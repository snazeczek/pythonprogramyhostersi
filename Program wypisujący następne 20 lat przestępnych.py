print("Tp jest program wypisujący następne 20 lat przestępnych")
r=input("Który mamy rok? :")
print("Oto kolejne 20 lat przestępnych")
for i in range(int(r),int(r)+81):
    if(i%4==0):
        print(i,"r.")