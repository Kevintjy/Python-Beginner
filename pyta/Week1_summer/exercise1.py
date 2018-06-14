class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.enroll_list = []
        self.wait_list = []
        self.course_capacity = 0


    def __str__(self):
        return ("The course {} has {} student(s) enrolled with".\
                format(self.course_name, len(self.enroll_list)) +
                " {} student(s) on the waitlist.".format(len(self.wait_list)))

    def __eq__(self, other):
        return self.course_name == other.course_name and\
               self.course_capacity == other.course_capacity and\
               sorted(self.enroll_list) == sorted(other.enroll_list) and\
               sorted(self.wait_list) == sorted(other.wait_list)

    def add_student(self, student_name):
        if len(self.enroll_list) < self.course_capacity:
            self.enroll_list.append(student_name)
            self.enroll_list.sort()
        else:
            self.wait_list.append(student_name)

    def set_course_capacity(self, course_capacity):
        self.course_capacity = course_capacity

    def get_enrolled_students(self):
        return self.enroll_list

    def get_waitlist(self):
        return self.wait_list

    def remove_student(self, student_name):
        if student_name in self.enroll_list:
            self.enroll_list[self.enroll_list.index(student_name)] =\
                self.wait_list[0]
            del self.wait_list[0]
        else:
            self.wait_list.remove(student_name)


if __name__ == '__main__':
    c = Course("CSC148")
    c.set_course_capacity(2)  # You may assume this number will always be a
    # positive integer and that set_course_capacity()
    # will be called before adding students and
    # never after adding students.

    c.add_student("Sophia")
    c.add_student("Danny")
    c.add_student("Jacqueline")

    assert str(c) == ("The course CSC148 has 2 student(s) enrolled with" +
                      " 1 student(s) on the waitlist.")

    # get_enrolled_students() should return the enrolled students in sorted
    # order.
    assert c.get_enrolled_students() == ['Danny', 'Sophia']

    # get_waitlist() should return the students on the waitlist in the order
    # that they were added.
    assert c.get_waitlist() == ['Jacqueline']

    c.add_student("David")
    assert c.get_waitlist() == ['Jacqueline', 'David']

    # if remove_student() removes an enrolled student, add in the first
    # waitlisted student to enrolled students.
    # HINT: The list method .pop() might be useful here.
    #       See help(list.pop) for details.
    c.remove_student("Danny")
    assert c.get_enrolled_students() == ['Jacqueline', 'Sophia']
    assert c.get_waitlist() == ['David']

    c.remove_student("David")
    assert c.get_waitlist() == []

    # When comparing 2 courses, they are the same if the enrolled students
    # are the same (regardless of order), the waitlist is the same
    # (and in the same order), and the course code and capacity are the same.
    c2 = Course("CSC148")
    c2.set_course_capacity(2)
    c2.add_student("Jacqueline")
    c2.add_student("Sophia")
    assert c == c2

    c2.add_student("David")
    assert c != c2

    # Below is how python_ta (PythonTA/pyTA/etc.) is called.
    # When run, your code should produce no errors from python_ta.
    # You must have python_ta installed for this to work (see Lab 1 and
    # the Software Installation page).
    import python_ta

    python_ta.check_all(config="ex1_pyta.txt")
