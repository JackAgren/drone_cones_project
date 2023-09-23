# High-Level Design Document

## Platform

The Drone Cones application will be a web app.

## Architecture

Client/Server Architecture

## Programming Languages and Frameworks

Django, Python, Vue.js

## Systems

### Account System

The account system is responsible for user accounts and logins. There are three types of user accounts:

* Customer
* Drone Owner
* Admin (Manager) 

#### User Data

User account data consists of a combination of data obtained by the user at
the creation of the account and data collected through the user's use of the app.
This data consists *at least* the following (based on the user's role):

**Customer**
* Email
* Password
* Delivery address
* Order history

**Drone Owner**
* Email
* Password
* Drone ID(s)
    * Referencing the corresponding rows in the Drone table

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
This is a database of all user accounts made and is also where admin operations regarding account data takes place (i.e. banning an account, making changes to password, etc.).
* **Account Info Databases** - 
These are separate databases for specific account types (customer, admin, drone owners) that holds specific information for their respective roles (i.e. customers will have order history info stored).
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

The ordering system defines how a user sees, selects and sends an order to the dronecones, and how the business stores past orders and tracks current ones.

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

A transaction can be defined as follows:

* Transaction ID
* Amount (in dollars)
* Transaction Name
* Description

An important financial transaction for Drone Cones is lease payments to drone owners who lease their drones.  A lease consists of the following:

* Drone Size Class - The size of the drone (large, medium, small)
* Monthly Payment Rate - How much the drone owner will get paid per month.  The monthly rate is fixed.  The rate is determined by the size of the drone.

The finance system can be broken down into the following sub-systems:

* **Transaction Database** - This is a database of all transactions that occurred.
* **Finance Database** - This is a database that holds current state of the business finance.  It also has operations to add or deplete cash.  The database might hold the following info:

    * Current Balance - How much money the company currently has.
    * Start of Month Balance - How much money the company had a start of current month.
    * Earnings/Deficit of Month Amount - How much money earned or lost for the current month.

* **Finance Report Generator** - This will allow admins to have a report of earnings, costs, and other relevant financial info.

* **Lease Payment System** - This is a tool that allows admins to make lease payments to drone owners.  This should query the Drone Database (under Drone System) to get a list of leases currently active.  The finance and transation databases should be updated as needed.

* **Customer Transaction Modifcation System** - This is a tool for admins to issue refunds or modify a customer transaction (i.e. applying a discount that may have been forgotten).  This also queries the order issues database from the customer support system for descriptions of the order issues to be resolved.  The finance and transation databases should be updated as needed.

**Considerations**

* Transactions must account for tax.  Use 3% tax rate for all food itmes, which is in accordance to Utah State Tax Commision.

* Price of ice cream scoops are all the same.  $1 per scoop.

### Drone System

The drone system is responsible for tracking data relevant to drones and drone owners.

A drone is defined as follows:

Add drone capacity (number of scoops, S, M, L)

* Drone ID - A unique identifier for a particular drone.
* Drone Size (small, medium, large) - Size class of drone.  Determines how many scoops it can hold and how much the lease for the drone costs.
* Drone owner ID - A unique identifier for the drone owner for a particular drone.
* Status (Busy, Available) - Whether a drone is currently performing orders is available for new orders.
* Order List - List of orders being delivered by a particular drone.

The drone system can be broken down into the following sub-systems:

* **Drone Database** - This is a database that tracks all drones that are currently leased to the company.  There are also tools for drone owners to add or remove drones from the drone database if they wish to lease or unlease their drones.

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

* **Order Issue Database** - This holds a queue of customer issues to be resolved.  Customers can add order issues via the customer support page, and admins can remove order issues when resolved via the Customer Transaction Modifcation System in the finance database.
* **Customer Complaint Database** - This simply holds all the customer complaints.
* **Customer Support Report Generator** - This will allow admins to receive a report of customer complaints and pending order issues.
* **Customer Support Page** - This is where a customer can enter in an order issue or customer complaint.  This consists of inputting whether the problem is order-related or complaint-related, customer info and a text description of the order issue or complaint.
