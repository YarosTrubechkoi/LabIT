class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def get_info(self):
        return(f'Заголовок:{self.title} Автор:{self.author} Год издания:{self.year}')
bookie=Book('Преступление и наказание.','Фёдор Достоевкий.','1866')
print(bookie.get_info())

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_radius(self):
        return self.radius
    def set_radius(self,new_radius):
        self.radius=new_radius
Circle1=Circle(5)
print('Нынешний радиус круга:',Circle1.get_radius())
Circle1.set_radius(7)
print('Новый радиус:',Circle1.get_radius())