from unittest.mock import Mock


json = Mock()
json.dumps({'a': 1})

print(json.dumps.assert_called())
print(json.dumps.assert_called_once())
print(json.dumps.assert_called_with({'a': 1}))
print(json.dumps.call_args)
print(json.dumps.call_count)
print(json.method_calls)
