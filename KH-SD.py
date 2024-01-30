import random
#import queue


landingrate = 12 
takeoffrate = 10 
landingtime = 2 
takeofftime = 3 


landingqueue = [] 
takeoffqueue = [] 


totaltime = 60 
runway = 0 
runwaytime = 0 
landingcount = 0 
takeoffcount = 0 
landingwait = 0 
takeoffwait = 0 
landinglength = 0 
takeofflength = 0 

#main
for time in range(totaltime):
    
    landingprob = random.random()
    takeoffprob = random.random()
    
    if landingprob < landingrate / 60:
        landingqueue.insert(0, time)
    if takeoffprob < takeoffrate / 60:
        takeoffqueue.insert(0, time)
    
    if runway == 0:
        if landingqueue:
            landingtime = landingqueue.pop(-1)
            landingcount += 1
            landingwait += time - landingtime
            runway = 1
            runwaytime = landingtime

            landinglength += 1
        elif takeoffqueue:
            takeofftime = takeoffqueue.pop(-1)
            takeoffcount += 1
            takeoffwait += time - takeofftime
            runway = 2
            runwaytime = takeofftime

            takeofflength += 1
    else:
        runwaytime -= 1
        if runwaytime == 0:
            runway = 0

average_landing_length = landinglength / totaltime
average_takeoff_length = takeofflength / totaltime
try:

    average_landing_wait = landingwait / landingcount
except:
    average_landing_wait = 0
try:

    average_takeoff_wait = takeoffwait / takeoffcount
except:
    average_takeoff_wait = 0

print("نتایج شبیه سازی فرودگاه برای یک ساعت:")
print("تعداد هواپیماهایی که فرود آمدند:", landingcount)
print("تعداد هواپیماهایی که برخاستند:", takeoffcount)
print("میانگین طول صف فرود:", average_landing_length)
print("میانگین طول صف برخاست:", average_takeoff_length)
print("میانگین زمان انتظار برای فرود:", average_landing_wait)
print("میانگین زمان انتظار برای برخاست:", average_takeoff_wait)
