const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const { listProducts, getItemById } = require('./data');

const app = express();
const client = redis.createClient();

const reserveStockById = promisify(client.set).bind(client);
const getCurrentReservedStockById = promisify(client.get).bind(client);

app.get('/list_products', (req, res) => {
  res.json(listProducts.map((item) => ({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity,
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(`item.${itemId}`) || 0;
    res.json({
      itemId: product.itemId,
      itemName: product.itemName,
      price: product.price,
      initialAvailableQuantity: product.initialAvailableQuantity,
      currentQuantity: parseInt(currentQuantity),
    });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(`item.${itemId}`) || 0;

    if (currentQuantity >= product.initialAvailableQuantity) {
      res.json({ status: 'Not enough stock available', itemId: itemId });
    } else {
      await reserveStockById(`item.${itemId}`, currentQuantity + 1);
      res.json({ status: 'Reservation confirmed', itemId: itemId });
    }
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
