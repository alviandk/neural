art1 = [73, 83, 57, 54, 74, 56, 23, 16, 90, 82, 61, 55, 5, 70, 87, 80, 10] #17
art2 = [13, 8, 66, 12, 30, 22, 36, 33, 96, 79, 3, 34, 32, 93, 29, 92, 75, 18, 25, 14, 52, 53, 59, 20, 38, 44, 91, 63, 76, 47, 35, 45, 26, 65, 2, 86, 37, 85, 9, 43, 24, 97, 40, 28, 98, 11, 89, 1, 95, 17, 100, 78, 99, 7, 4, 46, 64, 62, 60, 48, 27, 71, 39, 21, 72, 41, 68, 19, 77, 31, 15, 6, 88, 81, 51, 50, 67, 58, 69, 49, 94, 42] #82

som1 = [
      3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25,
      27, 28, 29, 30, 31, 35, 41, 43, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 60,
      61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 79, 80, 81, 82, 83,
      85, 86, 87, 90, 91, 92, 95, 96, 97, 98, 99
    ] #72

som2 = [
      1, 2, 4, 20, 26, 32, 33, 34, 36, 37, 38, 39, 40, 42, 44, 47, 53, 58, 59, 62, 75,
      77, 84, 88, 89, 93, 94, 100
    ] #28

art1_som1 = [common_item for common_item in art1 if common_item in som1]
art1_som2 = [common_item for common_item in art1 if common_item in som2]
art2_som1 = [common_item for common_item in art2 if common_item in som1]
art2_som2 = [common_item for common_item in art2 if common_item in som2]

print("art1_som1:", art1_som1)
print("art1_som2:", art1_som2)
print("art2_som1:", art2_som1)
print("art2_som2:", art2_som2)

print("percent art1_som1:", len(art1_som1)/float(72)*100)
print("percent art1_som2:", len(art1_som2)/float(28)*100)
print("percent art2_som1:", len(art2_som1)/float(82)*100)
print("percent art2_som2:", len(art2_som2)/float(82)*100)

