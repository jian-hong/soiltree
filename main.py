
meanpH= 7.26
meanO = 0.848

print("Soil sample")
Name = input()
print("pH of soil")
pH = float(input())
print("Salinity of soil")
Salinity = input()
print("Organic Matter of soil")
Organic= float(input())


if pH > meanpH*1.03:
    NpH = "High"
elif pH < meanpH*0.97:
    NpH = "Low"
else:
    NpH = "Moderate"

if Organic > meanO * 1.03:
    NOrganic = "High"
elif Organic < meanO * 0.97:
    NOrganic = "Low"
else:
    NOrganic = "Moderate"

Tree = ["Albizia lebbeck","Anogeissus latifolia","Eucalyptus tereticornis","Dalbergia sissoo","Grevillea robusta"]
TreepH = ["High","Low","Moderate","High","Low"]
TreeS = ["Low","Moderate","High","Low","High"]
TreeO = ["Low","Low","Moderate","High","High"]

print(NpH,Salinity,NOrganic)

if NpH==TreepH[0] and Salinity==TreeS[0] and NOrganic==TreeO[0]:
    print("You can plant " +Tree[0]+" on Soil "+Name)
elif NpH==TreepH[1] and Salinity==TreeS[1] and NOrganic==TreeO[1]:
    print("You can plant " +Tree[1]+" on Soil "+Name)
elif NpH==TreepH[2] and Salinity==TreeS[2] and NOrganic==TreeO[2]:
    print("You can plant " +Tree[2]+" on Soil "+Name)
elif NpH==TreepH[3] and Salinity==TreeS[3] and NOrganic==TreeO[3]:
    print("You can plant " +Tree[3]+" on Soil "+Name)
elif NpH==TreepH[4] and Salinity==TreeS[4] and NOrganic==TreeO[4]:
    print("You can plant " +Tree[4]+" on Soil "+Name)
else:
    print("You can plant other Timbers.")


