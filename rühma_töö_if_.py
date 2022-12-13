from math import *
from random import *

print("Isikukoodi kontrollimine")
text=input("Sisesta ikoodi")
print("Palun kirjuta teie isikukod: ")
n=len("Isikukod")
if n==11 and "text". isdigit():
    print("sobib")
else:
    print("Sa kirlutasid palju võii vähe sümboleid")
else:
    




















r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr:
        print(f"Ruudu pindala {Skv} m^2 on suurem ringi pindala Skr")
    elif Skr>Skv:
        print(f"Ringi pindala {Skv} m^2 on suurem ringi pindala Skr")
    else:
        print("Pindalad on võrdsed. {Skr} m^2")
else:
    print(f"{a} ja {r} paevad > kui 0 olla")

print()





