
# Wumail   🚀

# Introduction 📓
Wumail is a small library for extracting emails from a list of urls provided by you. The core uses requests_futures for handling large lists of urls.

---
## Installation 📝

To clone the repo, **you need to have git installed on your system.**
```sh
$ git clone https://github.com/Scr44gr/wumail.git
```
... remember to install the requirements!
```sh
$ pip install -r requirements.txt
```

---
## Usage  🚀
### Extracting emails 📧

```python
from wumail import EmailExtractor

urls = []
email_extractor = EmailExtractor(urls)
result = email_extractor.extract_emails()
```
### Change the regex pattern
You can change the regex pattern for more precise/custom extraction.
```python
...
from re import compile

custom_pattern = r'-*([\w\-\.]{1,100}@(?:\w[\w\-]+\.)+(?!png|jpg|svg)[\w]+)-*'

email_extractor.RE_EMAIL_PATTERN = compile(custom_pattern) # You need to compile the pattern!
```
---
## Donate ☕

If you like it you can buy me a coffee! [https://www.buymeacoff.ee/scr44gr](https://www.buymeacoff.ee/scr44gr)

[![Build](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoff.ee/scr44gr)

