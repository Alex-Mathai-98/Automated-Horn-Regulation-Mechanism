import csv,os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'XMachina.settings')
django.setup()

from main.models import Indices
from main.models import SensitivePoint



"""def populate1():
	count = 0
	for data in row:
		count+=1
		if count>11:
			break
		elif count>1:
			
			
			for j in range (4):
				s = StockInfo()
				s.name=data[0]
				s.round_no=(1+j)
				s.left=0
				s.priceinitial=float(data[1+j])
				s.pricefinal=float(data[1+j])
				s.exchange_rate=float(data[5+j])
				
				
				if(s.exchange_rate>2):

					s.stocktype=False
					
				else:
					s.stocktype=True 
				s.save()"""

def populate2():

	#count = 0
	file = open('cmbtr.csv', 'r')
	row = csv.reader(file)
	for data in row:
				print data[1]     
			

		