"""

This is just a general purpose library I wrote that I use in many of my Python applications

In python libs work just like static classes memory wise

e.g.:
import assistant
print assistant.dashed_line
"""

dashed_line = "--------------------------------------"
name_list = []
subject_list = []
# dictionary and staff are sets
dictionary = {"DEPARTMENT", "SUBJECTS", "FACULTY", "FACULTIES", "DEPARTMENTS", "SUBJECT", "INSTITUTE", "INSTITUTES"}
staff_semantics = {"PEOPLE", "STAFF"}


def _get_words(line: str) -> list:
    """
    This method return a clean of unwanted chars list of words from the line.

    :param line: str: A line read
    :return: list: List of words
    """
    """
    leading underscore means it's meant to be private, not that it actually is. :)
    Like in any language, Java included, where there's a will there's a way
    Here I' using liscomp which may seem confusing but is one of the best python feats in my opinion.
    It works very much like math Sets
    It could be accomplished by using regex but the kind of text should be known at first.
    I could compress it in one line code but it's bad when debugging your app.
    """
    unwanted = [';', ':', '.', ',']
    clean_line = ''.join(char for char in line if not char in unwanted)
    return clean_line.split()


def is_name(line: str) -> bool:
    """
    Given an ordered list and an input x, this function will return true if x is in the list

    e.g. list = ["ANNA", "BILL", "CLINTON", "DANIEL", "FERNANDO"]
    IsName("anna") => true
    IsName("ANNA") => true
    IsName("hello") => false

    :param line: A line read
    """
    """
    If you are 100% sure name_list is upper this code can be simplified
    line.upper() in name_list
    I'm not using binary search for python builtins are supposed to be very optimized
    If you are using big data I suggest pandas framework to handle this.
    Pandas use C compiled optimized algorithms
    """
    return line.upper() in [name.upper() for name in name_list]


def is_email(line: str) -> bool:
    """
    Given a string x
    If the first 6 letters are 'm', 'a', 'i', 'l', 't', 'o' then the function will return true
    E.g.
    IsEmail("mailto:quantumbiology@hotmail.wong") => true
    IsEmail("helo123") => false

    :param line: A line read
    """
    return 'mailto' == line[:6]


def is_department_link(line: str) -> bool:
    """
    Given an ordered list and an input x, this function will return true if x is in the list
    e.g. list = ["BIOLOGY", "CHEMISTRY", "GEOGRAPHY", "MATH", "PHYSICS"]
    IsDepartment("PHYSICS") => true
    IsDepartment("Physics") => true
    IsDepartment("anna") => false

    :param line:
    """
    """
    This method could be merged with is_name by a selector.
    """
    return line.upper() in [word.upper() for word in dictionary]


def breaker(line: str) -> list:
    """
    Given a senentence this function will break it down into a triangle
    e.g.
    Breaker("hello world") => ["hello world one",
                                     "world one",
                                           "one"]
    Breaker("hello my name is nathan okay") => ["hello my name is nathan okay",
                                                      "my name is nathan okay",
                                                         "name is nathan okay",
                                                              "is nathan okay",
                                                                 "nathan okay",
                                                                        "okay"]
    :param line:
    """
    f = [line]
    fields = [line[i+1:] for i in range(len(line)) if line[i] == ' ']

    return f + fields


def compare_subject(line: str) -> bool:
    """
    Given an input string x, CompareSubject(string) will return true if either GetWords() or Breaker() returns true
    SubjectList = ["BIOLOGY DEPARTMENT", "CHEMISTRY", "INSTITUTE OF GEOGRAPHY", "MATH", "SCHOOL OF PHYSICS"]
    CompareSubject("Biology") => true
    CompareSubject("School Of Physics") => true
    CompareSubject("hello") => false
    :param line:
    """
    subjects = flatten([_get_words(w) for w in subject_list] + [breaker(w) for w in subject_list])
    return line.upper() in subjects


def flatten(a):
    """
    Joins a sequence of sequences into a single sequence.  (One-level flattening.)
    E.g., join([(1,2,3), [4, 5], [6, (7, 8, 9), 10]]) = [1,2,3,4,5,6,(7,8,9),10]
    This is very efficient, especially when the subsequences are long.
    """
    n = sum([len(b) for b in a])
    l = [None]*n
    i = 0
    for b in a:
        j = i+len(b)
        l[i:j] = b
        i = j
    return l
