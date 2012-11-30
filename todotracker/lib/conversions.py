import datetime
from dateutil import tz

def convert_datetime_to_localtime(utcdate=datetime.datetime.utcnow()):
    local_tz = tz.tzlocal()
    utc_tz = tz.gettz('UTC')
    newdatetime = utcdate.replace(tzinfo=utc_tz)
    return newdatetime.astimezone(local_tz)
