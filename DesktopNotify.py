from plyer import notification
import datetime
import schedule
import time

now = datetime.datetime.now()
start_work = now.replace(hour=8, minute=30, second=0, microsecond=0)

def work_start():
    notification.notify(
            #title of the notification,
            title = format(datetime.date.today()),
            message = "Time to start work!",
            app_icon = "signofhealth.ico",
            )
def break_time():
    notification.notify(
            #title of the notification,
            title = format(datetime.date.today()),
            message = "Time to relax a bit!",
            app_icon = "signofhealth.ico",
            ) 

schedule.every().day.at("08:30").do(work_start)
schedule.every().day.at("09:22").do(break_time)
schedule.every().day.at("09:39").do(work_start)
schedule.every().day.at("10:31").do(break_time)
schedule.every().day.at("10:48").do(work_start)
schedule.every().day.at("11:40").do(break_time)
schedule.every().day.at("11:57").do(work_start)
schedule.every().day.at("12:49").do(break_time)
schedule.every().day.at("13:06").do(work_start)
schedule.every().day.at("13:58").do(break_time)
schedule.every().day.at("14:15").do(work_start)
schedule.every().day.at("15:07").do(break_time)
schedule.every().day.at("15:24").do(work_start)
schedule.every().day.at("16:16").do(break_time)
schedule.every().day.at("16:33").do(work_start)
schedule.every().day.at("17:25").do(break_time)

while True:
    schedule.run_pending()
    time.sleep(1)