import nltk
from nltk.corpus import brown
import ngram
from nltk.probability import LidstoneProbDist,WittenBellProbDist

def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output


with open("test.txt") as f:
    content = f.readlines()
s = "salam soroush siah ziaeinejad siah soreh soosk"
print(ngrams(s,1))
