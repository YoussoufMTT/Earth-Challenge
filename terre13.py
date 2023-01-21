import sys

from datetime import datetime

heure = sys.argv[1]

H = datetime.strptime(heure, '%I:%M%p')

new_heure = H.strftime('%H:%M')

print(new_heure)