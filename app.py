import streamlit as st
from pypdf import PdfReader
import ollama

st.set_page_config(page_title="School Assistant v2", page_icon="📚", layout="centered")

st.title("📚 My School & Work AI Assistant")
st.write("### Version 2: Chat with Your PDF (Optimized)")

uploaded_file = st.file_uploader("Drop your PDF file here", type="pdf")

if uploaded_file is not None:
    st.success("🎉 File uploaded successfully!")
    
    reader = PdfReader(uploaded_file)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text
            
    st.info(f"Successfully read {len(reader.pages)} pages of text.")
    
    st.write("---")
    st.write("### 🤖 Ask the AI about this document:")
    
    user_question = st.text_input("Enter your question here:")
    
    if user_question:
        # A clearer spinner so you know it hasn't crashed
        with st.spinner("CPU is processing the text and generating your answer... Please hold on!"):
            try:
                # We add instructions to tell the AI to keep its answer clear and concise
                prompt_content = (
                    f"You are a helpful school assistant. Answer the question directly based only on the text provided.\n\n"
                    f"Document Content:\n{full_text}\n\n"
                    f"User Question: {user_question}"
                )
                
                print("\n[STATUS] Sending document and question to Phi-3 Local AI...")
                
                # CHANGED MODEL TO llama3.2:1b FOR EXTRA SPEED
                response = ollama.chat(
                    model='llama3.2:1b',
                    messages=[
                        {'role': 'user', 'content': prompt_content}
                    ]
                )
                
                print("[STATUS] Answer received successfully!")
                
                st.write("#### 📝 Answer:")
                st.write(response['message']['content'])
                
            except Exception as e:
                st.error(f"Error talking to AI: {e}")