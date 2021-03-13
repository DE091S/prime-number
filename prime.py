#запрашиваем число на проверку
x = int(input("Chislo:",))
#провеяем число на делимость 
for i in range(2, x):
	if x%i==0:
		print("not")
		break
	else:
		continue

print("prime")