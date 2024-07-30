import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "shayanadnan81@gmail.com"
GMAIL_PASSWORD = "xwsb qgej ugys amll"
SHEET_URL = "https://api.sheety.co/0ace4f92ab586922f2e4ac9639572e2d/emails/sheet1"

def fetch_data():
    response = requests.get(SHEET_URL)
    response.raise_for_status()
    return response.json()['sheet1']

def calculate_net_salary(gross_salary):
    if gross_salary <= 50000:
        tax = 0
    elif gross_salary <= 100000:
        tax = 0.025 * (gross_salary - 50000)
    elif gross_salary <= 200000:
        tax = 1250 + 0.125 * (gross_salary - 100000)
    elif gross_salary <= 300000:
        tax = 13750 + 0.225 * (gross_salary - 200000)
    elif gross_salary <= 500000:
        tax = 36250 + 0.275 * (gross_salary - 300000)
    else:
        tax = 91250 + 0.35 * (gross_salary - 500000)

    net_salary = gross_salary - tax
    return net_salary, tax

def send_email(to_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)
        print(f"Email sent to {to_email}")

def main():
    employees = fetch_data()

    if not employees:
        print("No data to process.")
        return

    for employee in employees:
        email = employee.get('email')
        gross_salary = float(employee.get('salary', 0))

        net_salary, tax = calculate_net_salary(gross_salary)

        subject = "Your Salary Details for the Month"
        message = (
            f"Dear Employee,\n\n"
            f"We are pleased to inform you about your salary details for the month:\n\n"
            f"Gross Salary: PKR {gross_salary}\n"
            f"Payroll Tax Deducted: PKR {tax}\n"
            f"Net Salary After Tax: PKR {net_salary}\n\n"
            "Best regards,\n"
            "[Your Company Name]"
        )

        send_email(email, subject, message)

if __name__ == "__main__":
    main()
