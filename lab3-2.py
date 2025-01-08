def write_to_file(file_name, text, append=False):
    mode = "a" if append else "w"

    with open(file_name, mode) as file:
        file.write(text)
        print("Text has been written to the file.")


user_text = input("Введите текст для записи в файл: ")

# Запись текста в новый файл user_input.txt
write_to_file("user_input.txt", user_text, append=True)
