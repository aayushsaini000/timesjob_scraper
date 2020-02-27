
import requests
from app.util import serialize_doc
#from app.config import chainguardians_api_endpoint,chainguardians_le_api_endpoint
from app import mongo
#import datetime
#import dateutil.parser
import pymongo

from pymongo import MongoClient
import json

#--------Scheduler for fetching chainguardians assests details--------
#it
#account
#HR Recruitment
#Sales
#marketing
'''
urls = ['https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=35$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=11$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=20$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=32$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=23$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=25$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=22$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=34$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        ]
'''
             #'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=22$&txtKeywords=&pSize=1000&pIndex='+str(cou)+'',
            #'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=34$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
client = MongoClient("mongodb+srv://root:0vXPeLcPxME40Ydv@cluster0-v8o7t.mongodb.net/jobs_scraper?retryWrites=true&w=majority")
temp_db = client.jobs_scraper

'''
def naukri_date_change():
    print("running")
    mycryptoheroes_records = temp_db.jobs_details.find({})
    print("worked")
    mycryptoheroes_records = [serialize_doc(mycryptoheroes_record) for mycryptoheroes_record in mycryptoheroes_records]
    print(len(mycryptoheroes_records))
    for mycryptoheroes_record in mycryptoheroes_records:
        createdDate = mycryptoheroes_record['createdDate']
        title = mycryptoheroes_record['title']
        staticCompanyName = mycryptoheroes_record['staticCompanyName']
        date_time = dateutil.parser.parse(createdDate)
        job_object = dict(mycryptoheroes_record)
        job_object['createdDate'] = date_time
        checking = mongo.db.naukrijobs_data.update({"title":title,"staticCompanyName":staticCompanyName},{"$set":dict(job_object)},upsert=True)
'''

def naukri_date_change():
    print("running")
    mycryptoheroes_records = mongo.db.timesjobs_data.find({})
    mycryptoheroes_records = [serialize_doc(mycryptoheroes_record) for mycryptoheroes_record in mycryptoheroes_records]
    print(len(mycryptoheroes_records))
    for mycryptoheroes_record in mycryptoheroes_records:
        key = mycryptoheroes_record['keySkills']
        for ke in key:
            print(ke)


def Timesjobs():
    print("timesjobs")
    #urls = ['https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=35$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
    #    ]
    #for url in urls:
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=35$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "software development"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)


def accountjobs():
    print("accountjobs")
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=11$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "accounts"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)


def HRjobs():
    print("HRjobs")
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=20$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId']
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "HR Recruitment"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)


def Salesjobs():
    print("Salesjobs")
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=32$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "Sales"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)



def marketingjobs():
    print("marketingjobs")
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=23$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "marketing"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)


def customerjobs():
    print("customerjobs")
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=25$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "customer service"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)


def legaljobs():
    print("legaljobs")
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=22$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "legal"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)



"""
def Teachingjobs():
    print("Teaching")
    for cou in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=34$&txtKeywords=&pSize=1000&pIndex='+str(cou)+''
        #contract_url=url.replace("{{token_id}}",''+str(assetId)+'')
        assets = requests.get(url=working_url)
        response = assets.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "Teaching Education"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)
"""
def Teachingjobs():
    print("running")
    records = mongo.db.emailStored.find()
    records = [serialize_doc(record) for record in records]
    print(records)
    for recor in records:
        print("241")
        if "cvParsedInfo" in recor:
            print("243")
            idd = recor['_id']
            data=recor['cvParsedInfo']
            s1 = json.dumps(data)
            parsed_json = (json.loads(s1))
            print(idd)
            ret = mongo.db.emailStored.update({"_id":idd} ,{
                            "$set":{
                                    "cvParsedInfo":parsed_json
                                  
                            }})
