from _mail_alert import Email_Alert


def divide(x, y):
    try:
        result = x / y

    except ZeroDivisionError as e:
        Email_Alert(f'error = {e}').Set_connection()

    return result

if __name__ == '__main__':

    divide(1 , 0)

    