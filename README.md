This project is a REST API for working with vehicle and driver tables.
It contains a list of open endpoints for performing the following operations:

Operations with drivers:

- `/drivers/driver/ `
  GET - output of the list of drivers
  POST - creating a new driver

- `/drivers/driver/<driver_id>/`
  
  GET - obtaining information on a particular driver
  PUT - driver editing
  DELETE - driver removal

- `/drivers/driver/?created_at__gte=10-11-2021`
 
  GET - output of the list of drivers created after 10-11-2021

- `/drivers/driver/?created_at__lte=16-11-2021`

  GET - output of the list of drivers created before 16-11-2021

Operations with vehicles:

- `/vehicles/vehicle/ `
  GET - output of the list of cars
  POST - creating a new machine

- `/vehicles/vehicle/<vehicle_id>`
  GET - obtaining information on a specific car
  PUT - car editing
  DELETE - car removal

- `/vehicles/vehicle/?with_drivers=yes`
  GET - output of the list of cars with drivers

- `/vehicles/vehicle/?with_drivers=no`
  GET - output of the list of cars without drivers

- `/vehicles/set_driver/<vehicle_id>/ `
  PUT - editing the driver field for a specific car

As an example, the screenshot shows the `drivers/driver/` endpoint on the local host: `http://127.0.0.1:8000/drivers/driver`
![alt text](screens/screen1_drivers.png "drivers")

Get request displays a list of all drivers at the top of the window. With a POST request at the bottom of the page, you can add a new driver by filling in the first_name and last_name fields and clicking the POST button.
 
