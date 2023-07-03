from emails.EmailBase import EmailBase
import os

from pydantic import BaseModel

class EmailErrorsModel(BaseModel):
	"""Send email when an error happens

		Args:
			subject (str): Subject
			error_message (str): Error message
	"""
	subject: str
	error_message: str

class EmailErrors(EmailBase):
	def __init__(self, subject: str, error_message: str):
		self.subject = subject
		self.error_message = error_message
		super().__init__()

	def get_subject(self):
		return self.subject

	def get_receivers(self):
		email_receivers = os.environ.get('MyCloud_Emails_Receivers_Default').replace(' ', '').split(',')
		return email_receivers

	def get_html_body(self):
		html_body = f"""
		<h1>An error happened while performing task:</h1>
		<pre>
			{self.error_message}
		</pre>
		<br>Please check the logs for the given application
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
		pre {
			text-align: laft;
		}
		"""
		return html_styles