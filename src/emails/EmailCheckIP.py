from email.mime.text import MIMEText
from emails.EmailBase import EmailBase
import os

from pydantic import BaseModel

class EmailCheckIPModel(BaseModel):
	"""Send an email when new IP

		Args:
			new_ip (str): New IP
	"""
	new_ip: str


class EmailCheckIP(EmailBase):	
	def __init__(self, new_ip: str):
		"""Send an email when new IP

		Args:
			new_ip (str): New IP
		"""
		self.new_ip = new_ip
		super().__init__()


	def get_subject(self):
		subject = '[MyCloud IP] IP has changed'
		return subject

	def get_receivers(self):
		email_receivers = os.environ.get('MyCloud_Emails_Receivers_CheckIP').replace(' ', '').split(',')
		return email_receivers

	def get_html_body(self):
		html_body = f"""
		<h1>New MyCloud IP: {self.new_ip}</h1>
		"""
		return html_body

	def get_html_styles(self):
		html_styles = """
		h1 {
			color: gray;
			width: 100%;
			margin-top: 5em;
			text-align: center;
		}
		"""
		return html_styles