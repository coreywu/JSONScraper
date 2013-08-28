import urllib2
import json as simplejson
import random
import sqlite3 as lite

productIds = []
apiKeys = ["98bbbd30b3e4f621d9cb544a790086d6"]

file = open("productIds3.txt", "r")
for line in file:
  productIds.append(line.strip())
print productIds
file.close()

connection = lite.connect("productInfo.db")

with connection:

  cursor = connection.cursor()
  cursor.execute("DROP TABLE IF EXISTS ProductInfo")
  cursor.execute("CREATE TABLE ProductInfo(product_id INT, product_name TEXT,\
      ingredients TEXT, serving_size TEXT, calories INT, total_fat_g INT,\
      total_fat_percent INT, fat_saturated_g INT, fat_saturated_percent INT,\
      fat_trans_g INT, fat_trans_percent INT, cholesterol_mg INT, sodium_mg\
      INT, sodium_percent INT, carbo_g INT, carbo_percent INT, carbo_fibre_g\
      INT, carbo_fibre_percent INT, carbo_sugars_g INT, protein_g INT,\
      vitamin_a_percent INT, vitamin_c_percent INT, calcium_percent INT,\
      iron_percent INT, micro_nutrients TEXT, tips TEXT, diet_id INT, diet_type\
      TEXT)")
  for productId in productIds[:10]:
    url = "http://api.uwaterloo.ca/public/v2/foodservices/product/" + \
    str(productId) + ".json?key=" + str(apiKeys[random.randint(0, len(apiKeys) - 1)])
    req = urllib2.Request(url)
    opener = urllib2.build_opener()

    f = opener.open(req)
    data = simplejson.load(f)
    if data["meta"]["status"] == 200:
      if data["data"]["product_name"] != None:
        print "INSERT INTO ProductInfo VALUES(" + str(data["data"]["product_id"]) + ", "\
            + str(data["data"]["product_name"]) + ", " + str(data["data"]["calories"]) + ")"
        cursor.execute("INSERT INTO ProductInfo VALUES(:product_id,\
        :product_name, :ingredients, :serving_size, :calories,\
        :total_fat_g, :total_fat_percent, :fat_saturated_g,\
        :fat_saturated_percent, :fat_trans_g, :fat_trans_percent,\
        :cholesterol_mg, :sodium_mg, :sodium_percent, :carbo_g, :carbo_percent,\
        :carbo_fibre_g, :carbo_fibre_percent, :carbo_sugars_g, :protein_g,\
        :vitamin_a_percent, :vitamin_c_percent, :calcium_percent,\
        :iron_percent, :micro_nutrients, :tips, :diet_id,\
        :diet_type)", (\
        str(data["data"]["product_id"]),\
        str(data["data"]["product_name"]),\
        str(data["data"]["ingredients"]),\
        str(data["data"]["serving_size"]),\
        str(data["data"]["calories"]),\
        str(data["data"]["total_fat_g"]),\
        str(data["data"]["total_fat_percent"]),\
        str(data["data"]["fat_saturated_g"]),\
        str(data["data"]["fat_saturated_percent"]),\
        str(data["data"]["fat_trans_g"]),\
        str(data["data"]["fat_trans_percent"]),\
        str(data["data"]["cholesterol_mg"]),\
        str(data["data"]["sodium_mg"]),\
        str(data["data"]["sodium_percent"]),\
        str(data["data"]["carbo_g"]),\
        str(data["data"]["carbo_percent"]),\
        str(data["data"]["carbo_fibre_g"]),\
        str(data["data"]["carbo_fibre_percent"]),\
        str(data["data"]["carbo_sugars_g"]),\
        str(data["data"]["protein_g"]),\
        str(data["data"]["vitamin_a_percent"]),\
        str(data["data"]["vitamin_c_percent"]),\
        str(data["data"]["calcium_percent"]),\
        str(data["data"]["iron_percent"]),\
        str(data["data"]["micro_nutrients"]),\
        str(data["data"]["tips"]),\
        str(data["data"]["diet_id"]),\
        str(data["data"]["diet_type"]) ))
                                                                                              
print productIds



