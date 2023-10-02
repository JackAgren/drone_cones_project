# High-Level Design Document

## Overview
 
***TBD***

## Platform

The Drone Cones application will be a web app.

## Architecture

***TBD***

## Programming Languages and Frameworks

***TBD***

## Systems

### Account System

The account system is responsible for user accounts and logins. There are three types of user accounts:

* Customer
* Drone Owner
* Admin (Manager) 

#### User Data

User account data consists of a combination of data obtained by the user at
the creation of the account and data collected through the user's use of the app.
This data consists *at least* the following (based on the user's permission):

**Customer**
* Email
* Password
* Delivery address
* Order history

**Drone Owner**
* Email
* Password
* Drone ID(s)
    * Referencing the corresponding id's in the Drone table

**Admin**
* Email
* Password


#### User Permissions

Once a user is register for an account, the user will have different privileges granted to them based on account type.

**Customer**
* Log in to account
* View menu 
* Place an order
* View active order status
* View order history

**Drone Owner**
* Log in to account
* View drones registered under account
* Temporarily or permanently remove drone from service
* View payments
* View drone activity

**Admin**
* Log in to account
* View active and past orders
    * As well as a summary of past orders
* Check and update inventory
* View customer feedback
* View drone and drone owner info
* View incoming and outgoing payments
    * As well as a summary of financial activity
* Ban other users

#### Sub-Systems

The account system can be broken down into the following sub-systems:

* **Account Database** - 
This is a database of all user accounts made and is also where admin operations regarding account data takes place (i.e. banning an account, making changes to password, etc.). Permissions include (customer, admin, drone owners) that holds specific information for their respective roles (i.e. customers will have order history info stored).
* **Login Page** - 
This is where users will login into their accounts using their account credentials.
* **Registration Page** - 
This is where new user accounts will be made.
* **Account Page** - 
This is a page that will display user account info, as well as provide tools to users to modify info such as password and address.
* **Forgot Username/Password Page** - 
This is where users can contact customer support to help unlock their account.  For this project, an email system to send user credentials will not be made.
* **Authentication** - 
This will deal with security aspects of the user account logins in the background.

### Ordering System

The ordering system is responsible for issuing and tracking orders made by customers.  Both customer account holders AND non-account-holding customers should be able to use the ordering system.

An order can be defined as follows:

* Order ID - This is a unique ID that identifies a particular order
* Order Items List - This is a list of order items to be purchased.
* Total Cost - The cost of all items in the order, plus additional charges like tax.
* Estimated Time of Arrival - Tracks how much time the order will likely arrive while being delivered.

An order item is defined as follows:

* Container - Specifies the type () and size (number of scoops allowed in container) of a container that holds ice cream scoops.  The number of scoops placed onto a container cannot exceed the max size specified by the container size.
* Scoop List - A collection of ice cream scoops within the current container.  Each scoop is simply an ice cream flavor.
* Topping List - A collection of toppings added onto the scoops.

The ordering system can be broken down into the following sub-systems:

* **Menu** - Displays menu items and their availability.  It will query the inventory to determine which items are available, sales prices, etc..
* **Cart** - This is what will allow users to assemble their order.  This also tracks the total cost of the order.  Customer accounts should also option to use order history to fill out the cart.
* **Delivery and Payment** - This is where the user will input their delivery location and issue payment after confirming the order.  When payment is made, the finance system will add money to the finance database and update transaction database.
* **Order Tracking** - Once an order is placed, the order will be trackable by customers, displaying estimated time of arrival.  When the order is delivered, it should be placed into the customer's order history.  A database to hold pending orders should be considered.
  
### Inventory Management System

The inventory management system is responsible for tracking and updating the inventory.

An inventory item can be defined as follows:

* Item Name
* Item Type
* Current Quantity
* Sales Price per Unit
* Restock Cost per Unit

There are three types of inventory items:

* Containers (Cones, bowls, etc.)
* Ice Cream (Flavors)
* Toppings (Sprinkles, nuts, etc.)

**Considerations**: Units for each item type, as well as units in context of menu items need to be well-defined (i.e. Liters of ice cream vs. a "scoop" of ice cream needs to be defined).

The inventory system can be broken down into the following subsystems:

* **Inventory Database**: This is a database that holds all the inventory data and has functionality to query and update the inventory (restocking, depleting inventory for orders, etc.).  When inventory is restocked, the finance system will have money depleted from finance database and update the transactions database.
* **Inventory Report Generator**: This allows admins to see a report of the current state of the inventory.

### Finance System

The finance system is responsible for handling financial transactions and providing tools for admins to perform financial operations (generating reports, making lease payments, refunding customers, etc.)

The finance system can be broken down into the following sub-systems:

* **Orders Database** - Keeps track of orders made and allows easy auditing to keep track of finances and keep track of recipts. Will contain a field that contains the account that made the order as well as what was ordered and its price.

* **Finance Database** - This is a database that holds current state of the business finance.  It also has operations to add or deplete cash.  The database might hold the following info:

  - Current Balance


* **Finance Report Generator** - This will addlow admins to have a report of earnings, costs, and other relevant financial info.

* **Lease Payment System** - This is a tool that allows admins to make lease payments to drone owners.  The finance and transation databases should be updated as needed.

* **Customer Transaction Modifcation System** - This is a tool for admins to issue refunds or modify a customer transaction (i.e. applying a discount that may have been forgotten).  This also queries the order issues database from the customer support system for descriptions of the order issues to be resolved.  The finance and transation databases should be updated as needed.

### Drone System

The drone system is responsible for tracking data relevant to drones and drone owners.

A drone is defined as follows:

* Drone ID - A unique identifier for a particular drone.
* Drone Size (small, medium, large) - Size class of drone.  Determines how many scoops it can hold and how much the lease for the drone costs.
* Drone owner ID - A unique identifier for the drone owner for a particular drone.
* Status (Busy, Available) - Whether a drone is currently performing orders is available for new orders.
* Order List - List of orders being delivered by a particular drone.

The drone system can be broken down into the following sub-systems:

* **Drone Database** - This database will hold information about each registered drone. Admins will be able to have access to view information about registered drones. Drone owners will be able to see their own drones information. This database will keep track of, if the drone is available, its carrying capacity, its owner, and its location.   

### Customer Support System

The customer support system is responsible for handling order issues and customer complaints.

Order issues deal with problems with an order (overcharging the customer, forgetting to apply discounts, refunds, etc.) An order issue can be defined as follows:

* Order issue ID
* Customer info (provided by customer account or manual input for non-account holders)
* Order ID
* Description

A customer complaint is defined as follows:

* Customer complaint ID
* Customer info (provided by customer account or manual input for non-account holders)
* Description

The customer support system can be broken down into the following sub-systems:

* **Customer Complaint Database** - This simply holds all the customer complaints with the date they were issued and if they have been responded to or resolved.
* **Customer Support Report Generator** - This will allow admins to receive a report of customer complaints and pending order issues.
* **Customer Support Page** - This is where a customer can enter in an order issue or customer complaint.  This consists of inputting whether the problem is order-related or complaint-related, customer info and a text description of the order issue or complaint.
