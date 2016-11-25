#############################################################
#@Author: Sophie M. Greene
#25/11/2016
#############################################################
import MapReduce
import sys,time,json

'''
Join implements the following sql query in MapReduce
SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id

record[0]: record[1]
LineItem :records have 17 attributes including the identifier string.

Order :records have 10 elements including the identifier string.


'''

mr = MapReduce.MapReduce()

def mapper(record):
    # key: join on; here order_id
    # value: all record
    key = record[1]
    value=record
    if len(record) == 17:
      num_of_emits = 10
    else :
      num_of_emits =17
    # print(time.time(),len(record),record[0])
    for i in range(num_of_emits):
      mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: 
    # value: list of record id
    lorder = []
    litem = []
    total = []
    for x in list_of_values :
        if str(x[0]) == 'order' and x not in lorder:
          lorder.append(x)
        if str(x[0]) == 'line_item' and x not in litem:
          litem.append(x)
    for x in lorder :
      for y in litem :
        tmp = x + y
        if tmp not in total :
          total.append(tmp)
    # print(len(total))
    for t in total:
       mr.emit((t))
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  # txt=open('solutions/join.json').readlines()
  # en=lambda x: x.encode('latin1', errors='ignore')
  # data = [json.loads(en(x)) for x in txt]
  # print(data == mr.result)
  # print(len(mr.result))
