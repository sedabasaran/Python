###Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock ###

import sys

kullanıcı1= input("birinci oyuncunun adı?\n")
kullanıcı2 = input("ikinci oyuncunun adı?\n")

kullanıcı1_cevap = input("hangisini seçeceksiniz {} ;taş, kağıt, makas".format(kullanıcı1))
kullanıcı2_cevap = input("hangisini seçmek istersiniz {} taş; kağıt; makas".format(kullanıcı2))


def compare(k1,k2):
    if k1 ==k2:
        return ("beraberlik ! ")
    elif k1 =='taş':
        if k2=='makas':
            return("taş kazandı")
        else:
            return ("kağıt kazandı")
    elif k1 =='makas':
        if k2 =="kağıt":
            return("makas kazandı")
        else:
            return("taş kazandı")
    elif k1 == 'kağıt':
        if k2 =='taş':
            return("kağıt kazandı")
        else:
            return("makas kazandı")
    else:
        return("geçersiz işlem,lütfen taş,kağıt,makas üçlüsünden birini seçiniz,\n tekrar deneyiniz")
        sys.exit()
print(compare(kullanıcı1_cevap,kullanıcı2_cevap))
