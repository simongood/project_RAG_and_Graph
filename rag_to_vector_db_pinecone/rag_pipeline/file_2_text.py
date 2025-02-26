
def file_2_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    

if __name__ == "__main__":
    text = file_2_text('data/mock_file_data.txt')
    print(text)