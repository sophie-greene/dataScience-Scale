import json,sys,re,string,itertools

def splitSen(txt):

    delims = "?.,!:;"
    ww=''.join(l for l in txt if l in string.letters+' ')
    wor=ww.split(' ')
    words=[w.strip() for w in wor if len(w.strip())>0]
    return words
def disp(d):
    for k in d:
        #if type(k[1])==float:
            #k0=''.join(l for l in k[0] if l in string.letters)
        print (str(k[0])+" "+str(k[1]))
def main():
    en=lambda x: x.encode('latin1', errors='ignore')
   
    tweet_file = open(sys.argv[1])
   
    txt=tweet_file.readlines()

    tweetlines=[json.loads(t) for t in  txt]
    tweetText=list(map(lambda l: en(l['text']) if 'text' in l.keys() else '',tweetlines))
    words=list((itertools.chain(*[splitSen(t) for t in tweetText])))
    res=[[w,(len(list(filter(lambda x:x==w,words)))*1.0)/len(tweetText)] for w in words]
    disp(res)

if __name__ == '__main__':
    main()