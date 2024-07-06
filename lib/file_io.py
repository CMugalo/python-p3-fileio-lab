def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode = "w", encoding = "utf-8") as file_content:
        file_content.write("This is a test content.")

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode = "a", encoding = "utf-8") as append_content:
        append_content.write("\nAppended content.")

def read_file(file_name):
    with open(f"{file_name}.txt", mode = "r", encoding = "utf-8") as read_content:
        return read_content.read()


