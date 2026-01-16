3. JPMC, 9th Jan 2026
-----------------
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
- [x] Diff b/w list and tuple
- [x] Generator
- [x] Decorator 
- [x] Iterator
- [x] Diff Range and xrange
- [ ] List, dict, comprehension 
- [ ] Remove duplicates or find duplicate?
- [ ] Common elements from list
- [ ] Input [1,1,2,2,2] => Output [(1,2),(2,3)]
- [ ] Count vowels in string
- [ ] Max element from list
- [ ] Singletone class
- [ ] Monkey patching
- [ ] List comprehension
- [ ] What is memory leak
- [ ] How to convert json into python object
- [ ] Which package is used for reading xl file
- [ ] I have a dictionary it contains set of value, key is 1 and value is active and key is 2 value is inactive and last key is 3 value is proactive.
    I want to delete 1 key without changing original dictionary.
- [ ] If I want to get dictionary value using key but that key doesnt present in dictionary.
- [ ] Create a model student with name and location and save data into database using django
- [ ] Multiple decorator
- [ ] Asynch and await
- [ ] How to make generator
- [ ] I have a list [1,2,3,4,5] list 2 [4,5,6,7,8]
    Create a list where it will be combination of list and unique elements
- [ ] Check two strings are anagram or not?
- [ ] How to find file in a folder in python?
- [ ] Generator that gives square of number till 5 ?

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
