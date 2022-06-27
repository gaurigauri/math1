# By Gauri
import streamlit as st


def code_to_add_nums():
    with st.form():
		  num1 = st.number_input("number1", 0, 100,5, 1)
  		num2 = st.number_input("number2", 0, 100,5, 1)
      submitted = st.form_submit_button(label="add them")
      if submitted:
        	with st.spinner("Adding..."):
            	st.write(f"{num1} + {num2} =  {num1 + num2}\n") 

def main():
  st.title("Add two numbers")
  code_to_add_nums()

  
if __name__ == "__main__ ":
  main()
