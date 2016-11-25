import sys,json,re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp))
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
def tweetSent(txt,dct):
    words=re.findall("[a-zA-Z ]+", txt)
    wordsSent=list(map(lambda w: dct[w.lower()] if w.lower() in dct.keys() else 0,words))
    return sum(wordsSent)
def disp(arr):
    for r in arr:
        print('{0:g}'.format(r))
def main():
    sent_file=open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    txt=tweet_file.readlines()
    dctt=sent_file.readlines()
    #hw()
    #lines(dctt)
    #lines(txt)
    
    #print(sys.argv[1],sys.argv[2])
    dct={x.split('\t')[0].strip():float(str(x.split('\t')[1].strip())) for x in dctt}
    
    tweetlines=[byteify(json.loads(t))  for t in  txt]
    tweetText=list(map(lambda l: l['text'] if 'text' in l.keys() else '',tweetlines))
    sentments=[tweetSent(t,dct) for t in tweetText]
    disp(sentments)

if __name__ == '__main__':
    main()
