import streamlit as st
import main
import rag
import json
import os

st.set_page_config(page_title="Deepak: News Research Tool", layout="wide")
st.title("🧠 Deepak: News Research Tool")
st.sidebar.title("🔗 Input Settings")

urls = [st.sidebar.text_input(f"URL {i+1}", "") for i in range(3)]
process_btn = st.sidebar.button("🚀 Process")

if process_btn:
    valid_urls = [url.strip() for url in urls if url.strip()]
    if not valid_urls:
        st.sidebar.error("⚠️ Please enter at least one URL.")
        st.stop()

    with st.status("Fetching articles...", expanded=False):
        all_data = {}
        for url in valid_urls:
            text = main.scrape(url)
            if text:
                all_data[url] = text
            else:
                st.warning(f"⚠️ Skipped or empty: {url}")

        if all_data:
            # Save all scraped data to the JSON file
            with open("scraped3.json", "w", encoding="utf-8") as f:
                json.dump(all_data, f, indent=2, ensure_ascii=False)
            
            # Now build the index
            main.store()
            st.success("✅ Index created and saved.")
        else:
            st.error("❌ No valid content found.")

# Question-answer UI
query = st.text_input("💬 Ask something from the articles:")
if query:
    if not os.path.exists("docs.pkl"):
        st.warning("📦 Please process URLs first.")
    else:
        with st.spinner("🧠 Thinking..."):
            response = rag.rag_query(query)
            st.subheader("🔎 Answer")
            st.write(response)