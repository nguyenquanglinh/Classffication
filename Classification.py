class Base:
    def __init__(self, property_name):
        self.property = property_name


class Object_base:
    def __init__(self, property_s):
        self.property_s = property_s


class key_value:
    def __init__(self, key_d, value_d):
        self.value_d = value_d
        self.key_d = key_d

    def Get_item(self, str_0):
        if self.key_d == str_0:
            return self.value_d
        return self.key_d


class dict_d:
    def __init__(self):
        self.dict = []

    def len(self):
        return len(self.dict)

    def Add_value(self, keys_value):
        self.dict.append(keys_value)

    def Compare_item_to_list(self, list, str):
        for i in list:
            if i == str:
                return False
        return True

    def Get_value_number(self, data_):
        """
        lấy ra các giá trị trên cùng 1 cột trong bảng dữ liệu đồng thời tìm tất cả các thuộc tính trên đối tượng
        :param number:chỉ số cột
        :return:trả về các thuộc tính trên cùng 1 cột
        """
        result = [[]]
        number = 0
        while True:
            ret = []
            for i in self.dict:
                if i.key_d == number and True == self.Compare_item_to_list(ret, i.value_d):
                    ret.append(i.value_d)
            number += 1
            if len(ret) == 0:
                break
            result.append(ret)
        del result[0]
        return result


def doc_file(file_name):
    """
    đọc file từ 1 tên file
    :param file_name: tên file muốn đọc
    :return: 1 list của 1 list dùng để biểu diễn bảng dữ liệu đầu v
    """
    op = open(file_name, "r")
    a1 = op.readlines()
    list_arr = [[]]
    for i in a1:
        x = i.split()
        list_t = []
        for j in x:
            list_t.append(j)
        list_arr.append(list_t)
    del list_arr[0]
    return list_arr


def split_attribute(arr):
    """
    phân chia các thuộc tính vào trong dict theo cot
    :param arr: là bảng dữ liệu lấy r
    :return: dict gồm thuộc tính và stt
    """
    da_ta = dict_d()
    for i in arr:
        dem = 0
        for j in i:
            key_values = key_value(dem, j)
            da_ta.Add_value(key_values)
            dem += 1
    return da_ta


def create_attribute(data_table):
    """
    tạo các thuộc tính của đối tượng
    :param data_table:bảng dữ liệu
    :return:1 tập các thuộc tính
    """
    d1 = data_table[1]
    list_attribute = []
    for i in d1:
        list_attribute.append(Base(i))
    return list_attribute


def create_object(property_s):
    return Object_base(property_s)


while True:
    data_table = doc_file("input.txt")
data_dict = split_attribute(data_table)
xx = data_dict.Get_value_number(data_dict)
for i in xx:
    print(i)
