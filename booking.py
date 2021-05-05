from show_user import userinfo


class seating:
	record={}
	def __init__(self):
		self.vacant=True

	def book_seat(self,br,bc):
		seating.record[(br*100)+bc]=userinfo()
		seating.record[(br*100)+bc].set_info()
		self.vacant=False




