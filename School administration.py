import csv

def write_into_csv(student_list):
    

    with open('student_information.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Phone_no","Email_ID"])
            
            
        writer.writerow(student_list)





if __name__=='__main__':
    condition=True
   
    
    
    while(condition==True):
        
        student_name=input("Enter the student's name: ")
        student_age=input("Enter the student's age: ")
        student_phone_no=input("Enter the student's phone number: ")
        student_email_id=input("Enter the student's email id: ")
    
    
        student_list=[student_name,student_age,student_phone_no,student_email_id]
        print(student_list)
    
    
        
    
        
        
        
        choice_check=input("Type yes if the entered information is correct and no if not: ")
        if choice_check=='yes':
            
            write_into_csv(student_list)
            condition_check=input("do you want to make another entry. Respond with y/n: ")
            if condition_check=='y':
                condition=True
            elif condition_check=='n':
                condition=False
        elif choice_check=='no':
            print("\nPlease re-enter the values")
        