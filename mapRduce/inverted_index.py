#############################################################
#@Author: Sophie M. Greene
#25/11/2016
#############################################################
import MapReduce
import sys,time

'''
Inverted Index
Create an Inverted index. Given a set of documents, 
an inverted index is a dictionary where each word 
is associated with a list of the document identifiers 
in which that word appears.  
'''

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    
    value = record[1]
    # print(time.time(),record)
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, record[0])

def reducer(key, list_of_values):
    # key: word
    # value: list of record id
    total = []
    for v in list_of_values:
      if v not in total:
        total.append(v)
    mr.emit((key, total))
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
