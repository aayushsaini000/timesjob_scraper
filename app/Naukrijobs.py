import requests
from app.util import serialize_doc
from app import mongo
#import datetime
#import dateutil.parser
import pymongo
import json


urls = [
        'https://www.naukri.com/jobapi/v3/search?noOfResults=500&urlType=search_by_keyword&searchType=adv&keyword=accounting&pageNo={{pagenumber}}&sort=r&xt=catsrch&functionAreaId=1&seoKey=accounting-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=500&urlType=search_by_keyword&searchType=adv&keyword=information%20technology&pageNo={{pagenumber}}&sort=r&xt=catsrch&functionAreaId=24%2527&seoKey=information-technology-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=500&urlType=search_by_keyword&searchType=adv&keyword=bank&pageNo={{pagenumber}}&sort=r&xt=catsrch&functionAreaId=6&seoKey=bank-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=500&urlType=search_by_keyword&searchType=adv&keyword=hr&pageNo={{pagenumber}}&sort=r&xt=catsrch&functionAreaId=12&seoKey=hr-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=500&urlType=search_by_keyword&searchType=adv&keyword=marketing&pageNo={{pagenumber}}&sort=r&xt=catsrch&functionAreaId=15&seoKey=marketing-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=500&urlType=search_by_keyword&searchType=adv&keyword=sales&pageNo={{pagenumber}}&sort=r&xt=catsrch&functionAreaId=22&seoKey=sales-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=teaching&pageNo={{pagenumber}}&sort=r&xt=catsrch&functionAreaId=36&seoKey=teaching-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=medical&pageNo={{pagenumber}}&sort=r&xt=catsrch&industryId=20&seoKey=medical-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=recruitment&pageNo={{pagenumber}}&sort=r&xt=catsrch&industryId=34&seoKey=recruitment-jobs-{{pagenumber}}&src=jobsearchDesk&latLong=',
        'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=consultant&pageNo={{pagenumber}}&sort=r&xt=catsrch&industryId=52&seoKey=consultant-jobs-{{pagenumber}}&src=jobsearchDesk&latLong='
        ]

headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'clientid':'d3skt0p',
    'appid':'109',
    'systemid':'109',
    }



def NaukriJobs():
    print("running")
    count = 1
    for url in urls:
        try:
            for latestpage in range(1,100):
                workingurl = url.replace("{{pagenumber}}",''+str(latestpage)+'')
                respon = requests.get(url=workingurl,headers=headers)
                res = respon.json()
                JobDetails = res['jobDetails']
                for job in JobDetails:
                    try:
                        DataValidate(job=job,count=count)
                    except Exception:
                        pass
        except Exception:
            pass
        count = count + 1
        

def DataValidate(job=None,count=None):
    if job is not None:
        jobId = job['jobId']
        companyId = job['companyId']
        if count == 1:
            job['catg_key'] = "accountjobs"
        if count == 2:
            job['catg_key'] = "software development"
        if count == 3:
            job['catg_key'] = "bank jobs"
        if count == 4:
            job['catg_key'] = "HR Recruitment"
        if count == 5:
            job['catg_key'] = "marketing"
        if count == 6:
            job['catg_key'] = "Sales"
        if count == 7:
            job['catg_key'] = "Teaching Education"
        if count == 8:
            job['catg_key'] = "Medical"
        if count == 9:
            job['catg_key'] = "HR Recruitment"
        if count == 10:
            job['catg_key'] = "consultant jobs"
        UpdatingData = mongo.db.NaukriJobsData.update({"jobId":jobId,"companyId":companyId},{"$set":dict(job)},upsert=True)
    else:
        pass



#--------------------Dummy links------------------#

#'https://www.naukri.com/information-technology-jobs?xt=catsrch&qf[]=24',
#'https://www.naukri.com/accounting-jobs?xt=catsrch&qf[]=1',
#'https://www.naukri.com/bank-jobs?xt=catsrch&qf[]=6',#No
#'https://www.naukri.com/hr-jobs?xt=catsrch&qf[]=12',
#'https://www.naukri.com/application-programming-jobs?xt=catsrch&qf[]=24.01',#No
#'https://www.naukri.com/bpo-jobs?xt=catsrch&qf[]=8',#No
#'https://www.naukri.com/marketing-jobs?xt=catsrch&qf[]=15',
#'https://www.naukri.com/pharma-jobs?xt=catsrch&qf[]=16',#No
#'https://www.naukri.com/maintenance-jobs?xt=catsrch&qf[]=19',#No
#'https://www.naukri.com/sales-jobs?xt=catsrch&qf[]=22',
#'https://www.naukri.com/teaching-jobs?xt=catsrch&qf[]=36',
#'https://www.naukri.com/bpo-jobs?xt=catsrch&qi[]=7',#No
#'https://www.naukri.com/bank-jobs?xt=catsrch&qi[]=14',#No
#'https://www.naukri.com/engineering-jobs?xt=catsrch&qi[]=12',#No
#'https://www.naukri.com/teaching-jobs?xt=catsrch&qi[]=26',#No
#'https://www.naukri.com/information-technology-jobs?xt=catsrch&qi[]=25',#No
#'https://www.naukri.com/medical-jobs?xt=catsrch&qi[]=20',
#'https://www.naukri.com/recruitment-jobs?xt=catsrch&qi[]=34',
#'https://www.naukri.com/consultant-jobs?xt=catsrch&qi[]=52'
