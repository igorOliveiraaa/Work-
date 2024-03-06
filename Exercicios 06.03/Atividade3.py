from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

tarefas = []

class TarefaAPI(MethodView):
    def get(self):
        return jsonify(tarefas)

    def post(self):
        nova_tarefa = request.get_json()
        nova_tarefa['concluida'] = False
        tarefas.append(nova_tarefa)
        return jsonify(nova_tarefa), 201

    def delete(self, id_tarefa):
        tarefa = next((t for t in tarefas if t['id'] == id_tarefa), None)
        if tarefa:
            tarefas.remove(tarefa)
            return '', 204
        else:
            return 'Tarefa não encontrada', 404

    def put(self, id_tarefa):
        tarefa = next((t for t in tarefas if t['id'] == id_tarefa), None)
        if tarefa:
            tarefa['concluida'] = not tarefa['concluida']
            return jsonify(tarefa)
        else:
            return 'Tarefa não encontrada', 404

tarefa_view = TarefaAPI.as_view('tarefa_api')
app.add_url_rule('/tarefas', view_func=tarefa_view, methods=['GET', 'POST'])
app.add_url_rule('/tarefas/<int:id_tarefa>', view_func=tarefa_view, methods=['PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)

