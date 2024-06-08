import base64  # not recommended for secure data transmission, used here for demonstration
input_from_POST_username = 'cmFtcnVtcmFtMURuSzh4czhqMnkyYXlfTDRjSGk5cE8='
secret = "DnK8xs8j2y2ay_L4cHi9pO"

decoded = base64.b64decode(input_from_POST_username).decode('utf-8')
if secret in decoded :
    uname = decoded.replace(secret,"")
    print(uname)
