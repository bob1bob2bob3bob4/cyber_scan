import requests
import sys
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class NESSUS_API(object):


	def __init__(self, host='localhost', port=8834, username=None, password=None):
		
		self.username = username
		self.password = password
		self.base_url = "https://{}:{}".format(host, port)
		self.session = requests.Session()
		self.headers = {
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Referer": self.base_url,
		"Content-Type": "application/json",
		"Connection": "close"
		}


	def get_token(self):

		url = self.base_url + "/session"
		auth = {"username":self.username, "password": self.password}
		token = self.session.post(url, auth, self.headers, verify=False)
		if token.status_code == 200:
			return json.loads(token.text)["token"]
		else:
			raise Exeception("[-] Cannot get login token")
			exit(1)


	def login(self):
		if self.username is None or self.password is None:
			raise Exeception("[-] No username or password")
		else:
			self.token = self.get_token()
			self.headers ["X-Cookie"] = "token={}".format(self.token)


	def get_session(self):
		url = self.base_url + "/session"	
		resp = self.session.get(url, headers=self.headers)	
		return resp.text



	def get_folders(self):
		url = self.base_url + "/folders"	
		resp = self.session.get(url, headers=self.headers)	
		return resp.text


	def get_scans(self):
		url = self.base_url + "/scans"	
		resp = self.session.get(url, headers=self.headers)	
		return resp.text	