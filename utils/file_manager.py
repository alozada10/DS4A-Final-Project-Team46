import _pickle as c_pickle
import os


# Saves file in specific directory
def save(object_to_save,
         dir_path,
         file_name):

    # Verify the existence of the directory if it does not exist then create it
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # To save
    path = dir_path + '/' + file_name
    # Save func
    c_pickle.dump(object_to_save, open(path, 'wb'))


# Reads file from pickle
def read(path):
    # List with all the model names
    return c_pickle.load(open(path, 'rb'))


# Reads file to string
def read_file(loc_file):
    with open(loc_file, 'r') as my_file:
        data = my_file.read()
    return data

