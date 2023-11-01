# Schemas
Here is the defined schema for all of our tables

## Inventory
- **`id` (Number):** A unique identifier for the item.
- **`description` (String):** A textual description of the item. Forexample, it represents the flavor of the ice cream.
- **`costPerUnit` (Number):** The cost per unit of the item.
- **`quantity` (Number):** The quantity of the item available in stock.
- **`dateFilled` (String):** The date when the item was last restocked. It follows the format "YYYY-MM-DD".
- **`category` (String):** The category to which the item belongs such as 'cone', or 'topping'. This also helps determin what the unit is when describing the price, ie 'cone' = boxes, 'ice cream' = gallons.
    - Possible values: "cone", "topping", "ice cream"
- **`salesPrice` (Float):** Amount the item will be sold at to customers.

#### Example JSON Object:

```json
{
    "id": 1,
    "description": "Vanilla",
    "costPerUnit": 3.99,
    "quantity": 50,
    "dateFilled": "2023-10-24",
    "category": "ice cream",
    "salesPrice": 2.99
}
```

## Drone Info
- **`id` (Number)**: A unique identifier for the order.
- **`ownerId` (Number)**: Identifier of the associated owner of the drone.
- **`status` (String)**: The status of the drone, detemines weither drone is available to deliver an order. 
    - Possible values: "active", "inactive"
- **`size` (String)**: The size of a drone.
    - Possibel values: "small", "medium", "large"

#### Example JSON Object:

```json
{
    "id": 1,
    "ownerId": 21,
    "status": "active",
    "size": "small"
}
```


## Orders
- **`id` (Number)**: Unique identifier for the order.
- **`userID` (Number)**: Identifier of the user placing the order.
- **`droneID` (Number[])**: List of drone identifiers assigned to this order.
- **`order` (Object[])**: List of ordered items.
  - **`cone` (String)**: Type of cone for the ice cream.
  - **`iceCream` (String[])**: List of ice cream flavors.
    - Size of array indicates number of scoops
  - **`toppings` (String[])**: List of toppings added to the ice cream.
  - **`cost` (Number)**: Total cost of the ordered items.
- **`location` (String)**: Delivery address of the order.
- **`timeOrdered` (String)**: Timestamp indicating when the order was placed (in UTC).
- **`timeDelivered` (String)**: Timestamp indicating when the order was delivered (in UTC).

**Note:** The total cost of an entire order can be determined by summing the cost of each item purchased.

#### JSON Object Example:

```json
{
    "id": 1,
    "userID": 1,
    "droneID": [101, 102],
    "order": [
        {
            "cone": "Chocolate",
            "iceCream": ["Vanilla", "Strawberry"],
            "toppings": ["Sprinkles", "Whipped Cream"],
            "cost": 5.99
        },
        {
            "cone": "Waffle",
            "iceCream": ["Chocolate"],
            "toppings": ["Nuts"],
            "cost": 4.49
        }
    ],
    "location": "123 Main St, Cityville",
    "timeOrdered": "2023-10-29T10:30:00Z",
    "timeDelivered": "2023-10-29T11:15:00Z"
}
```

