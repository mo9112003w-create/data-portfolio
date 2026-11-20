from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Mohamed Saad | Data Engineer & Python Developer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CSS لتجميل البطاقات والشارات وضمان وضوح النصوص ---
st.markdown(
    """
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1150px;
    }
    .hero-box {
        background: linear-gradient(135deg, #161B22 0%, #1F2937 100%);
        border: 1px solid #30363D;
        border-left: 5px solid #00ADB5;
        border-radius: 14px;
        padding: 2rem;
        margin-bottom: 1.5rem;
    }
    .hero-title {
        margin: 0 0 0.3rem 0;
        color: #FFFFFF !important;
        font-size: 2.3rem;
        font-weight: 800;
        line-height: 1.2;
    }
    .hero-subtitle {
        color: #22D3EE !important;
        margin: 0;
        font-size: 1.1rem;
        font-weight: 600;
    }
    .hero-desc {
        color: #E5E7EB !important;
        font-size: 1.02rem;
        line-height: 1.65;
        margin-top: 0.85rem;
        margin-bottom: 0;
    }
    .skill-badge {
        display: inline-block;
        background-color: rgba(0, 173, 181, 0.16);
        color: #67E8F9 !important;
        border: 1px solid rgba(103, 232, 249, 0.35);
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.25rem 0.25rem 0.25rem 0;
    }
    .card {
        background-color: #161B22;
        border: 1px solid #2A313C;
        border-radius: 12px;
        padding: 1.35rem;
        margin-bottom: 1rem;
        transition: border-color 0.15s ease;
    }
    .card:hover {
        border-color: #00ADB5;
    }
    .card-title {
        margin: 0 0 0.25rem 0;
        color: #FFFFFF !important;
        font-size: 1.1rem;
        font-weight: 700;
    }
    .exp-role {
        color: #38BDF8 !important;
        font-weight: 700;
        font-size: 1.05rem;
    }
    .exp-meta {
        color: #9CA3AF !important;
        font-size: 0.88rem;
        margin-bottom: 0.6rem;
    }
    .card-text {
        color: #D1D5DB !important;
        margin-bottom: 0;
        line-height: 1.6;
    }
    .card ul {
        color: #D1D5DB !important;
        margin-bottom: 0;
        padding-left: 1.2rem;
    }
    .card li {
        margin-bottom: 0.35rem;
    }
</style>
""",
    unsafe_allow_html=True,
)


# --- دالة البحث عن الصورة بأمان ---
def get_profile_image():
    candidates = [
        "assets/profile.jpg",
        "assets/profile.jpeg",
        "assets/profile.png",
        "profile.jpg",
        "profile.jpeg",
        "profile.png",
        "assets/محمد.jpeg",
        "محمد.jpeg",
    ]
    for img_path in candidates:
        if Path(img_path).exists():
            return img_path
    return None


# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    img = get_profile_image()
    if img:
        st.image(img, use_container_width=True)
    else:
        st.markdown("### 👨‍💻 Mohamed Saad")
        st.info("Upload your photo to `assets/profile.jpg` to display it here.")

    st.markdown("## Mohamed Saad")
    st.markdown("**Data Engineer • Python • Healthcare IT**")
    st.markdown("📍 Alexandria, Egypt")
    st.markdown("📞 +20 101 615 9505")

    st.divider()
    st.markdown("### 🌐 Profiles & Links")
    st.markdown("- [GitHub](https://github.com/mo9112003w-create)")
    st.markdown(
        "- [Portfolio (GitHub Pages)](https://mo9112003w-create.github.io/saad-potofolio/)"
    )
    st.markdown("- [Kafiil](https://kafiil.com/u/mo_saad123)")

