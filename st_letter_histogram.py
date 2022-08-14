import streamlit as st
import pandas as pd
from PIL import Image

# input = text (sequence of letters)
#         gauri, radhika
# output = a: 3, d: 1, g: 1, h: 1, ... (histogram)

def increment_val(d, ch, increment_by=1):
    if ch not in d:
        d[ch] = 0
    d[ch] += increment_by

def set_bg_hack_url():
    """
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    """

    st.markdown(
        f"""
         <style>
         
         .stApp {{
             background: url("https://images7.alphacoders.com/696/thumb-1920-696556.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

def main():
    with st.form("letter_histogram"):
        d = dict()
        inp = st.text_input("Enter any text")
        do_it= st.form_submit_button("Run")
        if do_it:
            set_bg_hack_url()
            # image = Image.open('pink.jpg')
            # st.image(image, caption='Computing histogram ...')

            for ch in inp.lower():
                if 'a' <= ch <= 'z':
                    increment_val(d, ch)
            desc_order_letter = []
            desc_order_freq = []
            for k, v in sorted(d.items(), key=lambda k: k[1], reverse=True):
                # st.write(f"{k}: {v}\n")
                desc_order_letter.append(k)
                desc_order_freq.append(int(v))

            # df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
            df = pd.DataFrame({'letters': desc_order_letter, 'frequency': desc_order_freq})
            # df = pd.DataFrame(desc_order_freq, columns=desc_order_letter)
            # ax = df.plot.bar(x='letters', y='frequency', rot=0)
            st.table(df)
            # st.bar_chart(df)


if __name__ == '__main__':
    main()