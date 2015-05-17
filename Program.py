import nltk
import codecs
from sys import  argv
from collections import Counter
from nltk.corpus import brown
import ngram
from nltk.probability import LidstoneProbDist,WittenBellProbDist
import nltk

def TaggingBlank(input):
    if(PreBlank(input)[0]=='and' or PreBlank(input)[0]=='or'):
        return PrePreBlank(input)[1]
    elif(PostBlank(input)[0]=='and' or PostBlank(input)[0]=='or'):
        return PostPostBlank(input)[1]
    else:
        if (TypeOfBlankIsNoun(pre,post)):
            return "NN"
        elif(TypeOfBlankIsADJ(pre,post)):
            return "ADJ"
        elif(TypeOfBlankIsVerb(pre,post)):
            return "VBP"
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output
def Verb(input):
    for i in input:
        if (i[1]=='VBP' or i[1]=="VBD"):
            return i[0]
def PreBlank(input):
    for i in range(len(input)):
        if (input[i][0]=="$"):
            return input[i-1]
def PostBlank(input):
    for i in range(len(input)):
        if (input[i][0]=="$"):
            return input[i+1]

def PostPostBlank(input):
    for i in range(len(input)):
        if (input[i][0]=="$"):
            return input[i+2]

def PrePreBlank(input):
    for i in range(len(input)):
        if (input[i][0]=="$"):
            return input[i-2]

def TypeOfBlankIsNoun(pre,post):
    if (pre[1]=="ADJ"):
        return True
    elif (pre[0][-2::]=="'s"):
        return True
    elif (post[0] in ['is','am','are','was','were']):
        return True
    elif (pre[0] in ezafe):
        return True

def TypeOfBlankIsADV(pre,post):
    if (pre[1]=="VBP"):
        return True

def TypeOfBlankIsADJ(pre,post):
    if (post[1]=="NN"):
        return True
    elif (pre[0] in ['is','am','are','was','were']):
        return True
def TypeOfBlankIsVerb(pre,post):
    if (pre[1]=="NN" or pre[1]=="PRP"):
        return True
    elif(post[0] in ezafe):
        return True
    elif (pre[0] in ['is','am','are','was','were']):
        return True
sentence = input("Enter the sentence and obtain the blank with a '$': ")
ezafe=['the','a','an','about','after','along','as','at','befor','ebehind','between','by','down','during','except','for','from','in','of','on','with','without']
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
#print (tagged)
verb = Verb(tagged)
pre , post = PreBlank(tagged),PostBlank(tagged)
#print (TaggingBlank(tagged))
finalTag = TaggingBlank(tagged)
N=1000
lines=[]
f= open("miniTrain.txt","r")
s=''
#print (len(open("miniTrain.txt").readlines()))
for i in range(N):
    line=f.readline()
    lines.append(line)
    s = s+ " " + line
f.close()
CSMC = Counter(s.split()).most_common()
ngrams = []
for m in lines:
    ngrams1 = m
    ngrams2 = ngram.NGram.compare(sentence,m,k=3)
    ngrams.append([ngrams1,ngrams2])
ngrams.sort()
ls=[]
for j in range(10):
    tagged2 = nltk.pos_tag(nltk.word_tokenize(ngrams[j][0]))
    for k in tagged2:
        if k[1]==finalTag:
            ls.append(k[0])
a = sentence.index('$')
for m in ls:
    print (sentence[0:a],m,sentence[a+1::])

