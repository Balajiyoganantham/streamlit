# 🗡️ Zoro - Enhanced GitHub API Assistant

A powerful RAG (Retrieval-Augmented Generation) system built with Streamlit, LangChain, and Groq LLM for answering GitHub API questions.

## 🚀 Features

- **Smart Q&A System**: Ask questions about GitHub API and get accurate answers
- **Memory & Context**: Maintains conversation history for better context
- **Real-time Analytics**: Performance metrics and response statistics
- **Comprehensive Evaluation**: Built-in evaluation system with multiple metrics
- **Beautiful UI**: Modern, responsive interface with gradient styling

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Groq (Llama3-70B)
- **Vector Database**: ChromaDB
- **Embeddings**: Sentence Transformers
- **Framework**: LangChain
- **Visualization**: Plotly

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd github_documentation_RAG-main
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file with your Groq API key
GROQ_API_KEY=your_groq_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

## 🎯 Usage

1. **Initialize the System**: Click "Initialize System" to load documents and set up the RAG pipeline
2. **Ask Questions**: Use the chat interface to ask GitHub API questions
3. **View Analytics**: Check the Analytics tab for performance metrics
4. **Run Evaluation**: Use the Evaluation tab to test system performance

## 📊 Evaluation Metrics

The system includes comprehensive evaluation with:
- **F1 Score**: Measures answer accuracy
- **ROUGE-1 F1**: Measures text similarity
- **Keyword Coverage**: Measures expected keyword presence
- **Success Rate**: Overall evaluation success percentage

## 🔧 Configuration

Key configuration files:
- `rag_system/config.py`: System configuration
- `.streamlit/config.toml`: Streamlit settings
- `requirements.txt`: Python dependencies

## 📁 Project Structure

```
github_documentation_RAG-main/
├── app.py                 # Main Streamlit application
├── evaluation.py          # Evaluation system
├── rag_system/           # RAG system modules
│   ├── config.py         # Configuration
│   ├── embeddings.py     # Embedding models
│   ├── vectorstore.py    # Vector database
│   └── ...
├── documents/            # GitHub API documentation
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🚀 Deployment

The application is configured for Streamlit Cloud deployment with:
- Compatibility fixes for various environments
- Optimized dependencies for Python 3.13
- System package requirements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Balaji** - Enhanced with Memory & Analytics 🧠📊

---

*Powered by LangChain ConversationalRetrievalChain • Groq Llama3-70B • ChromaDB* 