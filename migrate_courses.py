import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def migrate():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()

    print("Disabling foreign key checks...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    print("Dropping existing courses table if exists...")
    cursor.execute("DROP TABLE IF EXISTS courses")

    print("Re-enabling foreign key checks...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    print("Creating new courses table with department column...")
    cursor.execute("""
        CREATE TABLE courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            platform VARCHAR(100) NOT NULL,
            link VARCHAR(500) NOT NULL,
            tags VARCHAR(255) DEFAULT '',
            icon VARCHAR(50) DEFAULT '📚',
            bg_gradient VARCHAR(255) DEFAULT '',
            badge_type VARCHAR(50) DEFAULT 'Free',
            has_cert BOOLEAN DEFAULT FALSE,
            rating VARCHAR(50) DEFAULT '',
            duration VARCHAR(50) DEFAULT '',
            views VARCHAR(50) DEFAULT '',
            department VARCHAR(100) DEFAULT ''
        )
    """)

    courses_data = [
        # ── Udemy ──────────────────────────────────────────────────────────────
        ("Web Developer Bootcamp", "Udemy", "https://www.udemy.com/course/the-complete-web-development-bootcamp/", "web paid cert", "🌐", "linear-gradient(135deg,#1e1b4b,#4c1d95);", "Paid", True, "", "74h 9m", "", ""),
        ("Python for Data Science and Machine Learning Bootcamp", "Udemy", "https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/", "data paid cert", "📊", "linear-gradient(135deg,#0c4a6e,#0369a1);", "Paid", True, "", "25h+", "", ""),
        ("Machine Learning A-Z™", "Udemy", "https://www.udemy.com/course/machinelearning/", "ml paid cert", "🤖", "linear-gradient(135deg,#14532d,#15803d);", "Paid", True, "", "44h+", "", ""),
        ("JavaScript Complete Guide", "Udemy", "https://www.udemy.com/course/javascript-the-complete-guide-2020-beginner-advanced/", "web paid", "📜", "", "Paid", False, "", "52h+", "", ""),
        ("React - The Complete Guide", "Udemy", "https://www.udemy.com/course/react-the-complete-guide-incl-redux/", "web paid", "⚛️", "", "Paid", False, "", "68–70h", "", ""),
        ("Angular Complete Course", "Udemy", "https://www.udemy.com/course/the-complete-guide-to-angular-2/", "web paid", "🅰️", "", "Paid", False, "", "34–35h", "", ""),
        ("Node.js Developer Course", "Udemy", "https://www.udemy.com/course/the-complete-nodejs-developer-course-2/", "web paid", "🟢", "", "Paid", False, "", "35h+", "", ""),
        ("Docker & Kubernetes Guide", "Udemy", "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/", "web paid", "🐳", "", "Paid", False, "", "22–23h", "", ""),
        ("AWS Certified Solutions Architect", "Udemy", "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/", "cloud paid", "☁️", "", "Paid", False, "", "27h+", "", ""),
        ("Complete Python Bootcamp", "Udemy", "https://www.udemy.com/course/complete-python-bootcamp/", "data paid", "🐍", "", "Paid", False, "", "22h", "", ""),

        # ── Coursera ───────────────────────────────────────────────────────────
        ('Machine Learning Specialization', 'Coursera', 'https://www.coursera.org/specializations/machine-learning-introduction', 'ml paid cert', '🧠', '', 'Paid', True, '', '3 months', '', ''),
        ('Python for Everybody', 'Coursera', 'https://www.coursera.org/specializations/python', 'data paid cert', '🐍', '', 'Paid', True, '', '8 months', '', ''),
        ('IBM Data Science Professional Certificate', 'Coursera', 'https://www.coursera.org/professional-certificates/ibm-data-science', 'data paid cert', '📊', '', 'Paid', True, '', '11 months', '', ''),

        # ── GeeksforGeeks – no department (existing general courses) ───────────
        ('Python Programming Language Complete Tutorial', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/python-programming-language/', 'data free', '🐍', 'linear-gradient(135deg,#052e16,#166534);', 'Free', False, '', '15–20h', '', ''),
        ('Data Structures and Algorithms Course', 'GeeksforGeeks', 'https://practice.geeksforgeeks.org/courses/dsa-self-paced', 'web paid cert', '📚', 'linear-gradient(135deg,#1e1b4b,#4c1d95);', 'Paid', True, '', '35–40h', '', ''),
        ('Full Stack Development Course', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/courses/full-stack-development-with-react-node-js', 'web paid cert', '💻', 'linear-gradient(135deg,#1a1a2e,#16213e);', 'Paid', True, '', '30–40h', '', ''),
        ("Machine Learning Tutorial", "GeeksforGeeks", "https://www.geeksforgeeks.org/machine-learning/", "ml free", "🤖", "linear-gradient(135deg,#2d1b69,#5b21b6);", "Free", False, "", "Self-paced", "", ""),
        ('Java Programming Course', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/java/', 'web free', '☕', 'linear-gradient(135deg,#0f172a,#1e40af);', 'Free', False, '', '15–20h', '', ''),
        ('C++ Programming Course', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/c-plus-plus/', 'web free', '💻', 'linear-gradient(135deg,#1e293b,#475569);', 'Free', False, '', '15h', '', ''),
        ('DBMS Complete Course', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/dbms/', 'data free', '🗄️', 'linear-gradient(135deg,#334155,#64748b);', 'Free', False, '', '10–15h', '', ''),
        ('Operating Systems Course', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/operating-systems/', 'web free', '⚙️', 'linear-gradient(135deg,#111827,#1f2937);', 'Free', False, '', '10h', '', ''),
        ('Computer Networks Course', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/computer-network-tutorials/', 'web free', '🌐', 'linear-gradient(135deg,#0f172a,#1e40af);', 'Free', False, '', '8–10h', '', ''),
        ('System Design Course', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/system-design-tutorial/', 'web free', '🏗️', 'linear-gradient(135deg,#065f46,#10b981);', 'Free', False, '', '12–15h', '', ''),

        # ── GeeksforGeeks – Cyber Security ────────────────────────────────────
        ('Ethical Hacking', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/ethical-hacking-tutorial/', 'cyber free', '🛡️', 'linear-gradient(135deg,#0f172a,#1e3a5f);', 'Free', False, '', '10h', '', 'Cyber Security'),
        ('Cyber Security Basics', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/introduction-to-ethical-hacking/', 'cyber free', '🔐', 'linear-gradient(135deg,#0f172a,#1e3a5f);', 'Free', False, '', '8h', '', 'Cyber Security'),
        ('Network Security', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/computer-networks/network-security/', 'cyber free', '🌐', 'linear-gradient(135deg,#0f172a,#1e3a5f);', 'Free', False, '', '8–10h', '', 'Cyber Security'),
        ('Penetration Testing', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/blogs/how-should-i-start-learning-ethical-hacking-on-my-own/', 'cyber free', '🧪', 'linear-gradient(135deg,#0f172a,#1e3a5f);', 'Free', False, '', '10–12h', '', 'Cyber Security'),
        ('Web Security', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/web-tech/web-security-considerations/', 'cyber free', '🔒', 'linear-gradient(135deg,#0f172a,#1e3a5f);', 'Free', False, '', '8h', '', 'Cyber Security'),

        # ── GeeksforGeeks – Business & Management ─────────────────────────────
        ('Digital Marketing', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/complete-digital-marketing-course-from-basic-to-advance/', 'business paid cert', '📈', 'linear-gradient(135deg,#1a1a2e,#16213e);', 'Paid', True, '', '10–15h', '', 'Business & Management'),
        ('Product Management', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/product-management/', 'business free', '📦', 'linear-gradient(135deg,#1a1a2e,#16213e);', 'Free', False, '', '8h', '', 'Business & Management'),
        ('Business Analytics', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/business-analytics/', 'business free', '📊', 'linear-gradient(135deg,#1a1a2e,#16213e);', 'Free', False, '', '10h', '', 'Business & Management'),
        ('Entrepreneurship', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/entrepreneurship/', 'business free', '🚀', 'linear-gradient(135deg,#1a1a2e,#16213e);', 'Free', False, '', '6–8h', '', 'Business & Management'),
        ('Project Management', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/software-engineering/software-project-management-spm/', 'business free', '🗂️', 'linear-gradient(135deg,#1a1a2e,#16213e);', 'Free', False, '', '8h', '', 'Business & Management'),

        # ── GeeksforGeeks – Finance ────────────────────────────────────────────
        ('Financial Modeling', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/finance/types-of-financial-models/', 'finance free', '💰', 'linear-gradient(135deg,#052e16,#166534);', 'Free', False, '', '10h', '', 'Finance'),
        ('Stock Market Basics', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/stock-market/what-is-stock-market/', 'finance free', '📉', 'linear-gradient(135deg,#052e16,#166534);', 'Free', False, '', '6h', '', 'Finance'),
        ('Investment Analysis', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/finance/investment-decision/', 'finance free', '📊', 'linear-gradient(135deg,#052e16,#166534);', 'Free', False, '', '8h', '', 'Finance'),
        ('Accounting Fundamentals', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/accountancy/basic-accounting-concepts/', 'finance free', '🧾', 'linear-gradient(135deg,#052e16,#166534);', 'Free', False, '', '6h', '', 'Finance'),
        ('Excel for Finance', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/excel-tutorial/', 'finance free', '📑', 'linear-gradient(135deg,#052e16,#166534);', 'Free', False, '', '8h', '', 'Finance'),

        # ── GeeksforGeeks – Design ─────────────────────────────────────────────
        ('UI/UX Design', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/ui-ux-design/ui-ux-design-tutorial/', 'design free', '🎨', 'linear-gradient(135deg,#2d1b69,#5b21b6);', 'Free', False, '', '10–12h', '', 'Design'),
        ('Graphic Design', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/graphic-design/what-is-graphic-design/', 'design free', '🖌️', 'linear-gradient(135deg,#2d1b69,#5b21b6);', 'Free', False, '', '8h', '', 'Design'),
        ('Figma', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/figma/figma-tutorial/', 'design free', '✏️', 'linear-gradient(135deg,#2d1b69,#5b21b6);', 'Free', False, '', '5–8h', '', 'Design'),
        ('Canva Design', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/blogs/canva-for-beginners/', 'design free', '🧩', 'linear-gradient(135deg,#2d1b69,#5b21b6);', 'Free', False, '', '4–6h', '', 'Design'),
        ('Web Design', 'GeeksforGeeks', 'https://www.geeksforgeeks.org/web-design/web-design-tutorial/', 'design free', '💻', 'linear-gradient(135deg,#2d1b69,#5b21b6);', 'Free', False, '', '10h', '', 'Design'),

        # ── GeeksforGeeks – Science ────────────────────────────────────────────
        ("Bioinformatics", "GeeksforGeeks", "https://www.geeksforgeeks.org/bioinformatics/what-is-bioinformatics/", "science free", "🧬", "linear-gradient(135deg,#0c4a6e,#0369a1);", "Free", False, "", "8h", "", "Science"),
        ("Biotechnology Basics", "GeeksforGeeks", "https://www.geeksforgeeks.org/biology/biotechnology/", "science free", "🔬", "linear-gradient(135deg,#0c4a6e,#0369a1);", "Free", False, "", "6h", "", "Science"),
        ("Environmental Science", "GeeksforGeeks", "https://www.geeksforgeeks.org/environmental-science/", "science free", "🌱", "linear-gradient(135deg,#0c4a6e,#0369a1);", "Free", False, "", "6h", "", "Science"),
        ("Physics Fundamentals", "GeeksforGeeks", "https://www.geeksforgeeks.org/physics/", "science free", "⚛️", "linear-gradient(135deg,#0c4a6e,#0369a1);", "Free", False, "", "8h", "", "Science"),
        ("Chemistry Fundamentals", "GeeksforGeeks", "https://www.geeksforgeeks.org/chemistry/", "science free", "🧪", "linear-gradient(135deg,#0c4a6e,#0369a1);", "Free", False, "", "8h", "", "Science"),

        # ── GeeksforGeeks – Exam Prep ──────────────────────────────────────────
        ("GATE Preparation", "GeeksforGeeks", "https://www.geeksforgeeks.org/gate/", "exam free", "🎓", "linear-gradient(135deg,#431407,#c2410c);", "Free", False, "", "Self-paced", "", "Exam Prep"),
        ("Coding Interview Preparation", "GeeksforGeeks", "https://www.geeksforgeeks.org/interview-preparation-for-software-developer/", "exam free", "👨‍💻", "linear-gradient(135deg,#431407,#c2410c);", "Free", False, "", "20–30h", "", "Exam Prep"),
        ("Quantitative Aptitude", "GeeksforGeeks", "https://www.geeksforgeeks.org/quantitative-aptitude/", "exam free", "➗", "linear-gradient(135deg,#431407,#c2410c);", "Free", False, "", "10–15h", "", "Exam Prep"),
        ("Logical Reasoning", "GeeksforGeeks", "https://www.geeksforgeeks.org/logical-reasoning/", "exam free", "🧠", "linear-gradient(135deg,#431407,#c2410c);", "Free", False, "", "8–12h", "", "Exam Prep"),
        ("Placement Preparation", "GeeksforGeeks", "https://www.geeksforgeeks.org/placements-gq/", "exam free", "📚", "linear-gradient(135deg,#431407,#c2410c);", "Free", False, "", "20h", "", "Exam Prep"),

        # ── YouTube ────────────────────────────────────────────────────────────
        ("JavaScript Full Course — Bro Code (12 hrs)", "YouTube", "https://www.youtube.com/watch?v=lfmg-EJ8gm4", "web free", "🎬", "linear-gradient(135deg,#450a0a,#991b1b);", "Free", False, "⭐ 4.9", "12h", "5M+ views", ""),
        ('Python for Machine Learning & Data Science — freeCodeCamp', 'YouTube', 'https://www.youtube.com/watch?v=7eh4d6sabA0', 'data ml free', '📉', 'linear-gradient(135deg,#3b0764,#6d28d9);', 'Free', False, '⭐ 4.9', '31h', '3M+ views', ''),

        # ── NPTEL ──────────────────────────────────────────────────────────────
        ('Introduction to Machine Learning — IIT Kharagpur', 'NPTEL', 'https://nptel.ac.in/courses/106105152', 'ml free cert', '🤖', 'linear-gradient(135deg,#431407,#c2410c);', 'Free', True, '⭐ 4.8', '8 weeks', '100K+', ''),
        ('Programming in Python — IIT Bombay', 'NPTEL', 'https://nptel.ac.in/courses/106101183', 'data free cert', '🐍', 'linear-gradient(135deg,#172554,#1e3a8a);', 'Free', True, '⭐ 4.7', '8–12 weeks', '200K+', ''),
        ("Data Science for Engineers", "NPTEL", "https://nptel.ac.in", "data free cert", "📊", "linear-gradient(135deg,#0f172a,#334155);", "Free", True, "⭐ 4.7", "8 weeks", "150K+", ""),
        ('Database Management Systems', 'NPTEL', 'https://nptel.ac.in', 'data free cert', '🗄️', 'linear-gradient(135deg,#1e293b,#475569);', 'Free', True, '⭐ 4.8', '8 weeks', '300K+', ''),
        ('Operating Systems', 'NPTEL', 'https://nptel.ac.in', 'web free cert', '💻', 'linear-gradient(135deg,#111827,#1f2937);', 'Free', True, '⭐ 4.7', '8 weeks', '250K+', ''),
        ('Computer Networks', 'NPTEL', 'https://nptel.ac.in', 'web free cert', '🌐', 'linear-gradient(135deg,#0f172a,#1e40af);', 'Free', True, '⭐ 4.6', '8 weeks', '200K+', ''),
        ('Artificial Intelligence', 'NPTEL', 'https://nptel.ac.in', 'ml free cert', '🧠', 'linear-gradient(135deg,#14532d,#15803d);', 'Free', True, '⭐ 4.7', '8–12 weeks', '180K+', ''),
        ("Software Engineering", "NPTEL", "https://nptel.ac.in", "web free cert", "⚙️", "linear-gradient(135deg,#4c1d95,#7c3aed);", "Free", True, "⭐ 4.6", "8 weeks", "150K+", ""),
        ('Cloud Computing', 'NPTEL', 'https://nptel.ac.in', 'cloud free cert', '☁️', 'linear-gradient(135deg,#1e40af,#3b82f6);', 'Free', True, '⭐ 4.6', '8–12 weeks', '120K+', ''),
        ('Big Data Computing', 'NPTEL', 'https://nptel.ac.in', 'data free cert', '📊', 'linear-gradient(135deg,#065f46,#10b981);', 'Free', True, '⭐ 4.7', '8–12 weeks', '140K+', ''),

        # ── Microsoft Learn ────────────────────────────────────────────────────
        ("Azure Fundamentals (AZ-900)", "Microsoft Learn", "https://learn.microsoft.com/en-us/certifications/azure-fundamentals/", "cloud free cert", "☁️", "linear-gradient(135deg,#0f172a,#2563eb);", "Free", True, "", "20–25h", "", ""),
        ("Azure AI Fundamentals", "Microsoft Learn", "https://learn.microsoft.com/en-us/certifications/azure-ai-fundamentals/", "ml free cert", "🤖", "linear-gradient(135deg,#14532d,#22c55e);", "Free", True, "", "10–15h", "", ""),
        ("Microsoft Power BI Data Analyst", "Microsoft Learn", "https://learn.microsoft.com/en-us/certifications/power-bi-data-analyst-associate/", "data free cert", "📊", "linear-gradient(135deg,#1e3a8a,#3b82f6);", "Free", True, "", "40h", "", ""),
        ("Azure Data Fundamentals", "Microsoft Learn", "https://learn.microsoft.com/en-us/certifications/azure-data-fundamentals/", "data free cert", "📈", "linear-gradient(135deg,#0f172a,#1e40af);", "Free", True, "", "12h", "", ""),
        ("Microsoft 365 Fundamentals", "Microsoft Learn", "https://learn.microsoft.com/en-us/certifications/microsoft-365-fundamentals/", "web free cert", "💼", "linear-gradient(135deg,#4c1d95,#7c3aed);", "Free", True, "", "8–10h", "", ""),
        ("Azure Developer Associate", "Microsoft Learn", "https://learn.microsoft.com/en-us/certifications/azure-developer/", "web free cert", "💻", "linear-gradient(135deg,#1e1b4b,#4c1d95);", "Free", True, "", "40–50h", "", ""),
    ]

    insert_query = """
        INSERT INTO courses (title, platform, link, tags, icon, bg_gradient, badge_type, has_cert, rating, duration, views, department)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    print("Inserting data...")
    cursor.executemany(insert_query, courses_data)
    conn.commit()

    print(f"Successfully migrated {cursor.rowcount} courses.")
    cursor.close()
    conn.close()

if __name__ == '__main__':
    migrate()
