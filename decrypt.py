f4g ={}    # dic des fréquences des 4-grammes
f = open('brut4g_fr.txt')
total = 0  # effectif total
for line in f:
    (w, c) = line.split(sep= ' ')
    f4g[w] = int(c)
    total += int(c)
    print (total)
for w in f4g:
    f4g[w] /= total  # calcul des fréquences
    #print (f4g)
f.close
print (f4g['ELLE'])