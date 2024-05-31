from usernotes import UserNotes

# Create a UserNotes object with valid credentials
valid_user = UserNotes("valid_username", "valid_password")

# Attempt to add, modify, delete, and retrieve notes
print(valid_user.add_note("Test Title", "Test Content"))
print(valid_user.modify_note("Test Title", "New Title", "New Content"))
print(valid_user.delete_note("New Title"))
print(valid_user.get_notes())

# Create a UserNotes object with invalid credentials
invalid_user = UserNotes("invalid_username", "invalid_password")

# Attempt to add, modify, delete, and retrieve notes
print(invalid_user.add_note("Test Title", "Test Content"))
print(invalid_user.modify_note("Test Title", "New Title", "New Content"))
print(invalid_user.delete_note("New Title"))
print(invalid_user.get_notes())