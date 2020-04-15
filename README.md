# Python-Flask-Microservice-Nginx-JWT
Flask microservices connected via Nginx + JWT encryption

1. Authentication Microservice - This service helps user to login in the system. 
                                 The service will call User manager service to check if the curreny user is valid or not
                                 and then respectively allow access in the system

2. User Manager Mcroservice - This service helps admin (current user after authorization) to create new users. 
                              Database used is postgresql.

3. Security - The create user functionality will be secured by Python JWT encode and decode

4. NGINX - Have used nginx for reverse proxy. With help of nginx.conf file, we can divert the calls to 80 port
           and then nginx will automatically divert the call to respective microservice as per the configuration file setup.
           

