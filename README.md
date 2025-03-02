 # Notion Buddy 📝

Notion Buddy is an AI-powered chatbot designed to help users create and optimize their Notion templates. Built with Streamlit and Google's Generative AI, it provides expert guidance on template design, database setup, formulas, and best practices.

## Features

- Interactive chat interface
- Expert guidance on Notion template creation
- Best practices and optimization tips
- Database structure recommendations
- Formula and automation assistance

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini Pro

## Setup Instructions

1. Clone this repository:
```bash
git clone <repository-url>
cd notion-buddy
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
   - Rename `.env.example` to `.env`
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Usage

1. Type your question about Notion templates in the chat input
2. Press Enter or click the send button
3. Receive expert guidance from Notion Buddy
4. Continue the conversation to refine your template design

## Example Questions

- "How do I structure a project management template?"
- "What's the best way to set up linked databases?"
- "Can you help me create a formula for task prioritization?"
- "What are some best practices for designing a knowledge base?"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.