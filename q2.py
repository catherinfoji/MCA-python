#2. Dictionary
#Create a dictionary to store the details of your company employees (name as key and
#birthdate as value).
#{ ‘Virat Kohli’: ‘5 November 1988’, ‘Umesh Yadav’: ‘25 October 1987’, ‘Manish Pandey’:
#‘10 September 1989’, ‘Rohit Sharma’: ‘30 April 1987’, ‘Ravindra Jadeja’: ‘6 December
#1988’, ‘Hardik Pandya’: ‘11 October 1993’ }
#Write a function birthDate() that takes the full name of your employees(as a string) and
#displays the given employee’s birthdate.
#>>>birthDate(‘Rohit Sharma’)
#‘30 April 1987’
emp = {
    'Virat Kohli': '5 November 1988',
    'Umesh Yadav': '25 October 1987',
    'Manish Pandey': '10 September 1989',
    'Rohit Sharma': '30 April 1987',
    'Ravindra Jadeja': '6 December 1988',
    'Hardik Pandya': '11 October 1993'
}

def birthdate(name):
    if name in emp:
        print (emp[name])
    else:
        print ("Employee not found.")
        
name = input("Enter the name:")
birthdate(name)





