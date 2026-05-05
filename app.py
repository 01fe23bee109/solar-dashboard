import streamlit as st

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("🌞 Solar Panel Monitoring Dashboard")

# Sidebar controls
st.sidebar.header("Control Panel")

fault = st.sidebar.selectbox("Fault Type", ["Clean", "Dusty", "Bird Drop"])
location = st.sidebar.selectbox("Location", ["TL", "TR", "BL", "BR"])
status = st.sidebar.selectbox("Status", ["Idle", "Cleaning", "Completed"])

# Main display
col1, col2, col3 = st.columns(3)

col1.metric("Fault", fault)
col2.metric("Location", location)
col3.metric("Status", status)

st.write("Panel View:")

st.write(f"Top Left: {'DIRTY' if location=='TL' else 'CLEAN'}")
st.write(f"Top Right: {'DIRTY' if location=='TR' else 'CLEAN'}")
st.write(f"Bottom Left: {'DIRTY' if location=='BL' else 'CLEAN'}")
st.write(f"Bottom Right: {'DIRTY' if location=='BR' else 'CLEAN'}")