# --- واجهة البداية (Hero Section) ---
st.markdown(
    """
<div class="hero-box">
    <div class="hero-title">Mohamed Saad</div>
    <div class="hero-subtitle">
        Data Engineer | Python, Web Scraping, Pandas &amp; Data Cleaning | Healthcare IT
    </div>
    <p class="hero-desc">
        Data Engineer with hands-on experience building automated data extraction pipelines, cleaning and
        transforming raw datasets with Python &amp; Pandas, designing ETL workflows, and managing real-world
        healthcare IT systems and SQL databases.
    </p>
    <div style="margin-top: 1rem;">
        <span class="skill-badge">Python</span>
        <span class="skill-badge">Data Extraction / Scraping</span>
        <span class="skill-badge">Pandas</span>
        <span class="skill-badge">Data Cleaning</span>
        <span class="skill-badge">ETL Pipelines</span>
        <span class="skill-badge">SQL Server</span>
        <span class="skill-badge">Flask &amp; Automation</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# --- مؤشرات سريعة ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Experience", "6+ Years", "Data & Healthcare IT")
m2.metric("Data Stack", "Python & Pandas", "Scraping & Cleaning")
m3.metric("Databases", "SQL Server", "ETL & Reporting")
m4.metric("Program", "DEPI", "Data Engineering")

st.divider()

# --- تبويبات منظمة ---
tab1, tab2, tab3, tab4 = st.tabs([
    "💼 Experience & Core Expertise",
    "🚀 Data & Engineering Projects",
    "🛠️ Skills Matrix",
    "📩 Contact",
])

# --- التبويب 1: الخبرات ---
with tab1:
    st.subheader("Core Data & Python Expertise")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
        <div class="card">
            <div class="exp-role">Data Extraction &amp; Web Scraping</div>
            <div class="exp-meta">Automated Collection • Structured Outputs</div>
            <p class="card-text">
                Extracting structured data from web pages and live operational systems using Python, Selenium,
                and automated scripts, exporting clean datasets directly into CSV/Excel or databases.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
        <div class="card">
            <div class="exp-role">Data Cleaning &amp; ETL with Pandas</div>
            <div class="exp-meta">Normalization • Validation • Transformation</div>
            <p class="card-text">
                Handling missing values, removing duplicates, standardizing formats, filtering noise, and running
                multi-stage ETL scripts with Pandas and Python for reliable analytics.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.subheader("Work Experience")
    st.markdown(
        """
    <div class="card">
        <div class="exp-role">Medical Device &amp; IT Technician</div>
        <div class="exp-meta">Dar Elsalaam Specialized Hospital • Apr 2025 – Present</div>
        <ul>
            <li>Maintain healthcare IT infrastructure, VMware ESXi servers, Cisco switches, and SQL Server databases.</li>
            <li>Build Python automation tools, outpatient reservation monitors, queue systems, and reporting workflows.</li>
            <li>Support data reporting and quality survey workflows for hospital operations and medical caravans.</li>
        </ul>
    </div>
    <div class="card">
        <div class="exp-role">Medical Equipment &amp; IT Infrastructure Specialist</div>
        <div class="exp-meta">El Amreya, Alexandria • Prior Experience</div>
        <ul>
            <li>Delivered technical support, hardware/network maintenance, and system reliability across clinical environments.</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

# --- التبويب 2: المشاريع ---
with tab2:
    st.subheader("Featured Projects")

    projects = [
        {
            "title": "E-Commerce Product Scraper & Dataset Builder (Noon Egypt)",
            "tags": "Python • Selenium • Pandas • CSV",
            "summary": (
                "Automated web scraper extracting product titles, prices,"
                " discounts, ratings, images, and URLs directly into"
                " structured CSV files for price and catalog analysis."
            ),
        },
        {
            "title": "Two-Stage Employee ETL & Data Cleaning Pipeline",
            "tags": "Python • Pandas • ETL • Data Quality",
            "summary": (
                "Modular data generation, cleaning, transformation, and loading"
                " pipeline ensuring consistent schemas and clean analytical"
                " records."
            ),
        },
        {
            "title": "Hospital Operations Data Engineering Pipeline (DEPI)",
            "tags": "Python • ETL • SQL • Analytics",
            "summary": (
                "Collaborative data engineering pipeline processing hospital"
                " operational records to support reporting and"
                " decision-making."
            ),
        },
        {
            "title": (
                "Outpatient Reservation Monitor & WhatsApp Notification Service"
            ),
            "tags": "Python • Web Scraping • Automation • SQL",
            "summary": (
                "Background Python service monitoring live outpatient bookings"
                " and automating patient notifications."
            ),
        },
        {
            "title": (
                "Real-Time Hospital Clinic Queue System & Caravan Survey App"
            ),
            "tags": "Python • Flask • SocketIO • Web Apps",
            "summary": (
                "Web-based clinic queue calling platform with voice/chime"
                " alerts and a Flask survey web app for medical caravan"
                " evaluation."
            ),
        },
        {
            "title": "Computer Vision Camera & Image Analysis System",
            "tags": "Python • Computer Vision • Image Processing",
            "summary": (
                "Graduation project analyzing camera video streams and frames"
                " for automated visual inspection and detection."
            ),
        },
    ]

    for p in projects:
        st.markdown(
            f"""
        <div class="card">
            <div class="card-title">{p['title']}</div>
            <div style="color: #22D3EE !important; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.5rem;">{p['tags']}</div>
            <p class="card-text">{p['summary']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# --- التبويب 3: مصفوفة المهارات ---
with tab3:
    st.subheader("Technical Skills")
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("**Data & Python**")
        st.markdown("""
        - Python & OOP
        - Pandas & Data Wrangling
        - Web Scraping & Data Extraction
        - Data Cleaning & Validation
        - ETL Pipelines & CSV/Excel Processing
        """)

    with col_b:
        st.markdown("**Databases & Web / Automation**")
        st.markdown("""
        - SQL Server & Relational Queries
        - Flask & SocketIO
        - Laravel (PHP)
        - n8n & Task Automation
        - Computer Vision Basics
        """)

    with col_c:
        st.markdown("**Systems, Networks & Tools**")
        st.markdown("""
        - VMware ESXi & Server Administration
        - Cisco Networking (CCNA Fundamentals)
        - Git & GitHub
        - Windows & Linux Environments
        """)

# --- التبويب 4: التواصل ---
with tab4:
    st.subheader("Get In Touch")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        details = st.text_area("Project / Opportunity Details")
        send = st.form_submit_button("Submit Inquiry")
        if send:
            if name and email and details:
                st.success(f"Thanks {name}! Your message has been recorded.")
            else:
                st.error("Please fill in your name, email, and message.")
