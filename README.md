# IOTmidsem_LNMIIT Q2
Multi-Client Chat System using TCP and Multithreading

This project is a simple multi-client chat application built using Python. It demonstrates how TCP sockets and multithreading work together to create a real-time communication system. Multiple clients can connect to a central server and exchange messages simultaneously.
The goal of this project is to clearly show how client-server architecture operates using TCP, and how multithreading allows multiple users to communicate without blocking each other.

Project Description

The system consists of two main programs: a TCP server and a TCP client.
The server listens for incoming client connections and accepts multiple users at the same time. Each connected client is handled in a separate thread, allowing the server to manage several conversations concurrently. When the server receives a message from one client, it broadcasts that message to all other connected clients.
The client connects to the server and allows a user to send and receive messages in real time. To achieve smooth communication, the client uses two threads — one for sending messages and another for receiving them. This ensures that incoming messages can be displayed even while the user is typing.

How the System Works
When the server starts, it creates a TCP socket, binds it to a host and port, and begins listening for connections. Every time a new client connects, the server creates a new thread dedicated to that client. The server maintains a list of all connected clients so it can forward messages appropriately.
On the client side, once connected to the server, two threads are started. One thread continuously listens for messages from the server, while the other allows the user to input and send messages. This enables real-time chat functionality.

Technologies Used

This project is implemented using:
Python 3
The socket module for TCP communication
The threading module for handling multiple clients concurrently

How to Run the Project
First, start the server:
python server.py
Then open multiple terminals and run:
python client.py
Each client will connect to the server and can start sending messages. Messages sent by one client will be broadcast to all other connected clients.
What This Project Demonstrates

This implementation clearly demonstrates:
The use of TCP sockets for reliable, connection-oriented communication
Proper multithreading to handle multiple clients independently

Correct broadcasting logic to distribute messages among connected users

Real-time bidirectional communication
