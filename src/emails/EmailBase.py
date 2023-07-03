import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import pathlib



from abc import abstractmethod, abstractstaticmethod

class EmailBase():
	"""Base class for sending email
	"""
	sender_email = os.environ.get("MyCloud_Emails_SENDER")
	sender_pass = os.environ.get("MyCloud_Emails_PASS")

	def __init__(self):
		self.message = MIMEMultipart("related")
		self.message["From"] = EmailBase.sender_email
		self.receiver_emails = self.get_receivers()

		self.message["Subject"] = self.get_subject()
		self.content = self.get_html(self.get_html_body(), self.get_html_styles())


	def send(self):
		# Attach html to message
		self.base_attach()
		self.attach()


		# Create secure connection with server and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(self.sender_email, self.sender_pass)

			for receiver_email in self.receiver_emails:
				self.message["To"] = receiver_email
				server.sendmail(self.sender_email, receiver_email, self.message.as_string())


	def base_attach(self):
		"""Add html parts to message
		"""
		self.message.attach(MIMEText(self.content, "html"))

		# Add app Icon
		fp = open(str(pathlib.Path(__file__).parent.resolve()) + "/../../resources/mycloud-icon.png", 'rb')
		msgImage = MIMEImage(fp.read())
		fp.close()
		msgImage.add_header("Content-ID", "<mycloudIcon>")
		self.message.attach(msgImage)


	def get_html(self, html_body: str, styles = None):
		"""HTML base template for email
		"""
		html_styles = styles if styles != None else ''
		return """
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Parisienne">
					<style>
					.foot {
							margin-top: 3em;
							display: flex;
							align-items: center;
							justify-content: right;
							width: 100%;
						}

						.sign {
							margin-left: 0.5em;
							text-align: center;
							justify-content: center;
							align-items: center;
							color: #2e4053;

							font-family: Parisienne;;
							font-size: 2em;
						}

						img {
							height: 4em;
							width: 4em;
						}

						@media screen and (max-width: 890px) {
							body {
								padding-left: 0;
								padding-right: 0;
								margin-left: 0;
								margin-right: 0;
							}

							.sign {
								font-size: 1.5em;
							}

							img {
							height: 3em;
							width: 3em;
							}
						}

		""" + html_styles + """
					</style>
				</head>
				<body>
			""" + html_body + """

				<div class="foot">
						<img src="cid:mycloudIcon" alt="icon" />
						<h3 class="sign">MyCloud</h3>
					</div>
				</body>
			</html>
			"""

	
	
	#################### To Override ####################
	

	@abstractmethod
	def get_subject(self):
		"""Return subject of email

		Returns:
			str: Subject of the email
		"""
		subject = ''
		return subject

	@abstractmethod
	def get_receivers(self):
		"""Get the receivers of the email

		Returns:
			list[str]: List of email receivers
		"""
		email_receivers = []
		return email_receivers

	@abstractmethod
	def attach(self):
		"""To attach files to email
		"""
		pass

	@abstractmethod
	def get_html_body(self):
		"""Get the html body of the email

		Returns:
			str: HTML body of the email
		"""
		html_body = ''
		return html_body

	@abstractmethod
	def get_html_styles(self):
		"""Get the html styles of the email

		Returns:
			str: HTML styles of the email
		"""
		html_styles = ''
		return html_styles

