# MyCloud Emails

Send various type of emails from MyCloud

# Set up gmail account

https://www.youtube.com/watch?v=g_j6ILT-X0k&t=124s

# Set up environment variables

```shell
cp src/.env-example src/.env
```

Then fill in the variables in `.env` file

# Build

```shell
docker build -t mycloud_emails:v1 .
```

# Run

```shell
docker run -d --restart unless-stopped -p 8000:8000 --name mycloud_emails -it `docker images | grep mycloud_emails | awk 'NR==1{print $3}'`
```

# Example Usage

```python
import requests, os

headers = {
	'Authorization': os.environ.get('MYCLOUD_EMAILS_TOKEN')
}

res = requests.post(f"{url_base}/general", json={
	"receivers": list_receivers,
	"subject": subject,
	"body": html_body,
	"styles": Optional[str]
	},
	headers=headers
)

print(res.status_code)
print(res.json())
```
