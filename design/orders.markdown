# Ordering System

The ordering system defines how a user sees, selects and sends an order to the business, and how the business stores past orders and tracks current ones.

## User View

The user will see a menu that displays what is available in the inventory. The user selects how they would like their ice cream, including options for toppings, flavor, and size. They then proceed to checkout to review their order.

## Order information

The order information that is stored for a registered user includes the contents (flavors, size, toppings, ect), User ID, price, and what drone

## Order processing and delivery

The order information is first sent in its entirety to the order processing system. This system is responsable for:

1. telling the admin system the current status of orders
2. Informing the inventory system which ingredients were used
3. Assigning orders to certain drones????????
4. Calculating the ETA and returning it to the user.

## QUESTIONS

+ Does the drone system or the order system assign drones to orders?
+ Do we want live orders in a database or just in a list on the server (noob moment)
