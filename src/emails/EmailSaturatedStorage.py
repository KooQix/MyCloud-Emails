from emails.EmailBase import EmailBase
import os

from pydantic import BaseModel

class EmailSaturatedStorageModel(BaseModel):
	"""Send email when storage is saturated

		Args:
			args (list): [(disk_name, usage), ...)]
	"""
	args: list

class EmailSaturatedStorage(EmailBase):
	def __init__(self, args: list):
		"""Send email when storage is saturated

		Args:
			args (list): [(disk_name, usage), ...)]
		"""
		self.args = args
		super().__init__()

	def get_subject(self):
		subject = '[MyCloud Saturated Storage] Saturated Storage'
		return subject

	def get_receivers(self):
		email_receivers = os.environ.get('MyCloud_Emails_Receivers_SaturatedStorage').replace(' ', '').split(',')
		return email_receivers

	def get_html_body(self):
		table_content = ''

		for arg in self.args:
			disk_name = arg[0]
			usage = arg[1]
			table_content += f"""
				<tr>
					<td>{disk_name}</td>
					<td>{usage}</td>
				</tr>
			"""
		html_body = f"""
		<table>
			<tr>
				<th>Disk name</th>
				<th>Disk Usage (%)</th>
			</tr>

			{table_content}
		</table>
		"""
		return html_body

	def get_html_styles(self):
		html_styles = """
		table {
			font-family: arial, sans-serif;
			border-collapse: collapse;
			width: 100%;
		}

		td,
		th {
			border: none;
			padding: 8px;
			border-radius: 0.5em;
			text-align: center;
		}
		th {
			background-color: rgb(88, 88, 247);
			color: white;
		}
		td {
			border-bottom: 1px solid #dddddd;
		}
		"""
		return html_styles