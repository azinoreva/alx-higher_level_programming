alx-higher_level_programming - 0x10-python-network_0 - Bash Script Descriptions
This README explains the functionality of each Bash script in the 0x10-python-network_0 directory of the alx-higher_level_programming GitHub repository. These scripts utilize the curl command for making HTTP requests and processing responses.

0-body_size.sh

Description: This script takes a URL as input, sends a GET request using curl, and displays the size of the response body in bytes.
Test Example:
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10  # Replace 10 with the actual response body size
guillaume@ubuntu:~/0x10$
1-body.sh

Description: This script takes a URL as input, sends a GET request using curl, and displays the response body only if the status code is 200 (OK).
Test Example:
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2  # Displayed if status code is 200
guillaume@ubuntu:~/0x10$
2-delete.sh

Description: This script takes a URL as input, sends a DELETE request using curl, and displays the response body.
Test Example:
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request  # Displayed on successful DELETE
guillaume@ubuntu:~/0x10$
3-methods.sh

Description: This script takes a URL as input, uses curl to send an OPTIONS request (to retrieve allowed methods), and displays the list of HTTP methods the server accepts for that URL.
Test Example:
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT  # Example list of allowed methods
guillaume@ubuntu:~/0x10$
4-header.sh

Description: This script takes a URL as input, sends a GET request with the custom header X-School-User-Id: 98 using curl, and displays the response body.
Test Example:
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!  # Displayed on successful request
guillaume@ubuntu:~/0x10$
5-post_params.sh

Description: This script takes a URL as input, sends a POST request using curl, includes form data with email set to test@gmail.com and subject set to I will always be here for PLD, and displays the response body.
Test Example:
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD  # Displayed form data
guillaume@ubuntu:~/0x10$
Note: These descriptions assume the provided web server on port 5000 is functional and serves appropriate responses for each script's test case. Replace placeholders like 10 and response content with the actual output you observe during testing.
