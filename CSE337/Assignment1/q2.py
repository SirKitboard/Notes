encryptedText = "pda lupdkj lnkcnwiiejc hwjcqwca swo ejrajpaz xu cqezk rwj nkooqi, w zqpydykilqpan lnkcnwiian, wxkqp 25 uawno wck. rwj nkooqi zabejaz deo ckwho bknlupdkj wo bkhhkso: wj awou wjz ejpqepera hwjcqwca fqop wo lksanbqh wo iwfknykilapepkno; klaj okqnya, ok wjukja ywj ykjpnexqpa pk epo zarahkliajp; ykzapdwp eo wo qjzanopwjzwxha wo lhwej ajcheod; oqepwxehepu bkn aranuzwu pwogo,whhksejc bkn odknp zarahkliajp peiao"
decryptedText = ""

for c in encryptedText:
    charIndex = ord(c)
    if(charIndex >= 65 and charIndex <= 90):
        # print('hi')
        newIndex = (charIndex - 61) % 26 + 65
        newChar = chr(newIndex)
        decryptedText = decryptedText + newChar
    elif (charIndex >= 97 and charIndex <= 122):
        # print('hello')
        newIndex = (charIndex - 93) % 26 + 97
        # print(newIndex)
        newChar = chr(newIndex)
        decryptedText = decryptedText + newChar
    else:
        decryptedText = decryptedText + c

print (decryptedText)
