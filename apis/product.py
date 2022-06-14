from flask import Blueprint

app_product=Blueprint("app_product",__name__)


@app_product.route("/api/product/list",methods=['GET'])
def product_list():
    data=[
        {"id": 1, "keyCode": "project1", "title": "项目一", "desc": "这是项目1描述", "operator": "admin",
         "update": "2020-04-06"},

        {"id": 2, "keyCode": "project2", "title": "项目而", "desc": "这是项目2描述", "operator": "user", "update": "2020-04-03"}
    ]
    resp_data={
        "code":20000,
        "data":data
    }
    return resp_data