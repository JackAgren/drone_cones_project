# Test Design
    - use REST API testing features for testing along with Djangos' testing functionality
    - run ```python manage.py test``` to run tests

## User Tests
    - Create a user
    - Delete a user
    - Create a guest
    - Delete a guest
    - Test that all user functions able to be used by guest work with guest
    - Test permissions (admin, customer, drone operator)
    - Test error is thrown if a duplicate user is created 
    - Get all users
    - Search for a user that doesn't exist
    - Edit an account with invalid permissions
    - Edit an account with valid permissions
    - Try to delete a user that doesn't exist
    - Edit an account that doesn't exist


## Inventory Tests
    - Create a new inventory item
    - Delete an inventory item
    - Restock an item
    - Check inventory status of an item
    - Check inventory status when out of stock
    - Try to order a inventory item that is out of stock
    - Try to make a duplicate item
    - Try to delete an item that doesn't exist


## Order Tests
    - Create a new order
    - Delete an order 
    - Try to delete an order that doesn't exist
    - Search an order
    - Search an order that doesn't exist
    - Attempt to create an order with an ice cream that is out of stock
    - Update delivery status
    - Test company earnings are calculating correctly
    - Test drone earnings are being calculated correctly


## Drone Tests
    - Register a new drone
    - Delete a drone
    - Change status of a drone
    - Check that drones are properly assigned
    - Check that errors are thrown if no drones are available
    - Make an order that requires more drones than one and check they are properly assigned
    - Get all owned drones
    - Get all drones that are available
    - Try to assign a drone that is unavailable  
    - Decomission a drone that doesn't exist
    - Attempt to make a duplicate drone
