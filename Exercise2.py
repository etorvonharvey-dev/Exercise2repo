try:
    note = input("Enter a short note: ")
    with open("notes.txt", "w") as file:
        file.write(note + "\n")
    print("Note saved successfully.\n")

    print("Reading file content:")
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

    new_note = input("\nEnter another note: ")
    with open("notes.txt", "a") as file:
        file.write(new_note + "\n")
    print("New note added.\n")

    print("Updated file content:")
    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print("An error occurred:", e)