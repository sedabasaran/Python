def emoji_cevirici(kullanıcı):
    sözcükler= kullanıcı.split(" ")
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


kullanıcı=input(">")
print(emoji_cevirici(kullanıcı))
