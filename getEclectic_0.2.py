# -*- coding: utf-8 -*-

import sys	# lib for working with arguments
from urllib.request import urlopen
import urllib

halfUrl = "http://www.maximtresk.ru/eklektika-"		# first part of url
paternString = "audio src="		# pattern for searching in page
numUrl = 0
lineArg = sys.argv
#print(len(lineArg))			#shows the number of arguments on the command line
# проверка кодировки
def getMp3Url(urlString):
	u = urlopen(urlString)			# getting full web page as HTTPResponse Objects
	webPage = u.read().decode("utf-8") 			# read, decode page from bytes to string and safe to variable
	
	################ temporary block #################
	#tts = webPage.find("<title>")+18
	#tte = webPage.find("</title>",tts)
	#print(webPage[tts:tte])
	############# end of temporary block #############
	
	# searching position of pattern in page
	startSearching = webPage.find(paternString)
	# print(startSearching)
	# find start of mp3-url
	startMp3Url = webPage.find('"', startSearching)
	# find end of mp3-url
	endMp3Url = webPage.find('"', startMp3Url + 1)
	# get full mp3-url
	mp3Url = webPage[startMp3Url+1:endMp3Url]
	
	return mp3Url
	
def getFileName(mp3Url,recNumber):
	startSuf = mp3Url.find("Eclectic-")
	strSuf = mp3Url[startSuf:]
	fileName = recNumber + "-" + strSuf
	return fileName

if ((len(lineArg)) > 1):
	numUrl = lineArg[1]				# last part of url
else:
	numUrl = input("Please enter track number: ")
	print()
	
fullUrl = halfUrl + numUrl + "/"
mp3url = getMp3Url(fullUrl)
fileName = getFileName(mp3url, numUrl)
print(fileName)
print(mp3url)
