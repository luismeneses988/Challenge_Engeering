def calculateNGrams(word, n):
    ngrams = []
    
    for i in range(0, len(word)):
        if i + n - 1 < len(word):
            ngrams.append(word[i:i+n])
    
    for i in range(len(word) - 1, -1, -1):
        if i-n >= 0: 
            actual_word = word[i-n+1:i+1]
            
            add = True
            for ngram in ngrams:
                if ngram == actual_word:
                    add = False

            if add:
                ngrams.append(actual_word)
    
    return ngrams

def mostFrequentNGram(word, n):
    ngrams = calculateNGrams(word, n)
    ngrams_freq = []

    for i in range(0, len(ngrams)):
        ngram = ngrams[i]
        ngram_count = 1

        for j in range(i+1, len(ngrams)):
            if ngram == ngrams[j]:
                ngram_count += 1
        
        info = {'ngram' : ngram, 'count' : ngram_count}
        ngrams_freq.append(info)

    ngram = ''
    max_repetitions = 0
    for info in ngrams_freq:
        if info['count'] > max_repetitions:
            max_repetitions = info['count']
            ngram = info['ngram']
        
    return ngram, max_repetitions

print(calculateNGrams('Slang', 1))
print('='*50)
print(calculateNGrams('Slang', 2))
print('='*50)
print(calculateNGrams('Slang', 3))
print('='*50)
print(calculateNGrams('Slang', 4))
print('='*50)
print(calculateNGrams('Slang', 5))

print('='*50)
print(mostFrequentNGram('to be or not to be',2))
