import streamlit as st
import openai

# Streamlit app layout
st.image("logo.png", width=120)
st.markdown("""
    <h1 style='color:#4A90E2;'>AI Entrepreneur Prompt Generator</h1>
    <p style='font-size:18px;'>Generate AI-powered social media prompts tailored to your business.</p>
""", unsafe_allow_html=True)

# OpenAI API key input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Define prompt templates
prompt_templates = {
    "Engagement Post Prompt": "Write a fun and engaging question I can ask my audience to boost comments. {business_details}",
    "Product Highlight Prompt": "Create a short Instagram caption that highlights the benefits of {business_details}. Make it cozy and inviting.",
    "Behind-the-Scenes Prompt": "Generate a caption for a behind-the-scenes photo of me preparing orders in {business_details}.",
    "Customer Testimonial Prompt": "Write a post using this customer review to build trust and encourage new buyers: '{business_details}'",
    "Storytelling Prompt": "Tell a short story about why I started {business_details} and how it connects to my passion for creativity.",
    "Promotion Prompt": "Write a caption for a limited-time offer: {business_details}. Make it urgent but friendly.",
    "Educational Tip Prompt": "Create a tip-of-the-day post for a wellness coach about {business_details}.",
    "Holiday-Themed Prompt": "Write a festive caption for a small business holiday post that thanks customers and shares {business_details}.",
    "Hashtag Suggestion Prompt": "Suggest 10 relevant hashtags for a post about {business_details} targeting eco-conscious buyers.",
    "Call-to-Action Prompt": "Write a caption that encourages followers to visit {business_details}."
}

# User input
selected_prompt = st.selectbox("Choose a prompt category:", list(prompt_templates.keys()))
business_details = st.text_input("Enter your business details or context:")

# Generate prompt using OpenAI
if st.button("Generate Prompt"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not business_details:
        st.warning("Please enter your business details.")
    else:
        openai.api_key = api_key
        final_prompt = prompt_templates[selected_prompt].format(business_details=business_details)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": final_prompt}]
            )
            generated_text = response.choices[0].message.content
            st.subheader("Generated Prompt")
            st.write(generated_text)
        except Exception as e:
            st.error(f"Error generating prompt: {e}")
