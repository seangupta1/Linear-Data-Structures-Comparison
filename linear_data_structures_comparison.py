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
        New_Node = sll_Node(Val)
        if self.Head is None:
            self.Head = New_Node
            return
        else:
            if Val < self.Head.Val:
                New_Node.next = self.Head
                self.Head = New_Node
                return
            else:
                Current = self.Head
                while(Current.next != None and Current.next.Val < Val):
                    Current = Current.next
                if Current.next == None:
                    Current.next = New_Node
                    return
                else:
                    New_Node.next = Current.next
                    Current.next = New_Node
                    return
    
    def Search(self, Key):
        Current = self.Head
        while(Current.next != None):
            if(Current.Val > Key):
                return False
            if Current.Val == Key:
                return True
            Current = Current.next
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
        New_Node = dll_Node(Val)
        if self.Head is None:
            self.Head = New_Node
            self.Current = self.Head
            self.Current_Index = 0
            return
        else:
            if Val < self.Head.Val:
                New_Node.next = self.Head
                self.Head.prev = New_Node
                self.Head = New_Node
                self.Current = self.Head
                self.Current_Index = 0
                return
            else:
                Current = self.Head
                while(Current.next != None and Current.next.Val < Val):
                    Current = Current.next
                if Current.next == None:
                    Current.next = New_Node
                    New_Node.prev = Current
                    return
                else:
                    New_Node.next = Current.next
                    New_Node.prev = Current
                    Current.next = New_Node
                    New_Node.next.prev = New_Node
                    return
    
    def Search(self, Key):
        if self.Head == None:
            print("Doubly linked list is empty")
            return False
        while self.Current.prev and Key < self.Current.Val:
            self.Current = self.Current.prev
        while self.Current.next and Key > self.Current.Val:
            self.Current = self.Current.next
        if Key == self.Current.Val:
            return True
        return False

def Linear_Search(Arr, key):
    for i in range(len(Arr)):
        if Arr[i] == key:
            return True
    return False

def list_test(filepath, random_words):
    words = []

    start_time = time.time()
    with open(filepath, 'r') as file:
        for line in file:
            words.append(line)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print(f"time to import as list = {elapsed_time_ms:.3f}")

    start_time = time.time()
    for element in random_words:
        Linear_Search(words, element)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print(f"time to search as list = {elapsed_time_ms:.3f}")

def singly_linked_list_test(filepath, random_words):
    sll = Singly_Linked_List()

    start_time = time.time()
    with open(filepath, 'r') as file:
        for line in file:
            sll.Insert(line)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print(f"time to import as singly linked list = {elapsed_time_ms:.3f}")

    start_time = time.time()
    for element in random_words:
        sll.Search(element)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print(f"time to search as singly linked list = {elapsed_time_ms:.3f}")

def doubly_linked_list_test(filepath, random_words):
    dll = Doubly_Linked_List()

    start_time = time.time()
    with open(filepath, 'r') as file:
        for line in file:
            dll.Insert(line)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print(f"time to import as doubly linked list = {elapsed_time_ms:.3f}")

    start_time = time.time()
    for element in random_words:
        dll.Search(element)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print(f"time to search as doubly linked list = {elapsed_time_ms:.3f}")

if __name__ == "__main__":
    filepath = 'HW 3/1000-most-common-words.txt'

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
    random.shuffle(random_words)

    list_test(filepath, random_words)
    print()
    singly_linked_list_test(filepath, random_words)
    print()
    doubly_linked_list_test(filepath, random_words)