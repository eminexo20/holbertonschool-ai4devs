# AI Explanations of Complex Code - osCommerce v2.3.4

This document provides structured, plain-English explanations generated with AI assistance for four critical and high-complexity sections of the **osCommerce Online Merchant v2.3.4** legacy PHP codebase.

---

## Section 1 – `shopping_cart::calculate()` (`catalog/includes/classes/shopping_cart.php`)

### Legacy Code Snippet
```php
function calculate() {
  global $currencies;

  $this->total = 0;
  $this->weight = 0;
  if (!is_array($this->contents)) return 0;

  reset($this->contents);
  while (list($products_id, ) = each($this->contents)) {$qty = $this->contents[$products_id]['qty'];

    $product_query = tep_db_query("select products_id, products_price, products_tax_class_id, products_weight from " . TABLE_PRODUCTS . " where products_id = '" . (int)$products_id . "'");
    if ($product = tep_db_fetch_array($product_query)) {
      $prid =$product['products_id'];
      $products_tax = tep_get_tax_rate($product['products_tax_class_id']);
      $products_price =$product['products_price'];
      $products_weight =$product['products_weight'];

      $specials_query = tep_db_query("select specials_new_products_price from " . TABLE_SPECIALS . " where products_id = '" . (int)$prid . "' and status = '1'");
      if (tep_db_num_rows($specials_query)) {
        $specials = tep_db_fetch_array($specials_query);
        $products_price =$specials['specials_new_products_price'];
      }

      $this->total +=$currencies->calculate_price($products_price,$products_tax, $qty);$this->weight += ($qty * $products_weight);
    }
  }
}
