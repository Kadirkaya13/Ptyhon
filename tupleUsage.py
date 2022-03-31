
## tuple : demet
#tuple=(1,2,34,4,5)
#tuple2=("beykent",1.2,True,6)
#print(tuple)
#print(type(tuple2))
#print(tuple[-1])
##tuple yapıları listeden farklı olarak içerisine girilen veri bir daha değiştirilemez


##tuple değerleri sırayla değişkenlere atanbilir fakat değişken sayısı ile
##demek içeriside bulunan eaman sayısı eşit olmak zorundadır aski taktirde hata verir
#demet=(3.14,1997,2022)
#pi,beykent,yil=demet
#print(pi)
#print(beykent)
#print(yil)


#liste1=[10,20,30,40,50]
#liste2=[100,200,300,400,500]

#print(liste1)
#print(liste2)

###zip
#demet = zip(liste1,liste2)
#print(type(demet))
#print(demet)

###zip çözme: pointer *
#demet2,demet3=zip(*demet)
#print(demet2)
#print(demet3)
#print(type(demet2))

##tuple'dan listeye çevirmek
#d1=(1,2,3,4,5)
#d2=(10,20,30,40,50)
#liste=list(d1)
#liste2=list(d2)

#print(type(liste))
#print(liste)


#Küme yapıları
#set
##küme yapılarında aynı elemandan en fazla 1 tane bulunabilir 
##küme yapılarında sırann bir önemi yoktur
#liste=["java","c#","python","javascript","c++","flutter","java"]
#kume=set(liste)
#print(type(kume))
#print(kume)

##pop fonksiyonu kümenin luşturduğu sırada bulunan ilk elemanı siler
#kume.pop()
#print(kume)

##eleman silme
#kume.discard("java")
#print(kume)

##güncelleme
#liste2=["sql","access","azure"]
#kume.update(liste2)
#print(kume)
##set'e sonradan eleman eklemek
#kume.add("html")
#print(kume)
#kume.add("c++")
#print(kume)

##kümelerde fonksiyonlar
#l1=set(["elma","armut","ayva","nar"])
#l2=set(["elma","çilek","elma","nar"])

##birleşim kümesi
#l3=l1.union(l2)
#print(l3)

##kesişim kümesi
#l4=l1.intersection(l2)
#print(l4)

##fark
#l5=l1.difference(l2)
#print(l5)

##kümeyi yazarak oluşturma
#a={15,12,14}
#print(a)
#print(type(a))


##dictionary: sözlük
##keys,values,items
#hisse={
#    "beykent":101.2,
#    "istanbul":170.2,
#    "ankara":101.2,
#    "muş":50.2,
#    }

#yh={
#    "sahara":90.2,
#    "ohara":90.2
#    }
#hisse=yh
#print(hisse)

#for sehir,deger in hisse.items():
#    print(sehir,"şehir adı",deger,"değeri")


#print(hisse.keys())
#print(hisse.values())
#print(hisse.items())

##birinci değer bulmaya çalıştığı değer ikinci değer bulamazsa döndürdüğü değer
#print(hisse.get("muş","bulunamadı"))
#print(hisse.get("harran","bulunamadı"))

#print(hisse["beykent"])
#print(hisse["ankara"])

##eleman ekleme
#hisse["izmir"]=180.5
#print(hisse)

##değer değiştirme
#hisse["muş"]=10000
#print(hisse)

#print(type(hisse))
#print(hisse)

#print("beykent" in hisse)
#print("izmir" in hisse)

#if("beykent"in hisse):
#    print("bulundu")
#else:
#    print("bulunamadı")

#if("izmir"in hisse):
#    print("bulundu")
#else:
#    print("bulunamadı")
