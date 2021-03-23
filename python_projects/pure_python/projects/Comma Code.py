spam = ['apples', 'bananas', 'tofu', 'cats']


def values(list_value):
    items_value = ' '

    for items in list_value:
        items_value = items_value + str(items)
        if list_value.index(items) == (len(list_value) - 2):
            items_value = items_value + ', and '

        elif list_value.index(items) == (len(list_value) - 1):
            items_value = items_value
        else:
            items_value = items_value + ', '
    return items_value


print(values(spam))
