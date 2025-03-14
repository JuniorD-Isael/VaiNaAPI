from flask import Flask, jsonify, request

import sqlite3

app = Flask(__name__)


def init_db():
    # sqlite3 crie o aquivo database.db e se conecte a variavel conn (connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS LIVORS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     imagem_url TEXT NOT NULL
                     );
        """)


@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados("imagem_url")

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
    INSERT INTO LIVROS (titulo, categoria, autor, imagem_url)
    VALUES ("{titulo}", "{categoria}", "{autor}", "{imagem_url}")
""")
    conn.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
