
class tanimoto(object):
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def check(self) -> object:
        intersection = []
        for index, common_item in enumerate(self.list1):
            if self.list1[index] == self.list2[index]:
                 intersection.append(common_item)
            
        return float(len(intersection)) / (len(self.list1) + len(self.list2) - len(intersection))
   
if __name__ == "__main__":
    A = ['0.5', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0']
    B = ['0', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1', '0.34']
    print("budi")
    print(tanimoto(A, B).check())

