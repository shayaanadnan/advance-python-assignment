import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# City ID mapping
CITY_IDS = {
    'Karachi': '1174872',
    'Lahore': '1172451',
    'Islamabad': '1162015'
    # Add more cities as needed
}

def weather_email_message(city_name: str, weather_update: str) -> str:
    '''
    Create good looking HTML based email message and fill with given args.
    '''
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WEATHER UPDATE</title>
</head>
<body style="font-family: Arial, sans-serif; color: #333;">
    <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px;">
        <h2 style="text-align: center; color: #007bff;">Weather Update for {city_name}</h2>
        <p>Dear Employee,</p>
        <p>Here's the latest weather update for your city:</p>
        <table style="border-collapse: collapse; width: 100%; margin-top: 20px;">
            <tr>
                <th style="border: 1px solid #dddddd; text-align: left; padding: 10px; background-color: #f2f2f2;">Description</th>
                <th style="border: 1px solid #dddddd; text-align: left; padding: 10px; background-color: #f2f2f2;">Details</th>
            </tr>
            <tr>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 10px;">Weather</td>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 10px;">{weather_update}</td>
            </tr>
        </table>
        <p style="margin-top: 20px;">Best regards,<br>[Shayan Adnan | Saadullah Khan]</p>
    </div>
</body>
</html>
    """

def fetch_email_and_city(sheety_api: str) -> list:
    '''
    Fetch data from google sheet with the help of `Sheety` by using its API.
    '''
    try:
        response = requests.get(sheety_api)
        response.raise_for_status()
        data = response.json()
        return [(row['email'], row['city']) for row in data['sheet1']]

    except requests.RequestException as e:
        print(f'Error fetching data from Sheety: {e}')
        raise Exception("Can't Fetch the data from google sheet, program can't go further.")

def fetch_weather_update(api_key: str, city_id: str) -> str:
    '''
    Fetch the weather from `Open Weather Map`'s API for given city.
    '''
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric'
    try:
        response = requests.get(weather_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{weather_description}, Temperature: {temperature}°C"
    except requests.RequestException as e:
        print(f'Error fetching weather data: {e}')
        if response is not None:
            print(f'Status Code: {response.status_code}')
            print(f'Response Body: {response.text}')
        return False

def send_email(smtp_server: str, smtp_tls_port: int, email_address: str, email_password: str, to_email: str, subject: str, body:str, html: bool=False) -> bool:
    '''
    Send HTML/PLAIN email through SMTP with TLS encryption.
    '''
    try:
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_email
        msg['Subject'] = subject
        html_or_plain = "html" if html else "plain"
        msg.attach(MIMEText(body, html_or_plain))
        with smtplib.SMTP(smtp_server, smtp_tls_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, to_email, msg.as_string())
            return True
    except smtplib.SMTPException as e:
        print(f'Error sending email to {to_email}. \nError: {e}')
        return False

def get_city_id(city_name: str) -> str:
    '''
    Get cities ID from our saved dictionary/hashmap that will may be used to fetch weather.
    '''
    return CITY_IDS.get(city_name, False)

def main(SHEETY_END_POINT: str, WEATHER_API: str, SMTP_SERVER: str, SMTP_TLS_PORT: int, SMTP_EMAIL: str, SMTP_EMAIL_PASSWORD: str, SUBJECT: str):
    email_city_pairs = fetch_email_and_city(SHEETY_END_POINT)
    for email, city_name in email_city_pairs:
        city_id = get_city_id(city_name)
        if not city_id:
            print(f'City ID not found for {city_name}, Skipped email: {email}')
            continue
        weather_update = fetch_weather_update(WEATHER_API, city_id)
        if not weather_update:
            print(f"Can't Fetch weather. \nDetails -> city: {city_name} | ID: {city_id}")
            continue
        body = weather_email_message(city_name, weather_update)
        mail_status = send_email(SMTP_SERVER, SMTP_TLS_PORT, SMTP_EMAIL, SMTP_EMAIL_PASSWORD, email, SUBJECT, body, html=True)
        if not mail_status:
            print(f"Weather update can't be sent to '{email}' for city {city_name}")
        else:
            print(f"Successfully fetched the weather and sent to '{email}'")
