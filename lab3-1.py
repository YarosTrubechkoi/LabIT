def read_file(file_name, meth):
    try:
        with open(file_name, "r") as file:
            if meth == "Полн":
                content = file.read()
                print(content)
            elif meth == "Строч":
                for line in file:
                    print(line.strip())
            else:
                print("Неверный метод чтения.Выберите другой.")
    except FileNotFoundError:
        print("File was not found.")


read_file("example.txt", "Строч")
