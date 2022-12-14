#Min: Let's Do This :) We got this
#Bushrah: Hello Hello, All
#Kingsley: Hello world
#Shannon: Hi team!
#James: Hi Everyoneeoa
#
#
from argparse import ArgumentParser
import pandas as pd
import re
import sys
class Contact:
    """ Reads a line of contact list and divides the contact info into different 
    attributes.
    
    """
    def __init__(self, contact):
        # Done by Bushrah (+ Min)
        """ reads the line and use regular expression to initialize contact values 
        (names, phone number, relation, etdc)
        
        Args: 
            name(str): the name of the person in contactlist
            address(str): the address of the person in contactlist
            email(str): the email of the person in contactlist
            phoneNum(int): the phoneNum of the person in contactlist
            relation(str): the relation with the person in contactlist 
        
        """
        
        self.contact = contact
        
        expr = re.search(r"""(?x)
                        ^(?P<name>\n.+)
                        \s
                        (?P<address>(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)(\n.+))
                        \s
                        (?P<email>.+?@.+")
                        \s
                        (?P<phoneNum>[^,])
                        \s
                        (?P<relation>\w)
                        """, contact)
        if expr:
            self.name = expr.group("name")
            self.address = expr.group("address")
            self.email = expr.group("email")
            self.phoneNum = expr.group("phoneNum")
            self.relation = expr.group("relation")
        else:
            raise ValueError
            
    
    def __repr__(self):
        # Done by Bushrah
        """ magic method that return formal representation of contact object
        Returns:
            returns self of the name, address, email, phoneNum, and relation
        
        """
        return self.name + ", " + self.address + ", "+ self.email + ", " + self.phoneNum + "," + self.relation
    
  
    def as_dict(self):
        # Done by James
        """ Returns all attributes as dictionary entries
        """
        return {'name': self.name, 'address': self.address, 
                'email': self.email,"phone number":self.phoneNum,
                "relation": self.relation }
    
    
    
def readCont(filename):
    # Done by Min
    """ Using with open, read all lines of contact file and puts them into a single list.
    
    Args:
        filename (str): the text filepath of the lines of contact info.
        
    Returns:
        contactList (list of str): a list of each line that is the Contact object.
    
    """
    
    contactList = []
    with open(filename, "r") as f:
        for line in f:
            contactList.append(Contact(line))
                
    return contactList


class Sort:
    """ Convert the list of contacts into a dataframe using panda. Then, sort them 
    to put different groups/cateogries of the contact into separate dataframes.
        
    """
    def __init__(self, list):
        # Done by Min (+ James)
        """ Creates an attribute of dataframe by converting the list argument.
        
        Args:
            list (list of str): the list of contact information made by function 
            readCont
        
        Side effects:
            contDf (dataframe): dataframe of the contact
        
        """
        self.contDf = pd.DataFrame([contact.as_dict() for contact in list])
    
    
    def categorize(self):
        # Done by James
        """ Sorts the master dataframe created with the init method of the 
        "Sort" class by making smaller dataframes from the main dataframe 
        depending on data from the amster data frame.
        
        Side effets:
            contDF (dataframe): changes how the dataframe is categorized and
            organized. Smaller dataframes are created depending on the 
            categories/groups.
        """
        contDf_copy = self.contDf.copy()
        
        parent_df = contDf_copy [contDf_copy ['relation'] == "Family"]
        co_worker_df = contDf_copy[contDf_copy['relation'] == "Coworker"]
        friend_df = contDf_copy[contDf_copy['relation'] == "Friend"]
        
        print(parent_df)
        print(co_worker_df)
        print(friend_df)
        
        
