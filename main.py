
def open_file(name_file):
      try:
            with open(name_file, 'r') as file:
                  contents = file.read()
            return contents
      except FileNotFoundError:
            return f"Błąd: Plik '{name_file}' nie został znaleziony."
      except Exception as e:
            return f"Wystąpił błąd: {e}"

name_file = 'file.txt'
contents = open_file(name_file)
print(contents)

def save_file(name_file, text):
      try:
            with open(name_file, 'w') as file:
                  file.write(text)
            return f"Plik '{name_file}'został zapisany."
      except Exception as e:
            return f"An error occured: {e}"

name_file = 'nowy_plik.txt'
text_to_save = "Oto przykładowy tekst, który zostanie zapisany w pliku." 
result = save_file(name_file, text_to_save)
print(result)