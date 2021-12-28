import streamlit as pinky

# Gauri for now, does not want this:
# 5 + x = 25 then find x
# x = 25 - 5 = 20
# 5 * x = 25 then find x
# x = 25/5 = 5
# 25 - x = 5, then find x
# x = 25-5 = 20
# 25/x = 5, then find x
# x = 25/5 = 5

# Gauri wants this:
# x + y = 10
# (1,9) (2,8) (3,7) (4,6) (5,5) ...
# Get value of x one by one using FOR loop
## (x, sum - x)  ... FOR loop y = 1 to SUM

# x - y = 10 (bound x, y between [1,50])
# (11,1) (12,2) (13,3) (14,4) (15,5) ...
## (y + subtra, y) ... FOR loop y = 1 to MAX(50)

# x * y = 10
# (1,10) (2,5) ...
## (x, mul/x) ... FOR loop x = 1 to MUL

# x / y = 10 (bound x, y between [1,50])
# (10,1) (20,2) (30,3) ...
## (10*y, y) ... FOR loop y = 1 to MAX(50)

# TODO add help.
# TODO add background colors.
def actual_demo():
    max_num = 50
    with pinky.form(key='missing_num_form'):
        operation = pinky.selectbox("", ["+", "-", "÷", "x"])
        answer = pinky.number_input("=", 0, 100, 10, 1)
        submitted = pinky.form_submit_button(label='find number 1 and 2')
        if submitted:
            with pinky.spinner("Calculating..."):
                if operation == "+":
                    ## (x, sum - x)  ... FOR loop y = 1 to SUM
                    for x in range(1, answer):
                        pinky.write(f"{int(x)} {operation} {int(answer-x)} =  {answer}\n")
                elif operation == "-":
                    ## (y + subtra, y) ... FOR loop y = 1 to MAX(50)
                    for y in range(1, max_num):
                        pinky.write(f"{int(y + answer)} {operation} {int(y)} =  {answer}\n")
                elif operation == "x":
                    ## (x, mul/x) ... FOR loop x = 1 to MUL
                    for x in range(1, answer):
                        if answer/x - int(answer/x) == 0:
                            pinky.write(f"{int(x)} {operation} {int(answer/x)} =  {answer}\n")
                elif operation == "÷":
                    ## (y, 10/y) ... FOR loop y = 1 to MAX(50)
                    for y in range(1, max_num):
                        pinky.write(f"{int(answer*y)} {operation} {int(y)} =  {answer}\n")

def main():
    pinky.title("Find two numbers such that:")
    actual_demo()


if __name__ == "__main__":
    main()
