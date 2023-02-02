 ~ This project was made by Benny Yakub. ~ 
This project is a client server interaction, where the client can send specific 
commands to the server, or the server wil just send back an echo. 
To run the project, you first need to run the 'echo_server.py' file then the 'echo_client.py' file.
The server starts by sending UDP broadcasts about it's current port and hostname. 
The client gets the broadcast and then connects through TCP to the server.
if the he client is the first to connect, he will get a wlecome message with the admin password, 
if not then he will just get a welcome message. Then the client needs to enter his name, 
then is able to run commands or send echo messages.