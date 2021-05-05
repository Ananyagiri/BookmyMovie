class userinfo:

	def __init__(self):
		self.user={'name':None,'gender':None,'age':None,'phone_no':None}

	def set_info(self):
		print('enter your name')
		name=input()
		self.user['name']=name

		while True:
			print('choose your gender:\n 1.male\n 2.female\n 3.other')
			no=int(input())
			if no==1:
				self.user['gender']='male'
				break
			elif no==2:
				self.user['gender']='female'
				break
			elif no==3:
				self.user['gender']='other'
				break
			else:
				print('choose a valid number')

		print('enter your age')
		while True:
			age=int(input())
			if age>0:
				self.user['age']=age
				break
			else:
				print('please put a valid input')

		print('enter your mobile number')
		while True:
			mobile=int(input())
			if mobile>999999999 and mobile<10000000000:
				self.user['phone_no']=mobile
				break
			else:
				print('please check the number')

	def get_info(self):
		return self.user