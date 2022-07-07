import streamlit as st


def calculator_code():
    with st.form(key="calculator"):
        tbl1 = st.number_input("table of", 2, 25, 2)
        num1 = st.number_input("number1", 1, 100000, 1)
        num2 = st.number_input("number2", 1, 100000, 1)

        op = st.selectbox("select an option", ["*", "+", "/", "-", "table"])
        submitted = st.form_submit_button(label="calculate")
        if submitted:
            if op == "table":
                for n in range(1, 11):
                    st.write(f"{n}*{tbl1} = {n * tbl1}")
            else:

                st.write(f"{num1} {op} {num2} = ")
                if op == "*":
                    st.write(f"{num1 * num2}")
                elif op == "+":
                    st.write(f"{num1 + num2}")
                elif op == "/":
                    st.write(f"{num1 / num2}")
                elif op == "-":
                    st.write(f"{num1 - num2}")


if __name__ == '__main__':
    st.title("calculator")
    calculator_code()
