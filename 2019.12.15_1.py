# def div(a, b):
#     return a/b
#
#
# # if div(10, 5) == 2:
# #     print("Passed")
# # else:
# #     raise Exception("FAILED")
#
# assert div(10, 5) == 2, "Failed"
# print("Passed")
#
#
# def sqr_sum(a, b):
#     return (a + b) ** 2
#
#
# assert sqr_sum(2, 2) == 16, "FAILED"
# print("PASSED")
# assert sqr_sum(1, 1) == 4, "FAILED"
# print("PASSED")
# assert sqr_sum(3, 3) == 36, "FAILED"
# print("PASSED")
# assert sqr_sum(4, 5) == 81, "FAILED"
# print("PASSED")


# asercje nie służą tylko do testowania!

# def div(a, b):
#    try:
#         return a/b
#    except ZeroDivisionError:
#        print("Nie można dzielić przez zero.")

#
# def div(a, b):
#     assert b != 0, "Nie można dzielić przez zero"
#     return a/b
#
#
# div(5, 0)


def concatenate(str1, str2):
    return str1 + str2


assert concatenate("asd", "fgh") == "asdfgh", "Failed"
assert concatenate("ala", "ma") == "alama", "Failed"
assert concatenate("", "") == "", "Failed"
