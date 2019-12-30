#takahashi, aoki, kaisu = [int(x) for x in input().split()]
takahashi, aoki, kaisu = [2,2,2]
taka_amari = takahashi - kaisu
ao_amari = aoki
if taka_amari<0:
    ao_amari = aoki+taka_amari
 
if taka_amari<0:
    taka_amari = 0
if ao_amari<0:
    ao_amari = 0
print(str(taka_amari) + " " + str(ao_amari))