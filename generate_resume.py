import os
from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        # Top banner with name and contact
        self.set_fill_color(10, 10, 15) # Dark theme color #0a0a0f
        self.rect(0, 0, 210, 40, 'F')
        
        # Name
        self.set_xy(15, 10)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 24)
        self.cell(0, 10, 'FRED OTIENO', ln=1)
        
        # Title
        self.set_x(15)
        self.set_font('Helvetica', '', 12)
        self.set_text_color(0, 201, 255) # Cyan accent
        self.cell(0, 5, 'Full-Stack Web Developer (MERN Stack)', ln=1)
        
        # Contact Info
        self.set_xy(110, 12)
        self.set_font('Helvetica', '', 9)
        self.set_text_color(243, 244, 246)
        self.cell(0, 4, 'Nairobi, Kenya', ln=1, align='R')
        self.set_x(110)
        self.cell(0, 4, 'obachi62@gmail.com', ln=1, align='R')
        self.set_x(110)
        self.cell(0, 4, '+254 782 091 381', ln=1, align='R')
        self.set_x(110)
        self.cell(0, 4, 'github.com/fred4377', ln=1, align='R')
        
        self.ln(20) # Spacer below header banner

    def section_heading(self, label):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(26, 115, 232) # Blue accent #1a73e8
        self.cell(0, 8, label.upper(), ln=1)
        self.set_draw_color(26, 115, 232)
        self.set_line_width(0.5)
        self.line(self.get_x(), self.get_y(), self.get_x() + 180, self.get_y())
        self.ln(4)

    def section_content(self, text, bold_prefix="", font_size=10, is_bullet=False):
        self.set_font('Helvetica', '', font_size)
        self.set_text_color(55, 65, 81) # Slate 700
        
        if is_bullet:
            self.cell(6, 5, chr(149), ln=0, align='C') # Bullet symbol
            self.set_x(self.get_x() + 1)
            
        if bold_prefix:
            self.set_font('Helvetica', 'B', font_size)
            self.cell(self.get_string_width(bold_prefix) + 1, 5, bold_prefix, ln=0)
            self.set_font('Helvetica', '', font_size)
            
        # Multi-line cell for text
        self.multi_cell(0, 5, text)
        self.set_x(15) # Reset left indent

def create_resume():
    pdf = ResumePDF('P', 'mm', 'A4')
    pdf.set_margins(15, 15, 15)
    pdf.add_page()
    
    # 1. Summary
    pdf.section_heading('Professional Summary')
    pdf.section_content(
        "Passionate and detail-oriented Full-Stack Web Developer with 3+ years of experience specializing "
        "in the MERN stack (MongoDB, Express.js, React.js, Node.js). A graduate of Inceptor Institute of "
        "Technology, with a proven track record of designing, building, and deploying 9+ dynamic web "
        "applications. Specialized in combining modern, humanized user interfaces with secure, efficient "
        "backend logic, RESTful API integrations, and localized payment features."
    )
    pdf.ln(4)
    
    # 2. Experience
    pdf.section_heading('Work Experience')
    
    # Freelance
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(17, 24, 39)
    pdf.cell(130, 5, 'Full-Stack Web Developer (Freelance Consultants)', ln=0)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, '2023 - Present', ln=1, align='R')
    pdf.ln(1)
    pdf.section_content("Develop and deploy high-performance full-stack web applications for local and global clients.", is_bullet=True)
    pdf.section_content("Build responsive, pixel-perfect frontend interfaces using React.js, TailwindCSS, and Bootstrap.", is_bullet=True)
    pdf.section_content("Develop secure backend servers and APIs with Node.js/Express, managing databases with MongoDB.", is_bullet=True)
    pdf.section_content("Integrate localized functionalities, including Lipa na M-Pesa STK push portals and Nairobi CBD delivery systems.", is_bullet=True)
    pdf.ln(3)
    
    # Academic projects
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(17, 24, 39)
    pdf.cell(130, 5, 'Software Developer (Academic & Portfolio Deployments)', ln=0)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, '2023 - 2025', ln=1, align='R')
    pdf.ln(1)
    pdf.section_content("Collaborated on coursework and portfolio-grade project deployments focusing on version control and speed.", is_bullet=True)
    pdf.section_content("Managed application builds and static assets deployments to Netlify, Vercel, and GitHub Pages.", is_bullet=True)
    pdf.ln(4)
    
    # 3. Education
    pdf.section_heading('Education')
    
    # Inceptor
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(17, 24, 39)
    pdf.cell(130, 5, 'Software Development & Full-Stack Web Development', ln=0)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, '2023 - Present', ln=1, align='R')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(75, 85, 99)
    pdf.cell(0, 5, 'Inceptor Institute of Technology -- Nairobi, Kenya', ln=1)
    pdf.ln(2)
    
    # Nyakach
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(17, 24, 39)
    pdf.cell(130, 5, 'Certificate in Information Communication Technology (ICT)', ln=0)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, '2021 - 2023', ln=1, align='R')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(75, 85, 99)
    pdf.cell(0, 5, 'Nyakach Technical and Vocational College (TVC) -- Nyakach, Kenya', ln=1)
    pdf.ln(4)

    # 4. Technical Skills
    pdf.section_heading('Technical Skills')
    pdf.section_content("React.js, JavaScript (ES6+), TypeScript, HTML5, CSS3, Tailwind CSS, Bootstrap", bold_prefix="Frontend:")
    pdf.section_content("Node.js, Express.js, Python, PHP, RESTful APIs, JWT Auth", bold_prefix="Backend:")
    pdf.section_content("MongoDB, Mongoose ODM", bold_prefix="Databases:")
    pdf.section_content("Git, GitHub, VS Code, npm, yarn, Vercel, Netlify, Render", bold_prefix="DevOps & Tools:")
    pdf.section_content("Requirements gathering, time management, active debugging, communication", bold_prefix="Soft Skills:")

    # Output file
    pdf_path = os.path.join(os.getcwd(), 'Fred_Otieno_Resume.pdf')
    pdf.output(pdf_path, 'F')
    print(f"Resume generated successfully at: {pdf_path}")

if __name__ == '__main__':
    create_resume()
