import streamlit as st
st.se_page_config(page_title='cats')
st.header("types of cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("persian cat")
  st.image("./persian.jpg",caption="persian cat",width=300,use_column_width=True)
  st.write("persian cats are cute")
with col2:
  st.subheader("Ragdoll Cat")
  st.image("./ragdoll.jpg",caption="Ragdoll Cat",eidth=300,use_column_width=True)
  st.write("Ragdoll cats are proud")
