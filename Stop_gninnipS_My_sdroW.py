def spin_words(sentence):
    answer = []
    if len(sentence) < 5:
        return sentence
    if ' ' in sentence:
        for word in sentence.split():
            answer.append(spin_words(word))
    else:
        return sentence[::-1]
    return ' '.join(answer)



dict_values = {
    'Welcome': 'emocleW',
    'to': 'to',
    'CodeWars': 'sraWedoC',
    'Hey fellow warriors': 'Hey wollef sroirraw',
    'This sentence is a sentence': 'This ecnetnes is a ecnetnes',
}


for sentence in dict_values:
    spin_words(sentence)