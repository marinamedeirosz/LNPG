def calculate_average(numbers):
  total = sum(numbers)
  return total / len(numbers)

def find_max(numbers):
  max_number = numbers[0]
  for number in numbers:
      if number > max_number:
          max_number = number
  return max_number

def get_numbers():
  numbers = input("Enter numbers separated by spaces: ").split()
  # Converte input para float e verifica se é numérico ou string
  numbers = [float(num) for num in numbers if num.isnumeric()]  
  return numbers

# Verifica se a lista está vazia
def verify_input(numbers):
  if len(numbers) != 0:  
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_max(numbers))
  else:
    print("No numbers entered.")
    
def main():
  numbers = get_numbers()
  verify_input(numbers)

if __name__ == "__main__":
  main()