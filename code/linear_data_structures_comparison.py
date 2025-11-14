import random
import time

class sll_Node:    
    def __init__(self, Val):
        self.Val = Val
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.Head = None
    
    def Insert(self, Val):
        New_Node = sll_Node(Val) # Create new node and set value
        if self.Head is None: # Set node to head if list is empty
            self.Head = New_Node
            return
        else:
            if Val < self.Head.Val: # Place node before head if value is less than head
                New_Node.next = self.Head
                self.Head = New_Node
                return
            else:
                Current = self.Head
                while(Current.next != None and Current.next.Val < Val): # Traverse the list until finding correct place for new node
                    Current = Current.next
                if Current.next == None: # If we are at the end of the list
                    Current.next = New_Node # Place new node at end of list
                    return
                else: # Not at end of list
                    New_Node.next = Current.next # Place node in current spot
                    Current.next = New_Node
                    return
    
    def Search(self, Key):
        Current = self.Head # Start at list head
        while(Current): # Traverse the list
            if(Current.Val > Key): # Past spot where key should be so stop searching
                return False 
            if Current.Val == Key: # Found key
                return True
            Current = Current.next # Traverse the list
        return False

class dll_Node:
    def __init__(self, Val):
        self.Val = Val
        self.prev = None
        self.next = None

class Doubly_Linked_List:
    def __init__(self):
        self.Head = None
        self.Current = None
    
    def Insert(self, Val):
        New_Node = dll_Node(Val) # Create new node and set value
        if self.Head is None: # Set node to head if list is empty
            self.Head = New_Node
            self.Current = self.Head
            self.Current_Index = 0
            return
        else:
            if Val < self.Head.Val: # Place node before head if value is less than head
                New_Node.next = self.Head
                self.Head.prev = New_Node
                self.Head = New_Node
                self.Current = self.Head
                self.Current_Index = 0
                return
            else:
                Current = self.Head
                while(Current.next != None and Current.next.Val < Val): # Traverse the list until finding correct place for new node
                    Current = Current.next
                if Current.next == None: # If we are at the end of the list
                    Current.next = New_Node # Place new node at end of list
                    New_Node.prev = Current
                    return
                else: # Not at end of list
                    New_Node.next = Current.next # Place node in current spot
                    New_Node.prev = Current
                    Current.next = New_Node
                    New_Node.next.prev = New_Node
                    return
    
    def Search(self, Key):
        if self.Head == None: # Check for empty list
            print("Doubly linked list is empty")
            return False
        while self.Current.prev and Key < self.Current.Val: # Traverse reverse
            self.Current = self.Current.prev
        while self.Current.next and Key > self.Current.Val: # Traverse forward
            self.Current = self.Current.next
        if Key == self.Current.Val: # Key found
            return True
        return False # Key not found

def Linear_Search(Arr, key):
    for i in range(len(Arr)): # Scan the array until key found or end reached
        if Arr[i] == key:
            return True
    return False

def list_test(filepath, random_words):
    words = []

    start_time = time.time() # Start clock for import
    with open(filepath, 'r') as file: # Load in file
        for line in file:
            words.append(line) # Add file words to list
    end_time = time.time() # End clock
    elapsed_time = end_time - start_time # Calculate elapsed time
    elapsed_time_ms = elapsed_time * 1000 # Convert to milliseconds
    print(f"time to import as list = {elapsed_time_ms:.3f}") # Print results

    start_time = time.time() # Start clock for search
    for element in random_words: # Loop through words to search
        Linear_Search(words, element) # Search for word
    end_time = time.time() # End clock
    elapsed_time = end_time - start_time # Calculate elapsed time
    elapsed_time_ms = elapsed_time * 1000 # Convert to milliseconds
    print(f"time to search as list = {elapsed_time_ms:.3f}") # Print results

def singly_linked_list_test(filepath, random_words):
    sll = Singly_Linked_List() # Initialize singly linked list

    start_time = time.time() # Start clock for import
    with open(filepath, 'r') as file: # Load in file
        for line in file: # Loop through each line in file
            sll.Insert(line) # Insert word into singly linked list
    end_time = time.time() # End clock
    elapsed_time = end_time - start_time # Calculate elapsed time
    elapsed_time_ms = elapsed_time * 1000 # Convert to milliseconds
    print(f"time to import as singly linked list = {elapsed_time_ms:.3f}") # Print results

    start_time = time.time() # Start clock for search
    for element in random_words: # Loop through each item
        sll.Search(element) # Search for word in singly linked list
    end_time = time.time() # End clock
    elapsed_time = end_time - start_time # Calculate elapsed time
    elapsed_time_ms = elapsed_time * 1000 # Convert to milliseconds
    print(f"time to search as singly linked list = {elapsed_time_ms:.3f}") # Print results

