import streamlit as st
import urllib.parse

st.set_page_config(page_title="Google Search Simulator", layout="centered")

st.title("🌍 Google Search Simulator")
st.caption("Simulate a localized Google search from any country and in any language.")

# --- Search Query ---
query = st.text_input("🔍 Enter your search query")

# --- Full list of Google-supported country codes (ISO 3166-1 Alpha-2) ---
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

# --- Google-supported languages (UI) ---
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
    selected_country = st.selectbox("🌐 Choose Country", options=list(country_codes.keys()), index=0)
with col2:
    selected_language = st.selectbox("🗣️ Choose Language", options=list(language_codes.keys()), index=0)

# --- Build the localized Google search URL ---
if query:
    gl = country_codes[selected_country]
    hl = language_codes[selected_language]
    encoded_query = urllib.parse.quote_plus(query)
    search_url = f"https://www.google.com/search?q={encoded_query}&gl={gl}&hl={hl}&pws=0"

    st.markdown("### 🔗 Localized Google Search Link")
    st.code(search_url, language="text")
    st.markdown(f"[🔍 Open Google Search in New Tab]({search_url})")

    st.markdown("---")
    st.caption(f"This search simulates a user in **{selected_country}** using the **{selected_language}** interface.")
