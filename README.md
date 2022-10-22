# Daily Quote Inspiration - Start your day right!
Wake up everyday on the positive note and let the first thing your mind see is something that'll get you pumped and out of bed ready to attack the day!

<p align="center">
<img src="https://i.imgur.com/LHCJZ2M.gif" height="500px" />
</p>

## How It's made: 
<p align="left">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" height=25>
</p>

<b>Technologies & Tools Utilized:</b> Python, Twilio API, other RESTful API.</b> This application creates automated scheduled text messages to opted in users at 7:00AM every day. These text messages are daily quotes that are being fetched from a free third-party api full of collections of inspirational quotes and uses Twilio's API to allow messaging between the server and the users phone. 

- I started off by importing the `Request` library for Python to start making API calls.
- I linked my Twilio account data such as `account_sid` and `auth_token` to allow me to start sending text messages to verified phone accounts.
- I used the `random` library to fetch one random quote from the API and use that data to send it to users.

## Lessons Learned
- This was my first project I've built in Python and it was a lot of fun learning the syntax and finally having a chance to integrate Twilio into a project. I learnt a ton in a short amount of time building this project such as fetching data from a third-party api in python, using the `random` library,  integrating Twilio and setting up automated task. 

## Installation: 
1. Clone repository
2. `pip install request, twilio, schedule`
3. Create or link your Twilio account and fill in your `account_sid` and `auth_token`
4. Add in your Twilio number and the targeted number you would like to have the message sent to.



## Future Optimizations:
- Created a paid Twilio account
- Integrate a frontend for users to register their number into a database that will be used for allowing multi-user SMS. (Currently twilio's free account only lets you set up one number)

<h2 align="center">
More Projects
</h2>
<table bordercolor="#66b2b2">
  <tr>
    <td width="33.3%"  style="align:center;" valign="top">
<a target="_blank" href="https://github.com/ssaryonjr/Chit-chat" align="center">Chitchat - Messaging App</a>
        <br />
      <a target="_blank" href="https://github.com/ssaryonjr/Chit-chat">
            <img src="https://github.com/ssaryonjr/ssaryonjr/raw/main/chitchat.gif?raw=true" width="100%" height="210px" />
        </a>
    </td>
    <td width="33.3%" valign="top">
<a target="_blank" href="https://github.com/ssaryonjr/iMovie-Reviews"> iMovie Reviews</a>
      <br />
        <a target="_blank" href="https://github.com/ssaryonjr/iMovie-Reviews">
          <img src="https://github.com/ssaryonjr/ssaryonjr/raw/main/imovie.gif?raw=true" width="100%" height="210px" />
        </a>
    </td>
    <td width="33.3%" valign="top">
<a target="_blank" href="https://github.com/ssaryonjr/iMovie-Reviews">T&K Nigerian Restaurant</a>
        <br />
        <a target="_blank" href="https://github.com/ssaryonjr/Naruto-Character-Selector">
          <img src="https://github.com/ssaryonjr/ssaryonjr/raw/main/ezgif.com-gif-maker%20(5).gif?raw=true" width="100%" height="210px" alt="Portfolio"/>
        </a>
    </td>
  </tr>
</table>
