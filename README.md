# 🎓 AI-Powered University Search Agent

🚀 An advanced, privacy-first tool that simplifies the university selection process by automating research and providing real-time, AI-generated insights — all running locally using [Ollama](https://ollama.com/).

## 🔍 Overview

The **AI-Powered University Search Agent** is designed to deliver tailored university recommendations and reports by leveraging local LLMs, smart querying, and dynamic research loops. With a focus on privacy and full customization, this tool helps students and researchers make informed decisions effortlessly.

---

## ✨ Features

### 1. 🌐 Web Research (via Tavily API)
- Retrieves **real-time data** on:
  - University rankings
  - Tuition fees
  - Scholarships
  - Cost of living
  - Admission rates
  - Housing & transport
  - Career opportunities

### 2. 🧠 Smart Query Generation
- Powered by LLMs to generate custom search queries
- Supports user-defined preferences and full query customization

### 3. ✍️ AI-Powered Summarization
- Summarizes web content and research findings using:
  - Mistral
  - Qwen-7B
  - LLaMA 2 / 3
  - Phi-3
  - Gemma
- Presents **clear, concise** insights for quick evaluation

### 4. 🔁 Adaptive Research Loops (LangGraph)
- Dynamically improves results over multiple iterations
- Refines strategies based on new data and user inputs

### 5. 🏫 University Recommendation Engine
- Compares institutions based on:
  - Academic reputation
  - Cost efficiency
  - Student experience
- Generates **personalized reports** and recommendations

---

## 🔐 Privacy & Customization

- **Runs Locally**: No external API calls to LLMs. All operations occur on your hardware with Ollama.
- **Supports Multiple Models**: Easily switch between:
  - Mistral (fast & affordable)
  - LLaMA 3 (balanced)
  - Phi-3 (concise, low-cost)
  - Gemma (complex analysis)
  - Mixtral (deep reasoning)
- **User-Controlled Settings**:
  - Query design
  - Search loops
  - Ranking preferences

---

## 🛠️ Tech Stack

- **LLMs**: Mistral, LLaMA 2/3, Phi-3, Qwen, Gemma, Mixtral
- **Frameworks**: [LangChain](https://www.langchain.com/), [LangGraph](https://www.langgraph.dev/)
- **Web Scraping/Research**: Tavily API
- **Deployment**: Local environment with [Ollama](https://ollama.com/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/university-search-agent.git
cd university-search-agent

2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Set Up Ollama
Download and install Ollama: https://ollama.com/download
Then pull desired models:

bash
Copy
Edit
ollama pull mistral
ollama pull llama3
# Add other models as needed
4. Run the Application
bash
Copy
Edit
python main.py
📄 Output
Structured JSON or Markdown reports

Tabulated comparisons between universities

Actionable insights for decision-making

🧩 Future Enhancements
Interactive UI with Streamlit or React

Integration with university APIs (e.g., QS, THE)

Offline support for pre-indexed datasets

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgments
Inspired by the challenges of manual college research

Powered by open-source LLMs and LangChain ecosystem

Built with ❤️ to help students make smarter choices









