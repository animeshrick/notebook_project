
# Django REST API: Notebook Management System

This project is a **Django REST API** for managing a notebook application where users can create, update, delete, and view notes. The project uses Django ORM, models, serializers, and APIView to provide a clean and scalable solution for CRUD operations.

---

## Features

1. **Create Notes:** Add new notes with a title and content.
2. **Update Notes:** Modify existing notes using the `id`.
3. **Delete Notes:** Remove notes using the `id`.
4. **Retrieve Notes:** Fetch all notes in the database.
5. **Timestamps:** Automatically tracks `created_at` and `updated_at` timestamps for all notes.

---

## Project Structure

```
notebook_project/
│
├── notebook_project/       # Django project settings and configurations
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── notes/                  # Django app for managing notebook functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Note model definition
│   ├── serializers.py      # DRF serializer for the Note model
│   ├── tests.py
│   ├── urls.py             # URL patterns for API
│   ├── views.py            # APIView-based logic
│
├── db.sqlite3              # SQLite database
├── manage.py               # Django management tool
```

---

## Prerequisites

Ensure you have the following installed:
- Python 3.11
- pip (Python package manager)
- Django (4.0+)
- Django REST Framework

---

## Installation

1. Clone the repository:
   ```bash
   https://github.com/animeshrick/notebook_project.git
   cd notebook_project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scriptsctivate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

| **HTTP Method** | **Endpoint**       | **Action**                         | **Required Parameters**          |
|------------------|--------------------|-------------------------------------|-----------------------------------|
| GET              | `/api/notes/`     | Fetch all notes                    | None                              |
| POST             | `/api/notes/`     | Create, update, or delete a note   | `action`, `id` (optional for some)|

### Request Examples

1. **Create a Note**
   - **Request Body:**
     ```json
     {
         "action": "create",
         "title": "My First Note",
         "content": "This is the content of the note."
     }
     ```

2. **Update a Note**
   - **Request Body:**
     ```json
     {
         "action": "update",
         "id": 1,
         "title": "Updated Note Title",
         "content": "Updated note content."
     }
     ```

3. **Delete a Note**
   - **Request Body:**
     ```json
     {
         "action": "delete",
         "id": 1
     }
     ```

4. **Retrieve All Notes**
   - **Request:** `GET /api/notes/`

---

## Timestamps
- **`created_at`**: Automatically set when the note is created.
- **`updated_at`**: Automatically updated when the note is modified.

---

## File Breakdown

1. **`models.py`:**
   - Defines the `Note` model with fields `title`, `content`, `created_at`, and `updated_at`.

2. **`serializers.py`:**
   - Converts the `Note` model to JSON and vice versa using DRF.

3. **`views.py`:**
   - Implements API endpoints using `APIView` to handle:
     - `create` (adding new notes)
     - `update` (editing notes)
     - `delete` (removing notes)

4. **`urls.py`:**
   - Maps API requests to the appropriate views.

---

## Future Enhancements

- Add user authentication for note management.
- Implement note search and filtering.
- Pagination for large datasets.
- Extend timestamps with additional details like timezone or user actions.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

- **Animesh Banerjee**  
  [GitHub Profile](https://github.com/animeshrick/)
