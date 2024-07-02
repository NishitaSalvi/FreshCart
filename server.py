from flask import Flask, request, jsonify
import products_dao
import uoms_dao
import orders_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route("/getProducts" , methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/deleteProduct" , methods=['POST'])
def delete_product(product_id):
    request_data = request.get_json()

    if 'product_id' not in request_data:
        return jsonify({'error': 'Product ID not provided'}), 400

    product_id = request_data['product_id']
    return_id = products_dao.delete_products(connection , product_id)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/getUom" , methods=['GET'])
def get_uoms():
    uoms = uoms_dao.get_uoms(connection)
    response = jsonify(uoms)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/insertProduct" , methods=['POST'])
def insert_product():
    request_data = request.get_json()

    product_data = request_data['data']
    return_id = products_dao.insert_new_product(connection , product_data)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/editProduct/<int:product_id>", methods=['PUT'])
def edit_product(product_id):
    request_data = request.get_json()

    products_dao.edit_product(connection, product_id, request_data)

    response = jsonify({'message': 'Product updated successfully'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/insertOrder" , methods=['POST'])
def insert_order():
    request_data = request.get_json()

    order_data = request_data['data']
    return_id = orders_dao.insert_order(connection , order_data)
    response = jsonify({
        'order_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/getOrders" , methods=['GET'])
def get_orders():
    orders = orders_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/insertUom" , methods=['POST'])
def insert_uom():
    request_data = request.get_json()

    uom_data = request_data['data']
    return_id = uoms_dao.insert_uom(connection , uom_data)
    response = jsonify({
        'uom_id': return_id
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    print("Starting Python FLask Server for Grocery Store MAnagement System")
    app.run(port=5000)


