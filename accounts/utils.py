

def detectUser(user):
    if user.role == 1:
        redirectUrl = 'vendor_dashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'cust_dashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl