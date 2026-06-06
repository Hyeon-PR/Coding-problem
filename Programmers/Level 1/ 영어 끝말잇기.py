def solution(n, words):
    word_chain = set()    
    prev_word = words[0][0]
    person, turn = 0, 0
    for i, word in enumerate(words):
        if prev_word and prev_word[-1] == word[0] and word not in word_chain:
            word_chain.add(word)
            prev_word = word 
            continue
        else:
            person = (i % n) + 1
            turn = (i // n) + 1
            break
    return [person, turn]