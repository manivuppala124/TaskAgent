import streamlit as st
import requests
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="TaskAgent Pro - AI Task Planner",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Section */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .header-title {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.3rem;
        font-weight: 400;
        line-height: 1.6;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #718096;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* Input Section */
    .input-container {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    .input-label {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1rem;
        display: block;
    }
    
    /* Results Section */
    .results-container {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }
    
    .result-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .result-icon {
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    
    .result-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2d3748;
    }
    
    /* Status indicators */
    .status-success {
        background: linear-gradient(135deg, #48bb78, #38a169);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .status-error {
        background: linear-gradient(135deg, #f56565, #e53e3e);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .status-warning {
        background: linear-gradient(135deg, #ed8936, #dd6b20);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Loading animation */
    .loading-container {
        text-align: center;
        padding: 2rem;
    }
    
    .loading-spinner {
        width: 40px;
        height: 40px;
        border: 4px solid #e2e8f0;
        border-top: 4px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 0 auto 1rem;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Example cards */
    .example-card {
        background: linear-gradient(135deg, #f7fafc, #edf2f7);
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 3px solid #667eea;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .example-card:hover {
        background: linear-gradient(135deg, #edf2f7, #e2e8f0);
        transform: translateX(5px);
    }
    
    .example-text {
        color: #4a5568;
        font-weight: 500;
        margin: 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header-container">
    <div class="header-title">🤖 TaskAgent Pro</div>
    <div class="header-subtitle">
        Intelligent Task Planning powered by Gemini 1.5 Flash<br>
        Transform your goals into actionable, structured plans with AI precision
    </div>
</div>
""", unsafe_allow_html=True)

# Feature highlights
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">AI-Powered Planning</div>
        <div class="feature-desc">Advanced Gemini 1.5 Flash model creates detailed, step-by-step plans for any goal</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Lightning Fast</div>
        <div class="feature-desc">Get comprehensive task breakdowns in seconds with optimized processing</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📋</div>
        <div class="feature-title">Structured Output</div>
        <div class="feature-desc">Receive organized plans with clear steps, timelines, and actionable insights</div>
    </div>
    """, unsafe_allow_html=True)

# Input Section
st.markdown("""
<div class="input-container">
    <label class="input-label">🎯 What would you like to accomplish?</label>
</div>
""", unsafe_allow_html=True)

# Example goals
st.markdown("**💡 Try these examples:**")
examples = [
    "Research top AI tools for productivity in 2025",
    "Create a 30-day fitness plan for beginners",
    "Plan a comprehensive digital marketing strategy for a startup",
    "Organize a team-building retreat for 20 employees",
    "Learn Python programming from scratch in 3 months"
]

example_cols = st.columns(2)
for i, example in enumerate(examples):
    with example_cols[i % 2]:
        if st.button(f"📌 {example}", key=f"example_{i}", use_container_width=True):
            st.session_state.goal_input = example

# Goal input
goal = st.text_area(
    "",
    placeholder="Enter your goal or objective here... Be as specific as possible for better results!",
    height=100,
    key="goal_input",
    value=st.session_state.get('goal_input', '')
)

# Action buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_button = st.button("🚀 Generate Task Plan", type="primary", use_container_width=True)

# Processing and Results
if run_button:
    if goal.strip():
        # Create results container
        results_placeholder = st.empty()
        
        with results_placeholder.container():
            st.markdown("""
            <div class="loading-container">
                <div class="loading-spinner"></div>
                <h3>🧠 TaskAgent is thinking...</h3>
                <p>Analyzing your goal and creating a comprehensive plan</p>
            </div>
            """, unsafe_allow_html=True)
        
        try:
            # Make API request
            response = requests.post(
                "http://127.0.0.1:8000/plan-task/", 
                json={"goal": goal}, 
                timeout=30
            )
            
            # Clear loading and show results
            results_placeholder.empty()
            
            if response.ok:
                data = response.json()
                
                # Success message
                st.markdown("""
                <div class="status-success">
                    ✅ <strong>Task plan generated successfully!</strong><br>
                    Your goal has been analyzed and broken down into actionable steps.
                </div>
                """, unsafe_allow_html=True)
                
                # Plan section
                st.markdown("""
                <div class="results-container">
                    <div class="result-header">
                        <span class="result-icon">📋</span>
                        <span class="result-title">Strategic Action Plan</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.code(data["plan"], language="markdown")
                
                # Summary section
                st.markdown("""
                <div class="results-container">
                    <div class="result-header">
                        <span class="result-icon">🎯</span>
                        <span class="result-title">Executive Summary</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="status-success">
                    {data["summary"]}
                </div>
                """, unsafe_allow_html=True)
                
                # Timestamp
                st.markdown(f"""
                <div style="text-align: right; color: #718096; font-size: 0.9rem; margin-top: 1rem;">
                    Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
                </div>
                """, unsafe_allow_html=True)
                
            else:
                error_detail = response.json().get('detail', 'Unknown error occurred')
                st.markdown(f"""
                <div class="status-error">
                    ⚠️ <strong>Request Failed</strong><br>
                    {error_detail}
                </div>
                """, unsafe_allow_html=True)
                
        except requests.exceptions.Timeout:
            results_placeholder.empty()
            st.markdown("""
            <div class="status-error">
                ⏱️ <strong>Request Timeout</strong><br>
                The request took too long to process. Please try again with a simpler goal.
            </div>
            """, unsafe_allow_html=True)
            
        except requests.exceptions.ConnectionError:
            results_placeholder.empty()
            st.markdown("""
            <div class="status-error">
                🔌 <strong>Connection Error</strong><br>
                Unable to connect to the TaskAgent API. Please ensure the backend service is running.
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            results_placeholder.empty()
            st.markdown(f"""
            <div class="status-error">
                ❌ <strong>Unexpected Error</strong><br>
                {str(e)}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="status-warning">
            📝 <strong>Goal Required</strong><br>
            Please enter a valid goal or objective before generating a task plan.
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #718096; padding: 2rem;">
    <p><strong>TaskAgent Pro</strong> - Powered by Gemini 1.5 Flash</p>
    <p>Transform your ambitions into achievable milestones with AI-driven planning</p>
</div>
""", unsafe_allow_html=True)