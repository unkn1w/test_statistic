# Build
Run this commands in app directory:
`docker-compose build`
`docker-compose up`

# API Endpoints

This API allows you to create, retrieve, and delete statistics objects.

### Resetting Statistics
To delete all the statistics objects, make a DELETE request to the `/statistics/reset` endpoint. If there are no statistics objects to delete, the API will return a message saying "Sorry, we do not have enough statistics to delete". If the deletion is successful, the API will return a message saying "Succesfully deleted [number of statistics objects] statistic objects".

### Creating Statistics
To create a new statistics object, make a POST request to the `/statistics/create` endpoint and pass in the statistics object as the request body. The API will then calculate the cost-per-click (CPC) and cost-per-mille (CPM) and save the object to the database. If there is an error during the creation, the API will return a message saying "Failed to create item" with a status code of 400. If the creation is successful, the API will return a message saying "Succesfully created!".

### Retrieving Statistics
To retrieve statistics objects, make a GET request to the `/statistics/` endpoint. You can also filter the results by a specific field by passing in the field name as a query parameter. The API will then return the statistics objects sorted by the specified field.

### Retrieving Statistics by Date Range
To retrieve statistics objects within a specific date range, make a GET request to the `/statistics/[start_date]/[end_date]/` endpoint, where `start_date` and `end_date` are in the format of `YYYY-MM-DD`. The API will then return the statistics objects within the specified date range.

#API Debug
For in-browser debug you can go to this url after starting the app:
`http://localhost:8008/docs`

#Tests
To run tests run this commands in terminal:
`docker-compose up -d --build`
`docker-compose exec web pytest .`
