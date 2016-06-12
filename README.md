# Movie Catalog

## Setup
You need Vagrant to run the application.  
[Here](https://www.vagrantup.com/docs/getting-started/) you can find instructions on how to install it.

## How to run
### On your PC
Open your shell in the main directory and run the following commands  
`vagrant up`  
and  
`vagrant ssh`

### In your vagrant shell
Use `cd /vagrant` to enter the app's directory  and run the following commands  
`python manage.py init_db`  
`python manage.py start`

### In your web browser
Navigate to [http://localhost:5000](http://localhost:5000)
