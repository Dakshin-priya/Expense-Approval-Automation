# 💰 Expense Approval Workflow  

## 📌 Problem Statement  
Managing expense approvals manually can be time-consuming and inefficient, especially in organizations with multiple approvers and varying approval limits. The **Expense Approval Workflow** powered by a **Small Language Model (SLM)** streamlines this process by automating key aspects:  

- 🔹 **Automatic substitution** based on vacation periods  
- 🔹 **Predicting approvers** and auto-routing based on spending limits  
- 🔹 **Auto-approving expenses** based on predefined compliance checks  

---

## 💡 Solution  
This project leverages **Generative AI (GenAI)** to create an intelligent **expense approval system** that:  

✔ **Automatically assigns substitute approvers** when the primary approver is on vacation.  
✔ **Predicts the appropriate approver** based on historical data and spending limits.  
✔ **Auto-approves routine expenses** that meet compliance requirements.  

---

## 🚀 Key Features  

### ✅ Automatic Substitution for Vacations  
- 📅 Detects when an approver is on leave.  
- 🔄 Assigns a substitute to ensure uninterrupted workflow.  

### 🔄 Predictive Approver Routing  
- 📊 Analyzes past approvals and spending limits.  
- 🏷 Predicts the best approver for each expense request.  

### 🤖 Auto-Approval of Routine Expenses  
- 📜 Predefined rules check if expenses meet compliance.  
- ⚡ Eligible expenses are **auto-approved** to minimize manual intervention.  

---

## ⚙️ Tech Stack  
- **🖥 Backend**: Flask  
- **🗄 Database**: PostgreSQL  
- **🤖 ML Model**: DistilBERT (Hugging Face Transformers)  
- **📚 Libraries**: Flask-CORS, psycopg2-binary, transformers, torch  

---

💡 **This AI-powered system enhances expense approval efficiency and reduces manual effort.**  
🚀 **Contribute, suggest improvements, or fork the repository!**  
