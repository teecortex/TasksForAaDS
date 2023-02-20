#import wikipedia
import docx
import re
import hashlib


#Обработка wiki страницы
# wikipedia.set_lang("ru")
# result = wikipedia.search("Стресс")
# page = wikipedia.page(result[0]).content
f = open('wikiStress.txt', encoding='utf-8')
# f.write(page)
wikiStrings = []
for r in f:
    wikiStrings.append(r[:-2])
wikiString = ' '.join(wikiStrings)

ThreeWiki = []
s1 = re.sub("[^А-Яа-яA-Za-z0-9]", " ", wikiString)
s1 = " ".join(s1.split())
WikiMass = s1.split(' ')
print(WikiMass)
Hashwiki = []
for i in range(len(WikiMass)-2):
    substring = WikiMass[i] + " " + WikiMass[i+1] + " " + WikiMass[i+2]
    ThreeWiki.append(substring)
    newhash = hashlib.md5(substring.encode())
    Hashwiki.append(newhash.hexdigest())



#Обработка реферата
doc = docx.Document('Stress.docx')
allText = []
for docpara in doc.paragraphs:
    allText.append(docpara.text)
print(allText[0])
Str_All_Text = ' '.join(allText)
s2 = re.sub("[^А-Яа-яA-Za-z0-9]", " ", Str_All_Text)
s2 = " ".join(s2.split())
mass_all_text = s2.split(' ')
threeWordRef = []
hashRef = []
for i in range(len(mass_all_text)-2):
    substring = mass_all_text[i] + " " + mass_all_text[i+1] + " " + mass_all_text[i+2]
    threeWordRef.append(substring)
    newhash = hashlib.md5(substring.encode())
    hashRef.append(newhash.hexdigest())



#Сравнение
plagiat_count = 0
for i in range(len(Hashwiki)):
    for j in range(len(hashRef)):
        if Hashwiki[i] != hashRef[j]:
            continue
        else:
            if ThreeWiki[i] == threeWordRef[j]:
                plagiat_count+=1
print(plagiat_count)
print("Процент плагиата в тексте:", str(round((plagiat_count/len(s2))*100, 2)) + "%")

