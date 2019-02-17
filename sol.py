# superBido ;)
def power_num(num,powe):
	result = num ** powe
	return result

def Power_digit_sum(num,powe):
	s_for_sum = str(power_num(num,powe))
	d_sum = 0
	for n in s_for_sum:
		d_sum += int(n)
	return d_sum

print Power_digit_sum(2,15)
#>>> 26
print Power_digit_sum(2,1000)
