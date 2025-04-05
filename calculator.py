def calculator():
    print("ماشین حساب ساده")
    num1 = float(input("عدد اول را وارد کنید: "))
    op = input("عملگر را وارد کنید (+ - * /): ")
    num2 = float(input("عدد دوم را وارد کنید: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("عملگر نامعتبر است.")
        return

    print("نتیجه:", result)

calculator()
