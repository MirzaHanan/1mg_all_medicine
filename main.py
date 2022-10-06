import requests
from bs4 import BeautifulSoup
import json
import csv

url = "https://www.1mg.com/drugs-all-medicines"

for i in range(1,1000):
    querystring = {"page":i,"label":"p"}
    # querystring = {"page":i}

    payload = ""
    headers = {"cookie": "VISITOR-ID=587e0978-d7f3-4e8a-ce8d-eb077fccbfed_acce55_1664611744; city=New%2520Delhi; geolocation=true; abVisitorId=393757; abExperimentShow=false; _csrf=D5aHimZgpc9vtoVBPCdEKydn"}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    soup = BeautifulSoup(response.text , "html.parser")

    try:
        script = soup.find_all("script")[24].text[32:-37]
        data = json.loads(script)
    except:
        script = soup.find_all("script")[25].text[32:-37]
        data = json.loads(script)
   
    with open('p(3).csv' ,'a' , newline= '' , encoding= 'utf-8') as f:
        csv_writer =  csv.writer(f)
        header = ['is_discontinued', 'manufacturer_name' , 'type' , 'price' , 'name' , 'id' , 'sku_id' , 'available' , 'pack_size_label' , 'link' , 'short_composition' , 'quantity']
        l1 = []
        for i in range(30):
            l1 = []
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['is_discontinued'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['manufacturer_name'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['type'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['price'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['name'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['id'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['sku_id'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['available'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['pack_size_label'])
            l1.append('https://www.1mg.com'+str(data["allMedicinePageReducer"]["data"]["skus"][i]['slug']))
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['short_composition'])
            l1.append(data["allMedicinePageReducer"]["data"]["skus"][i]['quantity'])

            csv_writer.writerow(l1)
        print(l1)

    #container > div > div > div.style__inner-container___3BZU9.style__white-bg___1qNti > ul > li:nth-child(7) > a