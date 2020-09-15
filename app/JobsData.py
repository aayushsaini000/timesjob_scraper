
import requests
from app.util import serialize_doc
from app import mongo
#import datetime
import dateutil.parser
import pymongo
import json

#------------------------------------Jobs functions---------------------------------------#
#it
#acpagecountnt
#HR Recruitment
#Sales
#marketing
#customer
#leagal
#teaching
#-----------------------------------------------------------------------------------------#



#-----Note*-> The only reason for define all function seperate we can fetch data for a specific job.
#          -> Also its a fast way for fetch all jobs data parallely for loop on urls will take much long to pull data.

def ItJobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=35$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
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
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)


def accountjobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=11$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
        jobs = response['jobsList']
        for job in jobs:
            companyName = job['companyName']
            Location = job['Location']
            adId = job['adId'] 
            expiry = job['expiry']
            date_time = dateutil.parser.parse(expiry)
            job_object = dict(job)
            job_object['expiry'] = date_time
            job_object['catg_key'] = "accountjobs"
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)


def HRjobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=20$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
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
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)


def Salesjobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=32$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
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
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)



def marketingjobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=23$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
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
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)


def customerjobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=25$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
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
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)


def legaljobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=22$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
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
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)



def Teachingjobs():
    for pagecount in range(0,500):
        working_url = 'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=34$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        JobRespData = requests.get(url=working_url)
        response = JobRespData.json()
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
            UpdatingData = mongo.db.timesjobs_data.update({"companyName":companyName,"Location":Location,"adId":adId},{"$set":dict(job_object)},upsert=True)






























#------------->Dummy data not deleted may be usefull later<----------------#


'''
urls = ['https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=35$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=11$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=20$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=32$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=23$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=25$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=22$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=34$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''
        ]
        #'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=22$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+'',
        #'https://jobbuzz.timesjobs.com/jobbuzz/loadMoreJobs.json?companyIds=&locationnames=&aosValues=&sortby=I&from=filter&faids=34$&txtKeywords=&pSize=1000&pIndex='+str(pagecount)+''

'''

"""
client = MongoClient("mongodb+srv://root:0vXPeLcPxME40Ydv@cluster0-v8o7t.mongodb.net/jobs_scraper?retryWrites=true&w=majority")
temp_db = client.jobs_scraper
"""


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
        UpdatingData = mongo.db.naukrijobs_data.update({"title":title,"staticCompanyName":staticCompanyName},{"$set":dict(job_object)},upsert=True)
'''

"""
def naukri_date_change():
    print("running")
    mycryptoheroes_records = mongo.db.timesjobs_data.find({})
    mycryptoheroes_records = [serialize_doc(mycryptoheroes_record) for mycryptoheroes_record in mycryptoheroes_records]
    print(len(mycryptoheroes_records))
    for mycryptoheroes_record in mycryptoheroes_records:
        key = mycryptoheroes_record['keySkills']
        for ke in key:
            print(ke)
"""