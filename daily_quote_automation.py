import requests, schedule, random
from twilio.rest import Client

#Collection of quotes from public third-party API. 
response = requests.get('https://type.fit/api/quotes')
quote_collection = response.json()
randomQuote = quote_collection[random.randint(0, len(quote_collection)-1)]

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_message(quote):
    account_sid = 'TWILIO_ACCOUNT_SID'
    auth_token = 'TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)
    quote_text, author = quote.values()

    message = client.messages \
                .create(
                    body= f"{quote_text} — {author}",
                    from_='TWILIO_NUMBER',
                    to='TARGETED_NUMBER'
                 )
    return message.body


#New quote will be scheduled once per day.
schedule.every().day.at("07:30").do(send_message(randomQuote))
