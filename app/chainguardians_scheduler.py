
import requests
from app.util import serialize_doc
#from app.config import chainguardians_api_endpoint,chainguardians_le_api_endpoint
from app import mongo
import datetime



#--------Scheduler for fetching chainguardians assests details--------

def Timesjobs():    
    print("running")
    for cou in range(0,50):
        print(cou)
        url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')              
        assets = requests.get(url=url)
        response = assets.json()      
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            checking = mongo.db.timesjobs_data.find_one({"companyName":companyName,"Location":Location,"adId":adId})
            if checking is None:
                ret = mongo.db.timesjobs_data.insert(dict(job))
            else:
                print("============================================================already exists=============================================")

