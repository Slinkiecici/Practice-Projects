from plyer import notification
import datetime

notification.notify(
            #title of the notification,
            title = format(datetime.date.today()),
            message = "You wrote this! Be proud.",
            app_icon = "signofhealth.ico",
            )