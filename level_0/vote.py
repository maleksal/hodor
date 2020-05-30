import requests

payload = {
    'id': '1419',
    'holdthedoor': 'Submit'}

for i in range(1024):
    requests.post("http://158.69.76.135/level0.php", data=payload)
