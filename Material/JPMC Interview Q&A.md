5. JPMC, 12th Jan 2026
---------------------
Round 1
-------
- Tell me about youself
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
OOPS
Design
DB - PG [Expected]
ORM [Expected]
Redis [Expected]
API - Rest API/ GraphQL [Expected]
Multiprocess
Multithreading
Debugging skills
PySpark [Expected]
Distributed Systems [Expected]


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

# Shared by Neha
[x] Data types and data structures
  Data Types
  int, float, str, list, tuple, dict, set
  
  Data Structures
  List, Stack, Queue, Dict, Set

- [x] Diff b/w list and tuple
  - List → mutable
  - Tuple → immutable
  - Set →
  - Dictionary →

  - [x] Generator
  ```
     def gen():
      for i in range(5):
          yield i
    - A generator is a function that produces values one at a time using yield instead of return.

      It saves memory and is used when working with large or infinite data.
      
      🔹 1️⃣ Generator Using yield
      def my_generator():
          yield 1
          yield 2
          yield 3
      
      g = my_generator()
      print(next(g))   # 1
      print(next(g))   # 2
      print(next(g))   # 3
      
      🔹 2️⃣ Generator with Loop
      def numbers(n):
          for i in range(n):
              yield i
      
      for x in numbers(5):
          print(x)
      
      
      Output:
      
      0 1 2 3 4
      
      🔹 3️⃣ Generator Expression (One-Line)
      
      Like list comprehension but with () instead of []
      
      gen = (x*x for x in range(5))
      
      print(next(gen))  # 0
      print(next(gen))  # 1
      
      🔹 4️⃣ Generator for Squares till 5 (Interview favorite)
      def square_gen():
          for i in range(1,6):
              yield i*i
      
      
      Output:
      
      1 4 9 16 25

- [x] Decorator
- [x] Iterator
  ```
  it = iter([1,2,3])
  next(it)
- [x] Diff Range and xrange
  - xrange python 2
  - Python 3 → only range (lazy)
- [ ] List, dict, comprehension 
  ```
  [x*x for x in range(5)]
  {k:v for k,v in d.items()}
- [ ] Remove duplicates or find duplicate?
  ```list(set(lst))```

- [ ] Common elements from list
  ```set(a) & set(b)```

- [ ] Input [1,1,2,2,2] => Output [(1,2),(2,3)]
  ``` [(k,v) for k,v in Counter(lst).items()] ```
- [ ] Count vowels in string
  ``` sum(1 for c in s if c in "aeiou") ```

- [ ] Max element from list
  ```max(lst)```

- [ ] Singleton class
  ```
  class Singleton:
    _instance=None
  ```
- [ ] Monkey patching
- [ ] List comprehension
- [ ] What is memory leak
- [ ] How to convert json into python object
  ```json.loads(data)```

- [ ] Which package is used for reading xl file
  ```openpyxl, pandas```

- [ ] I have a dictionary it contains set of value, key is 1 and value is active and key is 2 value is inactive and last key is 3 value is proactive.
    I want to delete 1 key without changing original dictionary.
  ```
    new = dict(old)
    del new[1]
  ```
- [ ] If I want to get dictionary value using key but that key doesnt present in dictionary.
  ```d.get(key, "Not found")```
- [ ] Create a model student with name and location and save data into database using django
- [ ] Multiple decorator
def login_required(func):
    def wrapper():
        print("Checking user")
        func()
    return wrapper

def log(func):
    def wrapper():
        print("Logging")
        func()
    return wrapper

@log
@login_required
def dashboard():
    print("User Dashboard")
Multiple decorators are applied bottom-up; the decorator closest to the function runs first.
- [ ] Async and await
- [ ] How to make generator
- [ ] I have a list [1,2,3,4,5] list 2 [4,5,6,7,8]
    Create a list where it will be combination of list and unique elements
- [ ] Check two strings are anagram or not?
  - sorted(string1) == sorted(string2)
- [ ] How to find file in a folder in python?
  - os.walk()
- [ ] Generator that gives square of number till 5 ?
  - (i*i for i in range(1,6))

[GIT]
- Git commands 
  - How to handle merge conflicts
  
     `Identify Conflicts: <<<<<<<, =======, and >>>>>>>, communicate, fix, push`
     or `git merge --abort`
  - (Tips to Prevent Conflicts)

     ```Integrate Often: Merge or rebase your feature branch with the main branch frequently. Small, Focused Commits: Keep commits small and specific to avoid large changes in one go. Communicate: Talk to teammates about areas you're both working on. Smaller Tasks: Break down work into smaller, manageable pieces (e.g., less than 3 days). ``` 
 
  - Diff Git fetch and git pull

    ``` The main difference is that git fetch downloads remote changes without modifying your local working files, while git pull downloads and automatically merges the changes into your current branch. In essence, git pull is a shortcut for git fetch followed by git merge ```
- What is git and version control system.
- Git stash

[Imp]
- Specially List, Tuple, Dictionary, Generator, Iterator, Lambda function, Comprehension ye imp h




[Agents]
> Provider - OpenAI      |  Model name - GPT-4.1, GPT-5 to GPT-5.2	
> Provider - Anthropic   |  Model name - Claude Haiku, Opus, Sonnet 4, 4.5
> Provider - Google      |  Model name - Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3 Pro
> Provider - Grok xAI    |  Model name - Code Fast 1
> Provider - Raptor mini |  Model name - Fine - tuned GPT-5 mini
