import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout='wide')
dropdown = st.selectbox("Basemap", ["HYBRID", "ROADMAP", "TERRAIN", "SATELLITE"])

m = leafmap.Map()
m.add_basemap(dropdown)
st.text('this is the main map to development')

m.to_streamlit()



