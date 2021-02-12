
import smtplib
from bs4 import BeautifulSoup 
import requests


# define source
source = requests.get('https://www.universityhealthsystem.com/coronavirus-covid19/vaccine').text

soup = BeautifulSoup(source, 'html.parser')


text = []
for strong in soup.findAll("strong"):
		text.append(strong.get_text())


		

for i in text:
	



	words = "Unfortunately, there are currently no vaccine appointments available. Once we receive more vaccine, we will open this scheduling tool and spread the news widely in the community. "

	if i not in words:

		print(i)
		EMAIL = "EMAIL"
		PASS = "PASSWORD"


		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login(EMAIL, PASS)


			subject = 'VACCINE NOTIFICATION'
			body = 'Vaccine appointments are now available at https://www.universityhealthsystem.com/coronavirus-covid19/vaccine'

			msg = f'Subject: {subject} \n\n{body}'
			recipients = ["recipients"]

			smtp.sendmail(EMAIL, recipients, msg)







