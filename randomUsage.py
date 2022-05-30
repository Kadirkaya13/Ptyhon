# Ptyhon
import random

#print(random.random())
#print(random.uniform(1,100))
#print(random.randint(1,100))
#print(int(random.uniform(1,100)))
#a=range(100)
#print(random.sample(a,5))

##soğuk sıcak
##1-100 arası random sayı oluşturur kullanıcı her seferinde sayıyı tahmin etmeye çaılışır
##kullanıcının başlangıçta 100 puanı vardır 
##her yanlış tahminde -5 puan kesilir
##oyun kuralları kullanıcı 15den fazla yanlış tahmin yaparsa
##kullanıcı 5 puandan düşükpuanı olursa kaybeder
##kullanıcı doğru bilirse kazanır
##soğuksa > sayıdan büyük
##sıcaksa > sayıdan küçük

#a = random.randint(1,100)
#kPuan=100
#say=15


#while(True):
   
#    if(say==0):
#        print("kaybettiniz")
#        print("puanınız:", kPuan)
#        break

#    if(kPuan<=5):
#        print("kaybettiniz")
#        print("puanınız:", kPuan)
#        break
#    print("Hakkınız :",say)
#    kSayı=int(input("bir sayı giriniz :"))
#    say-=1
#    if(kSayı==a):
#        print("Kazandınız")
#        print("puanınız:", kPuan)
#        break

#    if(kSayı>a):
#        print("soğuk")
#        kPuan-=5

#    if(kSayı<a):
#        print("sıcak")
#        kPuan-=5


#ranstgele 2 sayı oluşturur 1-100 arası
#dört işlem oluşturur
# 15 + 25 = ?
# 4 işlem oyunu kullanıcı doğru bilirse +5 puan kazanır
#kullanıcı yanlış bilirse -5 puan kaybeder
#oyun kullanıcı 0 puana veya 100 puana ulaşınca biler
#kullanıcıya başlangıçta 10 puan verilir


kPuan=10

while(True):
    if(kPuan<=0):
        print("kaybettiniz!!")
        break
    elif(kPuan>=100):
        print("Kazandınız!!!")
        break
    num1= random.randint(1,100)
    num2= random.randint(1,100)
    islem=random.randint(1,4)
    sonuc=None
    snum1= str(num1)
    snum2= str(num2)
    a="a"
    print("-------------------------------------------Oyun Başlangıçı-----------------------------------------------")
    if(islem==1):
        a=int(input(snum1+ " + " + snum2 + "= ?" ))
        sonuc=num1+num2
    b=int(input(snum1+ " - " + snum2 + "= ?" ))
    if(islem==2):
        a=int(input(snum1+ " - " + snum2 + "= ?" ))
        sonuc=num1-num2
    c=int(input(snum1+ " * " + snum2 + "= ?" ))
    if(islem==3):
        a=int(input(snum1+ " * " + snum2 + "= ?" ))
        sonuc=num1*num2
    d=int(input(snum1+ " / " + snum2 + "= ?" ))
    if(islem==4):
        a=int(input(snum1+ " / " + snum2 + "= ?" ))
        sonuc=num1/num2
    if(sonuc==a):
        print("Tebriker doğru bildiniz!!")
        kPuan+=5
    else:
        print("Yanlış bildiniz!!")
        kPuan-=5

    print("Puanınız = ",kPuan)
    print("-------------------------------------------Oyun Sonu-----------------------------------------------")
#primitive:
#int,float,bool
#String, None,Complex

#Lists, Tuple,
#Set, Dictionary

#liste1=[1,2,3,4,5,6]
#liste2=["a","b","c","d"]
#liste3=[True,False,True]
#liste4=[None,None]
#liste5=[2+3j,4+5j,25-21j]
#liste6=[12.3,10.5,12.12]
#print(liste1)
#print(type(liste1))
#liste7=[1,"a",True,None,2+4j,12.3]
#print(liste7)
#print(type(liste7[4]))


#liste=[1,2,3,4,5,6]
#print(len(liste))
#print("sıralama")
#list=liste
#liste+=[10]
#print(liste[2:5])
#print(liste[:5])
#print(liste[2:])
#print(liste[-1])
#print(liste[-2])
#print(liste[0:5:2])
#for i in list:
#    print(i)

#liste=[["Ayşe",90],["Fatma",100],[["Beykent","Üni"],"Mustafa",70]]
#print(liste[0])
#print(liste[0][1])
#print(liste[-1][1])
#print(liste[-1][0][1])


#liste=[10,20,30,40]
#liste[2]=170
#print(liste[2])

#liste=["KA"]*10

#for i in liste:
#    print(i)

#for i in enumerate(liste):
#    print(i)

##arrayi tersine yazma
#liste=[None]*10
#for i in range(0,len(liste)):
#    liste[i]=i*5
#print(liste)

#liste2=[None]*len(liste)
#sayac=len(liste)-1
#for i in range(0,len(liste)):
#    liste2[i]=liste[sayac]
#    sayac-=1
#print(liste2)

#liste=[None for i in range(0,10)]
#print(liste)

###"**"üst almak anlamına gelir
#liste=[i**2 for i in range(0,10)]
#print(liste)
#liste = [10,20,30,40,50,60]
##içerisine yazılan değerin indexini bulmayı sağlar
##aynı değerden 2 veya daha fazla varsa ilk karşılaştığı indexi yazar
#print(liste.index(30))

#liste=["a","b","c","d","e"]
###belirtilen indexte bulanan değeri siler
#sil=liste.pop(2)
#print(liste)

#nums=[11,22,33,44,55,66,11]
###belirtilen değerin liste içerinde kaç tane olduğunu sayar
#print(nums.count(11))


#import random as r

#liste=[None]*10

#for i in range(0,len(liste)):
#    liste[i]=r.randint(0,100)
#print(liste)


###20 elemanlı liste
##bu liste en az 4 tane 5
###3 tane9ve 6tane 10 olacak şekilde
###listeye rastgele sayılar(1,100)
###atayan program
#import random as r

#liste = [None] * 20
#i = 0
#sayac=0
#while(True):
#    print(sayac,". kez deneme")
#    sayac+=1
#    for i in range(0,len(liste)):
#        liste[i]=r.randint(0,10)
#        i+=1
#        bes = liste.count(5)
#        dokuz = liste.count(9)
#        on = liste.count(10)
#    if(bes>=2 and dokuz>=2 and on>=2):
#        print(liste)
#        print(bes,"tane 5",dokuz,"tane 9",on,"tane 10")
#        break

##silme ve tersine yazma
#liste=[1,4,56,8,9,6,25,36,24,45]
#del(liste[3])
#liste2=sorted(liste,reverse=True)
#print(liste2)
