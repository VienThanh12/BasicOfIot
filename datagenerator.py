import requests # pip install requests
import math
import time
import datetime
 
 
i = 0
 
while i < 10:
    measurement = {}
    measurement["api_key"] = "YBAFOM906CBFRBBA"
    #measurement["created_at"] = str(datetime.datetime.now())
    measurement["field1"] = 1024+5*math.sin(i/10)
    measurement["field2"] = 300 + 2 * math.cos(i/3)
    measurement["field3"] = 33+i%50
    # serialize the data to JSON format and send it by HTTP POST
    response = requests.post('http://localhost:3001/api/measurements',json=measurement)
    print(response.ok)
    print(response.json())
    time.sleep(1) # we must wait at least 15 seconds
    i+=1
 
 