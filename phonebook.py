import os
from contact import Contact
import argparse
import yaml


def main():
    try:
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--add',
                            help='Add a contact', action="store_true")
        parser.add_argument('--list',
                            help='List all contact', action="store_true")
        parser.add_argument('--show',
                            help='Show respective contact', action="store_true")
        parser.add_argument('--name', type=str, help="contact name", required=False)
        parser.add_argument('--address', type=str, default=None, help="address of the contact", required=False)
        parser.add_argument('--number', help="contact number", required=False)
        parser.add_argument('--email', default=None, help="email id of the contact", required=False)
        args = parser.parse_args()
        x = Pb()
        x.input(args)
    except argparse.ArgumentTypeError as e:
        print(e)


class Pb:

    def __init__(self):
        self.received = Contact()
        self.received_ser = []

    def parse(self, input_args):
        for k, v in input_args.__dict__.items():
            if hasattr(self.received, k):
                setattr(self.received, k, v)

    def add(self):
        contact_to_store = dict()
        if not self.received.name or not self.received.number:
            raise argparse.ArgumentTypeError("please enter name and number")
        contact_to_store[(self.received.name, self.received.number)] = self.received.get_contact()
        with open("data.yml", 'a+') as outfile:
            yaml.dump(contact_to_store, outfile, default_flow_style=False, allow_unicode=True)
        print("Contact added")

    def list(self):
        if os.path.exists("data.yml"):
            with open("data.yml", 'r') as stream:
                data = yaml.load(stream)
            self.__print_output(data)

    def show(self):
        if not self.received.name:
            raise argparse.ArgumentTypeError("enter a name to show")
        with open("data.yml", 'r') as stream:
            data = yaml.load(stream)
            for k, v in data.items():
                if k[0] == self.received.name:
                    self.received_ser = []
                    self.received_ser.append(v)
                    self.__print_output()
                    break
        if not self.received_ser:
            raise Exception("no contact found")

    def __print_output(self, contacts=None):
        if contacts:
            for k, v in contacts.items():
                for ik, iv in v.items():
                    print("%s: %s" % (ik, iv))
                print("\n")
        else:
            for contact in self.received_ser:
                for k, v in contact.items():
                    print("%s: %s" % (k, v))
                print("\n")

    def input(self, arguments):
        self.parse(arguments)
        try:
            if arguments.add:
                self.add()
            elif arguments.list:
                self.list()
            elif arguments.show:
                self.show()
            else:
                print("Operation Not found")
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    main()