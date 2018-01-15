
class tanimoto(object):
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def check(self) -> object:
        intersection = [common_item for common_item in self.list1 if common_item in self.list2]
        return float(len(intersection)) / (len(self.list1) + len(self.list2) - len(intersection))
        # c = [v for v in self.list1 if v in self.list2]
        # return float(len(c)) / len(self.list1) + len(self.list2) - len(c)


if __name__ == "__main__":
    A = ['0.5', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0']
    B = ['0', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1', '0.34']
    print("budi")
    print(tanimoto(A, B).check())

