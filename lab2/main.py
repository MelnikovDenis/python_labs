from company import *
from employee import *
from client import *
from person import *

company = Company("Кафе \"У Дениса\"", 
    [
        Employee("Мельников", "Денис", "Вячеславович", 19, 100000),
        Employee("Елькин", "Андрей", "Владиславович", 7, 9.9)
    ], 
    [
        Client("Глазырин", "Вячеслав", "Михайлович", 19, "Стейк"),
        Client("Глазырин", "Михаил", "Григорьевич", 51, "Пиво")        
    ]);
SerializeCompany(company, "test.json");
print(company);
deserialized = DeserializeCompany("test.json");
print(deserialized);