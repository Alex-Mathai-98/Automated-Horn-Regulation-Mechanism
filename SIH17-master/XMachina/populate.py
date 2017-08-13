import csv,os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'XMachina.settings')
django.setup()

from main.models import Indices
from main.models import SensitivePoint


file = open('cmbtr.csv', 'r')
cow = csv.reader(file)
row=list(cow)
for data in row:
	print data     
			

		