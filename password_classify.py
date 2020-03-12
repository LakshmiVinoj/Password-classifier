import check
def new_password():
    password=input("Enter password:")
    new_password_helper(password)

def new_password_helper(n):
    w=pass_length(n)+check_upper(n)+check_lower(n)+check_special_char2(n)+check_digit2(n)+check_space(n)
    if w>=6:
        print(" Good")
    elif w==4 or w==5:
        print(" Fair")
    else:
        print(" Weak")

def pass_length(n):
    if len(n)>=10:
        return 1 
    else:
        return 0
    
def check_upper(n):
    s=n[0:1]
    if s=="":
        return 0
    if str.isupper(s):
        return 1 
    else:
        return 0 + check_upper(n[1:])

def check_lower(n):
    t=n[0:1]
    if t=="":
        return 0
    if str.islower(t):
        return 1 
    else:
        return 0 + check_lower(n[1:])
    
def check_special_char(n):    
    y=n[0:1]
    if y=="":
        return 0
    if str.isalnum(y):
        return 0 + check_special_char(n[1:])
    else:
        return 1 + check_special_char(n[1:]) 
    
def check_special_char2(n): 
    if check_special_char(n)>=3:
        return 1
    else:
        return 0

def check_digit(n):  
    p=n[0:1]
    if p=="":
        return 0
    if str.isdigit(p):
        return 1 + check_digit(n[1:])
    else:
        return 0 + check_digit(n[1:])

def check_digit2(n):
    if check_digit(n)>=2:
        return 1
    else:
        return 0

def check_space(n):
    if n=="":
        return 0
    if n!=" ":
        return 1 
    else:
        return 0 + check_space(n[1:])

##Examples:
check.set_input("goodPlace12!@@")
check.set_print_exact(" Good")
check.expect("Example 1:",new_password(),None)

check.set_input("fairPlace !!!")
check.set_print_exact(" Fair")
check.expect("Example 2:",new_password(),None)

check.set_input("weak12")
check.set_print_exact(" Weak")
check.expect("Example 3:",new_password(),None)

##Tests:
check.set_input("1234")
check.set_print_exact(" Weak")
check.expect("Q4T1",new_password(),None)

check.set_input("WHEEEEEEEttttttttttttttttt")
check.set_print_exact(" Fair")
check.expect("Q4T2",new_password(),None)

check.set_input("99cenTs!! @@")
check.set_print_exact(" Good")
check.expect("Q4T3",new_password(),None)

check.set_input("$helloworld")
check.set_print_exact(" Weak")
check.expect("Q4T4",new_password(),None)
