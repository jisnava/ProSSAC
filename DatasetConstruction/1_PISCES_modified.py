#From PICSES output this code will extract only PDB ID's needed for further processing
#Output from Dunbrack copy pasted int a txt file
#This includes PDB_IB without chain name
with open('PISCES_1.txt','r') as f, open('PISCES_11_40ID_ID_only.txt', 'w') as f2:
	lines1=f.readlines()
	for j in (lines1):
		currentline=j.split(' ')
		#print(currentline[0])
		#print("\n")
		if j[4:5] =='A':
			f2.write(j[0:4]+'\n')
f2.close()
