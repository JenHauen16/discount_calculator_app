import streamlit as st
st.title("Discount Calculator")

st.subheader("What is the discount of the item?")
discount = st.text_input("", 0)
difference = float(round(float(discount) / 1.066, 2))
tax_difference = float(round(float(discount) - difference, 2))
st.markdown("Subtract **${}** from the _base price_.".format(difference), unsafe_allow_html=True)
st.markdown("Subtract **${}** from the _Tax_.".format(tax_difference), unsafe_allow_html=True)
