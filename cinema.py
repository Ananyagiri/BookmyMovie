from booking import seating

class movie:

	def __init__(self,rows,cols):
		self.rows=rows
		self.cols=cols
		self.records={}
		self.current_income=0
		self.total_income=0
		self.purchased=0
		for i in range(1,self.rows+1):
			for j in range(1,self.cols+1):
				self.records[(i*100)+j]=seating()
				self.total_income=self.total_income+movie.price(self.rows,self.cols,i,j)

	def show_seats(self):
		print(' ',end=' ')
		for m in range(1,self.cols+1):
			print(m,end=' ')
		print()
		for i in range(1,self.rows+1):
			print(i,end=' ')
			for j in range(1,self.cols+1):
				if self.records[(i*100)+j].vacant==True:
					print('S',end=' ')
				else:
					print('B',end=' ')
			print()		

	@staticmethod
	def price(R,C,nr,nc):
		if R*C<=60:
			return 10
		elif nr<= R//2:
			return 10
		else:
			return 8


	def buy_ticket(self):
		rn=int(input("enter the row number"))
		cn=int(input("enter the coloumn number"))
		if rn>0 and rn<=self.rows and cn>0 and cn<=self.cols:
			pass
		else:
			print('sorry! invalid input, try again.')
			return movie.buy_ticket(self)

		if self.records[(rn*100)+cn].vacant==False:
			print('the seat is already booked')
		else:
			print('the cost',movie.price(self.rows,self.cols,rn,cn),'$')
			print('press 1 to continue')
			x=int(input())
			if x==1:
				self.records[(rn*100)+cn].book_seat(rn,cn)
				self.current_income=self.current_income+movie.price(self.rows,self.cols,rn,cn)
				self.purchased=self.purchased+1
				print('booked successfully')
			else:
				print('you are redirected to the menu')
				return			


		    
	def statistics(self):
		print('number of purchased tickets:', self.purchased)
		print('percentage:',(self.purchased/(self.rows*self.cols))*100,'%')
		print('current income:',self.current_income,'$')
		print('total income:',self.total_income,'$')

	def ticket_userinfo(self):
		yr=int(input('enter the row number'))
		yc=int(input('enter the coloumn number'))
		if yr>0 and yr<=self.rows and yc>0 and yc<=self.cols:
			pass
		else:
			print('invalid input, try again.')
			return movie.ticket_userinfo(self)

		if self.records[(yr*100)+yc].vacant==False:
			info=self.records[(yr*100)+yc].record[(yr*100)+yc].get_info()
			print('name:',info['name'])
			print('gender:',info['gender'])
			print('age:',info['age'])
			print('contact no:',info['phone_no'])
		else:
			print('this seat is vacant.')




                    