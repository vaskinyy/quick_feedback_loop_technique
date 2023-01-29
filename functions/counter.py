def count_words(input_list):
    counter = {}

    for word in input_list:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
    return counter


words = ["car", "apple", "red", "the", "fox", "apple", "apple", "red"]
counts = count_words(words)
print(counts)

# # Better printing
# for word in counts:
#     print(word, counts[word])


# # Sorting in one line
# sorted_words = {key: value for key, value in sorted(counts.items(), key=lambda item: item[1])}
# print(sorted_words)

# # Sorting in multiple lines + debugger
# items = counts.items()
# print(items)
# sorted_items = sorted(counts.items(), key=lambda item: item[1])
# print(sorted_items)
# sorted_words_dict = {}
# for key, value in sorted_items:
#     sorted_words_dict[key] = value
# print(sorted_words_dict)
