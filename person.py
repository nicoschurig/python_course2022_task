class Person():
    def __init__(self, name, first_name, email, day, month, year):
        self._name = name
        self._first_name = first_name
        self._email = email
        self._day = day
        self._month = month
        self._year = year

        @property
        def name(self) -> str:           #Getter for name
            return self._name
        
        @name.setter
        def name(self, newname: str):    #Setter for name
            self._name = newname

        @property
        def first_name(self) -> str:                  #Getter for first name
            return self._first_name

        @first_name.setter
        def first_name(self, newfirstname: str):      #Setter for first name
            self._first_name = newfirstname

        @property
        def day(self) -> int:                        #Getter for day
            return self._day

        @day.setter
        def day(self, newday: int):                  #Setter for day
            self._day = newday

        @property
        def month(self) -> int:                      #Getter for month
            return self._month

        @month.setter
        def month(self, newmonth: int):              #Setter for month
            self._month = newmonth
        
        @property
        def year(self) -> int:                       #Getter for year
            return self._year
        
        @year.setter
        def year(self, newyear: int):                #Setter for year
            self._year = newyear