def check_even_odd():
    user_input = int(input("Enter Your Number : "))
    
    
    if user_input % 2 == 0: #even Number
        print(f"This number {user_input} is Even ")
    else: # Check Odd Number
        print(f"This number  {user_input} is Odd ")
        
check_even_odd()