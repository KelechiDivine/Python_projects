# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
# list_length = []
# list_count = 0
# list_lists = {}
#
# for values in tableData:
#     total_list_count = 0
#     list_count += 1
#
#     for variable in values:
#         total_list_count += len(values)
#
#         list_lists["list:", list_count] = total_list_count
#
#     print("list", list_count, total_list_count)
#
# item_in_list_count = list(list_lists.values())
#
# sorted_list_len = (sorted(item_in_list_count, reverse = True))
#
# longest = sorted_list_len[0]
#
# for keys in range(len(tableData[0])):
#
#     for key in range(len(tableData)):
#         print(tableData[key][keys], end=" ")
#         key += 1
#     print(" ".rjust(list_lists['list:', 1], "-"))
#     keys += 1
#


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def table_printer(list_lists):

    column_widths = [0] * len(list_lists)  # j has become variables

    for variables in range(len(list_lists[0])):

        for values in range(len(list_lists)):

            column_widths[values] = len((max(list_lists[values], key=len)))  # tab_data has become list_lists

            a = list_lists[values][variables]

            print(a.rjust(column_widths[values]), end=" ")  # col_widths has become column_widths

        print("\n")


# table_printer(tableData)
print(table_printer(tableData))