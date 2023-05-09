from emails.EmailBase import EmailBase

from pydantic import BaseModel
from typing import Optional

class EmailGeneralModel(BaseModel):
	"""Send an email when new IP

		Args:
			subject (str): Subject
			body (str): Body
	"""
	receivers: list
	subject: str
	body: str
	styles: Optional[str] = None

class EmailGeneral(EmailBase):
	def __init__(self, subject: str, body: str, receivers: list, styles: str = None):
		"""Send an email when new IP

		Args:
			subject (str): Subject
			body (str): Body (HTML)
			receivers (list): Receivers
			style (Optional[str]): CSS Styles
		"""
		self.subject = subject
		self.body = body
		self.receivers = receivers
		self.styles = styles
		super().__init__()

	def get_subject(self):
		return self.subject

	def get_receivers(self):
		return self.receivers

	def get_html_body(self):
		return self.body

	def get_html_styles(self):
		return self.styles