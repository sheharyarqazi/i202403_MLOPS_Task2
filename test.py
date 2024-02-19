from main import StudentsInMLOps

def test_enrollStudents():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(5)
    assert classroom.getTotalStrength() == 5

def test_dropStudents():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(10)
    classroom.dropStudents(3)
    assert classroom.getTotalStrength() == 7

def test_getClassName():
    classroom = StudentsInMLOps()
    assert classroom.getClassName() == "MLOps"
