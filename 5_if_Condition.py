# Handle marks and batch assignment
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("You will be a part of the A0 batch")
elif marks >= 60:
    print("You will be a part of the A1 batch")
elif marks >= 40:
    print("You will be a part of the A2 batch")
else:
    print("You will not be a part of any batch")

# Handle price decision
price = int(input("Enter the price: "))
if price > 1000:
    print("I will not purchase")
    if price < 2000:
        print("It's ok")
    elif price > 5000:
        print("This is too much")
else:
    print("surprisingly price is too low")
