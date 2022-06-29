# By Gauri for multiplication
import streamlit as st


def code_to_multiply_nums():
    with st.form(key="multiplication"):
        num1 = st.number_input("number1",0,100,5,1)
        num2 = st.number_input("number2", 0, 100, 4, 1)
        submitted = st.form_submit_button("multiply them")
        if submitted:
            st.write(f"{num1} * {num2} =	 {num1 * num2}\n")


if __name__ == '__main__':
    st.title("Multiply two numbers")
    code_to_multiply_nums()
