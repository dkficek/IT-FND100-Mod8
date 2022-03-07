# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Dan Ficek,March 4th 2020, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
choice_str = ""  #user's menu choice

class Product:
    """Stores data about a product:

    properties:
        prod_name: (string) with the products's  name
        prod_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Dan Ficek,March 6th, 2020,Modified code to complete assignment 8
    """

    # --Fields--
    # strProdName = ""
    # strProdPrice = ""

    # -- Constructor --
    def __init__(self, prod_name, prod_price):
        # 	   -- Attributes --
        self.__prod_name = prod_name
        self.__prod_price = prod_price

    # -- Properties --
    # prod_name

    @property  # DON'T USE NAME for this directive!
    def prod_name(self):  # (getter or accessor)
        return str(self.__prod_name).title()  # Title case

    @prod_name.setter  # The NAME MUST MATCH the property's!
    def prod_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__prod_name = value
        else:
            raise Exception("Names cannot be numbers")

    # prod_price

    @property  # DON'T USE NAME for this directive!
    def prod_price(self):  # (getter or accessor)
        return str(self.__prod_price).title()  # Title case

    @prod_price.setter  # The NAME MUST MATCH the property's!
    def prod_price(self, value):  # (setter or mutator)
        if str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Methods --
    def __str__(self):
        return self.prod_name + ',' + self.prod_price

    #-------End of Class-----
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Dan Ficek, 3-4-2022,Modified code to complete assignment 8
    """

      #----Methods-----
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of object rows
        """
        objFile = open(file_name, "w")  # open the file
        for objRow in list_of_product_objects:  # unpack the table into tasks and priorities
            objFile.write(objRow.prod_name + "," + objRow.prod_price + "\n")

        objFile.close()

        return list_of_product_objects

    @staticmethod
    def read_data_from_file(file_name):

        try:
            objFile= open(file_name,"r")
            for line in objFile:
                product,price=line.split(",")
                lstOfProductObjects.append(Product(product.strip(),float(price.strip())))

            return lstOfProductObjects
        except:
            print("There was no existing list of products in your directory!  Choose Option 2 to start the list.")
            print()  # new line for looks
            return lstOfProductObjects
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Display a menu of choices to the user"""
    @staticmethod
    def output_menu(): #display a menu to the user
        print('''
        Menu of Options
        1) Show the Current List of Products and Prices
        2) Add a Product and Price to the List
        3) Save Data to File and Exit the Program
        ''')
        print() #an extra line for looks

    @staticmethod
    def input_menu_choice():  #get choice from user
        choice = str(input("Enter an option [1 to 3]:  ")).strip()
        print() #extra line for looks
        return choice

    @staticmethod
    def output_current_list(list_of_objects):
        '''Shows current products and prices in the list of objects

        :param list_of_objects: (list) of objects to show
        :returns nothing;  just prints list'''

        print("********The Current Products and Prices in the list are:*******")
        for object in list_of_objects:
            print(object)
        print("***************************************************************")
        print() # an extra line for looks

    @staticmethod
    def input_new_product():
        '''Gets the new product and price to be added

        :return:(object) with name and price
        '''
        newProduct=input("\nEnter the name of a product to add: ")
        newPrice=float(input("\nEnter the price of that product: "))


        return Product(newProduct,newPrice)


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)


while (True):
    # Show user a menu of options
    IO.output_menu()
    # Get user's menu option choice
    choice_str= IO.input_menu_choice()

    if choice_str == '1':
        # Show user current data in the list of product objects
        IO.output_current_list(lstOfProductObjects)

    elif choice_str == '2':
        # Let user add data to the list of product objects
        addProduct = IO.input_new_product()
        lstOfProductObjects.append(addProduct)

    elif choice_str == '3':
        # let user save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        print("Data saved to file!")

        break

    else:
        print("Error!  Please enter one of the menu options.")

# Main Body of Script  ---------------------------------------------------- #
