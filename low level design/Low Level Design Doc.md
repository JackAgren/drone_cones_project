# Low-Level Design Document
## Tables
- User Table
    * Email: String
    * Password: String
    * UserID: Number
    * Permissions: String

- Order Table
    * OrderID: Number
    * UserID: Number
    * DroneID: Number[]
    * Cone: String[]
    * Ice Cream: String[]
    * Number of Scoops: String[]
    * Toppings: String[]
    * Cost: Float
    * Order Location: String
    * Number of Cones: Number
    * Time: Date
    * Time Delivered: Date

- Drone Info Table
    * DroneID: Number 
    * OwnerID: Number
    * Status: String
    * Type: String

- Inventory
    * ItemID: Number
    * Quantity: Number
    * CostPerUnit: Number
    * DateFilled: Date
    * Type: String

- Permissions Change Requests
    * RequestID: Number
    * PermissionRequested: String
    * ApprovalStatus: Boolean | Null

## Resources
- User Table
    * Create Account: PUSH
    ```
    function create_account(request) 
        if request.PUSH
            validate user info in body
            if invalid
                return jsonError("Invalid paramaters.")
            else
                push to database
    ```
    * Login: GET
    ```
    function login(request)
        if request.GET
            validate user login
            if invalid
                return jsonError("Incorrect username or password.")
            else
                return user_data 

    ```
    * Edit Account Info: PUSH
    ```
    function edit_account_info(request)
        if request.PUSH
            validate edit request
            if invalid
                return jsonError("Invalid account paramater")
            else
                edit table(request.userID).paramater(request.updated_info)
    ```
    * Delete Account: PUSH
    ```
    function delete_account(request)
        if request.PUSH
            validate delte request
            if invalid
                return jsonError("Account deletion denied")
            else
                edit table(request.userID).drop row
    ```
    * Update Permissions: PUSH
    ```
    function update_permissions(request)
        if request.PUSH
            if request.perm_request.approval_status
                if new permission = drone operator
                    if admin has approved drone operator
                        table(userID).permission = DRONE_OPERATOR
                    else 
                        return jsonError("Drone not associated with account")
                if new permission = admin
                    if at an admin has approved the request
                        table(userID).permission = ADMIN
                    else
                        return jsonError("Admin privileges have not been approved")
            else
                return jsonError("Admin must approve changes.")
    ```
    * Register Drone: PUSH
    ```
        if request.PUSH
            if user has permission DRONE_OPERATOR
                if request.drone is on approved drone list
                   Drone table.add(request.drone) 
            else
                return jsonError("User is not a drone operator.")
    ```

- Order Table
    * Get Order Based on Param: GET 
    ``` 
        function order_search(request)
            if user.permission == admin
                return jsonResponse(table(search category).param)
            else
                return jsonError(You do not nave permission to view this information.)
    ```
    * Make New Order: PUSH
    ```
        function new_order(request)
            Add order info to order table
            return jsonResponse("Order recieved")
    ```
    * Delete Order: PUSH
    ``` 
    function delete_order(request)
        if user.permission == admin
            remove(table(order_id))
            return jsonResponse(table(search category).param)
        else
            return jsonError(You do not nave permission to perform this action.)
     ```

    * Update Order: PUSH
    ``` 
    function order_update(request)
        if user.permission == admin
            find order using order id 
            table(id).update_category = new_value
            return jsonResponse(update successful)
        else
            return jsonError(You do not nave permission to perform this action.)
    ```


- Drone Table
    * Register Drone: PUSH
    ```
        function make_drone(request)
            if user.permission == drone_owner or admin
                If all info is present and a valid type
                    Add all info to drone table
                    return jsonResponse("Drone added successfully)
                else
                    return jsonError("Registration failed; check the information you entered and try again")
            else
                return jsonError("Register as a drone owner before registering your drone")

    ```
    * Update Drone Status: PUSH
    ```
         function drone_status(request)
            if user.permission == drone_owner or admin
                drone.status = request.status 
                return jsonResponse("Drone {drone} is now {status}.")
    ```
    * Get Status: GET
    ```
        function get_drone_status(request)
            If permission == admin or drone_owner or it's from the ordering system:
                return jsonResponse(droneID.status)
            else
                return jsonError("You don't have permission to view this information.")
    ```
    * Decomission Drone: PUSH
    ```
        function decomission_drone(request)
            If permission == admin or drone_owner:
                flag drone as decomissioned
                return jsonResponse("Drone successfully decomissioned.")
            else
                return jsonError("You don't have permission to remove this drone.")
    ```
    * Return All Drones With Same OwnerID: GET 
    ```
        function get_all_owned_drones(request)
            If permission == admin or drone_owner:
                from drone table get drones with ID == OwnerID
                return list of drones with shared OwnerID
            else
                return jsonError("You don't have permission to remove this drone.")
    ```

