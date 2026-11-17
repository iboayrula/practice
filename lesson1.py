# =====================================================================
#  LESSON 1: Variables, functions and if/else
# =====================================================================
#  How to use this file:
#    1. Read each section's explanation.
#    2. Do the TASK: replace the ___ or the word "pass" with your code.
#    3. Save (Ctrl + S) and run it in the terminal:   python lesson1.py
#    4. The checks at the bottom print PASS or NOT YET for each task.
#    5. After each task that passes: git add . / git commit / git push
#
#  Lines starting with # are COMMENTS. Python ignores them; they're for you.
# =====================================================================


# ---------------------------------------------------------------------
#  PART 1: VARIABLES
# ---------------------------------------------------------------------
#  A variable is a labelled box that holds a value.
#
#      city = "Sofia"        # text (called a "string"), always in quotes
#      age = 30              # whole number ("int")
#      price = 4.99          # number with decimals ("float")
#      is_raining = False    # True or False ("bool"), capital T / F
#
#  print() shows something in the terminal:
#      print(city)                     ->  Sofia
#      print("I live in", city)        ->  I live in Sofia
#      print(f"I live in {city}")      ->  I live in Sofia   (an "f-string")
#
#  The f-string is the one you'll use most: put f before the quotes,
#  then any variable inside { } gets filled in.

# TASK 1: Fill in your own values (replace each ___ ).
my_name = "Ibo"           # your name, in quotes
my_age = 37                # your age, a number, no quotes
likes_coding = True      # change to True if you're enjoying this :)

# TASK 2: Make a sentence using an f-string.
#   It should read exactly like:  My name is Ibo and I am 30 years old.
#   (with your own name and age, using the variables above)
sentence = "my_name, my_age ,likes_coding"

sentence = f"My name is {my_name} and I am {my_age} years old."

print(sentence)
       



# ---------------------------------------------------------------------
#  PART 2: FUNCTIONS  (the most important part)
# ---------------------------------------------------------------------
#  A function is a reusable mini-machine:  input  ->  work  ->  output.
#
#      def greet(name):              # "def" = define a function called greet
#          return f"Hello, {name}!"  # "return" = the output it gives back
#
#      greet("Ibo")                  # -> "Hello, Ibo!"
#      greet("Maria")                # -> "Hello, Maria!"
#
#  Rules to notice:
#    - the line with def ends with a colon  :
#    - everything inside the function is INDENTED (4 spaces, or press Tab)
#    - "name" is a PARAMETER: a placeholder filled in when you call it
#    - "return" hands the result back. Without it, the function gives None.
#
#  Why it matters for AI: an agent "tool" is just a function like this.
#  The AI decides to call get_weather("Sofia"), your function runs,
#  and its return value goes back to the AI.

# TASK 3: Finish this function so it returns  a + b.
def add(a, b):
    pass  # delete "pass" and write:  return a + b


# TASK 4: Write a function that turns Celsius into Fahrenheit.
#   Formula:  fahrenheit = celsius * 9 / 5 + 32
#   Example:  to_fahrenheit(100) should return 212.0
def to_fahrenheit(celsius):
    pass


# TASK 5: Write a function that builds a greeting with TWO parameters.
#   Example:  welcome("Ibo", "Sofia")  should return
#             "Welcome Ibo, how is the weather in Sofia?"
def welcome(name, city):
    pass


# ---------------------------------------------------------------------
#  PART 3: IF / ELSE  (making decisions)
# ---------------------------------------------------------------------
#      temperature = 25
#      if temperature > 30:
#          print("Hot")
#      elif temperature > 15:          # "else if": checked only if the first was False
#          print("Nice")
#      else:                           # everything else
#          print("Cold")
#
#  Comparisons:   >  <  >=  <=   ==  (equal)   !=  (not equal)
#  Note: = puts a value in a variable;  == ASKS "are these equal?"
#  Combine with:  and   or   not

# TASK 6: Return "even" if the number is even, otherwise "odd".
#   Hint: number % 2 gives the remainder after dividing by 2.
#         If the remainder == 0, the number is even.
def even_or_odd(number):
    pass


# TASK 7: Describe the weather.
#   Return "hot"  if celsius is 30 or more
#   Return "nice" if celsius is 15 or more (but under 30)
#   Return "cold" otherwise
def describe_weather(celsius):
    pass


# TASK 8 (challenge): Can this person rent a car?
#   They can if they are 21 or older AND have a licence.
#   Return True or False.
#   Example: can_rent_car(25, True) -> True,  can_rent_car(19, True) -> False
def can_rent_car(age, has_licence):
    pass


# =====================================================================
#  CHECKS: don't edit below this line. Just run the file and read the output.
# =====================================================================
def check(task, test):
    try:
        ok = test()
    except Exception as error:
        print(f"  Task {task}: NOT YET  (error: {error})")
        return False
    print(f"  Task {task}: {'PASS' if ok else 'NOT YET'}")
    return ok


print("\n--- Lesson 1 checks ---")
results = [
    check(1, lambda: my_name not in ("", "___") and isinstance(my_age, int) and my_age > 0),
    check(2, lambda: sentence == f"My name is {my_name} and I am {my_age} years old."),
    check(3, lambda: add(2, 3) == 5 and add(-1, 1) == 0),
    check(4, lambda: to_fahrenheit(100) == 212 and to_fahrenheit(0) == 32),
    check(5, lambda: welcome("Ibo", "Sofia") == "Welcome Ibo, how is the weather in Sofia?"),
    check(6, lambda: even_or_odd(4) == "even" and even_or_odd(7) == "odd" and even_or_odd(0) == "even"),
    check(7, lambda: describe_weather(35) == "hot" and describe_weather(30) == "hot"
                     and describe_weather(20) == "nice" and describe_weather(15) == "nice"
                     and describe_weather(5) == "cold"),
    check(8, lambda: can_rent_car(25, True) is True and can_rent_car(19, True) is False
                     and can_rent_car(30, False) is False and can_rent_car(21, True) is True),
]
print(f"\n{sum(results)} of {len(results)} tasks done.")
if all(results):
    print("All done! Commit and push, then tell Claude you finished lesson 1.")
