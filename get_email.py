import win32security
import win32net

def get_email_address(username):
    try:
        user_info = win32net.NetUserGetInfo(None, username, 4)
        return user_info['usr_comment']
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    # Replace with the username you want to retrieve the email address for
    target_username = "username"

    email_address = get_email_address(target_username)
    if email_address:
        print(f"Email address for {target_username}: {email_address}")
    else:
        print("Email address not found.")
