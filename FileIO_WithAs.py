with open("text.txt", "w") as textfile:
  textfile.write("Success!")


with open("text.txt", "w") as my_file:
  if not my_file.closed:
    my_file.close()
  my_file.write("OK")