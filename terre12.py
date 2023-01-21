import sys

from datetime import datetime

heure = sys.argv[1]

H = datetime.strptime(heure, "%H:%M")

new_heure = H.strftime("%I:%M %p")

print(new_heure) 