inputStr=input('enter a sentence ')
print(inputStr)
characterCount = 0
wordCount = 1
for eachChr in inputStr: 
    characterCount = characterCount + 1
    if(eachChr == ' '):
        wordCount = wordCount + 1
print(characterCount)
print(wordCount)