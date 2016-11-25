#############################################################
#@Author: Sophie M. Greene
#25/11/2016
#############################################################
import MapReduce
import sys,time,json

'''
Consider a simple social network dataset consisting of a set of 
key-value pairs (person, friend) representing a friend relationship 
between two people. Describe a MapReduce algorithm to count 
the number of friends for each person.

'''

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = 1
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: list of number of friends
    total = 0
    for v in list_of_values :
      total += v
    mr.emit((key,total))
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  # txt=open('solutions/join.json').readlines()
  # en=lambda x: x.encode('latin1', errors='ignore')
  # data = [json.loads(en(x)) for x in txt]
  # print(data == mr.result)
  # print(len(mr.result))
