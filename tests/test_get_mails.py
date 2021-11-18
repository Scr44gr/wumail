import pytest
from wumail import EmailExtractor

@pytest.fixture
def html_content():
    return '''
    <html>
    <head>
    <title>Test</title>
    </head>
    <body>
    <h1>Test</h1>
    <p>This is a test: mail@testmail.com/p>
    </body>
    </html>
    '''

@pytest.fixture
def email_extractor():
    return EmailExtractor([''], remove_duplicates_urls=True)

def test_get_mails(html_content, email_extractor):
    assert 'mail@testmail.com' in email_extractor.get_emails(html_content)