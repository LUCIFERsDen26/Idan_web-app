# Idan_web-app

This project demonstrates how to set up an authentication server using Casdoor in conjunction with Flask. The application leverages OAuth2 and OIDC authentication mechanisms. It adopts a microservices architecture and includes a web app component along with a Redis server for server-side session storage.

### Prerequisites
Docker must be installed on your system.
Familiarity with Docker Compose.

### Getting Started
Clone the Repository
```bash
git clone https://github.com/your-username/casdoor-auth-server.git
```
```bash
cd casdoor-auth-server
```
### Run the Docker Command to Start the AuthServer Container
```bash
docker run -d -p 8000:8000 --name AuthServer casbin/casdoor-all-in-one
```
### Configure Casdoor
Access the Casdoor web interface at ``` http://localhost:8000```
```
username : admin
password : 123
```
Set up your OAuth2 clients, user accounts, and permissions.

### Create an Environment File
Copy the example environment file ([.appenv](/.appenv)) and rename it to .env.
Fill in the necessary environment variables.
### Start the Web App and Redis Server
```bash 
docker-compose up
```

### Access the Web App
The web app will be available at ```http://localhost:5000```.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request.