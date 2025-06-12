# 🤖 TaskAgent Pro

> **Intelligent Task Planning powered by Gemini 1.5 Flash**

Transform your goals into actionable, structured plans with AI precision. TaskAgent Pro is a sophisticated AI-powered task planning system that breaks down complex objectives into manageable, step-by-step action plans.

![TaskAgent Pro Interface](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)

## ✨ Features

- **🧠 AI-Powered Planning**: Advanced Gemini 1.5 Flash model creates detailed, step-by-step plans for any goal
- **⚡ Lightning Fast**: Get comprehensive task breakdowns in seconds with optimized processing
- **📋 Structured Output**: Receive organized plans with clear steps, timelines, and actionable insights
- **🔍 Smart Research**: Automatic web search integration to enhance planning with current information
- **📊 Progress Tracking**: Built-in logging system to track your planning history
- **🎨 Modern UI**: Beautiful, responsive web interface built with Streamlit

## 🏗️ Architecture

TaskAgent Pro uses a multi-agent architecture powered by LangGraph:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Planner Agent  │ -> │  Search Agent   │ -> │Summarizer Agent │
│                 │    │                 │    │                 │
│ Breaks down     │    │ Finds relevant  │    │ Creates final   │
│ goals into      │    │ information     │    │ actionable      │
│ subtasks        │    │ via web search  │    │ summary         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Internet connection for web search functionality

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/taskagent-pro.git
   cd taskagent-pro
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

5. **Start the backend API**
   ```bash
   uvicorn api.main:app --reload --port 8000
   ```

6. **Launch the frontend (in a new terminal)**
   ```bash
   streamlit run frontend/app.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:8501` to access TaskAgent Pro

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Getting a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

## 📁 Project Structure

```
taskagent/
├── api/
│   └── main.py                 # FastAPI backend server
├── app/
│   ├── agents/
│   │   ├── planner_agent.py    # Goal breakdown agent
│   │   ├── search_agent.py     # Web search agent
│   │   └── summarizer_agent.py # Results summarization agent
│   ├── data/
│   │   └── task_logs.json      # Planning history logs
│   ├── langgraph/
│   │   └── task_graph.py       # LangGraph workflow orchestration
│   ├── tools/
│   │   ├── search_tool.py      # DuckDuckGo search integration
│   │   └── storage_tool.py     # Data persistence utilities
│   └── utils/
│       └── gemini.py           # Gemini API wrapper
├── frontend/
│   └── app.py                  # Streamlit web interface
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## 🎯 Usage Examples

### Example Goals You Can Try

- **📚 Learning**: "Learn Python programming from scratch in 3 months"
- **💼 Business**: "Plan a comprehensive digital marketing strategy for a startup"
- **🏃 Fitness**: "Create a 30-day fitness plan for beginners"
- **🎉 Events**: "Organize a team-building retreat for 20 employees"
- **🔬 Research**: "Research top AI tools for productivity in 2025"

### API Usage

You can also use the API directly:

```python
import requests

response = requests.post(
    "http://localhost:8000/plan-task/",
    json={"goal": "Launch a successful podcast"}
)

plan_data = response.json()
print(plan_data["plan"])
print(plan_data["summary"])
```

## 🔌 API Reference

### POST `/plan-task/`

Generate a task plan for a given goal.

**Request Body:**
```json
{
  "goal": "Your goal description here"
}
```

**Response:**
```json
{
  "goal": "Your goal description",
  "plan": "Detailed step-by-step plan",
  "summary": "Executive summary of the plan"
}
```

## 🛠️ Development

### Running in Development Mode

1. **Backend with auto-reload**
   ```bash
   uvicorn api.main:app --reload --port 8000
   ```

2. **Frontend with auto-reload**
   ```bash
   streamlit run frontend/app.py --server.runOnSave true
   ```

### Adding New Agents

To add a new agent to the system:

1. Create a new agent file in `app/agents/`
2. Implement the agent logic
3. Update `app/langgraph/task_graph.py` to include the new agent
4. Test the integration

### Customizing the UI

The Streamlit frontend uses custom CSS for styling. You can modify the appearance by editing the CSS in `frontend/app.py`.

## 📊 Logging and Analytics

TaskAgent Pro automatically logs all planning sessions to `app/data/task_logs.json`. Each log entry includes:

- Timestamp
- Original goal
- Generated summary
- Full planning data

## 🔒 Security Considerations

- **API Keys**: Never commit API keys to version control
- **Input Validation**: All user inputs are validated before processing
- **Rate Limiting**: Consider implementing rate limiting for production use
- **HTTPS**: Use HTTPS in production environments

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation as needed


## 🙏 Acknowledgments

- **Google Gemini**: For providing the powerful AI capabilities
- **Streamlit**: For the excellent web framework
- **FastAPI**: For the robust API framework
- **DuckDuckGo**: For search functionality
- **LangGraph**: For workflow orchestration


## 🗺️ Roadmap

- [ ] **Multi-language Support**: Support for planning in different languages
- [ ] **Team Collaboration**: Share and collaborate on plans with team members
- [ ] **Integration APIs**: Connect with popular productivity tools
- [ ] **Mobile App**: Native mobile applications
- [ ] **Advanced Analytics**: Detailed insights and progress tracking
- [ ] **Custom Agent Templates**: Create reusable agent templates
- [ ] **Export Options**: Export plans to various formats (PDF, Word, etc.)

---

<div align="center">
  <strong>Built with ❤️ using AI-powered technology</strong><br>
  <em>Transform your ambitions into achievable milestones</em>
</div>
