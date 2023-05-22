import streamlit as st


def main():
    with st.form("form"):
        mid_row_content = "x x x x"
        other_row_content = "x __ x"
        max_rows=st.number_input(label="Enter an odd number")
        run_pressed =st.form_submit_button(label="submit")
        if run_pressed:
            max_rows = int(max_rows) # we don't want decimal numbers.
            mid_pt=(1+max_rows)/2
            for i in range(1, max_rows+1):
                if i == mid_pt:
                    st.markdown(mid_row_content)
                else:
                    st.markdown(other_row_content)


if __name__ == '__main__':
    main()