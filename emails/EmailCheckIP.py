from email.mime.text import MIMEText
from emails.EmailBase import EmailBase


class EmailCheckIP(EmailBase):
	def __init__(self, args):
		self.new_ip = args[0]
		super().__init__()


	def validate_args(args: list):
		return len(args) == 1 and len(args[0].split('.')) == 4

	def err_usage():
		print("args: \n- New IP address")

	def get_subject(self):
		subject = '[MyCloud IP] IP has changed'
		return subject

	def get_receivers(self):
		email_receivers = [
			"kooqix.dev@gmail.com"
		]
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