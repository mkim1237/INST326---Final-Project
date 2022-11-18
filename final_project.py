#Min: Let's Do This :) We got this
#Bushrah: Hello Hello, All
#Kingsley: Hello world
#Shannon: Hi team!
#James: Hi Everyoneeoa
#
#


class Contact:
    """ Reads a line of contact list and divides the contact info into different 
    attributes.
    
    """
    def __init__(self, name, address, email, phoneNum):
        """ reads the line and use regular expression to initialize contact values 
        (names, phone number, relation, etdc)
        
        Args: 
            name(str): the name of the person in contactlist
            address(str): the address of the person in contactlist
            email(str): the email of the person in contactlist
            phoneNum(int): the phoneNum of the person in contactlist
        
        """
        

    
    def __repr__(self):
        """ magic method that return formal representation of contact object
        
        
        Returns:
        returns self of the name, address, email and phoneNum
        
        """
    

    

def readCont(filename):
    """ Using with open, read all lines of contact file and puts them into a single list.
    
    Args:
        filename (str): the text filepath of the lines of contact info.
        
    Returns:
        contactList (list of str): a list of each line that is the Contact object.
    
    """

class Sort:
    """ Convert the list of contacts into a dataframe using panda. Then, sort them 
    to put different groups/cateogries of the contact into separate dataframes.
        
    """
    def __init__(self, list):
        """ Creates an attribute of dataframe by converting the list argument.
        
        Args:
            list (list of str): the list of contact information made by function 
            readCont
        
        Side effects:
            contDf (dataframe): dataframe of the contact
        
        """
    
    def categorize(self):
        """ Sorts the master dataframe created with the init method of the 
        "Sort" class by making smaller dataframes from the main dataframe 
        depending on data from the amster data frame.
        Side effets:
            contDF (dataframe): changes how the dataframe is categorized and
            organized. Smaller dataframes are created depending on the 
            categories/groups.
        """
    

#class Find(Sort):
    """ Finds the person or category that the user is looking for.
    
    """
    #def __init__(self, search_name, search_category = None):
        """ use super() to initialize a smaller object that displays the contact
        that the user is looking for. It's a child function so that it can
        directly take the object and find what the user wants better.
        
        Args:
            search_name (string): the name of the contact that the user is look
            ing for.
            search_category (string): the category and or datafram column name
            that the user is searching for specifically. search_category is set
            to None by default incase the user simply wants to look for a person
            's name rather than including more information.
        
        
        """
    
    #def choose():
        """Returns back the found contact
        Args:
            search_name(str): stores the name of the found contact
        Returns:
            search_name(str): returns the found contact
            None: returns None if contact isn't found
        
        
        """
    #def __str__(self):
        """Returns an informal representation of the found contact (or all the found contacts)
        The representation will be in a list format containing strings: name, address, email, phoneNum
        of the found contact
        
        
        Returns:
            list(str) : the list representation
        """
            
        
        
#def Msg():
    """ use conditional expressions to send a message
    
    """
    
    

#def main(filepath):
    """ has optional parameters
    Args: 
         filepath(str): filepath containing contact list, address, email, name, phone number and messeges. 
    """


#if __name__ == "__main__":


