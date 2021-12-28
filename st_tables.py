import streamlit as pinky

def actual_demo():
    with pinky.form(key='qa_form'):
        num = pinky.number_input("Table of which number?", 0, 1000000, 5, 1)
        submitted = pinky.form_submit_button(label='Generate table of pinky')
        if submitted:
            with pinky.spinner("Generating table..."):
                pinky.write(f"pinkey says Table of {num}\n-----------------------")
                for times in range(1,10+1):
                  pinky.write(f"{times} x {num} =  {times * num}")

def main():
    pinky.title("Generate tables of numbers")
    actual_demo()


if __name__ == "__main__":
    main()
