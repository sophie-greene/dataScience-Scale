#############################################################
#@Author: Sophie M. Greene
#25/11/2016
#############################################################
import MapReduce
import sys,time,json

'''
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. 
Implement a MapReduce algorithm to check whether this property holds. 
Generate a list of all non-symmetric friend relationships.

'''

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = tuple(sorted(record))
    value = 'somevalue'
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: list of friends
    if len(list_of_values) == 1:
        mr.emit((key))
        mr.emit(tuple(reversed(key)))
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  # txt=open('solutions/asymmetric_friendships.json').readlines()
  # en=lambda x: x.encode('ascii', errors='ignore')
  # data = [tuple(str(s)for s in json.loads((x))) for x in txt]
  # print('data matches',list(sorted(data)) == list(sorted(mr.result)))
  # print(data)
  # print(len(mr.result),len(data))
