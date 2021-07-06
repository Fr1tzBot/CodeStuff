# https://github.com/WindowsVistaisCool/discord-slash-requests
import requests
import json
import discord
from discord.ext import commands
from discord_slash import SlashCommand, utils

def store(file, key=None, read=False, val=None):
	with open(file, 'r') as v:
		x = json.load(v)
	if read is not False:
		if key is None:
			return x
		else:
			return x[key]
	else:
		if val is None:
			with open(file, 'w') as v:
				json.dump(key, v, indent=4)
			return
		x[key] = val
		with open(file, 'w') as v:
			json.dump(x, v, indent=4)


head = store('config.json', 'slashConfig', True)['auth']

# internal
def checkURL():
  x = store('config.json', 'slashConfig', True)
  returns = []
  if x['appID'] is not None:
    returns.append(x['appID'])

  if x['guildID'] is not None and x['tempID'] is None:
    returns.append(x['guildID'])
  else:
    returns.append(x['tempID'])

  return returns

class sc:
	def setGID(ngid):
		x = store('config.json', None, True)
		x['slashConfig']['tempID'] = ngid
		store('config.json', x)
		print(f"Set new guild id to {ngid}")
	# Basic functions
	def get(comName=None, all=False):
		k = checkURL()
		url = f"https://discord.com/api/v8/applications/{k[0]}/guilds/{k[1]}/commands"
		f = requests.get(url, headers=head)
		if all is False:
			if comName is not None:
				d = None
				for com in f.json():
					if com['name'] == comName:
						d = com
						break
				return d
			g = []
			for com in f.json():
				name = com['name']
				id = com['id']
				g.append({"name": name, "id": id})
			return g
		return f.json()

	def post(jsonData):
	  k = checkURL()
	  url = f"https://discord.com/api/v8/applications/{k[0]}/guilds/{k[1]}/commands"
	  e = requests.post(url, headers=head, json=jsonData)
	  return e

	def rem(slashName):
		k = checkURL()
		url = f"https://discord.com/api/v8/applications/{k[0]}/guilds/{k[1]}/commands"
		f = requests.get(url, headers=head)
		d = None
		if slashName is not None:
			d = None
			for com in f.json():
				if com['name'] == slashName:
					d = com
					break
			if d is None: return
			id = 'id'
			r = requests.delete(url + f"/{com[id]}", headers=head)
			return r

 	# Permissions
	def perm(commandID, roleIDTuple=None, permTuple=None, *, includeSelf=True, user=None, userPerm=True, setAll=None):
		k = checkURL()
		url = f"https://discord.com/api/v8/applications/{k[0]}/guilds/{k[1]}/commands/{commandID}/permissions"
		eurl = f"https://discord.com/api/v8/applications/{k[0]}/guilds/{k[1]}/commands"
		if setAll is False:
			g = None
			f = requests.get(eurl, headers=head)
			for com in f.json():
				if com['id'] == f"{commandID}":
					g = com
					break
			if g['default_permission'] == True:
				g.pop('id')
				g.pop('version')
				g.pop('application_id')
				g.pop('guild_id')
				g['default_permission'] = False
				d = requests.post(eurl, headers=head, json=g)
				return d
			jData = {
				"permissions": []
			}
			r = requests.put(url, headers=head, json=jData)
			return r
		elif setAll is True:
			g = None
			f = requests.get(eurl, headers=head)
			for com in f.json():
				if com['id'] == f"{commandID}":
					g = com
					break
			g.pop('id')
			g.pop('version')
			g.pop('application_id')
			g.pop('guild_id')
			g['default_permission'] = True
			d = requests.post(eurl, headers=head, json=g)
			return d
		perms = []
		if includeSelf is True or (roleIDTuple is None and staff is False) and user is None:
			selfID = store('config.json', 'slashConfig', True)['selfID']
			selfData = {
				"id": selfID,
				"type": 2,
				"permission": True
			}
			perms.append(selfData)
		if roleIDTuple is not None:
			try:
				count = 0
				for roleID in roleIDTuple:
					permAllow = permTuple[count]
					count += 1
					roleData = {
						"id": roleID,
						"type": 1,
						"permission": permAllow
					}
					perms.append(roleData)
			except:
				return
		if user is not None:
			try:
				uid = str(user)
			except:
				return
			userData = {
				"id": uid,
				"type": 2,
				"permission": userPerm
			}
			perms.append(userData)
		jData = {
			"permissions": perms
		}
		r = requests.put(url, headers=head, json=jData)
		return r

class gl:
    def get(comName=None, all=False):
		k = checkURL()
		url = f"https://discord.com/api/v8/applications/{k[0]}/commands"
		f = requests.get(url, headers=head)
		if all is False:
			if comName is not None:
				d = None
				for com in f.json():
					if com['name'] == comName:
						d = com
						break
				return d
			g = []
			for com in f.json():
				name = com['name']
				id = com['id']
				g.append({"name": name, "id": id})
			return g
		return f.json()

	def post(jsonData):
	  k = checkURL()
	  url = f"https://discord.com/api/v8/applications/{k[0]}/commands"
	  e = requests.post(url, headers=head, json=jsonData)
	  return e

	def rem(slashName):
		k = checkURL()
		url = f"https://discord.com/api/v8/applications/{k[0]}/commands"
		f = requests.get(url, headers=head)
		d = None
		if slashName is not None:
			d = None
			for com in f.json():
				if com['name'] == slashName:
					d = com
					break
			if d is None: return
			id = 'id'
			r = requests.delete(url + f"/{com[id]}", headers=head)
			return r
