from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bauru_participa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Enquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    opcoes = db.relationship('OpcaoEnquete', backref='enquete', lazy=True)

class OpcaoEnquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enquete_id = db.Column(db.Integer, db.ForeignKey('enquete.id'), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    votos = db.Column(db.Integer, default=0)

db.create_all()

@app.route('/api/enquetes', methods=['POST'])
def criar_enquete():
    data = request.get_json()
    if 'titulo' not in data or 'descricao' not in data:
        return jsonify({'error': 'É necessário fornecer título e descrição para criar uma enquete'}), 400
    nova_enquete = Enquete(titulo=data['titulo'], descricao=data['descricao'])
    db.session.add(nova_enquete)
    db.session.commit()
    return jsonify({'message': 'Enquete criada com sucesso'}), 201

@app.route('/api/enquetes', methods=['GET'])
def listar_enquetes():
    enquetes = Enquete.query.all()
    return jsonify([{'id': enquete.id, 'titulo': enquete.titulo} for enquete in enquetes])

@app.route('/api/enquetes/<int:id>', methods=['GET'])
def detalhes_enquete(id):
    enquete = Enquete.query.get_or_404(id)
    opcoes = [{'id': opcao.id, 'descricao': opcao.descricao, 'votos': opcao.votos} for opcao in enquete.opcoes]
    return jsonify({'id': enquete.id, 'titulo': enquete.titulo, 'descricao': enquete.descricao, 'opcoes': opcoes})

@app.route('/api/enquetes/<int:id>/votar', methods=['POST'])
def votar_enquete(id):
    data = request.get_json()
    if 'opcao_id' not in data:
        return jsonify({'error': 'É necessário fornecer o ID da opção para votar'}), 400
    opcao = OpcaoEnquete.query.get(data['opcao_id'])
    if not opcao:
        return jsonify({'error': 'Opção de enquete não encontrada'}), 404
    opcao.votos += 1
    db.session.commit()
    return jsonify({'message': 'Voto registrado com sucesso'})

@app.route('/api/enquetes/<int:id>/resultados', methods=['GET'])
def resultados_enquete(id):
    enquete = Enquete.query.get_or_404(id)
    resultados = [{'descricao': opcao.descricao, 'votos': opcao.votos} for opcao in enquete.opcoes]
    return jsonify({'resultados': resultados})

@app.route('/api/enquetes/<int:id>/opcoes', methods=['GET', 'POST'])
def gerenciar_opcoes_enquete(id):
    if request.method == 'GET':
        enquete = Enquete.query.get_or_404(id)
        opcoes = [{'id': opcao.id, 'descricao': opcao.descricao, 'votos': opcao.votos} for opcao in enquete.opcoes]
        return jsonify(opcoes)
    elif request.method == 'POST':
        data = request.get_json()
        if 'descricao' not in data:
            return jsonify({'error': 'É necessário fornecer a descrição da opção'}), 400
        nova_opcao = OpcaoEnquete(enquete_id=id, descricao=data['descricao'])
        db.session.add(nova_opcao)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Já existe uma opção com essa descrição nesta enquete'}), 400
        return jsonify({'message': 'Opção adicionada com sucesso'}), 201

@app.route('/api/enquetes/<int:id_enquete>/opcoes/<int:id_opcao>', methods=['DELETE'])
def deletar_opcao_enquete(id_enquete, id_opcao):
    opcao = OpcaoEnquete.query.get_or_404(id_opcao)
    if opcao.enquete_id != id_enquete:
        return jsonify({'error': 'A opção não pertence à enquete especificada'}), 400
    db.session.delete(opcao)
    db.session.commit()
    return jsonify({'message': 'Opção deletada com sucesso'})

@app.route('/api/enquetes/<int:id>', methods=['DELETE'])
def deletar_enquete(id):
    enquete = Enquete.query.get_or_404(id)
    db.session.delete(enquete)
    db.session.commit()
    return jsonify({'message': 'Enquete deletada com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)

