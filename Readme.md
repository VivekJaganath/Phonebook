1. Phonebook: A simple tool to store your contacts with CLI using yaml

Usage: User can add store and retrieve contact details such as name, number, address and email.

Limitation: repetitions of contacts are not allowed, user cannot save the same name and number which is alreay entered.

2. To install the tool, run the following command:

python setup.py install

The prerequisites are argparse and pyyaml which will be automatically installed.

3. Contact can be added as below:

pycontacts --add --name xyz --number 81234756985 --email xyz@gmail.com --address paderborn

4. To List all the contacts use below command:

pycontacts --list

5. To see the details of a particular contact use below command: 

pycontacts --show --name xyz

6. The tool, once run will automatically create a yaml file with name 'data.yml'.

Authors

Vivek Jaganath
