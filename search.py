
def search(list, element):
    for i in range(len(list)):
        if element == numbers[i]:
           print("Element is in position: ", i)
           print("Number of calls to find element: ", i+1)
numbers = [1,4,6,7,3,8,9,2];
element = int(input("Enter element: "))

search(numbers, element)
