with open("shakespier.txt", mode = "r") as s_file:
    words_all = []
    for line in s_file.readlines():
        words = line.strip().split(" ")
        words_all = words_all + words
    
    print(len(words_all))
    unique_words = set(words_all)
    print(len(unique_words))

    with open("unique_words.txt", mode = "w") as write_file:
        for item in sorted(unique_words):
            write_file.write(item)
            write_file.write("\n")


print("finished")