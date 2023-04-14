# Is a Number Prime?
# A prime number is an integer greater than 1 that is only divisible by one and itself. 
# Write a function that determines whether or not its parameter is prime, returning True 
# if it is, and False otherwise. Write a main program that reads an integer from the user 
# and displays a message indicating whether or not it is prime. Ensure that the main program 
# will not run if the file containing your solution is imported into another program. 

# tạo hàm input giá trị N
def isPrimeNumber():
    while True:
        N= input("Enter your number N >0: (enter E to exit)");
        if N == "E":
            break;

# xét giá trị N <=1 
        N = int(N)
        try:
            if N<=1 :
                print(str(N) + " is not a prime number");
                return;
    # xét các giá trị i từ 2 đến N, nếu N chia hết cho 1 số i trong khoảng này thì không là số nguyên tố
            for i in range (2, N):
                if N % i == 0:
                    print(str(N) + " is not a prime number");
                    return
            print(str(N) + " is a prime number");
        except:ValueError
        print("Invalid value, enter a number only");

isPrimeNumber();

# import math

# def isPrimeNumber():
#     while True:
#         user_input = input("Enter your number N > 0: (enter E to exit) ")
        
#         if user_input == "E":
#             break
        
#         try:
#             N = int(user_input)
            
#             if N <= 1:
#                 print(str(N) + " is not a prime number")
#             else:
#                 is_prime = True
                
#                 for i in range(2, int(math.sqrt(N))+1):
#                     if N % i == 0:
#                         is_prime = False
#                         break
                
#                 if is_prime:
#                     print(str(N) + " is a prime number")
#                 else:
#                     print(str(N) + " is not a prime number")
                    
#         except ValueError:
#             print("Invalid input, enter a number greater than 0 or 'E'")
        
#     print("Program exited")

# isPrimeNumber()