from dotenv import load_dotenv
load_dotenv()

import sys
from emails.EmailBase import EmailBase

from emails.EmailCheckIP import EmailCheckIP

USAGE="python main.py <email-type> <args>"

COMMANDS: dict[str, EmailBase] = {
	"check-ip": EmailCheckIP
}

def print_usage():
	print(USAGE)
	print("\nAvailable email-type: ")
	print(list(COMMANDS.keys()))
	print("\n")


email_type = sys.argv[1]
if email_type in COMMANDS.keys():
	# Verification for each
	email_class = COMMANDS[email_type]
	args = sys.argv[2:] if len(sys.argv) > 2 else []

	if email_class.validate_args(args):
		try:
			em: EmailBase = email_class(args)
			em.send()
			print("Sent!")

		except Exception as e:
			print_usage()
			print(f"--- {email_class.__name__} ---\n")
			email_class.err_usage()
			print("\n")
			print("Error sending email: ")
			print(e.with_traceback())
	else:
		print_usage()
		print(f"--- {email_class.__name__} ---\n")
		email_class.err_usage()

else:
	print_usage()