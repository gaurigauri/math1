import streamlit as st
import sys

import st_addition
import st_calculator
import st_missing_numbers
import st_tables

sys.path.append(".")

FUNCTIONALITIES = {
    "Generate tables": st_tables,
    "Addition": st_addition,
    "Calculator": st_calculator,
    "Missing numbers": st_missing_numbers
}


def main():
    st.title("Gauri's calculator")
    fn = st.radio("What do you want to do?", list(FUNCTIONALITIES.keys()))
    if fn:
        FUNCTIONALITIES[fn].main()
    else:
        st.write("Please make a selection")


if __name__ == '__main__':
    main()
