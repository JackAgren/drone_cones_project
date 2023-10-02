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
