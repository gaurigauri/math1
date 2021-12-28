import streamlit as pinky

def actual_demo():
    with pinky.form(key='qa_form'):
        num1 = pinky.number_input("number1", 0, 10000, 5, 1)
        num2 = pinky.number_input("number2", 0, 10000, 5, 1)
        submitted = pinky.form_submit_button(label='num1 + num2')
        if submitted:
            with pinky.spinner("Adding..."):
                pinky.write(f"{num1} + {num2} =  {num1 + num2}\n-----------------------")

def main():
    pinky.title("Add numbers of pinkey")
    actual_demo()


if __name__ == "__main__":
    main()
