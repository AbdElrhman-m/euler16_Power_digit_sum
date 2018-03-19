# superBido ;)
def power_num(num,powe):
	result = num ** powe
	return result

def Power_digit_split(num,powe):
	result = power_num(num,powe)
	result_str = str(result)
	ls_of_re =[]
	while len(result_str) > 0:
		x = result_str[:1]
		
		ls_of_re.append(int(x))
		result_str = result_str[1:]
	return ls_of_re
def Power_digit_sum(num,powe):
	ls_for_sum = Power_digit_split(num,powe)
	d_sum = 0
	for n in ls_for_sum:
		d_sum += n
	return d_sum	

print Power_digit_sum(2,15)
#>>> 26
print Power_digit_sum(2,1000)
