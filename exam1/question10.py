def print_message(message, repeate_count):
    repeate_count = 1
    if repeate_count <= 1:
        return repeate_count
    else:
        return 0
      
  
print(print_message("its", "1"))

def print_message(message, repeate_count):
    x = 1
    while x < repeate_count:
        print(message)
        x += 1
      
  
print(print_message("its", 64))
