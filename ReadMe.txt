There link to validations list
https://docs.google.com/spreadsheets/d/1yffzxOKArVPX6OFWRoJd45-k3ZErXdzZmHkIc9BX460/edit?usp=sharing
Validatio list consists also some issue which I'd been find  during my test

And some general findings/remarks:
Error handling looks not 'user friendly' so error code and messages is not clear
Uniformity of answers for example for read all (if nothing in the response) is [] and delete all is OK
Also interesting behavior for a get request  http: // 0.0.0.0: 8091 / bear / returns - 404
but for example a request to a non-existent id returns empty so still there is no uniformity

Test automation:
run tests: pytest -s test_bears.py

