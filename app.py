import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: sans-serif;
        background-color: #f0f0f0;
    }
    .main .block-container {
        max-width: 800px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput, .stNumberInput, .stButton>button, p { /* Select input fields, button, and paragraphs */
        font-size: 1.2rem; /* Increase font size */
    }
    .stTitle { /* Select the title */
        font-size: 2rem; /* Increase title font size */
    }

    </style>
    """,
    unsafe_allow_html=True,
)


st.title("حاسبة كمية البوتاس المتبقية")

col1, col2, col3 = st.columns([1, 2, 1])  # Center the input fields

with col2:
    loading_rate = st.text_input("معدل التحميل (طن/ساعة):")
    location = st.text_input("الموقع (متر):")

    if st.button("احسب"):
        if loading_rate and location:  # Check if both inputs are filled
            try:
                loading_rate = float(loading_rate)
                location = float(location)
                if loading_rate > 0 and location > 0:
                    BELT_SPEED = 2.75
                    POTASH_DENSITY = 1500

                    loading_rate_kg_per_sec = loading_rate * 1000 / 3600
                    cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)
                    remaining_potash_volume = cross_sectional_area * location
                    remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY
                    remaining_potash_tons = remaining_potash_mass / 1000

                    st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
                else:
                    st.error("الرجاء إدخال قيم صحيحة لمعدل التحميل والموقع (أكبر من صفر).")

            except ValueError:
                st.error("الرجاء إدخال أرقام صحيحة.")
        else:
            st.error("الرجاء إدخال قيم لمعدل التحميل والموقع.")


st.markdown(
    """
    <div style="text-align: center; font-size: 14px; color: gray;">
        جميع الحقوق محفوظة &copy; 2025 علي السعودي
    </div>
    """,
    unsafe_allow_html=True,
)
