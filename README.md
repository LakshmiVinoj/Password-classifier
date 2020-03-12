# Password-classifier

The function new_password() consumes no values, but prompts the user with the phrase “Enter password: ” to enter a new password
as shown below in the sample interactions. The function determines how strong your password is based on the following criteria:

• It has at least 10 characters

• It has at least 1 uppercase character

• It has at least 1 lowercase character

• It has at least 3 non-alphanumeric characters (not necessarily distinct)

• It has at least 2 digits (not necessarily distinct)

• It contains no spaces

The function returns None and prints the strength of your password. If the password contains all of the
criteria listed above, then the function prints Good. If the password contains 4 or 5 out of the 6 criteria, then
the function prints Fair. Otherwise, the function prints Weak.
____________________________________________________________________________________________

# new_password

Reads in a string password and prints the strength of the password by following the criteria given in the question.
    
Effects:

  *One string in read in 
  
  *One string is printed
    
new_password: None->None
    
Examples:

*If the user enters "goodPlace12!@@" when new_password() is called,"Good" is printed.

*If the user enters "fairPlace !!!" when new_password() is called, "Fair" is printed.

*If the user enters "weak12!" when new_password() is called, "Weak" is printed.   
____________________________________________________________________________________________

#  new_password_helper

Prints the strength of the password n, by following the criteria given in the question.
    
new_password_helper: Str->Str
____________________________________________________________________________________________

# pass_length

Returns 1 if atleast ten characters are present in string n, otherwise returns 0.
    
pass_length: Str->Nat
____________________________________________________________________________________________

# check_upper

Returns 1 if atleast one uppercase letter is present in string n, otherwise returns 0.
    
check_upper: Str->Nat
____________________________________________________________________________________________

# check_lower

Returns 1 if atleast one lowercase letter is present in string n, otherwise returns 0.
    
check_lower: Str->Nat
____________________________________________________________________________________________

# check_special_char

Returns total number of non-alphanumeric characters in string n.
    
check_special_char: Str->Nat
____________________________________________________________________________________________

# check_special_char2

Returns 1 if atleast three non-alphanumeric characters are present in string n, otherwise returns 0.
    
check_special_char2: Str->Nat
____________________________________________________________________________________________

#  check_digit
Returns total number of digits in string n.
    
check_digit: Str->Nat
____________________________________________________________________________________________

# check_digit2

Returns 1 if atleast two digits are present in string n, otherwise returns 0.
    
check_digit2: Str->Nat
____________________________________________________________________________________________

# check_space

Returns 1 if space is absent in string n, otherwise returns 0.
    
check_space: Str->Nat
____________________________________________________________________________________________

# Examples:

>new_password() => None

 Enter password : goodPass12!@@
 
 Good


>new_password() => None

Enter password : fairPass !!!

Fair

>new_password() => None

Enter password : weak12!

Weak
