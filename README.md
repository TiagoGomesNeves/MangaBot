
# MangaBot for Discord

This is a mangabot for discord that allows users to give them info on certain manga, ask it to retrieve a random manga and allows users to create a profile and store their top 5 favourite mangas.



## Bot Commands

?Profile : this command if not used before generates a profile for the user and stores it on a database. The next ?profile commands will show that users top 5 list.

?setListAt number mangaName : this allows users to alter their top 5 list by choosing a mangaName and a position on the list to place it in

?random: this generates a random number which corresponds to a myanimelist id and uses an api to retrive that manga's information

?recommend mangaName: this uses the mangaName and an api to grab information about that manga like its name, author, genres, and synopsis 



## Environment Variables

If you want to run this bot yourself, you will need to add the following environment variables to your .env file

`BOT_TOKEN`: which is your bots token obtained from the discord website

`DB_CONNECTION`: which is a mongodb atlas database connection, which you can see how to setup here https://www.mongodb.com/products/platform/atlas-database


