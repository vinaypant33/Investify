import sys
sys.path.append('Views') ## Doing this to add the folder in the import path

## Importing Modules
from tkinter import messagebox
from pubsub import pub

## Importing the - Pre made files
from Views import first_page
from Views import styles
from Views import dashboard





def calling_dashboard():
    pass



def calling_login_page():
    main_file  = first_page.login_page(350 , 450)
    main_file.defining_controls()
    main_file.placing_controls()



if __name__ == '__main__':
    calling_login_page()
