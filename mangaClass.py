import json
import random
import requests
import os

class Manga:
    def __init__(self, mangaName):
        self.mangaName = mangaName
        self.mangaTitle = ""
        self.mangaType = ""
        self.mangaStatus = ""
        self.mangaPublished = ""
        self.mangaScore = ""
        self.mangaRank = ""
        self.mangaSynopsis = ""
        self.mangaAuthor = ""
        self.mangaGenres = ""


    def getMangaData(self):
        name = self.mangaName
        link = f"https://api.jikan.moe/v4/manga?q={name}&limit=1"
        try:
            response = requests.get(link)
        except requests.exceptions.HTTPError as e:
            return(e.args[0])
        
        data = json.loads(response.content)
        mangaDetails = data["data"][0]

        self.mangaTitle= mangaDetails["title"]
        self.mangaType=mangaDetails["type"]
        self.mangaStatus=mangaDetails["status"]
        self.mangaPublished=mangaDetails["published"]["from"][:10]
        self.mangaScore=mangaDetails["score"]
        self.mangaRank=mangaDetails["rank"]
        self.mangaSynopsis=mangaDetails["synopsis"]
        self.mangaAuthor=mangaDetails["authors"][0]["name"]
        genres =""
        for genre in mangaDetails["genres"]:
            genres = genres + " " + genre["name"]

        self.mangaGenres = genres

        return 

    def mangaRandom(self):
        while True:
            id = random.randint(1,20290)
            link = f"https://api.jikan.moe/v4/manga/{id}"
            try:
                response = requests.get(link)
            except requests.exceptions.HTTPError as e:
                return(e.args[0])
            print(response)
            if response.status_code != 404:
                break

        data = json.loads(response.content)
            
        name= data["data"]["title"]
        self.mangaName = name
        self.getMangaData()
        return

    def mangaDesc(self):
        return( 
        f"""Title: {self.mangaTitle}
Type: {self.mangaType}
Author: {self.mangaAuthor}
Published: {self.mangaPublished}
Status: {self.mangaStatus}
Score: {self.mangaScore}
Rank: {self.mangaRank}
Genres: {self.mangaGenres}
Synopsis: {self.mangaSynopsis}""")


