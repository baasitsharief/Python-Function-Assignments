def cg_cal(n, cred, grade):
	totalpoints = 0
	totalcreds = 0
	for i in range(n):
		totalpoints += grade[i]*cred[i]
		totalcreds += cred[i]
	cgpa = float(totalpoints/totalcreds)
	if cgpa < 5 :
		return "sed_lyf"
	elif cgpa > 9 :
		return "GGWP"
	else : 
		return cgpa
