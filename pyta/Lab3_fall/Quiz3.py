class Student :
    """ A university student .
    === Instance attributes ===
    st_num :
    This student 's student number .
    name :
    This student 's name .
    courses :
    A dictionary containing the courses this student has taken .
    Each key is a course code like 'csc148 ',
    and its value is the student 's grade in the course .
    credits :
    The number of credits this student has earned .
    One credit is earned each time the student passes a course .
    """
    st_num : int
    name : str
    courses : dict
    credits : int
    def __init__ ( self , st_num : int , name : str ) -> None :
        """ Initialize this student .
        """
        self . st_num = st_num
        self . name = name
        self . courses = {}
        self . credits = 0
    def complete_course ( self , course : str , grade : int ) -> None :
        """ Record the fact that this student has completed a course .
        """
        self . courses [ course ] = grade
        if grade >= 50:
            self. credits += 1

class GraduateStudent ( Student ) :
    """ A graduate student .
    === Additional instance attributes ===
    supervisor :
    The name of this graduate student 's supervisor .
    meetings :
    The dates on which this graduate student 's thesis committee met.
    Each date is represented as a str.
    """
    supervisor : str
    meetings :[ str ]
    def __init__( self , st_num : int , name : str , supervisor : str ) -> None :
        """ Initialize this graduate student .
        """
        Student.__init__(self, st_num, name)
        self . supervisor = supervisor
        self . meetings = []





g = GraduateStudent (1234567 , ' Ursula ' , ' Professor Fleet ')
g . complete_course ( ' csc148 ' , 92)
g . supervisor = ' Professor McIlraith '