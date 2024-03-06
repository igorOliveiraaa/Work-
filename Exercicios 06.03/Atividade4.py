from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

produtos = []
carrinho = []

class ProdutoAPI(MethodView):
    def get(self):
        return jsonify(produtos)

    def post(self):
        novo_produto = request.get_json()
        produtos.append(novo_produto)
        return jsonify(novo_produto), 201

    def put(self, id_produto):
        produto = next((p for p in produtos if p['id'] == id_produto), None)
        if produto:
            produto.update(request.get_json())
            return jsonify(produto)
        else:
            return 'Produto não encontrado', 404

    def delete(self, id_produto):
        produto = next((p for p in produtos if p['id'] == id_produto), None)
        if produto:
            produtos.remove(produto)
            return '', 204
        else:
            return 'Produto não encontrado', 404

class CarrinhoAPI(MethodView):
    def get(self):
        return jsonify(carrinho)

    def post(self):
        item = request.get_json()
        carrinho.append(item)
        return jsonify(item), 201

    def delete(self, id_produto):
        item = next((i for i in carrinho if i['produto']['id'] == id_produto), None)
        if item:
            carrinho.remove(item)
            return '', 204
        else:
            return 'Item não encontrado no carrinho', 404

produto_view = ProdutoAPI.as_view('produto_api')
app.add_url_rule('/produtos', view_func=produto_view, methods=['GET', 'POST'])
app.add_url_rule('/produtos/<int:id_produto>', view_func=produto_view, methods=['PUT', 'DELETE'])

carrinho_view = CarrinhoAPI.as_view('carrinho_api')
app.add_url_rule('/carrinho', view_func=carrinho_view, methods=['GET', 'POST'])
app.add_url_rule('/carrinho/<int:id_produto>', view_func=carrinho_view, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
