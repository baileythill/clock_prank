import streamlit as st
from datetime import datetime
import pytz

def calculate_time_until_event():
    target_date = datetime(2025, 12, 25, tzinfo=pytz.UTC)
    current_time = datetime.now(pytz.UTC)
    time_left = target_date - current_time
    
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    
    return days, hours, minutes, seconds

# Set page config
st.set_page_config(page_title="Countdown to the Big Flush")

# Add custom CSS with Christmas theme and animations
st.markdown("""
    <style>
        /* Christmas color scheme */
        :root {
            --christmas-red: #D42426;
            --christmas-green: #165B33;
            --snow-white: #FFFFFF;
            --gold: #FFD700;
        }
        
        .snowflake {
            color: var(--snow-white);
            font-size: 1.5em;
            position: fixed;
            animation: fall 10s linear infinite;
        }
        
        @keyframes fall {
            0% { transform: translateY(-100vh) rotate(0deg); }
            100% { transform: translateY(100vh) rotate(360deg); }
        }
        
        .countdown-box {
            background-color: var(--christmas-red);
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            color: var(--snow-white);
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .title {
            color: var(--christmas-green);
            text-align: center;
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 30px;
        }
        
        .number {
            font-size: 3em;
            font-weight: bold;
            color: var(--gold);
        }
        
        .label {
            font-size: 1.2em;
            margin-top: 5px;
        }
    </style>
    
    <!-- Add snowflakes -->
    <div class="snowflakes">
        """ + ''.join([f'<div class="snowflake" style="left: {i}%; animation-delay: {i/10}s;">❄</div>' for i in range(0, 100, 10)]) + """
    </div>
    """, unsafe_allow_html=True)

# Add title
st.markdown('<h1 class="title">🎄 Countdown to the Big Flush 🎄</h1>', unsafe_allow_html=True)

# Get countdown values
days, hours, minutes, seconds = calculate_time_until_event()

# Create columns for countdown display
col1, col2, col3 = st.columns(3)

# Display countdown boxes
with col1:
    st.markdown(f"""
        <div class="countdown-box">
            <div class="number">{days}</div>
            <div class="label">Days</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="countdown-box">
            <div class="number">{hours}</div>
            <div class="label">Hours</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="countdown-box">
            <div class="number">{minutes}</div>
            <div class="label">Minutes</div>
        </div>
    """, unsafe_allow_html=True)

# Add festive message
st.markdown("""
    <div style='text-align: center; margin-top: 30px; color: #165B33; font-size: 1.5em;'>
        🎅 Ho Ho Ho! The Sh*tter is gonna be full! 🎁
    </div>
""", unsafe_allow_html=True)

# Add auto-refresh
st.markdown("""
    <meta http-equiv="refresh" content="60">
""", unsafe_allow_html=True)