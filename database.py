import sqlite3
from datetime import datetime

DATABASE = "database/simulator.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scenario_id INTEGER NOT NULL,
            user_answer TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            is_correct INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_attempt(
    scenario_id,
    user_answer,
    correct_answer,
    is_correct
):
    connection = get_connection()

    connection.execute("""
        INSERT INTO attempts (
            scenario_id,
            user_answer,
            correct_answer,
            is_correct,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        scenario_id,
        user_answer,
        correct_answer,
        int(is_correct),
        datetime.now().isoformat()
    ))

    connection.commit()
    connection.close()

def get_statistics():
    connection = get_connection()

    total = connection.execute(
        "SELECT COUNT(*) FROM attempts"
    ).fetchone()[0]

    correct = connection.execute(
        "SELECT COUNT(*) FROM attempts WHERE is_correct = 1"
    ).fetchone()[0]

    phishing_answers = connection.execute(
        "SELECT COUNT(*) FROM attempts WHERE user_answer = 'phishing'"
    ).fetchone()[0]

    legitimate_answers = connection.execute(
        "SELECT COUNT(*) FROM attempts WHERE user_answer = 'legitimate'"
    ).fetchone()[0]

    connection.close()

    accuracy = 0

    if total > 0:
        accuracy = round((correct / total) * 100, 1)

    return {
        "total": total,
        "correct": correct,
        "phishing_answers": phishing_answers,
        "legitimate_answers": legitimate_answers,
        "accuracy": accuracy
    }

def get_attempts():
    connection = get_connection()

    attempts = connection.execute("""
        SELECT
            id,
            scenario_id,
            user_answer,
            correct_answer,
            is_correct,
            timestamp
        FROM attempts
        ORDER BY id DESC
    """).fetchall()

    connection.close()

    return attempts
