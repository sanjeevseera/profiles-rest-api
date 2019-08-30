# Profiles Rest API
Profiles Rest API source code.

## Creating a Django Project and App
[Django App](https://github.com/sanjeevseera/profiles-rest-api/commit/f0595edf2db82d57c521006f77ff5e19841b1d64)
### Start django project
django-admin.py startproject profile_project .
### Sreate django application
python manage.py startapp profiles_api
### Enable app in Django settings file
profile_project > settings.py >
INSTALLED_APPS [
  'rest-framework',
  'rest_framework.authtoken',
  'profiles_api',]
### Run Server
python manage.py runserver


## Setup the Database
[create databases](https://github.com/sanjeevseera/profiles-rest-api/commit/70c914bc3be9d71830e679a5a4df2faeeca7eeaa)

## APIView added POST
[Hello APIview](https://github.com/sanjeevseera/profiles-rest-api/commit/107b8fd92d62e24c8edb7345da1ebe414dc2c645)

[Added GET, PUT, PATCH, DELETE](https://github.com/sanjeevseera/profiles-rest-api/commit/c30d78831e830205797acfd8f890595d862502d8)

## View Sets
[View sets to Profile api](https://github.com/sanjeevseera/profiles-rest-api/commit/0d0d542b44e6645c33673e6110a5bae06b702f01)


## Profile ViewSet
[profiles ViewSet](https://github.com/sanjeevseera/profiles-rest-api/commit/43f8866a5b7c83dd5e29c2c1f06658d491461349)

[profiles permissions](https://github.com/sanjeevseera/profiles-rest-api/commit/1664a5b68cd8a81409cf6e9638a4f6345af4856d)

## search user profile
[search user profile](https://github.com/sanjeevseera/profiles-rest-api/commit/65242eb9f2701762f2e6e60c363ac01fdb0b2724)

## Login API
[login API](https://github.com/sanjeevseera/profiles-rest-api/commit/1664a5b68cd8a81409cf6e9638a4f6345af4856d)

