import requests

email={'name':'AnnMarie',
		'lastname':'Torres',
		'email':'annmarietorres@outlook.com',
		'message':'I am brand new to Python!'}

r=requests.post('https://lambdaschool.com/contact-form',json=email)

print(r.text)