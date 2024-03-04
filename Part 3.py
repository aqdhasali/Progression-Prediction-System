# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# The links for the references are in bottom of this code.
# Student ID: 20210860 / w1954000
# Date: 19.11.2022






#Creating and Initializng Variables
pass_c = 0   #To store the pass credits of the students
defer_c = 0  #To store the defer credits of the students
fail_c = 0   #To store the fail credits of the students
total = 0    #To store the credits and check whether the credits are  valid or not
cont='y'or'q' #to continue or end the program
student_count= 0  #To increase the student count
progress_student_count = 0   #To increase the count of the student who got progress
retriever_student_count = 0 #To increase the count of the student who got retriever
trailer_student_count = 0    #To increase the count of the student who got trailer
exclude_student_count  = 0   #To increase the count of the student who got exclude
progress_list = []  #To store the credits of the student who got progress to a list
trailer_list=[]      #To store the credits of the student who got trailer to a list
retriever_list=[]    #To store the credits of the student who got retriever to a list
exclude_list=[]      #To store the credits of the student who got exclude to a list
progress_string_list = ''  #to convert the Progress list into a string 
trailer_string_list = ''   #to convert the trailer list into a string 
retriever_string_list = '' #to convert the reriever list into a string 
exclude_string_list = ''   #to convert the exclude list into a string 


#Functions
def file():
    """" To open the file and store the marks of the students """
    file = open("MyText.txt","w")
    file.write("Progress : ")
    file.write(progress_string_list)
    file.write("\nTrailer : ")
    file.write(trailer_string_list)
    file.write("\nRetriever : ")
    file.write(retriever_string_list)
    file.write("\nExclude : ")
    file.write(exclude_string_list)

    file.close()
    return


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
while cont=="y":
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
                progress_list.extend([pass_c,defer_c,fail_c]) #To add the student marks as a nested list .
                progress_string_list = ','.join([str (elements) for elements in progress_list]) #geeksforgeeks.com #using list comprhension I have converted this list into to a string so that I can store into the file.
                             
            elif pass_c == 100 and (defer_c == 20 and fail_c == 0) or (defer_c == 0 and fail_c == 20):
                print("Progress - (Module trailer)")
                trailer_student_count+=1 
                student_count+=1
                trailer_list.extend([pass_c,defer_c,fail_c])
                trailer_string_list = ','.join([str (elements) for elements in trailer_list]) #geeksforgeeks.com
                        
            elif 0<= pass_c <= 80  and (0<= defer_c <=120 and 0<= fail_c <80):
                print("Do not Progress – module retriever")
                retriever_student_count+=1
                student_count+=1
                retriever_list.extend([pass_c,defer_c,fail_c])
                retriever_string_list = ','.join([str (elements) for elements in retriever_list]) #geeksforgeeks.com
                        
            elif 0<= pass_c <= 80  and (0<= defer_c <=40 and  fail_c >=80):
                print("Exclude")
                exclude_student_count+=1
                student_count+=1
                exclude_list.extend([pass_c,defer_c,fail_c])
                exclude_string_list = ','.join([str (elements) for elements in exclude_list]) #geeksforgeeks.com

        except ValueError:
            print("Integer Required")
        break

    #To generate multiple outputs
    while True:
        cont = input("Enter (y) to CONTINUE or Enter (q) to QUIT and view the results :   ")
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

Histogram()


print("-------------------------------------------------------------------------------------------------------------------------------------------------------")

file() #calling the function and printing it. 
file = open("MyText.txt","r")
r = file.read()
print(r)
file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#referenced sources links:
#https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/?ref=lbp
