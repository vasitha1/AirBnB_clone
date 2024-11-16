=> AirBnB clone - The console
================================

- Description: This project is a simplified clone of the AirBnB web application
It includes a command interpreter to manage objects, a storage system to save
and retrieve data, and various models representing different
entities in the application.

Project Structure
Here's a quick overview of the project structure:

AirBnB_clone/
├── AUTHORS
├── console.py
└── models/
    ├── __init__.py
    ├── amenity.py
    ├── base_model.py
    ├── city.py
    ├── place.py
    ├── review.py
    ├── state.py
    ├── user.py
    └── engine/
        ├── __init__.py
        └── file_storage.py
- Explanation of Each Component
1. AUTHORS
Purpose: This file contains the names and contact information of contributor
to the project.

2. console.py
Purpose: This is the command interpreter for the project. It allows users to
interact with the application through various commands such as creating,
updating, and deleting objects.

Interaction: It interacts with the models module to perform
operations on the objects stored in the application.

3. models/
Purpose: This directory contains all the model definitions
and the storage engine for the project.

4. models/__init__.py
Purpose: This file initializes the models module and sets up the storage engine.

Interaction: It ensures that the storage engine is properly initialized and available for use throughout the project.

5. models/amenity.py
Purpose: Defines the Amenity class, which represents an amenity in the application (e.g., Wi-Fi, pool).

Interaction: Inherits from BaseModel and interacts with the storage engine to save and retrieve amenity objects.

6. models/base_model.py
Purpose: Defines the BaseModel class, which is the base class for all other 
models. It provides common attributes and methods such as id, created_at, updated_at, and save().

Interaction: Other models inherit from BaseModel to gain these common attributes and methods.
It interacts with the storage engine to save and retrieve objects.

7. models/city.py
Purpose: Defines the City class, which represents a city in the application.

Interaction: Inherits from BaseModel and interacts with the storage engine to save and retrieve city objects.

8. models/place.py
Purpose: Defines the Place class, which represents a place or property in the application.

Interaction: Inherits from BaseModel and interacts with the storage engine to save and retrieve place objects.

9. models/review.py
Purpose: Defines the Review class, which represents a review of a place in the application.

Interaction: Inherits from BaseModel and interacts with the storage engine to save and retrieve review objects.

10. models/state.py
Purpose: Defines the State class, which represents a state in the application.

Interaction: Inherits from BaseModel and interacts with the storage engine to save and retrieve state objects.

11. models/user.py
Purpose: Defines the User class, which represents a user in the application.

Interaction: Inherits from BaseModel and interacts with the storage engine to save and retrieve user objects.

12. models/engine/
Purpose: This directory contains the storage engine for the project.

13. models/engine/__init__.py
Purpose: This file initializes the engine module.

14. models/engine/file_storage.py
Purpose: Defines the FileStorage class, which is responsible for serializing and
deserializing objects to and from a JSON file.

Interaction: The FileStorage class provides methods to save, retrieve, and delete objects.
It interacts with all the model classes to perform these operations.

Interaction Between Components
Command Interpreter (console.py):

The command interpreter allows users to interact with the application by entering commands.

It uses the models module to perform operations on objects, such as creating, updating, and deleting them.

Models (models/):

The models represent different entities in the application, such as users, places, cities, states, amenities, and reviews.

Each model inherits from BaseModel to gain common attributes and methods.

The models interact with the storage engine to save, retrieve, and delete objects.

Storage Engine (models/engine/file_storage.py):

The FileStorage class is responsible for serializing objects to a JSON file and deserializing them back into objects.

It provides methods to save, retrieve, and delete objects.

The storage engine interacts with all the model classes to perform these operations.

