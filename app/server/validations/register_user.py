from webargs import fields, validate

register_user_args = {
    "username":fields.Str(required=True),
    "password":fields.Str(required=True,validate=lambda p: len(p)>=6),
    "email":fields.Str(required=True)
}