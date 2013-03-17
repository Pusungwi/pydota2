#!/usr/bin/env python

# pydota2 v0.1
# Dota 2 WebAPI in Python module
# Author : Yi 'Pusungwi' Yeon Jae
# License : New BSD License

import os
import json
import urllib.request, urllib.parse

VERSION_NUMBER = 0.1
WEBAPI_KEY = "E1005C7F35530B7E4E462FF4C5090253"
#see http://wiki.teamfortress.com/wiki/WebAPI/GetMatchHistory
GAME_MODE = ["All Pick", "Single Draft", "All Random", "Random Draft", "Captain's Draft", "Captain's Mode", "Death Mode",
 "Diretide", "Reverse Captain's Mode", "The Greeviling", "Tutorial", "Mid Only", "Least Played", "New Player Pool"]

class pyDota2:
	def __init__(self, apiKey):
		#very basic dota2 json webapi
		print("pydota2 " + str(VERSION_NUMBER))
		
		#check unauthorized webapi key
		testAuthorizationUrl = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=" + apiKey
		requestHtml = urllib.request.urlopen(testAuthorizationUrl)

		self.webApiKey = apiKey

	def getMatchDetailDict(self, matchID):
		#TODO: get match detail dict from match id

	def getMatchHistoryDict(self, playerName=None, heroID=None, gameMode=None, skill=None, minDate=None, maxDate=None, 
		minPlayers=None, accountID=None, leagueID=None, startMatchID=None, matchesRequested=None, tournamentGamesOnly=False):
		optionalUrl = ""
		if playerName != None:
			optionalUrl += "player_name=" + urllib.parse.quote(playerName) + "&"
		if heroID != None:
			optionalUrl += "hero_id=" + str(heroID) + "&"
		if gameMode != None:
			optionalUrl += "game_mode=" + str(gameMode) + "&"
		if skill != None:
			optionalUrl += "skill=" + str(skill) + "&"
		if minDate != None:
			optionalUrl += "date_min=" + str(minDate) + "&"
		if maxDate != None:
			optionalUrl += "date_max=" + str(minDate) + "&"
		if minPlayers != None:
			optionalUrl += "min_players=" + str(minDate) + "&"
		if accountID != None:
			optionalUrl += "account_id=" + str(minDate) + "&"
		if leagueID != None:
			optionalUrl += "league_id=" + str(minDate) + "&"	
		if startMatchID != None:
			optionalUrl += "start_at_match_id=" + str(startMatchID) + "&"	
		if matchesRequested != None:
			optionalUrl += "matches_requested=" + str(matchesRequested) + "&"	
		if tournamentGamesOnly == True:
			optionalUrl += "tournament_games_only=1&"	

		print("getting Dota 2 Data...")
		jsonUrl = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?" + optionalUrl + "key=" + self.webApiKey
		print(jsonUrl)
		tRawJSON = urllib.request.urlopen(jsonUrl)
		decodedRawJSON = tRawJSON.read().decode("ascii")
		resultDict = json.loads(decodedRawJSON)["result"]
	
		return resultDict

if __name__ == "__main__":
	pydota = pyDota2(WEBAPI_KEY);
	resultDict = pydota.getMatchHistoryDict(playerName="Gongwonchong", matchesRequested=1)

	print(resultDict)
