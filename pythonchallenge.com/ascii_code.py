# coding:utf8
file_translate = "C:\\Users\\Administrator\\Desktop\\python\\translate.txt"
char ="map"
#char = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

asciis = []

translates = []

for chars in char:
    print chars
    if chars == "(":
        translates.append(chars)
    elif chars == ")":
        translates.append(chars)
    elif chars == ".":
        translates.append(chars)
    elif chars == ",":
        translates.append(chars)
    elif chars == " ":
        translates.append(chars)
    elif chars == "'":
        translates.append(chars)
    else:
        ascii = ord(chars)
        print "ascii is: %d"% ascii
        ascii = ascii + 2
        print "ascii + 2 is %d"% ascii
        if ascii > 122:
            ascii = ascii - 26
        print "now ascii = %d"% ascii
        chars = chr(ascii)
        translates.append(chars)
        print chars
    print chars
    with open(file_translate,"a+") as f:
        f.write(str(chars))


#        asciis.append(ascii)
#        print asciis
#
## 如果不再ascii字母区间内，就直接输出，如果在字母区间内，才会判断num是否在字母区间，
## 大于则减去26
#for num in asciis:
#    while num >"90":
#        num = num - 26
#    translate = chr(num)
#    print num
#    translates.append(translate)


#for i in char:
#    number = ord(char)
#    numbers = number + 3
#    numbers.append(numbers)
#
#for p in numbers:
#    chars = chr(p)
#    translate.append(chars)
#
print translates

#file_ascii = "C:\\Users\\Administrator\\Desktop\\python\\ascii.txt"
#with open(file_translate, "w") as f:
#    f.write(asciis)

#file_translate = "C:\\Users\\Administrator\\Desktop\\python\\translate.txt"
#with open(file_translate, "w") as f:
#    f.write(str.(translates())
