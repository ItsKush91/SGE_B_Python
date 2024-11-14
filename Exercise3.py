print("Enter your mark:")
mark = float(input())

if mark<5:
    print("Suspès")
elif mark>=5 and mark<=6.5:
    print("Aprovat")
elif mark>=6.6 and mark<=8:
    print("Notable")
elif mark>8 and mark<=10:
    print("Excel·lent")
else:
    print("Invalid mark")