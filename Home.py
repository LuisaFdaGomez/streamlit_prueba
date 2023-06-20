import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout='wide')

m = leafmap.Map()
m.add_basemap('HYBRID')
m.to_streamlit()

st.text('this is the main map to development')

