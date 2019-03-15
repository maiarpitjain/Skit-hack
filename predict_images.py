#ch=int(input("Enter number of students whose data would you want to add in your database"))
def set_attendence_in_csv(p_employee):
    # Writing to an excel 
    # sheet using Python 
    import xlwt 
    from xlwt import Workbook 

    # Workbook is created 
    wb = Workbook() 

    # add_sheet is used to create sheet. 
    sheet1 = wb.add_sheet('Sheet 1') 
    lentgh=len(p_employee)

    for i in range(lentgh):
        sheet1.write(i, 0, p_employee[i]) 
    
    wb.save('result.xls') 

def run_attendance():
        
    def get_student_names():
        l_student=[]
        import csv
        count=0
        with open('example2.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if count%2==0:
                    l_student.append(row[0])
                count=count+1
            return l_student

    student_names=get_student_names()
    import create_100_images

    
    p_employees=create_100_images.predict_images(len(student_names),student_names)
    set_attendence_in_csv(p_employees)
    print(p_employees)

#run_attendance()
