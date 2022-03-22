def emoji_cevirici(kullanici):
    sözcükler= kullanici.split(" ")
    emojiler= {
        ":)":"😃",
        ":(":"😞",
        ":-)":"😀",
        ":-O":"😮",
        ":-P":"😛",
        ":-S": "😢",
        ":'(":"🥺",
        ":-$":"😊",
        "(H)":"😎",
        ":-@":"😡",
        "8-l":"🤓",
        "(L)":"❤️",
        "(*)":"⭐"
    }
    sonuc = ""
    for sözcük in sözcükler:
        sonuc+=emojiler.get(sözcük, sözcük )+ " "
    return sonuc


kullanici=input(">")
print(emoji_cevirici(kullanici))
