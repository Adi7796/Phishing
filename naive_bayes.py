import math


def calculateProbabilty(tupple, mean ,std):
    temp=[]
    tupple=tupple.split(',')[:-1]
    mean=mean.split(',')
    std=std.split(',')
    prob=1
    for i in range(len(tupple)):
        try:
            exp=math.exp(-(math.pow(float(tupple[i]) - float(mean[i]),2)/float( 2*math.pow(float(std[i]),2) ) ) )
        except :
            continue
        pdf=(1/(math.sqrt(2*math.pi)  * float(std[i]) ))*exp
        prob=prob*pdf
    return prob

def squareRoot(dataset):
    temp=[]
    dataset=dataset.split(',')
    for x in dataset:
        temp.append(str(round(math.sqrt(float(x)),4)))
    return ','.join(temp)


def stdev(dataset, mean):
    test = initiate(len(dataset[0].split(',')))
    # print mean
    # print len(mean)
    mean = mean.split(',')
    # print len(mean)
    length = len(dataset)
    for i in range(len(dataset)):
        temp = []
        for j in range(len(mean)):
            # print dataset[i].split(",")[j]
            temp.append(str(pow(float(dataset[i].split(',')[j]) - float(mean[j]), 2) / float(length)))
        temp = ','.join(temp)
        test = addition(test, temp)
    test = squareRoot(test)
    return test

def division(dataset,dividend):
    temp=[]
    dataset=dataset.split(',')
    for i in range(len(dataset)):
        temp.append(str(round(float(dataset[i])/dividend,4)))
    return ','.join(temp)



def addition(x,mean):
    test=[]
    mean=mean.split(',')
    x=x.split(',')
    #print len(mean),len(x)
    for i  in range(len(mean)):
        #print x[i],mean[i]
        test.append(str(float(x[i])+float(mean[i])))
    return ','.join(test)


def initiate(lenght):
    temp=[]
    #print lenght
    for i in range(lenght):
        temp.append('0')
    return ','.join(temp)

def findmean(dataset):
    #print dataset
    #print len(dataset[0].split(','))
    mean=initiate(len(dataset[0].split(','))-1)
    for i in range(len(dataset)):
        mean=addition(dataset[i][:-1],mean)
    mean=division(mean,len(dataset))
    return mean




def splitDataset(dataset,ratio):
    temp=[]
    test=[]
    for i in range(len(dataset)):
        if i < len(dataset)*ratio:
            temp.append(dataset[i])
        else:
            test.append(dataset[i])
    return temp,test

def phish(dataset):
    phish=[]
    good=[]
    for x in dataset:
        if x.split(',')[-1].split('\n')[0] == '1':
            phish.append(x)
        else:
            good.append(x)
    return phish,good



if __name__ == '__main__':
    f=open('dataset2.txt','r')
    dataset=f.readlines()
    f.close()
    dataset,test=splitDataset(dataset,0.67)
    #print len(dataset)
    #print len(test)
    phis,good = phish(dataset)
    phishmean =findmean(phis)
    goodmean=findmean(good)
    print phishmean
    print goodmean

    phishstd=stdev(phis,phishmean)
    goodstd=stdev(good,goodmean)
    print phishstd
    print goodstd



    #testing


    correct=0

    for x in test:
        phishprob=calculateProbabilty(x,phishmean,phishstd)

        goodprob=calculateProbabilty(x,goodmean,goodstd)

        if phishprob<goodprob:
            if x.split(',')[-1].split('\n')[0]  == '-1':
                correct+=1
            #print "phishing"
        else:
            if x.split(',')[-1].split('\n')[0]  == '1':
                correct+=1
#print "not phishing"

    print correct
    print len(test)
    accuracy =  float(correct)/float(len(test))

    print accuracy

