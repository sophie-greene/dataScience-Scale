import json,sys,re,string,itertools

def tweetSent(txt,dct):

    delims = "?.,!:;"
    ww=''.join(l for l in txt if l in string.letters+' ')
    wor=ww.split(' ')
    words=[w.strip() for w in wor ]
    
    wordsSent=list(map(lambda w: sum(dct[w]) if w in dct.keys() else 0.0,words))
    
    sentm=sum(wordsSent)
    rdct=[]
    for w in words:
        if len(w.strip())>0:
            lstt=[w,0.0,0.0]
            if sentm>0:
                if w in dct.keys():
                    if sentm>dct[w][0]:
                        lstt[1]=sentm
                    else:
                        lstt[1]=dct[w][0]
                    lstt[2]=(dct[w][1])
                else:
                    lstt[1]=sentm

            if sentm<0:
                if w in dct.keys():  

                    lstt[1]=dct[w][0]
                    if sentm<dct[w][1]:
                        lstt[2]=sentm
                    else:
                        lstt[2]=dct[w][1]
                else:
                    lstt[2]=sentm
            rdct.append(lstt)       
    return rdct
def disp(d):
    for k in d:
        if type(k[1])==float:
            k0=''.join(l for l in k[0] if l in string.letters)
            print (str(k0)+' '+str(k[1]))
def main():
    en=lambda x: x.encode('latin1', errors='ignore')
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
   
    txt=tweet_file.readlines()
    dctt=sent_file.readlines()

    dcttt={x.split('\t')[0].strip():float(str(x.split('\t')[1].strip())) for x in dctt}

    dct={k:[v,0.0] if v>0  else [0.0,v] for k,v in dcttt.items() }
    

    tweetlines=[json.loads(t) for t in  txt]
    tweetText=list(map(lambda l: en(l['text']) if 'text' in l.keys() else '',tweetlines))
    #t=tweetText[-1000]
    res=list((itertools.chain(*[tweetSent(t,dct) for t in tweetText])))
    #print(res[1])
    ress=[[item[0],item[1]] if abs(item[1])>=abs(item[2]) else [item[0],item[2]] for item in res if len(item[0].strip())>0 ]
    #res=[k for k in res if len(k[0].strip())>0]
    disp(ress)

if __name__ == '__main__':
    main()