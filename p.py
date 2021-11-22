import argparse
def config(d,device_name):
	print(device_name)

	
#I am doing the changes for the first time in github reposirtroy
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--device_name', dest='device_name',
                    help='device_name')


parser.add_argument('-s', '--store', dest='store',
                    help='Store a simple value')

parser.add_argument('-c', '--store_const', dest='store_const',
                    help='Store a constant value')

parser.add_argument('-d', '--constant', dest='constant',help='constant value')
parser.add_argument('-f', '--fixed', dest='fixed',help='fixed value')


results = parser.parse_args()
key1=['simple_value','constant_value']
key2=['store_true1','boolean_switch2']
# d=dict(zip(key1,list1))
if results.device_name=='pk5k':
	list1=[results.store,results.store_const]
	d=dict(zip(key1,list1))
	print(d)
	config(d,results.device_name)
else:

	list2=[results.constant,results.fixed]
	d1=dict(zip(key2,list2))
	print(d1)
	config(d1,results.device_name)


