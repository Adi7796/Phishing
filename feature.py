import socket

from pip import req
from urlunshort import is_shortened
from urllib2 import urlopen
import whois
import datetime
import urllib,re
import urllib2
import requests as req
import progressbar



positive='1'
negative='-1'
neutral='0'
currMonth=datetime.datetime.month
currYear=datetime.datetime.year



def getIpaddress(name):
    try:
        socket.gethostbyname(name)
        return positive
    except:
        return negative


def urlLenght(name):
    if len(name) > 54 :
        return negative
    elif len(name)>45 and len(name) <=54:
        return neutral
    else:
        return positive


def shortenUrl(name):
    if is_shortened(name) is True:
        return negative
    else:
        return positive

def atTherate(name):
    if '@' in name:
        return negative
    else:
        return positive

def doubleSlash(name):
    if '//' in name :
        return negative
    else:
        return positive

def dash(name):
    if '-' in name:
        return negative
    else:
        return positive


def subDomain(name):
    if name.count('.') > 2 :
        return negative
    elif name.count('.')>1:
        return neutral
    else:
        return positive


def port(name):
    if len(name.split(':')) ==1 :
        return positive
    name=name.split(':')[1]
    if name is not '80' or  name is not '443' :
        return negative
    else:
        return positive

def https(name):
    if 'https' in name or 'HTTPS' in name :
        return negative
    else:
        return positive

def CodeLength(name):
    code = urlopen("http://{}".format(name)).code
    if (code / 100 >=4):
        return negative
    else:
        return positive





def Domainregisterationlength(name):
    try:
        if name.updated_date == None:
            return negative
        else:
            return positive
    except:
        return negative

def ageOfDomain(name):
    try:

        date=name.expiration_date
        if type(date) is list:

            date=date[0]

        year=date.year
        month=date.month
        if year==currYear and month-currMonth >6 :
            return neutral
        elif year!=currYear :
            return positive
        elif year == currYear and month - currMonth<6:
            return negative
        else:
            return negative
    except:
        return negative

def dnsRecord(name):
    try:
        if name.dnssec == None :
            return negative
        else:
            return positive
    except:
        return negative


def whoisSection(name):
    return whois.whois(name)



def pageRank(name):

    xml = urllib.urlopen('http://data.alexa.com/data?cli=10&dat=s&url=%s' % name).read()

    try:
        rank = int(re.search(r'<POPULARITY[^>]*TEXT="(\d+)"', xml).groups()[0])
        return positive
    except Exception as e:
        return negative


def scrapping(data,url):
    dataset=[]
    for line in data:
        if '://' in line:
            line = line.split('://')
            line = line[1:]
            temp = []
            for x in line:
                dataset.append(x.split('"')[0])
    #print len(dataset)
    count = 0
    for x in dataset:
        if url in x:
            count += 1
    if count == 0 :
         return negative
    elif len(dataset)/count > 0.5 :
        return positive
    else:
        return negative


def linkInTags(data,url):
    dataset = []
    for line in data:
        if 'script' in line or 'meta' in line or 'link' in line:
            line = re.split('<script>|</script> | <meta>|</meta> | <link> | </link>', line)
            for x in line:
                if '://' in x:
                    temp = x.split('://')[1]
                    dataset.append(temp.split('/')[0])
                    # dataset.append(line)
    count = 0
    for x in dataset:
        if url in x:
            count+=1
    if count == 0 :
         return negative
    elif len(dataset)/count > 0.5 :
        return positive
    else:
        return negative



def readhtml(name):
    url='http://'+name
    usock = urllib2.urlopen(url)
    data = usock.read()
    dataset=data.split('\n')

    return dataset

def Submit(data):
    for line in data:
        if '<form ' in line and 'action' in line:
            test = line.split('action="')[1]
            test = test.split('"')[0]
            if len(test) > 1 :
                return positive
            else:
                return negative
    return positive

def Request(name):

    try:
        resp = req.get("http://{}".format(name), allow_redirects=False)

        if resp.status_code == 301 :
            return negative
        else:
            return positive
    except:
        return negative

def statisticalReport():
    return neutral

def googleIndex():
    return neutral

def ssl():
    return neutral

def linktoPage():
    return neutral

def datasetGenerator(line):
    temp=[]
    temp.append(getIpaddress(line))
    temp.append(urlLenght(line))
    temp.append(shortenUrl(line))
    temp.append(atTherate(line))
    temp.append(doubleSlash(line))
    temp.append(dash(line))
    temp.append(subDomain(line))
    temp.append(port(line))
    temp.append(https(line))
    temp.append(CodeLength(line))
    #whoisTemp=whoisSection(line)
    #temp.append(Domainregisterationlength(whoisTemp))
    #temp.append(ageOfDomain(whoisTemp))
    #temp.append(dnsRecord(whoisTemp))
    temp.append(pageRank(line))
    htmlData=readhtml(line)
    temp.append(scrapping(htmlData,line.split('.')[0]))
    temp.append(linkInTags(htmlData,line.split('.')[0]))
    temp.append(Submit(htmlData))
    temp.append(Request(line))
    #temp.append(ssl())
    #temp.append(linktoPage())
    #temp.append(googleIndex())
    #temp.append(statisticalReport())

    return ','.join(temp)

if __name__ == '__main__':
    dataset=[]
    f=open('data_set.txt','r')
    test=f.readlines()
    limit=len(test)
    bar = progressbar.ProgressBar()
    for i in bar(range(len(test))):
        try:
            feature=datasetGenerator(test[i].split('\n')[0])
        except:
            continue
        if i <= limit/2 :
            feature= feature+',-1\n'
        else:
            feature = feature +',1\n'
        dataset.append(feature)

    f=open('feature2.txt','w')
    for x in dataset:
        f.write(x)


