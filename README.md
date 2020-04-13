# Python-Flask-Microservice-Nginx-JWT
Flask microservices connected via Nginx + JWT encryption

1. User Manager Mcroservice - This service helps user in registration. Database used is postgresql.

2. Authentication Microservice - This service helps user to login in the system. 
                                 The service will call User manager service to check if the user is valid or not and 
                                  then respectively allow access in the system

3. NGINX - Have used nginx for reverse proxy. With help of nginx.conf file, we can divert the calls to 80 port
           and then nginx will automatically divert the call to respective microservice as per the configuration file setup.
           
4. Security - The calls will be secured by Flask JWT encryption.
