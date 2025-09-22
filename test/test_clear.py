from database.database import UserRepository, DB_PATH

# Test clear functionality
repo = UserRepository(DB_PATH)

# First, insert a test user
user_id = repo.create({"name": "Test Clear", "email": "clear@test.com"})
print('Inserted test user with id:', user_id)

# Clear the database
repo.clear_all()
print('Database cleared')

# Try to find the user (should return None since DB is cleared)
row = repo.find(user_id)
print('Trying to find cleared user:', row)  # Should print None