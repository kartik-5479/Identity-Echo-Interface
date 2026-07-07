import streamlit as st

st.set_page_config(
    page_title="The Identity Echo Interface",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.title("🤖 AI Dashboard")

    st.success("MirAI Virtual Summer Internship 2026")

    st.divider()

    st.subheader("📋 Instructions:")

    st.write("1. Enter your Name.")
    st.write("2. Enter your Message.")
    st.write("3. Click Transmit.")
    st.divider()

# Title and Introduction
st.title("🚀 The Identity Echo Interface")
st.write(
    "Welcome! Please enter your name and a message below, then click **Transmit**."
)

st.divider()

# User Inputs
user_name = st.text_input(
    "👤 Enter your Name:",
    placeholder="Enter your full name"
)

user_message = st.text_area(
    "💬 Enter your Message:",
    height=150,
    placeholder="Type your message here..."
)

st.divider()

# Button
transmit = st.button(
    "🚀 Transmit",
    use_container_width=True
)

# Validation & Output

if transmit:

    if not user_name.strip():
        st.error("Please provide your name.")

    elif not user_message.strip():
        st.warning("Please type a message to transmit.")

    else:

        # Required Success Message
        st.success(
            f"Transmission successful! Greetings, {user_name}. "
            f"We received your message: {user_message}"
        )

        # Token Calculation
        total_characters = len(user_message)
        estimated_tokens = round(total_characters / 4, 2)

        # Required Info Message
        st.info(
            f"System Check: Your message will consume approximately "
            f"{estimated_tokens} tokens from our context window."
        )

        st.divider()

        # Analytics
        st.subheader("📊 Transmission Analytics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Characters", total_characters)

        with col2:
            st.metric("Estimated Tokens", estimated_tokens)

        with col3:
            st.metric("Status", "Success")

        st.divider()
        st.balloons()

st.caption(
    "❤️ Made with Streamlit | MirAI Virtual Summer Internship 2026"
)