class Find(Sort):
    """ Finds the person or category that the user is looking for.
    
    """
    def __init__(self, list):
        # Done by James
        """ use super() to initialize a smaller object that displays the contact
        that the user is looking for. It's a child function so that it can
        directly take the object and find what the user wants better.
        
        Args:
            list (list of str): list of contact to be put into super class' init/   
        """
        super().__init__(list)
        
        
    
    def choose(self):
        # Done by James
        """Returns back the found contact
        Args:
            search_name(str): stores the name of the found contact
        Side effects:
            choose_df (dataframe): prints a dataframe of the chosen category or name.
        """
        search_fname= input ("Enter the contact's first name.\n")
        search_lname= input ("Enter the contact's last name. Enter none if no last name.\n")
        search_category= input ("Enter the contact's relationship to you, or enter none if do not wish to use a category.\n")
        
        print (search_fname+search_lname)
        
        if search_lname == "" and search_category== "":
            contDf_copy1 = self.contDf.copy()
            self.choose_df = contDf_copy1 [contDf_copy1 ['name'] == search_fname]
            print(self.choose_df)
            
            
        elif search_lname == "":
            contDf_copy1 = self.contDf.copy()
            self.choose_df = contDf_copy1 [(contDf_copy1 ['name'] == 
                                       search_fname) 
                                      & 
                                      (contDf_copy1["relation"]== 
                                                    search_category)]
            print(self.choose_df)
            
        elif search_category == "":
            contDf_copy1 = self.contDf.copy()
            full_name= (search_fname+" "+search_lname)
            self.choose_df = contDf_copy1 [contDf_copy1 ['name'] == 
                                       full_name]
            print(self.choose_df)
            
            
        else:
            contDf_copy1 = self.contDf.copy()
            full_name= (search_fname+" "+search_lname)
            self.choose_df = contDf_copy1 [(contDf_copy1 ['name'] == 
                                       full_name) 
                                      &
                                      (contDf_copy1["relation"]== 
                                                    search_category)]
            print(self.choose_df)     
        
        
        
    def __str__(self):
        # Done by Shannon (+ James)
        """Returns an informal representation of the found contact 
        (or all the found contacts)
        The representation will be in a list format containing strings: 
        name, address, email, phoneNum of the found contact
        
        Returns:
            list(str) : the list representation
        """
        
        repr_list= []
        repr_name = str(self.choose_df.iloc[0, 0])
        repr_address = str(self.choose_df.iloc[0, 1])
        repr_email = str(self.choose_df.iloc[0, 2])
        repr_phoneNum = str(self.choose_df.iloc[0, 3])
        repr_relation = str(self.choose_df.iloc[0, 4])
        
        repr_list.append({'name': repr_name, 
                          'address': repr_address,
                          'email': repr_email,
                          'phoneNum': repr_phoneNum,
                          'relation': repr_relation})
        
        
        return  (f"{repr_name} {repr_address}  {repr_email} {repr_phoneNum} {repr_relation}")

    def Msg(self):
        # Done by Shannon (+ Min)
        """Sends a message to the contact
        
        Args: 
            name (string): name of the contact that message is being sent to
            
        Side effects:
            Prints an f string of the message
        
        """
        if self.choose_df["relation"] == "Family":
            return f"Emergency Family Meeting Required!"
        elif self.choose_df["relation"] == "Coworker":
            return f"Reminder for Work/Assignment Due within 24 Hours!"
        elif self.choose_df["relation"] == "Friend":
            return f"Party Plan Incoming~!"
        else:
            return f"Currently Unavailable"
    
    
def main(filepath):
    # Done by Kingsley (+ Min)
    """ Sort and organize the contact litst, then find a person to message or notify.
    Args: 
         filepath(str): filepath containing contact list, address, email, name, phone number and messeges. 
         
    Side effects:
        Prints the message or notification written to the person
    """
    contList = readCont(filepath)
    print(contList)
    
    lookingFor = Find(Sort(filepath))
    print(f"Quick Message Sent: {lookingFor.Msg()}")
    
def parse_args(arglist):
    # Done by Kingsley
    """ Parse command line arguments.
    
    Expect a mandatory argument:
        filename: path to a file of names and info of families.
    
    Args:
        arglist (list of str): arguments from the command line.
        
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="file contains contacts of people")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)

        
        