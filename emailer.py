import requests
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import datetime
import os
from jsonpath_ng import jsonpath, parse

load_dotenv()

def main():
    data = []
    with open('./config.json') as f:
        data = json.load(f)
        response_data = []
        for i in range(len(data)):
            if data[i]['request_type'] == "html":
                try:
                    response = requests.get(data[i]['source'])
                    soup = BeautifulSoup(response.content, 'html.parser')
                    element = soup.select(data[i]['path'])
                    response_data.append(element[data[i]["select_index"]].get_text())
                except:
                    print("Failed to fetch source: " + data[i]['source'])
                    response_data.append("Error")
            if data[i]['request_type'] == 'json-api':
                try:
                    response = requests.get(data[i]['source'])
                    response = json.load(response)
                    jsonpath_expression = parse(data[i]['path'])
                    jsonpath_expression.find(response)[0]
                except:
                    print("Failed to fetch source: " + data[i]['source'])
                    response_data.append("Error")

        formatted_body = ""
        for d in range(len(data)):
            formatted_body += f"<h3>- {data[d]['title']}: {response_data[d]}</h3>"

        final_html = f"""
        <html>
        <body style='font-family:monospace;color:black'>
        <h1>{datetime.datetime.now().strftime('%Y-%m-%d')}</h1>
        {formatted_body}
        </body>
        </html>
        """

        a = requests.post(
        f"https://api.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={"from": os.getenv("MAILGUN_FROM"),
              "to": os.getenv("MAILGUN_TO"),
              "subject": "Your Daily Vigilance Report",
              "html": final_html})
        print(a)

if __name__ == '__main__':
    main()
