# Django City Location Package

A reusable Django app for managing city location data with geolocation features, including geocoding and reverse geocoding using **geopy**.

## Features
- Manage cities with geolocation data (latitude, longitude).
- Geocode city names to geographic coordinates using **geopy**.
- Reverse geocode coordinates back to city names.
- Simple integration with Django ORM.

## Tech Stack

- **Django**: Web framework for building the app.
- **geopy**: For geocoding and reverse geocoding.
- **Python**: Programming language for backend logic.
- **SQL**: Database supported by Django ORM.

## Installation
1. Install the package:
   ```
   pip install django-cityloc
    ```

## Usage 
 1. Creating a City 
    ```
    from cityloc.models import City
    
    # Create a city with geolocation
    city = City.objects.create(name="New York")

    ```

 2. Geocoding 
    ```
    city = City.objects.get(name="New York")
    geolocation = city.get_geolocation()
    print(geolocation)  # {'latitude': 40.7128, 'longitude': -74.0060}

    ```

 3. Reverse Geocoding 
    ```
    city_name = City.get_city_from_coordinates(40.7128, -74.0060)
    print(city_name)  # "New York"

    ```

## Running Test
```
python manage.py test cityloc
```
