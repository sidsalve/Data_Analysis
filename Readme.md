Assignments  
	-solution for 3rd Assignment
		Data Analysis
	Used Technology: Python3

	This assignment is to find out topper from student report
	Student report is generating randomly 
	like student id,gender,subject marks(english,maths,science,history and geography)
	average marks across all file subjects
	

	to compile the program 
		$python3 student_report_data_analysis.py 100
		
		here 100 is the number of students,this program will
		generate 100 records of students and write it into
		a .csv file , program ask you to save result into file ,
		then provide file name(without extension .csv)
		This file is then open by program and compute the
		result and give output 
	
	Eg:
		$python3 student_report_data_analysis.py 10
		
		output:
			---Inserting marks---
			---Inserting marks---
			---Inserting marks---	
			---Inserting marks---
			---Inserting marks---
			---Inserting marks---
			---Inserting marks---
			---Inserting marks---
			---Inserting marks---
			---Inserting marks---
			You want to create .csv file Y/N:Y	#enter Y to create file
			Enter file name:report 			#provide file name	
			report.csv File Creating.....
			File Created..
			------########------
			Overall Topper id:333,marks:75.0	#overall topper with id and marks
			Male Topper id:333,marks:75.0
			Female Topper id:346,marks:47.4
			--Subject Wise Topper--
			English Topper id:470,marks:84
			Math Topper id:333,marks:95
			Science Topper id:180,marks:80
			History Topper id:296,marks:97
			Geography Topper id:333,marks:92

		
	 
