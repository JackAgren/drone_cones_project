
const TOKEN = '';
const AUTH_HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': `Token ${TOKEN}`
};

async function populateAllInventory(qty=20) {
    //ice cream
    await addItem("Chocolate", .5, .25, "Ice Cream", qty);
    await addItem("Strawberry", .5, .25, "Ice Cream", qty);
    await addItem("Vanilla", .5, .25, "Ice Cream", qty);
    await addItem("Mint", .5, .25, "Ice Cream", qty);
    await addItem("Peanut Butter", .5, .25, "Ice Cream", qty);
    await addItem("Pistachio", .5, .25, "Ice Cream", qty);
    await addItem("Mystery", .5, .25, "Ice Cream", qty);
    await addItem("Cheesecake", .5, .25, "Ice Cream", qty);

    //topping
    await addItem("Cookie Dough", .3, .15, "Topping", qty);
    await addItem("Oreo", .3, .15, "Topping", qty);
    await addItem("Sprinkles", .3, .15, "Topping", qty);
    await addItem("Chocolate Sauce", .3, .15, "Topping", qty);
    await addItem("S'mores", .3, .15, "Topping", qty);
    await addItem("Mixed Berries", .3, .15, "Topping", qty);
    await addItem("Strawberries", .3, .15, "Topping", qty);

    //cones
    await addItem("Sugar", .49, .20, "Container", qty);
    await addItem("Waffle", .49, .20, "Container", qty);
    await addItem("Cup", .49, .20, "Container", qty);
    await addItem("Waffle Bowl", .49, .20, "Container", qty);
}

async function restockAllInventory(qty=20) {
    //ice cream
    await restockItem("Chocolate", qty);
    await restockItem("Strawberry", qty);
    await restockItem("Vanilla", qty);
    await restockItem("Mint", qty);
    await restockItem("Peanut Butter", qty);
    await restockItem("Pistachio", qty);
    await restockItem("Mystery", qty);
    await restockItem("Cheesecake", qty);

    //topping
    await restockItem("Cookie Dough", qty);
    await restockItem("Oreo", qty);
    await restockItem("Sprinkles", qty);
    await restockItem("Chocolate Sauce", qty);
    await restockItem("S'mores", qty);
    await restockItem("Mixed Berries", qty);
    await restockItem("Strawberries", qty);

    //cones
    await restockItem("Sugar", qty);
    await restockItem("Waffle", qty);
    await restockItem("Cup", qty);
    await restockItem("Waffle Bowl", qty);
}

function restockItem(name, qty) {
    const options = {
        method: 'POST',
        headers: AUTH_HEADERS,
        body: JSON.stringify({
            description: name,
            quantity: qty,
        }),
    };

    fetch('http://localhost:8000/inventory/update_item', options)
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log('Restock successful:', data);
        });
}

function addItem(name, salePrice, costPerUnit, category, qty) {

    let options = {
        method: 'POST',
        headers: AUTH_HEADERS,
        body: JSON.stringify({
            description: name,
            quantity: qty,
            salesPrice: salePrice,
            costPerUnit: costPerUnit,
            category: category
        }),
    };

    fetch('http://localhost:8000/inventory/add', options)
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log('Add successful:', data);
        });
}