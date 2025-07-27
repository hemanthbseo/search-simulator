import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

st.set_page_config(page_title="Google Search Simulator", layout="centered")

st.title("🌍 Google Search Simulator")
st.caption("Simulate a localized Google search from any country and in any language.")

# --- Search Input ---
query = st.text_input("🔍 Enter your search query", "")

# --- Dropdown Data ---
country_codes = {
    "United States": "us",
    "United Kingdom": "gb",
    "Germany": "de",
    "France": "fr",
    "India": "in",
    "Japan": "jp",
    "Australia": "au",
    "Brazil": "br",
    "Canada": "ca",
    "South Africa": "za",
    "Italy": "it",
    "Netherlands": "nl",
    "Spain": "es",
    "Sweden": "se",
    "Mexico": "mx",
    "Russia": "ru",
    "Singapore": "sg",
    "Switzerland": "ch",
    "New Zealand": "nz",
    "Norway": "no",
    "China": "cn",
    "Poland": "pl",
    "South Korea": "kr",
    "Thailand": "th",
    "Argentina": "ar",
    "Turkey": "tr",
    "Belgium": "be",
    "Austria": "at",
    "Czech Republic": "cz",
    "Ireland": "ie",
    "Portugal": "pt"
}

language_codes = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Portuguese (Brazil)": "pt-BR",
    "Portuguese (Portugal)": "pt-PT",
    "Hindi": "hi",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Italian": "it",
    "Russian": "ru",
    "Arabic": "ar",
    "Dutch": "nl",
    "Polish": "pl",
    "Swedish": "sv",
    "Turkish": "tr",
    "Thai": "th",
    "Hebrew": "iw",
    "Norwegian": "no",
    "Czech": "cs",
    "Finnish": "fi",
    "Danish": "da",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Greek": "el"
}

# --- UI Dropdowns ---
col1, col2 = st.columns(2)
with col1:
    selected_country = st.selectbox("🌐 Choose Country", options=list(country_codes.keys()))
with col2:
    selected_language = st.selectbox("🗣️ Choose Language", options=list(language_codes.keys()))

# --- Search Button ---
if st.button("🔎 Search"):
    if not query.strip():
        st.warning("Please enter a search query.")
    else:
        gl = country_codes[selected_country]
        hl = language_codes[selected_language]
        encoded_query = urllib.parse.quote_plus(query.strip())
        search_url = f"https://www.google.com/search?q={encoded_query}&gl={gl}&hl={hl}&pws=0"

        # Open the URL in a new browser tab using JavaScript
        components.html(
            f"""
            <script>
            window.open("{search_url}", "_blank");
            </script>
            """,
            height=0,
        )
