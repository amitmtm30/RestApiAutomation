import json

odics = '{"K1":"Val1", "K2":"Val2"}'
json_result = json.loads(odics)
print(json_result)
print(json_result['K1'])