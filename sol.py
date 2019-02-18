# superBido ;)
def power_num(num,powe):
	"""It takes two numbers and return the value of the first number multiply by itself powe number of time"""
	result = num ** powe
	return result

def Power_digit_sum(num,powe):
	"""it takes 2 number and returns the sum of digit of power_num function"""
	s_for_sum = str(power_num(num,powe))
	d_sum = 0
	for n in s_for_sum:
		d_sum += int(n)
	return d_sum

print Power_digit_sum(2,15)
#>>> 26
print Power_digit_sum(2,1000)
