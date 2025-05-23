import sqlite3

def consultar_jogos():
    conn = sqlite3.connect("resultados/jogos.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, data_hora, dezenas
        FROM jogos
        ORDER BY id DESC
        LIMIT 10
    """)

    jogos = cursor.fetchall()

    if jogos:
        print("\n🗂 Últimos jogos gerados:\n")
        for jogo in jogos:
            print(f"ID: {jogo[0]} | Data: {jogo[1]} | Dezenas: {jogo[2]}")
    else:
        print("Nenhum jogo encontrado no banco de dados.")

    conn.close()

if __name__ == "__main__":
    consultar_jogos()
