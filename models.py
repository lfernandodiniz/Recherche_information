


class Machine:
    def __init__(self, model, function):
        self.model = model
        self.function = function

class Trouble_relation:
    def __init__(self, description_fault, description_cause, description_resolution, description_reference, trouble_no=None, fault_no=None):
        self.description_fault = description_fault
        self.description_cause = description_cause
        self.description_resolution = description_resolution
        self.description_reference = description_reference
        self.trouble_no = trouble_no
        self.fault_no = fault_no


class User:
    def __init__(self, id, name, pwd):
        self.id = id
        self.name = name
        self.pwd = pwd