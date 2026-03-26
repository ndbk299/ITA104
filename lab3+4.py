
# -- Bảng Khách hàng
# CREATE TABLE "AI21303".Customer (
#     customer_id SERIAL PRIMARY KEY,
#     customer_name VARCHAR(100) NOT NULL,
#     phone VARCHAR(20),
#     address VARCHAR(255)
# );

# -- Bảng Sản phẩm
# CREATE TABLE "AI21303".Product (
#     product_id SERIAL PRIMARY KEY,
#     product_name VARCHAR(150) NOT NULL,
#     unit_price DECIMAL(10,2) NOT NULL
# );

# -- Bảng Hóa đơn
# CREATE TABLE "AI21303".Invoice (
#     invoice_id SERIAL PRIMARY KEY,
#     invoice_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     customer_id INT NOT NULL,
#     total_amount DECIMAL(12,2) NOT NULL,
#     CONSTRAINT fk_invoice_customer 
#         FOREIGN KEY (customer_id) 
# 		REFERENCES "AI21303".Customer(customer_id)
# );

# -- Bảng Chi tiết hóa đơn
# CREATE TABLE "AI21303".InvoiceDetails (
#     invoice_id INT NOT NULL,
#     product_id INT NOT NULL,
#     quantity INT NOT NULL CHECK (quantity > 0),
#     unit_price_at_purchase DECIMAL(10,2) NOT NULL,
#     CONSTRAINT pk_invoice_product PRIMARY KEY (invoice_id, product_id),
#     CONSTRAINT fk_invoicedetails_invoice
#         FOREIGN KEY (invoice_id)
#         REFERENCES "AI21303".Invoice (invoice_id),
#     CONSTRAINT fk_invoicedetails_product
#         FOREIGN KEY (product_id)
#         REFERENCES "AI21303".Product (product_id),
#     CONSTRAINT uq_invoice_product UNIQUE (invoice_id, product_id)
# );

# CREATE TABLE "AI21303".Supplier(
# 	supplier_id INT PRIMARY KEY,
# 	supplier_name VARCHAR(255)NOT NULL,
# 	contact_phone VARCHAR(15) UNIQUE
# )

# INSERT INTO "AI21303".Customer (customer_id, customer_name, phone, address) VALUES
# (1, 'Nguyen Van A', '0901234567', 'Hà Nội'),
# (2, 'Tran Thi B', '0912345678', 'Hồ Chí Minh'),
# (3, 'Le Van C', '0923456789', 'Đà Nẵng'),
# (4, 'Pham Thi D', '0934567890', 'Hải Phòng'),
# (5, 'Hoang Van E', '0945678901', 'Cần Thơ'),
# (6, 'Do Thi F', '0956789012', 'Huế'),
# (7, 'Bui Van G', '0967890123', 'Nha Trang'),
# (8, 'Dang Thi H', '0978901234', 'Quảng Ninh'),
# (9, 'Vu Van I', '0989012345', 'Nam Định'),
# (10, 'Nguyen Thi J', '0990123456', 'Bắc Ninh');

# INSERT INTO "AI21303".Product (product_id, product_name, unit_price) VALUES
# (1, 'Laptop Dell Inspiron', 15000000),
# (2, 'Laptop HP Pavilion', 16000000),
# (3, 'Laptop Asus VivoBook', 14000000),
# (4, 'Laptop MacBook Air', 25000000),
# (5, 'Laptop Lenovo ThinkPad', 18000000),
# (6, 'Điện thoại iPhone 14', 22000000),
# (7, 'Điện thoại Samsung Galaxy S23', 20000000),
# (8, 'Điện thoại Oppo Reno8', 12000000),
# (9, 'Điện thoại Xiaomi Redmi Note 12', 8000000),
# (10, 'Điện thoại Vivo V27', 10000000),
# (11, 'Tai nghe AirPods Pro', 5500000),
# (12, 'Tai nghe Sony WH-1000XM4', 7000000),
# (13, 'Tai nghe JBL Tune 500', 1200000),
# (14, 'Chuột Logitech MX Master', 2500000),
# (15, 'Chuột Razer DeathAdder', 1800000),
# (16, 'Bàn phím cơ Keychron K2', 2200000),
# (17, 'Bàn phím Logitech K380', 900000),
# (18, 'Màn hình LG UltraWide 34"', 9500000),
# (19, 'Màn hình Samsung Odyssey G5', 8500000),
# (20, 'Ổ cứng SSD Samsung 1TB', 3000000);

# INSERT INTO "AI21303".Supplier (supplier_id, supplier_name, contact_phone, email) VALUES
# (1, 'Công ty TNHH Logitech Việt Nam', '0903333333', 'contact@logitech.vn'),
# (2, 'Công ty TNHH Razer Việt Nam', '0904444444', 'contact@razer.vn');


# SELECT*FROM "AI21303".Customer
# SELECT*FROM "AI21303".Product
# SELECT*FROM "AI21303".Invoice
# SELECT*FROM "AI21303".InvoiceDetails
# SELECT*FROM "AI21303".Supplier

# SELECT 
# 	product_name AS "TenSanPham",
# 	unit_price AS "DonGia"
# FROM "AI21303".Product

# SELECT customer_id,customer_name,phone,address
# FROM "AI21303".Customer
# WHERE customer_name LIKE '%Van%'

# SELECT product_id,product_name,unit_price
# FROM "AI21303".Product
# ORDER BY unit_price ASC

# SELECT product_id,product_name,unit_price
# FROM "AI21303".Product
# ORDER BY unit_price ASC
# LIMIT 3

# ALTER TABLE "AI21303".Supplier
# ADD COLUMN  email VARCHAR(100)

# ALTER TABLE "AI21303".Product
# ADD COLUMN supplier_id INT,
# ADD	CONSTRAINT fk_product_supplier
#         FOREIGN KEY (supplier_id)
#         REFERENCES "AI21303".Supplier (supplier_id)

# UPDATE "AI21303".Supplier
# 	SET contact_phone = '0968869979'
# 		WHERE supplier_id = 1

# DELETE FROM "AI21303".Product
# 	WHERE product_id = '8'

# CREATE TABLE "AI21303".TestTable(
# 	"ID" INT
# )

# SELECT * FROM "AI21303".TestTable

# ALTER TABLE "AI21303".Supplier
# DROP COLUMN contact_phone

# DROP TABLE "AI21303".TestTable
