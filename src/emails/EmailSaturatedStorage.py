from emails.EmailBase import EmailBase
import os

class EmailSaturatedStorage(EmailBase):
	def __init__(self, args: list):
		self.args = args[0].replace(' ', '').split(',')
		super().__init__()

	def validate_args(args: list):
		"""
		Args like "name_disk_1: percentage_usage, name_disk_2: percentage_usage"
		"""
		return len(args) == 1 and len(args[0].split(':')) > 0

	def err_usage():
		print("args: \n- 'name_disk_1: percentage_usage, name_disk_2: percentage_usage'")

	def get_subject(self):
		subject = '[MyCloud Saturated Storage] Saturated Storage'
		return subject

	def get_receivers(self):
		email_receivers = os.environ.get('MyCloud_Receivers_SaturatedStorage').replace(' ', '').split(',')
		return email_receivers

	def get_html_body(self):
		table_content = ''

		for arg in self.args:
			disk_name = arg.split(':')[0]
			usage = arg.split(':')[1]
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