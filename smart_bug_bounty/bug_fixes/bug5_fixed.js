function roundCurrency(amount) {
  return Math.round((amount + Number.EPSILON) * 100) / 100;
}

function calculateCartSummary(items, taxRate) {
  let subtotal = 0;

  const lineItems = items.map((item) => {
    const lineTotal = roundCurrency(item.price * item.quantity);
    subtotal = roundCurrency(subtotal + lineTotal);
    return {
      ...item,
      lineTotal,
    };
  });

  const tax = roundCurrency(subtotal * taxRate);
  const total = roundCurrency(subtotal + tax);

  return {
    items: lineItems,
    subtotal,
    tax,
    total,
  };
}

if (require.main === module) {
  const originalCart = [{ name: "Book", price: 19.99, quantity: 2 }];
  const summary = calculateCartSummary(originalCart, 0.08);
  console.assert(originalCart[0].price === 19.99, "Original item must not be mutated");
  console.assert(summary.subtotal === 39.98, "Subtotal mismatch");
  console.assert(summary.tax === 3.2, "Tax rounding mismatch");
  console.assert(summary.total === 43.18, "Total mismatch");
  console.log("bug5_fixed.js: All assertions passed.");
}

module.exports = { calculateCartSummary, roundCurrency };
