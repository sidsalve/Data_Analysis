import sys
import csv
import random

s_id=[]
s_gen=[]
eng=[]
math=[]
sci=[]
hist=[]
geo=[]
avg=[]
gen_l=['M','F']	
main=[]
def write_in_csv():
	chk=input("Do You want to create .csv file Y/N:")
	if chk=='Y' or chk=='y':
		filename=input("Enter file name:")
		fn=filename+".csv"
		print(fn+" File Creating.....")
		file1=open(fn,'w')
		for i in range(int(sys.argv[1])):
			writer=csv.writer(file1)
			writer.writerow((s_id[i],s_gen[i],eng[i],math[i],sci[i],hist[i],geo[i],avg[i]))
		print("File Created..")
		file1.close()
		return fn
	else:
		print("To see result please create .csv file")
		exit(0)	

def read_csv(fn):
	max1=0
	ind1=0
	max2=0
	ind2=0
	max3=0
	ind3=0
	sub1_max=0
	ind4=0
	sub2_max=0
	ind5=0
	sub3_max=0
	ind6=0
	sub4_max=0
	ind7=0
	sub5_max=0
	ind8=0	
	csv.register_dialect('myDialect',delimiter=',')
	with open(fn,'r') as f:
		reader=csv.reader(f,dialect='myDialect')
		for row in reader:
			if float(row[7])>float(max1):
				max1=row[7]
				ind1=row[0]
			if row[1]=="M":
				if float(row[7])>float(max2):
					max2=row[7]
					ind2=row[0]
			if row[1]=="F":
				if float(row[7])>float(max3):
					max3=row[7]
					ind3=row[0]
			if float(row[2])>float(sub1_max):
				sub1_max=row[2]
				ind4=row[0]
			if float(row[3])>float(sub2_max):
				sub2_max=row[3]
				ind5=row[0]
			if float(row[4])>float(sub3_max):
				sub3_max=row[4]
				ind6=row[0]
			if float(row[5])>float(sub4_max):
				sub4_max=row[5]
				ind7=row[0]
			if float(row[6])>float(sub5_max):
				sub5_max=row[6]
				ind8=row[0]
		f.close()
	print("------########------")				
	print("Overall Topper id:{0},marks:{1}".format(ind1,max1))
	print("Male Topper id:{0},marks:{1}".format(ind2,max2))
	print("Female Topper id:{0},marks:{1}".format(ind3,max3))
	print("--Subject Wise Topper--")
	print("English Topper id:{0},marks:{1}".format(ind4,sub1_max))
	print("Math Topper id:{0},marks:{1}".format(ind5,sub2_max))
	print("Science Topper id:{0},marks:{1}".format(ind6,sub3_max))
	print("History Topper id:{0},marks:{1}".format(ind7,sub4_max))
	print("Geography Topper id:{0},marks:{1}".format(ind8,sub5_max))


if __name__=="__main__":
	arg=len(sys.argv)
	if(arg<2 or arg>2):
		print("Warrning: check parameter")
		print("for help type after program name '-h' or '--help' ")
	elif sys.argv[1]=="-h" or sys.argv[1]=="--help":
		print("please give any number after program name as argument")
		print("eg: program_name 100")	
	else:
		for i in range(int(sys.argv[1])):
			def id():
				id1=random.randint(100,500)
				if id1 in s_id:
					#print("WARNING **:Enter again Id Exist")
					id()
				else:
					s_id.append(id1)
			id()
			gen1=random.choice(gen_l)
			s_gen.append(gen1)
			#print("---Inserting marks---")
			mark=random.randint(35,100)	
			eng.append(mark)
			mark=random.randint(35,100)	
			math.append(mark)
			mark=random.randint(35,100)	
			sci.append(mark)
			mark=random.randint(35,100)		
			hist.append(mark)
			mark=random.randint(35,100)	
			geo.append(mark)		
		for i in range(len(s_id)):
			s=float((eng[i]+math[i]+sci[i]+hist[i]+geo[i])/5)
			avg.append(s)
		fn=write_in_csv()
		#calculate_result()
		read_csv(fn)
	
		
