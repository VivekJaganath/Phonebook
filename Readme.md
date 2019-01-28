Phonebook: A simple tool to store your contacts with CLI using yaml

Usage: User can add store and retrieve contact details such as name, number, address and email.

Limitation: repetitions of contacts are not allowed, user cannot save the same name and number which is alreay entered.

To install the tool, run the following command:

python setup.py install

The prerequisites are argparse and pyyaml which will be automatically installed.

Contact can be added as below:

pycontacts --add --name xyz --number 81234756985 --email xyz@gmail.com --address paderborn

To List all the contacts use below command:

pycontacts --list

To see the details of a particular contact use below command: 

pycontacts --show --name xyz

The tool, once run will automatically create a yaml file with name 'data.yml'.

Authors

Vivek Jaganath
