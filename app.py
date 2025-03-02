import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Configure page settings
st.set_page_config(
    page_title="Notion Buddy",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #e6f3ff;
    }
    .bot-message {
        background-color: #f0f2f6;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation" not in st.session_state:
    # Custom prompt template for Notion expertise
    template = """You are Notion Buddy, an expert AI assistant specializing in helping users create and optimize Notion templates.
    You have extensive knowledge about Notion's features, best practices, and template design principles.
    
    Current conversation:
    {history}
    Human: {input}
    AI Assistant:"""

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=template
    )

    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7,
        convert_system_message_to_human=True
    )

    # Set up conversation memory
    memory = ConversationBufferMemory(return_messages=True)
    
    # Create conversation chain
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=True
    )

# Header
st.title("🤖 Notion Buddy")
st.markdown("""
Welcome to Notion Buddy! I'm your personal assistant for creating amazing Notion templates.
Ask me anything about:
- Template design and structure
- Database setup and relations
- Formulas and automations
- Best practices and optimization
""")

# Display chat messages
for message in st.session_state.messages:
    with st.container():
        st.markdown(f"""<div class="chat-message {'user-message' if message['role'] == 'user' else 'bot-message'}">
            {'👤' if message['role'] == 'user' else '🤖'} {message['content']}
            </div>""", unsafe_allow_html=True)

# Chat input
if user_input := st.chat_input("Ask me about Notion templates..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    try:
        # Get response from conversation chain
        response = st.session_state.conversation.predict(input=user_input)
        
        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update the chat display
        st.rerun()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        if "GOOGLE_API_KEY" not in os.environ:
            st.warning("Please make sure you have set up your Google API key in the .env file!")


