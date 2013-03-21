#!/usr/bin/env python
"""
    pydota2
    ~~~~~~

    A module for DOTA 2 WebAPI.

    :copyright: (c) 2013 by Yi 'Pusungwi' Yeon Jae
    :license: New BSD License, see LICENSE for more details.
"""

import os
import json
import urllib.request, urllib.parse

VERSION_NUMBER = 0.2
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

	def getHeroesDict(self, language="en_us"):
		#A list of heroes within Dota 2.
		print("getting Dota 2 Heroes...")
		heroesUrl = "https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=" + self.webApiKey + "&language=" + language
		heroesJSON = urllib.request.urlopen(heroesUrl)
		heroesDecodedJSON = heroesJSON.read().decode("ascii")
		resultDict = json.loads(heroesDecodedJSON)

		return resultDict

	def getRaritiesDict(self, language="en_us"):
		#Dota 2 item rarity list.
		print("getting Dota 2 Rarities...")
		raritiesUrl = "http://api.steampowered.com/IEconDOTA2_570/GetRarities/v1/?key=" + self.webApiKey + "&language=" + language
		raritiesJSON = urllib.request.urlopen(raritiesUrl)
		raritiesDecodedJSON = raritiesJSON.read().decode("ascii")
		resultDict = json.loads(raritiesDecodedJSON)

		return resultDict

	def getMatchHistoryDictBySequenceNum(self, startAtMatchSeqNum, matchesRequested=25):
		#A list of matches ordered by their sequence num.
		print("getting Match History Dict By Sequence Number...")
		mHistorySNumUrl = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/?key=" + self.webApiKey + "&start_at_match_seq_num=" + str(startAtMatchSeqNum) + "&matches_requested=" + str(matchesRequested)
		mHistorySNumJSON = urllib.request.urlopen(mHistorySNumUrl)
		mHistorySNumDecodedJSON = mHistorySNumJSON.read().decode("ascii")
		resultDict = json.loads(mHistorySNumDecodedJSON)

		return resultDict

	def getTeamInfoDictByTeamID(self, startAtTeamID=0, teamRequested=10):
		#A list of all the teams set up in-game.
		print("getting Team Info Dict By TeamID...")
		tTeamIDUrl = "https://api.steampowered.com/IDOTA2Match_570/GetTeamInfoByTeamID/v001/?key=" + self.webApiKey + "&start_at_team_id=" + str(startAtTeamID) + "&teams_requested=" + str(teamRequested)
		tTeamIDJSON = urllib.request.urlopen(tTeamIDUrl)
		tTeamIDDecodedJSON = tTeamIDJSON.read().decode("ascii")
		resultDict = json.loads(tTeamIDDecodedJSON)

		return resultDict

	def getLiveLeagueGamesDict(self):
		#A list of in-progress league matches, as well as details of that match as it unfolds.
		print("getting Dota 2 Live League Gaming...")
		lLeagueUrl = "https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/?key=" + self.webApiKey
		lLeagueJSON = urllib.request.urlopen(lLeagueUrl)
		lLeagueDecodedJSON = lLeagueJSON.read().decode("ascii")
		resultDict = json.loads(lLeagueDecodedJSON)

		return resultDict

	def getLeagueListingDict(self, language="en_us"):
		#Information about DotaTV-supported leagues.
		print("getting Dota 2 League Listing...")
		lListingUrl = "https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v0001/?key=" + self.webApiKey + "&language=" + language
		lListingJSON = urllib.request.urlopen(lListingUrl)
		lListingDecodedJSON = lListingJSON.read().decode("ascii")
		resultDict = json.loads(lListingDecodedJSON)

		return resultDict

	def getMatchDetailDict(self, matchID):
		#Information about a particular match.
		print("getting Dota 2 Match Detail...")
		matchDetailUrl = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=" + self.webApiKey + "&match_id=" + matchID
		mDetailJSON = urllib.request.urlopen(matchDetailUrl)
		mDetailDecodedJSON = mDetailJSON.read().decode("ascii")
		resultDict = json.loads(mDetailDecodedJSON)

		return resultDict

	def getMatchHistoryDict(self, playerName=None, heroID=None, gameMode=None, skill=None, minDate=None, maxDate=None, 
		minPlayers=None, accountID=None, leagueID=None, startMatchID=None, matchesRequested=None, tournamentGamesOnly=False):
		#A list of matches, filterable by various parameters.
		#for more detail information. see http://wiki.teamfortress.com/wiki/WebAPI/GetMatchHistory
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

		print("getting Dota 2 Match history...")
		matchHistoryUrl = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?" + optionalUrl + "key=" + self.webApiKey
		mHistoryJSON = urllib.request.urlopen(matchHistoryUrl)
		mHistoryDecodedJSON = mHistoryJSON.read().decode("ascii")
		resultDict = json.loads(mHistoryDecodedJSON)
	
		return resultDict

if __name__ == "__main__":
	#visit http://steamcommunity.com/dev and get API key.
	pydota = pyDota2("INSERT STEAM API KEY HERE");
	tmpMHistoryDict = pydota.getMatchHistoryDict(matchesRequested=1)
	tmpMDetailDict = pydota.getMatchDetailDict("151800962")
	tmpHeroesDict = pydota.getHeroesDict()
	tmpLListingDict = pydota.getLeagueListingDict()
	tmpLLeagueDict = pydota.getLiveLeagueGamesDict()
	tmpTInfoDict = pydota.getTeamInfoDictByTeamID()
	tmpMDetailSNDict = pydota.getMatchHistoryDictBySequenceNum("3000")
	tmpRaritiesDict = pydota.getRaritiesDict()

	print(tmpMHistoryDict)
	print(tmpMDetailDict)
	print(tmpHeroesDict)
	print(tmpLListingDict)
	print(tmpLLeagueDict)
	print(tmpTInfoDict)
	print(tmpMDetailSNDict)
	print(tmpRaritiesDict)