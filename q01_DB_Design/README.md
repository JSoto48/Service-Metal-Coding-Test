# Question 1: Database Design
I tried to make the foundation of this schema is extensible without being over-engineered.

## Product Example
https://www.pvcfittingsonline.com/collections/pvc-gate-valves/products/2-pvc-socket-gate-valve-spears-2022-020

This was the product I used as a reference for designing the database schema.

---

## Database Schema

Using SQLite for development simplicity, but the schema is compatible with MySQL.


### Products Table
```sql
CREATE TABLE "products_product" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(500) NOT NULL,
    "sku" varchar(100) NOT NULL UNIQUE,
    "description" text NOT NULL,
    "main_category" varchar(100) NOT NULL,
    "subcategory" varchar(100) NOT NULL,
    "price" decimal NOT NULL,
    "stock_quantity" integer NOT NULL,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);
```


### Product Images Table
```sql
CREATE TABLE "products_productimage" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "product_id" bigint NOT NULL REFERENCES "products_product" ("id"),
    "image_url" varchar(200) NOT NULL,
    "alt_text" varchar(200) NOT NULL,
    "is_primary" bool NOT NULL,
    "display_order" integer NOT NULL,
    FOREIGN KEY ("product_id") REFERENCES "products_product" ("id")
);

CREATE INDEX "products_productimage_product_id" ON "products_productimage" ("product_id");
```


### Product Specifications Table
```sql
CREATE TABLE "products_productspecs" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "product_id" bigint NOT NULL REFERENCES "products_product" ("id"),
    "spec_name" varchar(100) NOT NULL,
    "spec_value" varchar(300) NOT NULL,
    FOREIGN KEY ("product_id") REFERENCES "products_product" ("id")
);

CREATE INDEX "products_productspecs_product_id" ON "products_productspecs" ("product_id");
```

---

## Design Decisions

### 1. Two-Level Category Structure
I noticed the website has a broader category to organize subcategories of products. Instead of a complex hierarchical category model, I used two simple fields for flexibility:
- `main_category`: Top-level (e.g., "Valves", "Pipe Fittings", "Accessories")
- `subcategory`: Product type (e.g., "Gate Valves", "PVC Fittings")

### 2. Key-Value Specifications
Rather than creating specific columns for each product attribute (size, PSI, material), I used a separate `ProductSpecs` table with `spec_name` and `spec_value` fields.

**Example:**
```
Product: 2" PVC Gate Valve
  - Material: PVC
  - O-rings: EPDM
  - End Type: Socket
  - Max Pressure: 200 PSI @ 73°F
  - Standards: NSF certified for potable water use
```

### 3. Multiple Images Per Product
Products typically have multiple shots like the front, side, and showing off specific features. The `ProductImage` model supports multiple images with:
- `is_primary`: Explicitly marks the main product image, for thumbnail and consistency
- `display_order`: Controls gallery sequence
- `alt_text`: Accessibility, SEO, and fallback
#### Note:
I used URLField for images just for this example, in a real backend system we would probably change this to ImageField.

### 4. Stock Quantity
Used `stock_quantity` (integer) paired with an `updated_at` field to monitor inventory updates.

---

## Testing
#### 1. Install requirements
```bash
cd q01_DB_Design
pip install -r requirements.txt
```

#### 2. Create a superuser
```bash
cd backend
python manage.py createsuperuser
```

#### 3. Run seed command to populate DB entries
```bash
python manage.py seedProducts
```

#### 4. Navigate to admin panel
```bash
python manage.py runserver
Visit: http://127.0.0.1:8000/admin/
```

