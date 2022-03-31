##fonksiyonlar

##fonksiyonu oluşturmadan önce çağıramazsın
#def metot():
#    print("selam dünya")
#    ##argüman almıyor ve grtiye değer döndürmüyor
#metot()


###geriye değer döndüren metot
#def kareHesaplama():
#    sonuc=3*3
#    return sonuc

#print(kareHesaplama())

###default değer olarak y değerine 2 verildi 
##değer girilmez ise y değişkeni 2 olarak sayılır
#def usAl(x,y=2):
#    kare=x**y
#    return kare

#print(usAl(5))
#print(usAl(5,3))


## * args kwargs
#def carpim(*args):
#    sonuc=1
#    for i in args:
#        sonuc*=i
#    return sonuc

#print(carpim(5))
#print(carpim(5,5))
#print(carpim(5,6,5,3))
#print(carpim(5,2,3,4,5))
#print(carpim(5,8,6,54,5))
#print(carpim(5,9,6,3,2,5,1,4,7,8))

#def birlestir(*beykent):
#    sonuc=""
#    for i in beykent:
#        sonuc+=" "+i
#    return sonuc


#print(birlestir("beykent"))
#print(birlestir("beykent","üniversitesi"))
#print(birlestir("beykent","üniversitesi","hadımköy"))


#def hesapla(x,y):
#    sonuc1=x*y
#    sonuc2=x/y
#    sonuc3=x-y
#    sonuc4="beykent"
#    sonuc5=True
#    return sonuc1,sonuc2,sonuc3,sonuc4,sonuc5

#s1,s2,s3,s4,s5= hesapla(5,5)

#print(s1)
#print(s2)
#print(s3)
#print(s4)
#print(s5)

##lambda
#kare=lambda x:x**2
#carpim = lambda x,y=9:x*y

#print(kare(5))
#print(kare(11))
#print(carpim(10,20))
#print(carpim(150))


##özyinelemeli: recursive method/function
##base recurse
##iteration recurse

#def faktoriyel(x):
#    if(x==1):
#        #base
#        return 1
#    else:
#        return x*faktoriyel(x-1)
###bir metot bir bellekte tutulur

#print(faktoriyel(3))


##buble sort

#def bubleSort(liste):
#    boyut = len(liste)
#    for i in range(0,boyut-1):
#        for j in range(0,boyut-1-i):
#            if(liste(j>liste[j+1])):
#                temp=liste[j]
#                liste[j]=liste[j+1]
#                liste[j+1]=temp
#    return liste

#liste=[12,15,9,6,60,14,17,30,26,1]
#k=set(liste)
###düzensiz listeyi 
###sıralanıp ekrana yansıtılacak

#print(bubleSort(k))



#def tekSayi():
#    for i in range(0,100):
#     if(i%2==1):
#        print(i)

#def ciftSayi():
#    for i in range(0,100):
#     if(i%2==0):
#       print( i)

#def sayilar():
#    for i in range(1,1000):
#        print( i)


#print(tekSayi())
#print(ciftSayi())
#print(sayilar())
