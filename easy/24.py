n = input()
   
a_values = []
b_values = []
ver_oshibki_na_servere_i = []
obshaja_veroyatnost_oshibki = 0
p_i = []

for i in range(int(n)):
   a, b = map(int, input().split())
   a_values.append([a, b])  
   ver_oshibki_na_servere_i.append((a / 100) *  (b / 100))
   obshaja_veroyatnost_oshibki = obshaja_veroyatnost_oshibki + ver_oshibki_na_servere_i[i]
   
for i in range(int(n)):
   print((ver_oshibki_na_servere_i[i] / obshaja_veroyatnost_oshibki))