# Low Level Frontend Design

## Account Pages

## Customer Pages

### View Menu & Select Items

The user can:
* Select a suggested cone
* Create their own cone
* Add a cone to their cart
* Move to the cart page
* Return to the dashboard page

Requests made to the backend:
* Get available cones, ice cream flavors, and toppings
    * As well as their prices

### View Cart & Check Out

The user can:
* View their cart
* Edit/remove items in their cart
* Return to the menu page
* Enter location information
* Place their order (which moves them to the order tracking page)

Requests made to the backend:
* Place a new order

### Track Order

The user can:
* View how far away their order is from arrival
* Be automatically moved to the order arrived page when the order completes

Requests made to the backend:
* Periodically checks to see the status of the order

### Order Arrived

The user can:
* Return to the dashboard page

Requests made to the backend:
* n/a

### Order History

The user can:
* View their past orders
* Select one to reorder (sends user to the checkout page)
* Return to the dashboard

## Drown Owner Pages

## Admin Pages
