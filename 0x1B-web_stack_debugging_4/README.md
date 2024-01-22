# Web_stack debugging 4
The server works fine but the issue is that it couldn't handle many requests concurently.
To fix this, I found out that the error was that it couldn't open many file descriptors at once so i changed the limit; which was set as an environment variable at /etc/default/nginx