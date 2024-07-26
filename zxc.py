from datetime import datetime
then = datetime(2012, 3, 5, 23, 8, 15)        # Random date in the past
now  = datetime.now()                         # Now
duration = now - then 
                        # For build-in functions
print(duration)