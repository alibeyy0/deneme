meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey.",
    "LOL": "Komik bir şeye verilen cevap.",
    "ROFL": "Bir şakaya karşılık verilen cevap.",
    "SHEESH": "Onaylamama ifadesi.",
    "CREEPY": "Tüyler ürpertici, ürkütücü anlamına gelen söz.",
    "AGGRO": "Agresifleşmek, sinirlenmek anlamına gelen söz.",
    "OMG": "Aman tanrım anlamında şaşırma ifadesi.",
    "NGL": "Gerçekten öyle, yalan söylemiyorum anlamına gelen söz."
}

while True:
    word = input("Sözlükten anlamını öğrenmek istediğiniz bir kelimeyi girin: ").upper()

    while word not in meme_dict.keys():
        add_word = input("Kelime sözlükte yok. Yeni bir kelime ve açıklamasını eklemek ister misiniz? (Evet/Hayır): ").lower()
        if add_word == "evet":
            new_word = input("Lütfen yeni kelimeyi girin: ").upper()
            new_meaning = input("Lütfen kelimenin anlamını girin: ")
            meme_dict[new_word] = new_meaning
            print("Kelimeniz sözlüğe eklendi.")
        else:
            
            break

    if word in meme_dict.keys():
        print(meme_dict[word])
