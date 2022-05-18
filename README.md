# django_models
[PR](https://github.com/ayat93a/django_models)

# Feature Tasks
- Django Models project
    - snacks app
        - Snack model
            - title field
            - purchaser field
            - description field
- `SnackListView` that extends appropriate generic view associated url path is an `empty string`

- `SnackDetailView` that extends appropriate generic view associated url path is `<int:pk>/`

- link in snack_list template to related detail page for each snack
-  link back to Home (snack_list) page from detail page.

To run this project in your device :
```
- $ git clone git@github.com:ayat93a/django_models.git
- $ cd snacks_crud_project
- $ poetry install
- $ poetry shell
- $ python manage.py runserver
```