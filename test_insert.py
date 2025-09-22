from database.database import UserRepository, DB_PATH

repo = UserRepository(DB_PATH)
# insert a test user
user_id = repo.create({"name": "Test User", "email": "test@example.com"})
print('Inserted id:', user_id)
row = repo.find(user_id)
print('Row from DB:', row)
