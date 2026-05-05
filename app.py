import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("🌞 Solar Panel Monitoring Dashboard")
st.caption("Prototype system for intelligent solar panel monitoring")

# Sidebar controls

st.sidebar.header("Control Panel")

image_type = st.sidebar.selectbox(
"Image Type",
["Dirty Panel", "Reflecting Panel"]
)

fault = st.sidebar.selectbox("Fault Type", ["Clean", "Dusty", "Bird Drop"])
location = st.sidebar.selectbox("Location", ["TL", "TR", "BL", "BR"])
status = st.sidebar.selectbox("Status", ["Idle", "Cleaning", "Completed"])

# Auto adjust fault for reflection mode

if image_type == "Reflecting Panel":
  fault = "Glare / Reflection"

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

st.divider()

st.subheader(f"📸 {image_type} View")

# Select image

if image_type == "Dirty Panel":
image_path = "panel.jpg"
color = "red"
else:
image_path = "reflecting.jpg"
color = "yellow"

# Load image

img = Image.open(image_path)
draw = ImageDraw.Draw(img)

# Get dimensions

width, height = img.size

# Define quadrant boxes

boxes = {
"TL": (0, 0, width//2, height//2),
"TR": (width//2, 0, width, height//2),
"BL": (0, height//2, width//2, height),
"BR": (width//2, height//2, width, height),
}

# Draw highlight box

if location in boxes:
draw.rectangle(boxes[location], outline=color, width=5)

# Show image

st.image(img, caption="Highlighted Fault Area", use_container_width=True)

# Status message

if image_type == "Reflecting Panel":
st.warning("⚠ High reflection detected → efficiency may drop")
else:
st.error("⚠ Dirt detected → cleaning required")
