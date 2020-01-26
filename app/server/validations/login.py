from webargs import fields, validate

login_args = {
    "username":fields.Str(required=True),
    "password":fields.Str(required=True,validate=lambda p: len(p)>=6)
}