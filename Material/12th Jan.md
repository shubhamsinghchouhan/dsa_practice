5. JPMC, 12th Jan 2026
---------------------

Round 1
-------
- Tell me about yourself
  - Explain recent project architecture [Aumni]
  - Explain about your python project
  - Parking lot problem
    - 3 floors, car 100 and bike 60 per hour, ticketing system, employee
      - LLD
      - DB queries, GROUP BY, JOINS
      - APIs
      - total sum(cache)
      - How many cars left
    - Binary search

Round 2
-------
  F8850
  - Vue js
  - 

Round 3
-------
  - OOPS
  - Design
  - DB - PG [Expected]
  - ORM [Expected]
  - Redis [Expected]
  - API - Rest API/ GraphQL [Expected]
  - Multiprocess
  - Multithreading
  - Debugging skills
  - PySpark [Expected]
  - Distributed Systems [Expected]

4. JPMC, 9th Jan 2026
---------------------
   - Tuple versus List using code, why Tuple is immutable, Can we add an elements in tuple, why?
     - Shallow copy versus deep copy using code example.
     - What is decorator with code examples?
     - What is Static method and class methods and their differences.
     - Property in Python.
     - What is 'with' keyword in python?
       - The with statement in Python simplifies resource management by automatically handling setup and cleanup, ensuring files or connections close safely even if errors occur.

         Replaces long try-except–finally blocks with cleaner syntax.
         Improves readability by reducing unnecessary boilerplate code.

         - Example: Using with statement to Open a File:
         **with open(...) as file**:
           - Opens the file safely and assigns it to file.
           Inside the block, file.read() Reads the file content.
           When the block ends, Python automatically closes the file even if an error occurs.

  
      with open("sample.txt", "r") as file:
        data = file.read()
        print(data)

  - What is abstract in python?
  - Linked List and detect cycle and list

2. JPMC, Dot NET., 18th Dec 2026
--------------------------------
- Agile
   ```
    Agile is an iterative software development methodology where work is delivered in small cycles called sprints.
    Agile focuses on iterative delivery, customer feedback, and continuous improvement.
    Why used?
    
    Fast delivery
    
    Continuous feedback
    
    Easy to adapt to change
    
    Example
    Sprint (2 weeks):
    
    Day 1 → planning
    
    Daily → stand-up
    
    End → demo + retrospective
- Constructors
  - Used to initialize objects. parameterized/non-parameterized
  ```
  class User:
    def __init__(self, name):
        self.name = name
- Access Modifiers (Python Style)
  ```
    Type        Meaning
    Public      name
    Protected   _name
    Private     __name

    class A:
      def __init__(self):
          self.name = "public"
          self._age = 20
          self.__salary = 5000

- Polymorphism
   ```
    Same function behaves differently.

    class Dog:
        def speak(self):
            return "Bark"
    
    class Cat:
        def speak(self):
            return "Meow"
- Abstraction

  Hiding implementation.
    ```
      from abc import ABC, abstractmethod
    
      class Payment(ABC):
          @abstractmethod
          def pay(self): pass

- Encapsulation
  Wrapping data + methods.
  ```
    class Bank:
      def __init__(self):
        self.__balance = 1000

- Inheritance
  ```
    class A:
    pass

    class B(A):
    pass

- Normalization

  Remove duplicate data. Example: Instead of storing customer name multiple times → store customer_id

- 10 GB chunks
  ```
  def read_chunks(file):
    with open(file) as f:
        while True:
            data = f.read(1024*1024)
            if not data:
                break
            print(data)

- Decorators
  ```
  def log(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

- Middleware
  Runs before/after request
  ```
  @app.before_request
  def auth():
    print("Auth check")

- Assembly
  ```Compiled file: .pyc Executed by Python VM```

- reverse string
  ```s[::-1]```

- Second highest element from an array
  ```sorted(set(arr))[-2]```

1. JPMC, Java, Ashwini
----------------------
- Find duplicate occurrences
  ```
  from collections import Counter
  Counter(arr)

- How many number divisible by given number
  ``` [x for x in arr if x%k==0] ```

- Kadane`s
  ```
  max_sum = curr = arr[0]
  for i in arr[1:]:
    curr = max(i, curr+i)
    max_sum = max(max_sum, curr)
