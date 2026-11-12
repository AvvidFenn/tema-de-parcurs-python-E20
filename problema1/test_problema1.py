import pytest
from problema1 import Employee, Manager

@pytest.fixture(autouse=True)
def rest_counters():
    Employee.emp_count = 0
    Manager.mgr_count = 0

def test_creare_employee():
    emp = Employee("Ion", 4000, {"Task 1":"Completed"})

    assert emp.name == "Ion"
    assert emp.salary == 4000
    assert emp.tasks == {"Task 1":"Completed"}
    assert Employee.emp_count == 1

def test_creare_manager():
    
    mgr = Manager("Ionita", 6000, {"Task 2":"In progress"}, "Breakfast Leader", "Catering")
    assert mgr.name == "Ionita"
    assert mgr.salary == 6000
    assert mgr.tasks == {"Task 2":"In progress"}
    assert mgr.position == "Breakfast Leader"
    assert mgr.departament == "Catering"
    assert Manager.mgr_count == 1

