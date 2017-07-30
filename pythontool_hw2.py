import os
import sys
import json
import csv
import re
from urllib.request import urlopen

def getCountry(ipAddress):
        if __name__ == '__main__':
                response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
                responseJson = json.loads(response)
                return responseJson.get("country_code")
        

f = open("iplist.txt", "rt")
lines = f.readlines()


with open('iplist.csv', "w") as csvfile:
        fieldnames = ['ip address', 'country code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for line in lines:
                
                ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
                ipnumber_line = len(ip)

                i = 0
                
                while i < len(ip):

                        print(str(ip[i]))
               
                        value = getCountry(str(ip[i]))
                        print(value)
                           
                        writer.writerow({'ip address': str(ip[i]), 'country code': value})

                        i += 1

f.close()

        


 

                
