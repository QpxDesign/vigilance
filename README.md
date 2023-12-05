## Vigilance: Keep Track of the Web
### Mailgun-Powered Emails of Data Scraped from Webpages

### How to use
1. Create a [mailgun](https://www.mailgun.com/) account, and add in all your credentials into a .env file like so:
```
MAILGUN_DOMAIN=""
MAILGUN_API_KEY=""
MAILGUN_FROM="
MAILGUN_TO="
```
2. Install dependencies (`pip install -r requirements.txt`)
3. Add in your desired webpages/API endpoints to the config.json file (it contains a few template entries)
4. Conduct a test run, to make sure your HTML Query Selectors and/or JSON paths work
5. Add it to your crontab, or otherwise schedule it

### Config Reference
```
  {
    "source":"https://example.com", - SOURCE URL
    "request_type":"html", - Either HTML or json-api
    "path":"", - Either HTML element selector (like .class div) or JSON path (like data.contents.text)
    "select_index":0, Only used with HTML, index of selected element (when there are more than one elements selected)
    "title":""
  }
```
