import json

with open("sozluk.json", "r", encoding="utf-8") as f:
    cmd_kod_sozluk = json.load(f)

while True:
    cmd_kod_sozluk1 = input("Lütfen aramak istedidiğiniz kodun açıklamasını yazın veya çıkmak için 'q' tuşuna basın: ")
    if cmd_kod_sozluk1.lower() == 'q':
        break
    for hata, aciklama in cmd_kod_sozluk.items():
        if hata.lower() == cmd_kod_sozluk1.lower():
            print(aciklama)
            break
    else:
        print("Girdiğiniz açıklama yanlş/listemizde yok.")