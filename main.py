import streamlit as st

# Set Streamlit Page Configuration
st.set_page_config(page_title="Sharmeen Asif - Portfolio", page_icon="🚀", layout="wide")

# Apply Background Color (Light Gray-Yellow)
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f7f5e6;  /* Light Gray-Yellow */
            padding: 20px;
        }
        .main-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333333;
        }
        .section {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .menu {
            background-color: #333;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
        .menu a {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            margin: 5px;
            font-size: 18px;
        }
        .menu a:hover {
            background-color: #555;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Menu Bar
st.markdown(
    """
    <div class="menu">
        <a href="#home">🏠 Home</a>
        <a href="#services">🛠 Services</a>
        <a href="#about-us">📖 About Us</a>
        <a href="#contact-us">📞 Contact Us</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Home Section
st.markdown('<div class="main-container" id="home">', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.title("Sharmeen Asif")
st.write("🚀 Web Developer | AI Software Engineer")
st.write("Building cutting-edge AI applications and scalable web solutions.")
st.markdown('</div>', unsafe_allow_html=True)

# Services Section
st.markdown('<div class="section" id="services">', unsafe_allow_html=True)
st.header("Our Services")
st.markdown("""
✅ **Web Development** - Modern and scalable web applications using **Next.js, React, and WordPress**.  
✅ **AI & Machine Learning** - Chatbots, NLP, and Agentic AI solutions.  
✅ **E-Commerce Solutions** - Custom-built online stores and POS systems.  
✅ **Cloud & DevOps** - Deployments on AWS, Firebase, and Docker.  
""")
st.markdown('</div>', unsafe_allow_html=True)

# About Us Section
st.markdown('<div class="section" id="about-us">', unsafe_allow_html=True)
st.header("About Us")
st.write("""
We specialize in **Next.js, WordPress, AI-driven applications, and Agentic AI research**.
Our expertise includes chatbot development, NLP, and full-stack web development.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Us Section
st.markdown('<div class="section" id="contact-us">', unsafe_allow_html=True)
st.header("Contact Us")
st.write("📧 Email: codeshery@gmail.com")
st.markdown("[🔗 LinkedIn](https://linkedin.com) | [GitHub](https://github.com/shery123pk)")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
