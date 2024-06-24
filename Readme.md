## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/bhyeanhasan/InternTask.git
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:

    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```sh
    python manage.py runserver
    ```

- **Users**
  - Register: `POST /api/users/register/`
  - Login: `POST /api/users/login/`
  - Retrieve User: `GET /api/users/<id>/`
  - Update User: `PUT /api/users/<id>/update/`, `PATCH /api/users/<id>/update/`
  - Delete User: `DELETE /api/users/<id>/delete/`

- **Projects**
  - List/Create Projects: `GET /api/projects/`, `POST /api/projects/`
  - Retrieve/Update/Delete Project: `GET /api/projects/{id}/`, `PUT /api/projects/{id}/`, `DELETE /api/projects/{id}/`

- **Tasks**
  - List/Create Tasks within a Project: `GET /api/tasks/{project_id}/task/`, `POST /api/tasks/{project_id}/task/`
  - Retrieve/Update/Delete Task: `GET /api/tasks/{id}/`, `PUT /api/tasks/{id}/`, `DELETE /api/tasks/{id}/`

- **Comments**
  - List/Create Comments on a Task: `GET /api/comments/{task_id}/comment/`, `POST /api/comments/{task_id}/comment/`
  - Retrieve/Update/Delete Comment: `GET /api/comments/{id}/`, `PUT /api/comments/{id}/`, `DELETE /api/comments/{id}/`
