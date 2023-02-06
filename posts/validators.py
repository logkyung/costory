from django.core.exceptions import ValidationError

def validator_symbols(value):
    if ("#" in value) or ("@" in value) or ("&" in value):
        raise ValidationError('"#"와 "@" "&"는 포함될 수 없습니다.', code='symbol-err')