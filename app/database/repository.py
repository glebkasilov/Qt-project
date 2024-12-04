import sqlite3


class BaseRepository:
    pass


class UserRepository(BaseRepository):
    @classmethod
    def get_user(self, user_id) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        user = cur.execute(
            "SELECT * FROM Users WHERE id_user = ?", (user_id,)
        ).fetchone()
        return user

    @classmethod
    def get_users(self) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        users = cur.execute("SELECT * FROM Users").fetchall()
        return users

    @classmethod
    def get_user_by_email(self, email) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        user = cur.execute(
            "SELECT * FROM Users WHERE email = ?", (email,)
        ).fetchone()
        return user

    @classmethod
    def add_user(self, user_data: dict) -> None:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Users (email, password) VALUES (?, ?)",
            (
                user_data['email'],
                user_data['password']
            )
        )
        con.commit()

    @classmethod
    def delete_user(self, user_id: int) -> None:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        cur.execute("DELETE FROM Users WHERE id_user = ?", (user_id,))
        con.commit()

    @classmethod
    def update_user(self, user_id: int, user_data: dict) -> None:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        cur.execute(
            "UPDATE Users SET email = ?, password = ? WHERE id_user = ?",
            (
                user_data['email'],
                user_data['password'],
                user_id
            )
        )
        con.commit()

    @classmethod
    def delete_all_users(self) -> None:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        cur.execute("DELETE FROM Users")
        con.commit()

    @classmethod
    def get_all_emails(self) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        emails = cur.execute("SELECT email FROM Users").fetchall()
        return emails

    @classmethod
    def get_all_passwords(self) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        passwords = cur.execute("SELECT password FROM Users").fetchall()
        return passwords


class PictureRepository(BaseRepository):
    @classmethod
    def get_picture(self, id) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        picture = cur.execute(
            "SELECT * FROM Pictures WHERE id = ?", (id,)
        ).fetchone()
        return picture

    @classmethod
    def get_pictures(self) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        pictures = cur.execute("SELECT * FROM Pictures").fetchall()
        return pictures

    @classmethod
    def add_picture(self, picture_data: dict) -> None:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Pictures (id_picture, login, directory) VALUES (?, ?, ?)",
            (
                picture_data['id_picture'],
                picture_data['login'],
                picture_data['directory']
            )
        )
        con.commit()

    @classmethod
    def delete_picture(self, picture_id: int) -> None:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        cur.execute("DELETE FROM Pictures WHERE id_picture = ?", (picture_id,))
        con.commit()

    @classmethod
    def delete_all_pictures(self) -> None:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        cur.execute("DELETE FROM Pictures")
        con.commit()

    @classmethod
    def get_all_pictures_ids_by_user(self, user_id) -> list:
        con = sqlite3.connect('app/database/example_database.db')
        cur = con.cursor()
        pictures = cur.execute(
            "SELECT id_picture FROM Pictures WHERE id_user = ?", (user_id,)).fetchall()
        return pictures
