__author__ = 'Scr44gr'
from queue import Queue
from typing import List
from requests_futures.sessions import FuturesSession
from requests import Response
from re import compile, Pattern
from .utils import clean_urls
from requests.exceptions import ConnectionError


class EmailExtractor:
    """
    Class to extract emails from a queue of urls.
    """
    RE_EMAIL_PATTERN : Pattern = compile(r'[\w\.-]+@[\w\.-]+')
    MAX_WORKERS: int = 10

    def __init__(self, urls: List[str], **kwargs):
        self.urls: List[str] = urls
        self.emails : Queue = Queue()
        self.set_up_environment(**kwargs)

    def set_up_environment(self, **kwargs):
        """
        Set up environment for the process.
        """
        if kwargs.get('remove_duplicates_urls'):
            filename: str = kwargs.get('cache_filename', './cache.pkl')
            self.urls: List[str] = clean_urls(self.urls, filename)

        if kwargs.get('custom_email_pattern'):
            self.RE_EMAIL_PATTERN: Pattern = compile(kwargs.get('custom_email_pattern'))

        if kwargs.get('max_workers'):
            self.MAX_WORKERS: int = kwargs.get('max_workers')

    def extract_emails(self):
        """
        Extract emails from queue of urls.

        for this process we use requests_futures.
        """
        session = FuturesSession(max_workers=self.MAX_WORKERS)
        queue = Queue()
        for url in self.urls:
            queue.put(session.get(url))

        return self._extract_emails_from_queue(queue)
    
    def _extract_emails_from_queue(self, queue: Queue):
        
        while not queue.empty():
            try:
                response : Response = queue.get().result()
                if response.status_code == 200:
                    extracted_emails: List[str] = self.get_emails(response.text)
                    [self.emails.put(email) for email in extracted_emails if email not in self.emails.queue]
            except (ConnectionError, RecursionError):
                continue
        return list(self.emails.queue)

    def get_emails(self, text: str):
        """
        Extract emails from a text.
        """
        return list(set([email.group() for email in self.RE_EMAIL_PATTERN.finditer(text)]))

    @property
    def current_emails(self):
        """
        Get current emails.
        """
        return self.emails.queue

    @property
    def current_emails_size(self):
        """
        Get current emails size.
        """
        return self.emails.qsize()