
import requests
from app.util import serialize_doc
#from app.config import chainguardians_api_endpoint,chainguardians_le_api_endpoint
from app import mongo
import datetime



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
            job_object = dict(job)
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
            job_object = dict(job)
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
            job_object = dict(job)
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
            job_object = dict(job)
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
            job_object = dict(job)
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
            job_object = dict(job)
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
            job_object = dict(job)
            job_object['catg_key'] = "legal"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)


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
            job_object = dict(job)
            job_object['catg_key'] = "Teaching Education"
            checking = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)
        print("============================================================already exists=============================================",cou)
