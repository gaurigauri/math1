import streamlit as st


def calculator_code():
    with st.form(key="calculator"):
        num1 = st.number_input("number1", 0, 100000, 1)
        num2 = st.number_input("number2", 0, 100000, 1)
        op = st.selectbox("select an option", ["*", "+"])
        submitted = st.form_submit_button(label="calculate")
        if submitted:
            st.write(f"{num1} {op} {num2} = ")
            if op == "*":
                st.write(f"{num1 * num2}")
            elif op == "+":
                st.write(f"{num1 + num2}")


if __name__ == '__main__':
    st.title("calculator")
    calculator_code()
