# Overview

This is a script for the Django-based `datacenter` project. The script contains functions that manipulate data in the `Schoolkid`, `Teacher`, `Lesson`, `Subject`, `Commendation`, `Mark`, and `Chastisement` models. Specifically, it can perform the following actions:

* Adjust poor grades of a schoolkid
* Remove any chastisements linked to a schoolkid
* Add a commendation for a schoolkid in a specific subject

# Functions
### The script contains three functions:
* `fix_marks(schoolkid)`: Accepts a `Schoolkid` object and changes any grade that is a 2 or 3 to a 5.

* `remove_chastisements(schoolkid)`: Accepts a `Schoolkid` object and removes all chastisements related to this schoolkid.

* `create_commendation(name, subject)`: Accepts a name of a schoolkid and a subject title. It creates a commendation for the first found schoolkid with the given name in the specified subject. The commendation is given by a randomly chosen teacher and is assigned to a random lesson of the subject. The commendation text is also chosen randomly from a list.

# Usage

Before using this script, make sure you have Django and the `datacenter` project properly installed and configured. Also, make sure you have correctly populated the `Schoolkid`, `Teacher`, `Lesson`, `Subject`, `Commendation`, `Mark`, and `Chastisement` models with the necessary data.

To use the functions in the script, import them into your Django shell or another Python script in the `datacenter` project.

Here's an example of how to use these functions:
```python
from datacenter.models import Schoolkid
from your_script import fix_marks, remove_chastisements, create_commendation

# Get a schoolkid
schoolkid = Schoolkid.objects.get(full_name__contains="Ivan Ivanov")

# Fix their marks
fix_marks(schoolkid)

# Remove their chastisements
remove_chastisements(schoolkid)

# Create a commendation for them in Math
create_commendation("Ivan Ivanov", "Mathematics")
```

In the case when `create_commendation` encounters multiple schoolkids with the same name or doesn't find a schoolkid at all, it will print a message to the console and won't create a commendation.

# Disclaimer

Please use this script responsibly. Changing students' marks, deleting chastisements, or adding commendations could have serious ethical and educational implications. It's important to respect the integrity of educational records and to ensure that all students are assessed fairly and accurately. This script should be used for testing or data management purposes only.

## Project goals
The code is written for educational purposes - this is a lesson in a course on Python and web development at [Devman](https://dvmn.org).
