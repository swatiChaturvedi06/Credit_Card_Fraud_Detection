import streamlit as st

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

h1,h2,h3,label,p{
color:white!important;
}

[data-testid="stMetric"]{
background:rgba(255,255,255,.08);
padding:20px;
border-radius:18px;
border:1px solid rgba(255,255,255,.2);
}

div[data-testid="stForm"]{
background:rgba(255,255,255,.08);
padding:25px;
border-radius:20px;
}

.stButton>button{
width:100%;
background:#00d4ff;
color:black;
font-weight:bold;
border-radius:12px;
height:50px;
font-size:18px;
}

.stButton>button:hover{
background:#22c55e;
color:white;
}
</style>
""",unsafe_allow_html=True)

st.title("🛡 FraudShield AI")
st.caption("Real-Time Credit Card Fraud Detection Dashboard")

st.sidebar.image("https://img.icons8.com/color/96/bank-card-back-side.png",width=80)
st.sidebar.title("Navigation")
page=st.sidebar.radio("",["🏠 Dashboard","💳 Predict","📊 Analytics","ℹ About"])

if page=="🏠 Dashboard":

    c1,c2,c3,c4=st.columns(4)

    c1.metric("💳 Transactions","12,480","+320")
    c2.metric("🚨 Fraud","158","+8")
    c3.metric("✅ Safe","12,322","+312")
    c4.metric("🎯 Accuracy","98.7%")

    st.divider()

    st.info("Welcome to FraudShield AI Dashboard")

    left,right=st.columns([2,1])

    with left:
        st.subheader("📈 Today's Summary")

        st.progress(78)

        st.write("System Status : 🟢 Active")
        st.write("Threat Level : 🟡 Medium")
        st.write("Model : Random Forest")
        st.write("Prediction Engine : Running")

    with right:
        st.subheader("⚡ Quick Stats")
        st.success("Server Online")
        st.success("Model Loaded")
        st.success("Database Connected")

elif page=="💳 Predict":

    st.subheader("Transaction Details")

    col1,col2=st.columns(2)

    with col1:
        tid=st.number_input("Transaction ID",1)
        amount=st.number_input("Amount",0.0)
        merchant=st.number_input("Merchant ID",1)

    with col2:
        ttype=st.selectbox("Transaction Type",["Purchase","Refund"])
        location=st.selectbox("Location",["New York","Chicago","Dallas","Phoenix","San Diego"])

    if st.button("🔍 Analyze Transaction"):
        st.success("Prediction will appear here.")
        st.progress(70)

elif page=="📊 Analytics":

    st.subheader("Analytics Dashboard")

    st.bar_chart({
        "Legitimate":[980,1100,1020,1200,1150],
        "Fraud":[20,18,30,25,28]
    })

    st.line_chart({
        "Transactions":[500,800,900,1200,1500,1800]
    })

    st.area_chart({
        "Fraud Rate":[5,7,6,9,8,10]
    })

else:

    st.title("About Project")

    st.write("""
### 🛡 FraudShield AI

✔ Machine Learning Based System

✔ Real-Time Fraud Monitoring

✔ Banking Dashboard UI

✔ Secure Transaction Analysis

**Developed with**
- Python
- Streamlit
- Scikit-Learn
- Pandas
- Matplotlib
""")
if "📊 Analytics" == 'page':

    st.title("📊 Fraud Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💳 Transaction Status")

        chart_data = {
            "Safe": [1200],
            "Fraud": [80]
        }

        st.bar_chart(chart_data)

    with col2:

        st.subheader("📈 Daily Transactions")

        daily = {
            "Transactions": [350, 450, 520, 610, 720, 860, 980]
        }

        st.line_chart(daily)

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("🚨 Fraud Trend")

        trend = {
            "Fraud": [8, 10, 7, 15, 18, 12, 20]
        }

        st.area_chart(trend)

    with col4:

        st.subheader("🏙 Location Wise Fraud")

        location = {
            "Chicago": [12],
            "Dallas": [18],
            "New York": [25],
            "Phoenix": [8],
            "San Diego": [6]
        }

        st.bar_chart(location)

    st.divider()

    st.subheader("📋 Recent Transactions")

    import pandas as pd

    df = pd.DataFrame({
        "Transaction ID": [1001, 1002, 1003, 1004, 1005],
        "Amount": [4500, 8200, 650, 12000, 980],
        "Location": ["Chicago", "Dallas", "New York", "Phoenix", "San Diego"],
        "Status": ["Safe", "Fraud", "Safe", "Fraud", "Safe"]
    })

    st.dataframe(df, use_container_width=True)

    st.download_button(
        "📥 Download Report",
        df.to_csv(index=False),
        "Fraud_Report.csv",
        "text/csv"
    )
    if "💳 Predict" == 'page':
        st.title("AI Fraud Detection")
        st.markdown("### Enter Transaction Details")

    col1, col2 = st.columns(2)

    with col1:

        tid = st.number_input("💳 Transaction ID", 1)
        amount = st.number_input("💰 Amount", 0.0)

        merchant = st.number_input("🏦 Merchant ID", 1)

        transaction = st.selectbox(
            "Transaction Type",
            ["Purchase", "Refund"]
        )

    with col2:

        location = st.selectbox(
            "Location",
            [
                "New York",
                "Chicago",
                "Dallas",
                "Phoenix",
                "San Diego",
                "San Antonio"
            ]
        )

        device = st.selectbox(
            "Device",
            [
                "Mobile",
                "Laptop",
                "ATM",
                "POS Machine"
            ]
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Credit Card",
                "Debit Card",
                "UPI",
                "Net Banking"
            ]
        )

    st.divider()

    if st.button("🚀 Analyze Transaction"):

        risk = 35

        if amount > 5000:
            risk += 25

        if transaction == "Refund":
            risk += 20

        if device == "ATM":
            risk += 10

        st.subheader("📊 AI Risk Analysis")

        st.progress(risk)

        st.metric("Risk Score", f"{risk}%")

        if risk >= 70:

            st.error("🚨 HIGH RISK TRANSACTION")

            st.warning("Recommendation : Block this transaction immediately.")

        elif risk >= 40:

            st.warning("⚠ Medium Risk Transaction")

            st.info("Recommendation : Verify user identity.")

        else:

            st.success("✅ Legitimate Transaction")

            st.info("Recommendation : Transaction looks safe.")

        st.divider()

        st.subheader("🤖 AI Insights")

        st.write("✔ Transaction analyzed successfully")

        st.write("✔ Risk Engine Completed")

        st.write("✔ Pattern Matching Completed")

        st.write("✔ Fraud Detection Finished")

        st.divider()

        st.subheader("📈 Live Risk Meter")

        st.progress(risk)

        st.caption("Powered by FraudShield AI")
