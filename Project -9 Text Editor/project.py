import os

def open_file(filename):
    if not os.path.exists(filename):
        print("File does not exist. A new file will be created.")
        return ""
    with open(filename, 'r') as f:
        return f.read()

def save_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print("File saved successfully.")

def edit_file(content):
    print("\nCurrent Content (press Enter twice to finish editing):")
    print("-" * 40)
    print(content)
    print("-" * 40)
    print("Start typing below:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("== Simple Text Editor ==")
    filename = input("Enter filename: ")
    
    content = open_file(filename)
    
    while True:
        print("\nMenu:")
        print("1. View File")
        print("2. Edit File")
        print("3. Save File")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\n--- File Content ---")
            print(content)
        elif choice == '2':
            content = edit_file(content)
        elif choice == '3':
            save_file(filename, content)
        elif choice == '4':
            print("Closing the text editor.")
            break
        else:
            print("Invalid option. Try again.")

main()
