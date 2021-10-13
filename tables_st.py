import streamlit as st

def actual_demo():
    with st.form(key='qa_form'):
        num = st.text_input(label="Table of which number?", value=5, type="int")
        submitted = st.form_submit_button(label='Generate table')
        if submitted:
            with st.spinner("Generating table..."):
                st.write(f"Table of {num}\n-----------------------")
                for times in range(1,10+1):
                  st.write(f"{times}x{num}={times*num}")  

def main():
    st.title("Generate tables of numbers")
    actual_demo()


if __name__ == "__main__":
    main()