- Inventory Table
    * Update Inventory: PUSH
    ```
        function increment_inventory(request)
            If user.permission == admin:
                find inventory item using ItemID
                add value to Quantity
                set DateFilled to current date
            else
                return jsonError("You don't have permission update the inventory.")
        
        function decrement_inventory(request)
            find inventory item using ItemID
            If Quantity >= value:
                subtract value from Quantity
            else
                return jsonError("Insufficent resources.")
    ```
    * Add new item to Inventory: PUSH
    ```
        function add_inventory_item(request)
            If user.permission == admin:
                add new row to table
                ItemID = next unique number
                Quantity = given value
                CostPerUnit = given value
                DateFilled = todays date
                Type = given value
            else
                return jsonError("You don't have permission to add to the inventory.")
    ```
    * Remove From Inventory: PUSH
    ```
        function remove_from_inventory(request)
            If user.permission == admin:
                find inventory item using ItemID
                remove item row from table
            else
                return jsonError("You don't have permissions to edit the inventory.")
    ```
    * Get Inventory Status: GET 
    ```
        function get_inventory(request)
            If user.permission == admin:
                find inventory item using ItemID
                return jsonResponse({item json object})
            else
                return jsonError("You don't have permission update the inventory.")
    ```


- Permission Change Requests
    * Add Request: PUSH
    ```
        if request.PUSH
            if request is valid
               Permission Change Request table.add(request.request) 
            else
               return jsonError("Requst invalid")
    ```
    * Delete Request: PUSH
    ```
        if request.PUSH
            if user permissions is ADMIN
               table.delte(requestID) 
            else
               return jsonError("User does not have permssion")
    ```
    * Approve Request: PUSH
    ```
        if request.PUSH
            if user permissions is ADMIN
               table.requestID.status = true 
            else
               return jsonError("User does not have permission")
    ```
    * Get Request: GET
    ```
        if request.PUSH
            if user permissions is ADMIN
                return table.request.all
            else
               return jsonError("User does not have permission")
    ```

## Django

Django will serve as a server and as storage for the data tables. We'll keep data tables in their own apps (mostly) to have a design that is modular, easy to maintain, and easy to upgrade.

+ User: contains the User table and permission request table. Handles login validation and permission checking.
+ Drones: Contains the Drone table.
+ Inventory: Contains the inventory table.
+ Orders: Contains the orders table.

Each app will also have an api usage view that is only accessable to admin account holders. This could potentially be removed in the final version, but it will be useful as we build up the application.

# Low Level Frontend Design

## UI Diagrams Figma Project Link
https://www.figma.com/file/kuxGFMhTcyI4Y4n39xwAdq/DroneCones_UX_Blueprint?type=design&node-id=0%3A1&mode=design&t=ioyr94quhipTfDVW-1

## Account/Main Pages

### Home

The user can:

* Move to the login page
* Move to the menu page
* Move to the page to create a customer account
* Move to the page to create a drone owner account
* Move to the page to apply to create an admin account

No requests are made to the backend.

### Login

The user can:

* Enter their login information and attempt to log in
    * If login is successful, the user is moved to the dashboard page
* Move to the page to create an account
* Move to the customer support page

Requests made to the backend:

* Verify login information
    * And get user ID / role (permissions)

### Dashboard

The user can (depending on the permissions of their role):

* Access admin tools
    * Move to the financial records page
    * Move to the manage payments page
    * Move to the manage inventory page
    * Move to the manage accounts page
    * Move to the manage menu page
* Access drone owner tools
    * Move to the drone registration page
    * Move to the payments page
    * Move to the drone activity page
* Access customer options
    * Move to the menu page
    * Move to the order history page

No requests made to the backend from the initial dashboard.

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

No requests are made to the backend.

### Order History

The user can:

* View their past orders
* Select one to reorder (sends user to the checkout page)
* Return to the dashboard

## Drone Owner Pages
### Menu
The drone owner will have options to move between the registration, activity, and payments pages.
### Drone Registration
The drone owner can:

* Register a new drone
* Temporarily remove a drone from service
* Permanently remove a drone from service

Requests made to the backend:

* Query drone data
    * Get drone ID, name
* Change drone data
    * Change drone status

### Drone Activity
The drone owner can:

* View data for each drone registered

