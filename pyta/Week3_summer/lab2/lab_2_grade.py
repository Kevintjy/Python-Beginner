class Grade:
    def __init__(self, grade):
        self.grade = grade

    def convert(self):
        raise NotImplementedError

    def __str__(self):
        return str(self.grade)

    def __eq__(self, other):
        return self.grade == other.grade

class NumericGrade(Grade):
    def __init__(self, grade):
        if 0 <= grade <= 49:
            self.grade = 'F'
        if 50 <= grade <= 52:
            self.grade = "D-"
        if 53 <= grade <= 56:
            self.grade =  "D"
        if 57 <= grade <= 59:
            self.grade ="D+"
        if 60 <= grade <= 62:
            self.grade = "C-"
        if 63 <= grade <= 66:
            self.grade = "C"
        if 67 <= grade <= 69:
            self.grade = "C+"
        if 70 <= grade <= 72:
            self.grade = "B-"
        if 73 <= grade <= 76:
            self.grade = "B"
        if 77 <= grade <= 79:
            self.grade = "B+"
        if 80 <= grade <= 84:
            self.grade =  "A-"
        if 85 <= grade <= 89:
            self.grade = "A"
        if 90 <= grade <= 100:
            self.grade = "A+"

class LetterGrade(Grade):
    def __init__(self, grade):
        self.grade = grade



if __name__ == '__main__':
    equivalent_grades = []
    list_of_grades = [NumericGrade(73), LetterGrade("A-"), LetterGrade("B-"),
                      NumericGrade(72)]
    grade_to_find = NumericGrade(72)  # Create a grade that we want to find matches equivalent_grades = []
    for grade in list_of_grades:
        if grade == grade_to_find:
            equivalent_grades.append(grade)
    expected_grades = [list_of_grades[2], list_of_grades[3]]
    assert equivalent_grades == expected_grades