def countVowels(s:str):
    vowels='aeiouAEIOU'; count=0
    for letter in s:
        if letter in vowels:
            count+=1
    return count
res=countVowels("HelloWorld")
print(f"No of vowels{res}") 