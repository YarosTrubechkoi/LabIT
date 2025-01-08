class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'{self.name},{self.id}'


class Manager(Employee):
    def __init__(self, department, name, id):
        Employee.__init__(self,name, id)
        self.department = department

    def get_info(self):
        return f'{self.name},{self.id},{self.department}'

    def manage_project(self):
        return f"{self.name} из отдела {self.department} работает над проектом АНУБИС"


class Technician(Employee):
    def __init__(self, specialization, name,id):
        Employee.__init__(self,name, id)
        self.specialization = specialization

    def get_info(self):
        return f"{self.name},{self.id},{self.specialization}"

    def perform_maintenance(self):
        return f"{self.name},{self.specialization}, в данный момент решает проблему сервера"




class TechManager(Manager, Technician):
    def __init__(self, name, id, dep, spec):
        Manager.__init__(self, dep,name,id)
        Technician.__init__(self, spec,name,id)
        self.Team = []
    def control_projects(self):
        return f"{self.name},{self.specialization}, в данный момент решает проблему АНУБИСА"

    def add_employee(self,employee):
        self.Team.append(employee)

    def get_info(self):
        return (f'{self.name}, {self.id}, {self.department}, {self.specialization}')

    def get_team_info(self):
        return ("\n".join(self.Team))



tech_manager = TechManager("Грно", "Ыщыш", "Чмо", "Мандад")
Григорий = Employee("adad", "daada")
Дима=Technician('Абоба','Негр','Тракторщик')
Ярос=TechManager('Гандос','228','Теннис','Сосание')
tech_manager.add_employee(Ярос.get_info())
tech_manager.add_employee(Григорий.get_info())
tech_manager.add_employee(Дима.get_info())
tech_manager.add_employee(tech_manager.get_info())
print(tech_manager.control_projects())
print(tech_manager.get_team_info())
