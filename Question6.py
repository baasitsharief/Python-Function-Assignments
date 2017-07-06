def pygLatin(word):
    #takes a word. processes accordingly.
    vowels=['a','e','i','o','u']
    word=word.lower().strip()

    if(not word):
        return ''
    if(word.isnumeric()):
        new_word=word
    elif(word[0] in vowels):
        new_word=word+'hay'
    else:
        new_word=word[1:]+word[0]+'ay'
    return new_word

def pygLatin_sentence(sentence):
    #takes a sentence. breaks into words. passes words to pygLatin
    new_words=[]
    words=sentence.split(' ')
    for word in words:
        new_words.append(pygLatin(word))
    new_sentence=' '.join(new_words).strip()
    return(new_sentence)

def to_pygLatin(paragraph):
    #takes entire paragraph. breaks into sentences. passes sentences to pygLatin_sentence
    new_paragraph=[]
    sentences=paragraph.split('.')
    for sentence in sentences:
        new_paragraph.append(pygLatin_sentence(sentence))
    return('. '.join(new_paragraph))

paragraph=input() #input string
paragraph+=' '

print(to_pygLatin(paragraph))