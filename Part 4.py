# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# The links for the references are in bottom of this code.
# Student ID: 20210860 / w1954000
# Date: 19.11.2022






#Creating and Initializng Variables
pass_c = 0    #to store the pass credits of students
defer_c = 0    #to store the defer credits of students
fail_c = 0     #to store the fail credits of students
total = 0        #to calculate the total addition of the marks to check whether its valid or not
cont= 'y'or'q' #to continue or end the program
student_count= 0    #to increase the student count
progress_student_count = 0     # To increase the count of the student who got progress
retriever_student_count = 0    # To increase the count of the student who got retriever
trailer_student_count = 0      # To increase the count of the student who got trailer
exclude_student_count  = 0     # To increase the count of the student who got exclude
progress_list = [] #to store the progress marks of students
trailer_list=[]    #to store the trailer marks of students
retriever_list=[]   #to store the retriever marks of students
exclude_list=[]      #to store the exclude marks of students
progress_string_list = '' #To convert the progress list into string and store into the dictionary 
trailer_string_list =''    #To convert the trailer list into string and store into the dictionary 
retriever_string_list=''   #To convert the retriever list into string and store into the dictionary 
exclude_string_list=''     #To convert the exclude list into string and store into the dictionary 
student_dict={} #to create the student dictionary
student_id='' #To store the student ID's

def Histogram():
    """ To print the histogram based on the student count and the outcomes of the number of the students who got the particular grade """
    print("Histogram")
    print("Progress",progress_student_count ,":","*" * progress_student_count)
    print("Trailer",trailer_student_count ,":","*" * trailer_student_count)
    print("Retreiver",retriever_student_count ,":", "*" * retriever_student_count)
    print("Excluded",trailer_student_count ,":","*" * exclude_student_count)

    print(student_count,"outcomes in total.")
    return

print("-----------------Students Outcome Calculation Program------------------------")



#Process
while  cont=="y" :
    student_id = input("Enter Student ID :  ")
    while True:
        try:
            pass_c = int(input("Enter your credits at PASS : "))
            if (pass_c<0 or pass_c>120) or pass_c%20!=0:      #to check whether the input is in the valid range    
                print("Out of range")
                continue
            
            else:
                while True:
                    defer_c = int(input("Enter your credits at DEFER : "))
                    if (defer_c<0 or defer_c>120) or defer_c%20!=0:
                        print("Out of range")
                        continue
                    else:
                        break
                while True:
                    fail_c = int(input("Enter your credits at FAIL : "))
                    if (fail_c<0 or fail_c>120) or fail_c%20!=0:
                        print("Out of range")
                        continue
                    else:
                        break
    
            total = pass_c + defer_c + fail_c   #To check whether the addition of the marks is valid
            if total<120 or  total > 120:
                print("Total Incorrect")
            elif pass_c == 120 and defer_c == 0 and fail_c == 0 :
                print("Progress")
                progress_student_count+=1 #to increment the count of student who got progress
                student_count+=1 
                progress_list.extend([pass_c,defer_c,fail_c]) #To add the student marks as a nested list.
                progress_string_list = ','.join([str (elements) for elements in progress_list])
                student_dict[student_id] = "Progress - " + progress_string_list # TonyStaunton
                progress_list.clear() #so that the list is cleared and the new progress records are stored

                        
                        
            elif pass_c == 100 and (defer_c == 20 and fail_c == 0) or (defer_c == 0 and fail_c == 20):
                print("Progress - (Module trailer)")
                trailer_student_count+=1 
                student_count+=1
                trailer_list.extend([pass_c,defer_c,fail_c])
                trailer_string_list = ','.join([str (elements) for elements in trailer_list]) #geeksforgeeks.com
                student_dict[student_id] = "Module trailer - " + trailer_string_list # TonyStaunton
                trailer_list.clear()
                        
                        
            elif 0<= pass_c <= 80  and (0<= defer_c <=120 and 0<= fail_c <80):
                print("Do not Progress – module retriever")
                retriever_student_count+=1
                student_count+=1
                retriever_list.extend([pass_c,defer_c,fail_c])
                retriever_string_list = ','.join([str (elements) for elements in retriever_list]) #geeksforgeeks.com
                student_dict[student_id] = "Module retriever - " + retriever_string_list # TonyStaunton
                retriever_list.clear()
                        
            elif 0<= pass_c <= 80  and (0<= defer_c <=40 and  fail_c >=80):
                print("Exclude")
                exclude_student_count+=1
                student_count+=1
                exclude_list.extend([pass_c,defer_c,fail_c])
                exclude_string_list = ','.join([str (elements) for elements in exclude_list]) #geeksforgeeks.com
                student_dict[student_id] = "Exclude - " + exclude_string_list # TonyStaunton
                exclude_list.clear()
                        

        except ValueError:
            print("Integer Required")
        break

    #To generate multiple outputs
    while True:
        cont = input("Enter (y) to CONTINUE or Enter (q) to QUIT and view the results :  ")
        cont = cont.lower()
        if  cont=="y":
            pass
            break
            
        elif cont=="q":
            print("Exit program")
            break
        else:
            print("Invalid Input")
        
        
        
       
        
        
    
#Histogram
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
Histogram()   #Calling the function
print(student_dict) #Printing the dictionary



print("-------------------------------------------------------------------------------------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#referenced sources link:
#https://www.youtube.com/watch?v=kiTh-YgzzPo
#https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/?ref=lbp



