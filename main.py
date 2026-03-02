from pyscript import display, document

#Function to validate username and password input during sign-in
def validate_signin(e):

    # Clear previous output by overwriting the div 
    output_div = document.getElementById("output") 
    output_div.innerHTML = ""

    errors = []
    # Retrieve the entered username from the HTML input field
    username = document.getElementById("username").value
    # Calculate the length of the username
    username_length = len(username)

    #checks if entered username is atleast 7 characters long
    if username_length < 7:
        display(f"Username is short. Add atleast {7 - username_length} more characters to proceed.")
   
    #Retrieve the entered password from the HTML input field
    password = document.getElementById("password").value
    #Calculate the length of the password
    password_length = len(password)

    #Validate password length (must be at least 10 characters)
    if password_length < 10:
        errors.append(f"Password is short. Add at least {10 - len(password)} more characters to proceed.")
    #Validate if password contains at least one number
    if password.isalpha():
        errors.append("Password must contain at least 1 number.")
    #Validate if password contains at least one letter
    if password.isdigit():
        errors.append("Password must contain at least 1 letter.") 
 
# Display Results
    
    if errors: 
        output_div.innerHTML = "<br>".join(errors) 
    else: 
        output_div.innerHTML = "Account created successfully!"
        


