def edit_text():
      print("Witaj w prostym edytorze tekstu!")
      print("Wpisz 'zapisz' aby zapisać plik, 'wczytaj' aby wczytać plik, lub 'wyjście' aby zakończyć edycję.")
      
      text = ""
      
      while True:
            line = input("Wpisz tekst: ")
            if line.lower() == 'zapisz':
                  file_name = input("Podaj nazwę pliku, do którego chcesz zapisać: ")
                  save_file(file_name, text)
                  print(f"Tekst zapisany w pliku {file_name}.")
            elif line.lower() == 'wczytaj':
                  file_name = input("Podaj nazwę pliku, który chcesz wczytać: ")
                  loaded_text = open_file(file_name)
                  print("Wczytany tekst \n" + loaded_text)
                  text = loaded_text
            elif line.lower() == 'wyjście':
                  print("Zakończono edycję.")
                  break
            else:
                  text += line +"\n"
                  
      return text

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

edit_text()