
import urllib2
import smtplib
import time
import datetime
from apscheduler.scheduler import Scheduler


def function1():
    try:
        f = urllib2.urlopen('http://www.pes.edu/results/7-sem')
        data=f.read()
        if data!="":
            if "Results" in data:
                FROMADDR = "trialsample7@gmail.com"
                LOGIN = FROMADDR
                PASSWORD = "sample123"
                TOADDRS = ["pavan0591@gmail.com"]
                SUBJECT = "Results have been announced . Please check!"

                msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (FROMADDR, ", ".join(TOADDRS), SUBJECT))
                msg += "\nAll the best . Haraye Namaha\r\n"

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.set_debuglevel(1)
                server.ehlo()
                server.starttls()
                server.login(LOGIN, PASSWORD)
                server.sendmail(FROMADDR, TOADDRS, msg)
                server.quit()
            #print "Mail has been sent."
    except:
        print "Not yet out!"
            
today = datetime.date.today()
sched = Scheduler()
sched.start()
day = today.day
month = today.month
sched.add_cron_job(function1, month='1', day='10', hour='10-15',minute='0,5,9,14,18,21,23,28,31,35,42,44,47,52,53,56,58')
    
