import pytest
from wumail import EmailExtractor


@pytest.fixture
def urls():
    return [
        'https://creatuaplicacion.com/contacto/',
    ]

@pytest.fixture
def email_extractor(urls):
    return EmailExtractor(urls, remove_duplicates_urls=True)

def test_extract_mails(email_extractor):
    result = email_extractor.extract_emails()
    assert 'contacto@creatuaplicacion.com' in result

def test_failed_extract_mail(email_extractor):
    email_extractor.urls = ['https://wumail.test/failed/']
    result = email_extractor.extract_emails()
    assert isinstance(result, list)