Requests made to the backend:

* Query drone data
    * Get deliveries
    * Get status
### Earnings

The drone owner can:

* View their current balance

Requests made to the backend:

* Query user
* Query orders

## Admin Pages

### Manage Accounts

The admin user can:

* View list of all registered accounts.
* Modify the account type via dropdown menu.
* Modify whether the account is active or banned.

Requests made to the backend:

* Query accounts database to generate a list of accounts consisting of:
  * User ID
  * Email
  * Account Type
  * Account Status
* Given a specific user account:
  * Request to change Account Type in database.
  * Request to change Account Status in database.

### Manage Inventory

The admin user can:

* View list of all inventory items.
* Restock items.

Requests made to the backend:

* Query inventory database to generate a list of inventory items consisting of:
  * Item ID
  * Item Name
  * Item Cost per Unit
  * Quantity
* Given a specific item:
  * Request to modify quantity of an item in inventory database.
  * Request to modify balance in finance database.
  * Request to modify current month profit/deficit.
  * Request to add new transaction corresponding to restock action.

* Stock Status is *dervied* from whether or not quantity is or is not 0.

### Manage Lease Payments

The admin user can:

* View list of active leases.
* Make lease payments to selected unpaid leases.

Requests made to the backend:

* Query drones database to generate a list of leases consist of:
  * Drone ID
  * Drone Owner ID
  * Drone Size Class
  * Amount Due
* Given a specific drone ID:
  * Request to modify amount due data point corresponding to the drone ID.
  * Request to modify balance in finance database.
  * Request to modify current month profit/deficit.
  * Request to add new transaction corresponding to lease payment action.
  
* Payment status is *dervied* from whether or not amount due is or is not 0.

### Financial Records

The admin user can:

* See current balance.
* See current earnings for the month.
* See a list of all transactions, arranged from most recent to lease recent.
* Generate a finance report (printable document or PDF).

Requests made to the backend:

* Query finance database to generate:
  * Current Balance
  * Current Month Starting Profit
    * Recorded at the start of each month.
  * Current Month Profit/Deficit
    * Calculated by summing together all transactions from start of month to current date.
  * A list of transactions consisting of:
    * Transaction ID
    * Transaction Type
    * Description
    * Amount

### Manage Menu

The admin user can:

* See list of menu items.
* Add/Remove menu items.
* Edit the price of menu itmes.

Requests made to the backend:

* Query inventory database and menu database to generate list of menu items consisting of:
  * Item ID (from inventory database)
  * Item Name (from inventory database)
  * Item Type (from inventory database)
  * Sales Price (from menu database)
* Given an item ID to remove:
  * Request deletion of menu item in menu item database.
  * Request deletion of corresponding inventory item.
* Given an item ID to edit:
  * Request modification of menu item sales price.
* Given an item name, item tpye, cost per unit, and sales price,
  * Request insertion of corresponding inventory item in inventory database.
  * Request insertion of menu item in menu item database.

* Stock Status is *dervied* from whether or not quantity (from inventory database) is or is not 0.

## UI Diagrams

![Image](./Screenshots/HomePage.png)
![Image](./Screenshots/LoginPage.png)
![Image](./Screenshots/RegistrationPage.png)
![Image](./Screenshots/Dashboard%20-%20Customer.png)
![Image](./Screenshots/Menu%20Page.png)
![Image](./Screenshots/Checkout.png)
![Image](./Screenshots/Order%20Status.png)
![Image](./Screenshots/Arrived.png)
![Image](./Screenshots/Dashboard%20-%20Admin.png)
![Image](./Screenshots/Financial%20Records.png)
![Image](./Screenshots/Manage%20Lease%20Payments.png)
![Image](./Screenshots/Manage%20Lease%20Payments%20-%20Pay%20Lease.png)
![Image](./Screenshots/Manage%20Inventory.png)
![Image](./Screenshots/Manage%20Inventory%20-%20Restock.png)
![Image](./Screenshots/Manage%20Accounts.png)
![Image](./Screenshots/Manage%20Menu.png)
![Image](./Screenshots/Manage%20Menu%20-%20Menu%20Item%20Add.png)
![Image](./Screenshots/Manage%20Menu%20-%20Menu%20Price%20Edit.png)
![Image](./Screenshots/Dashboard-Drone%20Owner.png)
![Image](./Screenshots/Drone%20Registration.png)
![Image](./Screenshots/Drone%20Registration%20-%20New%20Drone.png)
![Image](./Screenshots/Drone%20Activity.png)
![Image](./Screenshots/Drone%20Earnings.png)