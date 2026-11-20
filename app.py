import streamlit as st
from pathlib import Path

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Mohamed Saad | Data Engineer & IT Specialist",
    page_icon="📊",
    layout="wide",
)

# --- تحسينات CSS بسيطة ---
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; }
    .project-card {
        background-color: #1E2129;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #00ADB5;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    # إذا وضعت صورتك في assets/profile.png قم بإلغاء التعليق عن السطر التالي:
    # st.image("assets/profile.png", width=180)
    st.title("Mohamed Saad")
    st.caption("Data Engineer | Healthcare IT & Medical Systems")
    st.write("📍 Alexandria, Egypt")
    st.write("📞 +20 101 615 9505")
    
    st.divider()
    st.subheader("🔗 Links & Profiles")
    st.markdown("- [GitHub](https://github.com/mo9112003w-create)")
    st.markdown("- [Previous Portfolio](https://mo9112003w-create.github.io/saad-potofolio/)")
    st.markdown("- [Kafiil](https://kafiil.com/u/mo_saad123)")
    
    # زر تحميل السيرة الذاتية إذا كانت موجودة
    cv_path = Path("assets/cv.pdf")
    if cv_path.exists():
        with open(cv_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download CV",
                data=pdf_file.read(),
                file_name="Mohamed_Saad_CV.pdf",
                mime="application/pdf",
                use_container_width=True
            )

# --- القسم الرئيسي (Hero Section) ---
st.title("👋 Hi, I'm Mohamed Saad")
st.subheader("Data Engineer & Healthcare IT Infrastructure Specialist")
st.write(
    "Results-driven Data Engineer and IT Specialist with 6+ years of experience in healthcare IT systems, "
    "building automated ETL pipelines, web scraping solutions, real-time web applications, and managing "
    "enterprise servers & databases."
)

# --- أرقام سريعة (Metrics) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Experience", "6+ Years", "Healthcare IT & Data")
col2.metric("Core Stack", "Python & SQL", "ETL & Automation")
col3.metric("Infrastructure", "VMware & Cisco", "Servers & Networks")
col4.metric("Track", "DEPI Graduate", "Data Engineering")

st.divider()

# --- المهارات التقنية (Skills) ---
st.header("🛠️ Technical Skills")
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("**Data Engineering & Automation**")
    st.write("• Python (Pandas, Selenium, Requests)\n• ETL Pipelines & Data Cleaning\n• Web Scraping & API Integration\n• n8n Workflow Automation")

with s2:
    st.markdown("**Databases & Backend**")
    st.write("• SQL Server & PostgreSQL\n• Flask & SocketIO (Real-time Apps)\n• Laravel (PHP)\n• Automated Database Backups")

with s3:
    st.markdown("**IT Infrastructure & Cloud**")
    st.write("• VMware ESXi & Active Directory\n• Cisco Routing & Switching (CCNA)\n• Linux / Windows Server Admin\n• Computer Vision (Video Analytics)")

st.divider()

# --- أبرز المشاريع (Featured Projects) ---
st.header("🚀 Featured Projects")

projects = [
    {
        "title": "Hospital Operations Data Engineering Pipeline (DEPI Graduation Project)",
        "tech": "Python • SQL • ETL • Data Analytics",
        "desc": "End-to-end data pipeline ingesting, cleaning, transforming, and analyzing hospital operational data to optimize resource allocation and patient flow.",
        "link": "https://github.com/mo9112003w-create"
    },
    {
        "title": "Real-Time Hospital Clinic Queue System",
        "tech": "Python • Flask • SocketIO • Bilingual TTS",
        "desc": "Local network queue management system deployed at Dar Elsalaam Specialized Hospital featuring bank-style chimes, Arabic/English voice announcements, and mobile control.",
        "link": "https://github.com/mo9112003w-create/hospital-queue"
    },
    {
        "title": "Automated Outpatient WhatsApp Notifier & Scraper",
        "tech": "Python • Web Scraping • SQL Server • Automation",
        "desc": "Background service monitoring live outpatient reservations from the hospital ERP system and sending automated WhatsApp queue alerts to patients.",
        "link": "https://github.com/mo9112003w-create"
    },
    {
        "title": "E-Commerce Web Scraper & ETL Pipeline (Noon Egypt)",
        "tech": "Python • Selenium • Pandas • CSV",
        "desc": "Automated scraping pipeline extracting product pricing, discounts, ratings, and metadata into structured datasets for market analysis.",
        "link": "https://github.com/mo9112003w-create"
    },
    {
        "title": "Computer Vision Camera Analytics System",
        "tech": "Python • OpenCV • Image Processing",
        "desc": "Graduation project focused on real-time video stream analysis and automated object/event detection from surveillance cameras.",
        "link": "https://github.com/mo9112003w-create"
    }
]

for proj in projects:
    st.markdown(f"""
    <div class="project-card">
        <h4>{proj['title']}</h4>
        <p style="color: #00ADB5; font-size: 0.9rem;"><b>{proj['tech']}</b></p>
        <p>{proj['desc']}</p>
        <a href="{proj['link']}" target="_blank" style="color: #00ADB5; text-decoration: none;">🔗 View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- نموذج تواصل سريع (Contact Form) ---
st.header("📬 Get In Touch")
with st.form("contact_form"):
    c_name = st.text_input("Your Name")
    c_email = st.text_input("Your Email")
    c_msg = st.text_area("Message")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        if c_name and c_email and c_msg:
            st.success(f"Thank you {c_name}! Your message has been noted.")
        else:
            st.warning("Please fill in all fields.")
