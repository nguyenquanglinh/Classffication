class People:
    def __init__(self, name, age, work, income, need):
        self.name = name
        self.age = age
        self.work = work
        self.income = income
        self.buy_computer = 0
        self.not_buy_computer = 0
        self.need = need


class Iffication:
    """
    phân loại theo tuổi
    """

    def __init__(self, people):
        self.people = people

    def ifficationAge(self):
        if self.people.age < 15:
            self.people.not_buy_computer += 3
        # tuổi 15-25
        if 15 <= self.people.age <= 25:
            # nếu là học sinh
            if self.people.work == "student":
                # độ quan trọng bằng =1
                if self.people.need == "normal":
                    # có thể mua or không mua
                    self.people.buy_computer += 2
                elif self.people.need == "no":
                    # không mua thì not buy
                    self.people.not_buy_computer += 1
                    self.people.buy_computer += 1
                else:
                    self.people.buy_computer += 3
            else:
                if self.people.need == "normal":
                    # có thể mua or không mua
                    self.people.buy_computer += 1
                elif self.people.need == "no":
                    # không mua thì not buy
                    self.people.not_buy_computer += 1
                    self.people.buy_computer += 1
                else:
                    self.people.buy_computer += 3


people = People("linh", 18, "student", "1tr5", "no")
people1 = People("Linh", 13, "student", "1tr2", "")
people2 = People("", 24, "", "1tr2", "")
ip = Iffication(people2)
ip.ifficationAge()
print(ip.people.buy_computer)
print(ip.people.not_buy_computer)