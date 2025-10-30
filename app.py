import streamlit as st
import requests
import datetime
from PIL import Image
from io import BytesIO

# --- Title and description ---
st.set_page_config(page_title="NASA APOD Gallery", page_icon="🪐", layout="wide")
st.title("🌌 NASA Astronomy Picture of the Day")
st.write("Displays the last 7 days of NASA's Astronomy Picture of the Day (APOD).")

# --- API key (use DEMO_KEY or your own from https://api.nasa.gov) ---
API_KEY = "DEMO_KEY"

# --- Date range selection ---
today = datetime.date.today()
days = st.slider("How many past days to show:", 1, 7, 7)

# --- Loop over days and show images ---
for i in range(days):
    date = today - datetime.timedelta(days=i)
    date_str = date.isoformat()
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date_str}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("media_type") == "image":
            st.subheader(f"{data['title']} ({date_str})")
            st.image(data['url'], use_column_width=True, caption=data.get("explanation", ""))
        else:
            st.warning(f"{date_str} is not an image (media_type: {data.get('media_type')})")
    except Exception as e:
        st.error(f"Error loading {date_str}: {e}")
