from emails.EmailBase import EmailBase
import os

class EmailErrors(EmailBase):
	def __init__(self, args: list):
		self.subject = args[0]
		self.error_message = args[1]
		super().__init__()

	def validate_args(args: list):
		"""
		Args like: 'subject' 'error_message'
		"""
		return len(args) == 2

	def err_usage():
		print("args: \n- 'subject' 'error_message'")
				

	def get_subject(self):
		return self.subject

	def get_receivers(self):
		email_receivers = os.environ.get('MyCloud_Receivers_Default').replace(' ', '').split(',')
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