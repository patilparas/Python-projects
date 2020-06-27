#get sentence from user

original = input("enter the sentence: ").strip().lower()

#slipt sentence into words

words =original.split()
print(words)

#loop through the words and convert to pig latin

new_words = []
for word in words:
#if it starts with the vowels,just add yay otherwise, move the first consonant cluster to end, and add ay
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        new_word = rest + cons + "ay"
        new_words.append(new_word)

        
#stick words back together

output = " ".join(new_words)

#output the final string

print(output)
