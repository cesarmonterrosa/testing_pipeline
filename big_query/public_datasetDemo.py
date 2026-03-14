from google.cloud import bigquery

#pip install google-cloud-bigquery


def query_public_dataset():
    client = bigquery.Client()

    query = """
    SELECT order_items.order_id, order_items.user_id, order_items.product_id, products.name, products.category
    FROM `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
    JOIN `bigquery-public-data.thelook_ecommerce.products` AS products
    ON order_items.product_id = products.id LIMIT 10;
    """

    results = client.query(query).result()


    #always double check the output matches the query columns
    for row in results:
        print(f"Order ID: {row.order_id}, User ID: {row.user_id}, Product ID: {row.product_id}, Name: {row.name}, Category: {row.category}")

if __name__ == "__main__":
    query_public_dataset()