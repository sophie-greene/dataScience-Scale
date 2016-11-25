#############################################################
#@Author: Sophie M. Greene
#25/11/2016
#############################################################
import MapReduce
import sys,time,json

'''
Assume you have two matrices A and B in a sparse matrix format, 
where each record is of the form i, j, value. 
Design a MapReduce algorithm to compute the matrix multiplication A x B

'''

mr = MapReduce.MapReduce()

def mapper(record):
    # key: id
    N=5
    if str(record[0]) == 'a' :
        for i in range(N):
            key = record[1],i
            value = record[0],record[2],record[3]
            mr.emit_intermediate(key, value)
    elif str(record[0]) == 'b' :
        for i in range(N):
            key = i,record[2]
            value = record[0], record[1], record[3]
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: sequence
    # value: not relevant
    a = [x for x in list_of_values if x[0] == 'a' ]
    b = [x for x in list_of_values if x[0] == 'b']
    res = 0
    for ai in a:
        for bi in b:
            if ai[1] == bi[1] :
                res += ai[2] * bi[2]
    mr.emit( ( key[0],key[1], res ) )



if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  txt=open('solutions/multiply.json').readlines()
  en=lambda x: x.encode('ascii', errors='ignore')
  data = [str(tuple(json.loads(x))) for x in txt]
  mrres =[str(x) for x in mr.result]
  print('data matches',list(sorted(data)) == list(sorted(mrres)))
  # print(data)
  print(len(mr.result),len(data))
 