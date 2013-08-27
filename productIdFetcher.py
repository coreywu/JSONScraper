import urllib2
import json as simplejson
import random

productIds = []
apiKeys = ["5ab81ac0dd6bf53edc3340ac33dea247", "f26cec69697e8e4fad2ef6042ef2a725",
"8ad2ba56f6d21563d239fda4bd4449fc", "f90d59e55d0c500f640b9f35391e3ebe",
"d13911a55bf47f520b7955655d83eb6a", "cbe4ef746dd324d9906b162f7af47c9d",
"7448d02a91ffd2576232d4ee6f1494cb", "70787add4ce61c3f9f559e772689533e"]

file = open("productIds.txt", "w")

for i in range(0, 5000):
  key = str(apiKeys[random.randint(0, len(apiKeys) - 1)])
  url = "http://api.uwaterloo.ca/public/v2/foodservices/product/" + str(i) + \
  ".json?key=" + key
  
  req = urllib2.Request(url)
  opener = urllib2.build_opener()

  f = opener.open(req)
  data = simplejson.load(f)
  if data["meta"]["status"] == 200:
    if data["data"]["product_name"] != None:
      productIds.append(i);
      file.write(str(i) + '\n')
  elif data["meta"]["status"] == 401:
    print "Invalid API key " + key 


print productIds
  



