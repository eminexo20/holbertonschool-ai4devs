function calculateCartSummary(items, taxRate) {
  let subtotal = 0;

  for (const item of items) {
    item.price = item.price * item.quantity;
    subtotal += item.price;
  }

  const tax = subtotal * taxRate;
  const total = subtotal + tax;

  return {
    items,
    subtotal,
    tax,
    total,
  };
}

module.exports = { calculateCartSummary };
