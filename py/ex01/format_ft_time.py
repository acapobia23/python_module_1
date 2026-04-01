import time
import datetime

second = round((time.time()), 4)
date = datetime.datetime.now()
print("Seconds since January 1, 1970:", second, "or", f"{second:.2e}", " in scientific notation")
print(date.strftime("%b %d %Y"))