import streamlit as st
import urllib.parse

# --- Page Settings ---
st.set_page_config(page_title="Google Search Simulator", layout="centered")

st.title("🌍 Google Search Simulator")
st.caption("Perform a Google search from any country and language. Great for localized SEO testing.")

# --- Search Query ---
query = st.text_input("🔍 Enter your search query", "best engagement rings")

# --- Dropdowns for Country (gl) and Language (hl) ---
country_options = {
    "United States (us)": "us",
    "United Kingdom (gb)": "gb",
    "Germany (de)": "de",
    "France (fr)": "fr",
    "India (in)": "in",
    "Japan (jp)": "jp",
    "Australia (au)": "au",
    "Brazil (br)": "br",
    "Canada (ca)": "ca"
}

language_options = {
    "English (en)": "en",
    "German (de)": "de",
    "French (fr)": "fr",
    "Spanish (es)": "es",
    "Hindi (hi)": "hi",
    "Japanese (ja)": "ja",
    "Portuguese (pt-BR)": "pt-BR"
}

col1, col2 = st.columns(2)

with col1:
    selected_country = st.selectbox("🌐 Choose Country", list(country_options.keys()))
with col2:
    selected_language = st.selectbox("🗣️ Choose Language", list(language_options.keys()))

# --- Build URL ---
if query:
    gl = country_options[selected_country]
    hl = language_options[selected_language]
    encoded_query = urllib.parse.quote_plus(query)
    search_url = f"https://www.google.com/search?q={encoded_query}&gl={gl}&hl={hl}&pws=0"

    st.markdown("### 🔗 Localized Google Search Link")
    st.code(search_url, language="text")
    st.markdown(f"[🔍 Perform Search in New Tab]({search_url})")

    st.markdown("---")
    st.caption(f"Simulates a search for '{query}' in {selected_country.split('(')[0].strip()} using the {selected_language.split('(')[0].strip()} interface.")

