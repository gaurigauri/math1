# By Gauri
import streamlit as st


def code_to_add_3_nums():
	with st.form(key="addition"):
		num1 = st.number_input("number1",0,100000,0,1)
		num2 = st.number_input("number2",0,100000,0,1)
		num3 = st.number_input("number3",0,100000,0,1)
		submitted = st.form_submit_button(label="add them")
		if submitted:
			#with st.spinner("Adding...")
			st.write(f"{num1} + {num2} + {num3} =   {num1 + num2 + num3}\n")

if __name__ == '__main__':
	st.title("Add three numbers")
	code_to_add_3_nums()