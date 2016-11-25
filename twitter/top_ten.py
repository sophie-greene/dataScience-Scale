import json,sys,re,string,itertools

def extract(txt):
    res=[]
    en=lambda x: ''.join(l for l in x.encode('latin1', errors='ignore') if l in string.letters+' ')
    d=json.loads(txt)
   
    if 'entities' in d.keys() and 'hashtags' in d['entities'].keys():
            for t in d['entities']['hashtags']:
                if type(t)==dict and 'text'in t.keys():
                    tt=en(t['text'])
                    if len(tt)>0:
                        res.append(tt.lower().strip())
    return res
def tweetSent(txt,dct):

    delims = "?.,!:;"
    ww=''.join(l for l in txt if l in string.letters+' ')
    wor=ww.split(' ')
    words=[w.strip() for w in wor ]
    
    wordsSent=list(map(lambda w: sum(dct[w]) if w in dct.keys() else 0.0,words))
    
    return sum(wordsSent)
def disp(d):
    for k,v in d:
        
            print (str(k)+' '+str(v))
def main():
    en=lambda x: x.encode('latin1', errors='ignore')
    
    tweet_file = open(sys.argv[1])
   
    txt=tweet_file.readlines()
    d=list(itertools.chain(*[extract(t) for t in txt]))
    dct=dict.fromkeys(set(d),0)
    for it in d:
        dct[it]+=1
    res=[[k, (v*1.0)] for k,v in dct.items()]
    ress=list(sorted(res,key=lambda l:l[1], reverse=True))[0:10]
    disp(ress)

if __name__ == '__main__':
    main()