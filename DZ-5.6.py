def count_subjects():
    try:
        mydict = {}
        with open("text_file_5.txt", encoding='utf-8') as file:
            for line in file:
                name, stats = line.split(':')
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f"{mydict}")
    except:
        return


count_subjects()
