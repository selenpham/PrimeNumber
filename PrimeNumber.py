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

