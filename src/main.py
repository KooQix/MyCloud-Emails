from dotenv import load_dotenv
load_dotenv()

import os

import sys

from emails.EmailBase import EmailBase

from emails.EmailCheckIP import EmailCheckIP, EmailCheckIPModel
from emails.EmailSaturatedStorage import EmailSaturatedStorage, EmailSaturatedStorageModel
from emails.EmailErrors import EmailErrors, EmailErrorsModel
from emails.EmailGeneral import EmailGeneral, EmailGeneralModel

from fastapi import FastAPI, HTTPException, Request
import datetime

USAGE="uvicorn main:app"



app = FastAPI()


def send(email: EmailBase):
	try:
		email.send()
		return {"message": "Email sent!"}
	except Exception as e:
		print(datetime.datetime.now().strftime("\n%Y-%m-%d %H:%M:%S:\n"))
		print(f"Error sending email:\n{e.with_traceback()}")

		try:
			err_email = EmailErrors(f"[Error] {email.get_subject()}", f"{e.with_traceback()}")
			err_email.send()
		except Exception as e:
			print(datetime.datetime.now().strftime("\n%Y-%m-%d %H:%M:%S:\n"))
			print(f"Error sending error email:\n{e.with_traceback()}")

		raise HTTPException(status_code=500, detail=f"An error occurred while handling the task: {e}")
	

#########	Endpoints #########

@app.middleware("http")
async def verif_auth(request: Request, call_next):
	try:
		authorization_token = request.headers["Authorization"]
	except Exception:
		raise HTTPException(status_code=401, detail="Unauthorized")

	if authorization_token == os.environ.get("MyCloud_Emails_TOKEN"):
		response = await call_next(request)
		return response
	else:
		raise HTTPException(status_code=401, detail="Unauthorized")


@app.post("/general")
def check_ip(model: EmailGeneralModel):
	return send(EmailGeneral(model.subject, model.body, model.receivers, model.styles))

@app.post("/check-ip")
def check_ip(model: EmailCheckIPModel):
	return send(EmailCheckIP(model.new_ip))


@app.post("/saturated-storage")
def check_ip(model: EmailSaturatedStorageModel):
	return send(EmailSaturatedStorage(model.args))

@app.post("/error")
def check_ip(model: EmailErrorsModel):
	return send(EmailErrors(model.subject, model.error_message))