def doubly_linked_list_test(filepath, random_words):
    dll = Doubly_Linked_List() # Initialize doubly linked list

    start_time = time.time() # Start clock for import
    with open(filepath, 'r') as file:
        for line in file: # Loop through each line in file
            dll.Insert(line) # Insert word into doubly linked list
    end_time = time.time() # End clock
    elapsed_time = end_time - start_time # Calculate elapsed time
    elapsed_time_ms = elapsed_time * 1000 # Convert to milliseconds
    print(f"time to import as doubly linked list = {elapsed_time_ms:.3f}") # Print results

    start_time = time.time() # Start clock for search
    for element in random_words: # Loop through each item
        dll.Search(element) # Search for word in doubly linked list
    end_time = time.time() # End clock
    elapsed_time = end_time - start_time # Calculate elapsed time
    elapsed_time_ms = elapsed_time * 1000 # Convert to milliseconds
    print(f"time to search as doubly linked list = {elapsed_time_ms:.3f}") # Print results

if __name__ == "__main__":
    filepath = '1000-most-common-words.txt' # Path to input file

    # List of random words to search in the lists
    random_words = [
    "abacus", "abandon", "ability", "abnormal", "abolish", "absence", "absent", "absurd", "academy", "accelerate",
    "accent", "accept", "access", "accident", "acclaim", "acclimate", "accompany", "accomplish", "account", "accuse",
    "acquire", "acquit", "acrobatic", "activate", "adapter", "addiction", "address", "adjacent", "adopt", "advance",
    "adventure", "adverse", "advice", "affair", "affect", "affiliate", "afford", "agency", "agenda", "agility",
    "alcohol", "alert", "allegro", "almanac", "allocate", "amateur", "amazing", "amplify", "ancestor", "ancient",
    "android", "analyze", "ancestor", "angelic", "angry", "animal", "annex", "anxiety", "apology", "apparel",
    "appeal", "applied", "appraise", "arbitrary", "arrange", "arrive", "ascend", "aspect", "assault", "assert",
    "assess", "assign", "assist", "assure", "athlete", "attempt", "balance", "bachelor", "beacon", "beefy",
    "billion", "blessing", "breathe", "bravery", "brevity", "brilliant", "brisk", "bubbles", "budget", "buffet",
    "capital", "capture", "cattle", "celebrity", "center", "cereal", "chaotic", "charter", "chase", "chicken",
    "chronic", "climate", "clumsy", "comfort", "compass", "compare", "complex", "conform", "confuse", "connect",
    "contain", "contrast", "control", "convene", "crystal", "cuisine", "current", "daring", "debate", "decide",
    "define", "defuse", "delight", "demand", "depart", "derive", "design", "detect", "define", "diamond",
    "disease", "display", "doctor", "domain", "donate", "doubt", "dynamic", "eclipse", "elevate", "embellish",
    "embody", "emerge", "engage", "enlist", "enrage", "enroll", "enrich", "escape", "escort", "examine",
    "excuse", "expand", "expose", "extreme", "fabric", "famous", "flavor", "flood", "forbid", "formula",
    "freight", "genuine", "gravity", "guitar", "gutter", "habitat", "harmony", "honor", "horizon", "hostage",
    "impact", "income", "induce", "inquire", "insert", "inspire", "intend", "invest", "journey", "justice",
    "knight", "lattice", "lecture", "lending", "listen", "manner", "manual", "mature", "mentor", "minute",
    "modern", "motivate", "murder", "natural", "notable", "nurture", "obvious", "object", "offend", "optimize",
    "overcome", "owner", "paddle", "parent", "parcel", "parole", "patrol", "patient", "pleasure", "project",
    "propose", "pursue", "rattle", "reaction", "recover", "relax", "relief", "remedy", "revolve", "reword",
    "safety", "scatter", "secure", "select", "settle", "shadow", "shining", "simple", "society", "subtle",
    "success", "supply", "tactile", "tease", "template", "tension", "ticket", "transfer", "trivial", "turbine",
    "unclear", "unfold", "unique", "unwind", "update", "venture", "verify", "victory", "vivid", "wager",
    "wander", "weigh", "wholesome", "witness", "wonder", "warrant", "yield", "young", "zealous", "zenith"
    ]
    random.shuffle(random_words) # Shuffle words for random search order

    list_test(filepath, random_words) # Test with Python list
    print() # Spacer between tests
    singly_linked_list_test(filepath, random_words) # Test with singly linked list
    print() # Spacer between tests
    doubly_linked_list_test(filepath, random_words) # Test with doubly linked list
