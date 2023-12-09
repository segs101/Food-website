![logo png](https://github.com/segs101/Food-website/assets/116885152/09097b88-cc99-4e0c-b462-915136fd74bf)
# [Foodhub](https://foodhub-blond.vercel.app/)

Foodhub is a Django restaurant website crafted using HTML, CSS, Python (Django), and Bootstrap 5.

## Installation

1. Create a virtual environment and activate it:

    ```bash
    py -m venv env
    env\Scripts\activate
    ```

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. In `food/settings.py`, set `DEBUG` to `False`:

    ```python
    DEBUG = False
    ```

2. Change the database settings to the default SQLite database:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

3. Add the following line under `MEDIA_URL`:

    ```python
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    ```

4. In `food/urls.py`, uncomment the following line:

    ```python
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
