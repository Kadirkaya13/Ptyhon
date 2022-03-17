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
