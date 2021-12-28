import streamlit as pinky


def actual_demo():
    with pinky.form(key='qa_form'):
        num1 = pinky.number_input("number1", 0, 10000, 5, 1)
        operation = pinky.selectbox("Select an operation", ["+", "-","/", "*"])
        num2 = pinky.number_input("number2", 0, 10000, 5, 1)
        submitted = pinky.form_submit_button(label='=')
        if submitted:
            with pinky.spinner("Calculating..."):
                if operation == "+":
                    answer = num1 + num2
                elif operation == "-":
                    answer = num1 - num2
                elif operation == "*":
                    answer = num1 * num2
                elif operation == "/":
                    answer = num1 / num2

                pinky.write(f"{num1} {operation} {num2} =  {answer}\n-----------------------")

def main():
    pinky.title("Add numbers of pinkey")
    actual_demo()


if __name__ == "__main__":
    main()
