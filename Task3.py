def format_string(s, operations):
    def lower(text):
        return text.lower()
    def upper(text):
        return text.upper()
    def reverse(text):
        return text[::-1]
    for operation in operations:
        if operation.lower()=="reverse":
            s=reverse(s)
        elif operation.lower()=="minimize":
            s=lower(s)
        elif operation.lower()=="uppercase":
            s=upper(s)
    return s

s = "hello world"
operations = ['Uppercase', 'ReVerse']
print(format_string(s, operations))
