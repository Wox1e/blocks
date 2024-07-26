from django import template
import datetime
import pytz

register = template.Library()

@register.simple_tag
def get_time_difference(posting_time):
    current_time = datetime.datetime.now(pytz.utc)
    

    duration = current_time - posting_time
    duration_in_s = duration.total_seconds()

    years = int(divmod(duration_in_s, 31536000)[0])
    days  = int(duration.days)
    hours = int(divmod(duration_in_s, 3600)[0])  
    minutes = int(divmod(duration_in_s, 60)[0]) 

    if years > 0:
        return f"{years}y"
    elif days > 0:
        return f"{days}d"
    elif hours > 0:
        return f"{hours}h"
    elif minutes > 0:
        return f"{minutes}min"
    else:
        return "Just now"
