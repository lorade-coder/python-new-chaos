word=input("enter a word : ")
text=" "
consonant=0
count=0
for letter in word : 
    vowel="a,e,i,o,u"
    
    if letter  in vowel :
        text+=letter
        count+=1
    else :
     text +=letter
     consonant+=1
print(count)
print("number of consonant = ",consonant)
    
