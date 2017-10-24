import requests
import threading

def CALL():
	r = requests.post("http://localhost:158", data={'number': 12524})
	print(r.status_code, r.reason)
	print(r.text)

def CACALL():
	for _ in range(100):
		threading.Thread(target = CALL,args = ()).start()

for _ in range(100):
	threading.Thread(target = CACALL,args = ()).start()


