# QueryMind AI 🧠

QueryMind AI is an interactive conversational AI assistant built with **Streamlit**, **LangChain**, and **Google Gemini** (`gemini-3.5-flash-lite`).

## Features

- ⚡ Fast, contextual question-answering powered by Google Gemini
- 💬 Clean chat interface with conversation history preservation
- 🛠️ Simple and extensible LangChain integration

## Getting Started

### Prerequisites

- Python 3.10+
- A Google Gemini API Key ([Google AI Studio](https://aistudio.google.com/))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vansh-026/QueryMind-AI.git
   cd QueryMind-AI
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   # Windows:
   .\env\Scripts\activate
   # macOS/Linux:
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file in the root directory based on `.env.example`:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

### Running the App

Launch the Streamlit app:
```bash
streamlit run apps/1_QnABot.py
```
