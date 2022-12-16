import pickle

class DataManager():
    def __init__(self, file_name):
        self._file_name = file_name                     #name of file, containing the data

    @property
    def filename(self) -> str:
        return self._file_name

    @filename.setter
    def filename(self, newfilename: str):
        self._file_name = newfilename

    def read_data(self):                                #reads data from file, given by name (_file_name)
        person_pickle = open(self._file_name, "rb")
        person_list = pickle.load(person_pickle)
        person_pickle.close()

        return person_list
    
    def write_data(self, person_list):                  #writes data into file given by name (_file_name)
        person_pickle = open(self._file_name, "wb")
        pickle.dump(person_list, person_pickle)
        person_pickle.close()