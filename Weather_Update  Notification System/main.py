from weather_email import main

# Constants
SMTP_EMAIL = r"shayanadnan81@gmail.com"
SMTP_EMAIL_PASSWORD = r"ofpx drua dled vjzh"
SMTP_SERVER = r"smtp.gmail.com"
SMTP_TLS_PORT = 587

OPEN_WEATHER_MAP_API = '60a72eaebe920a0542bca714b9111b81'
SHEETY_END_POINT = 'https://api.sheety.co/0ace4f92ab586922f2e4ac9639572e2d/emails/sheet1'

SUBJECT = "Daily Weather Update"

if __name__ == "__main__":
    main(SHEETY_END_POINT, OPEN_WEATHER_MAP_API, SMTP_SERVER, SMTP_TLS_PORT, SMTP_EMAIL, SMTP_EMAIL_PASSWORD, SUBJECT)
