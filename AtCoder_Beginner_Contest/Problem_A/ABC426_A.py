x, y = input().split()
ver =  ["Ocelot", "Serval", "Lynx"]
if ver.index(x) < ver.index(y):
    print("No")
else:
    print("Yes")