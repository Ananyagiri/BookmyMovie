from cinema import movie

print('Welcome to BookMyMovie')

while True:
	t_rows=int(input('enter the total number of rows'))
	t_cols=int(input('enter the total number of coloumns'))
	if t_rows>0 and t_cols>0:
		break
	else:
		print('enter a valid number')

mymovie=movie(t_rows,t_cols)

while True:
	print('1.show the seats\n 2.buy a ticket\n 3.statistics\n 4.showbooked ticket user info\n 5.exit')
	choice=int(input())
	if choice==1:
		mymovie.show_seats()
	elif choice==2:
		mymovie.buy_ticket()
	elif choice==3:
		mymovie.statistics()
	elif choice==4:
		mymovie.ticket_userinfo()
	elif choice==5:
		print('Thank you! visit again.')
		break
	else:
		print('enter a valid number')
		