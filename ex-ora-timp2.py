from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print(current_year)
print(current_month)
print(current_day)

# Substitutia stringurilor
from datetime import datetime
new = datetime.now()

print("%s-%s-%s" % (new.year, new.mont, new.day))