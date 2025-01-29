import streamlit as st
from datetime import datetime
import pytz

def calculate_time_until_event():
    # Set the target date (November 15, 2025)
    target_date = datetime(2025, 11, 27, tzinfo=pytz.UTC)
    # Get current time in UTC
    current_time = datetime.now(pytz.UTC)
    # Calculate the difference
    time_left = target_date - current_time
    
    # Calculate days, hours, minutes, and seconds
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    
    return days, hours, minutes, seconds

# Set page config
st.set_page_config(page_title="Countdown to the Big Flush")

# Add title with custom styling
st.markdown("""
    <h1 style='text-align: center; color: #1E88E5;'>
        Countdown to the Big Flush
    </h1>
    """, unsafe_allow_html=True)

# Add countdown timer
days, hours, minutes, seconds = calculate_time_until_event()

# Create three columns for the countdown display
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2>{days}</h2>
            <p>Days</p>
        </div>
        """, unsafe_allow_html=True)
    
with col2:
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2>{hours}</h2>
            <p>Hours</p>
        </div>
        """, unsafe_allow_html=True)
    
with col3:
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2>{minutes}</h2>
            <p>Minutes</p>
        </div>
        """, unsafe_allow_html=True)

# Add auto-refresh to update the countdown
st.markdown("""
    <meta http-equiv="refresh" content="60">
    """, unsafe_allow_html=True)