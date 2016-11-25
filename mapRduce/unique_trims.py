#############################################################
#@Author: Sophie M. Greene
#25/11/2016
#############################################################
import MapReduce
import sys,time,json

'''
Consider a set of key-value pairs where each key is sequence id and
 each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string of nucleotides,
 then remove any duplicates generated.
'''

mr = MapReduce.MapReduce()

def mapper(record):
    # key: id
    # value: sequence
    value = 1 #doesnt matter
    key = record[1][:-10]
    # print(len(record))
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: sequence
    # value: not relevant
      
    mr.emit(key)
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  # txt=open('solutions/unique_trims.json').readlines()
  # en=lambda x: x.encode('ascii', errors='ignore')
  # data = [str(json.loads(x)) for x in txt]
  # print('data matches',list(sorted(data)) == list(sorted(mr.result)))
  # print(data)
  # print(len(mr.result),len(data))
 