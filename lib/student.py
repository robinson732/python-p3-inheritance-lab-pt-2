# Superclass
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

# Subclass
class ChattyStudent(Student):
    def hello(self):
        # Call the parent class method
        super().hello()
        # Add the chatty extra phrase
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        # Call the parent class method ten times
        for _ in range(10):
            super().raise_hand()

