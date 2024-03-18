import json

path = "../data/gemotest/parsed_data/gemotest-23ec49ba-9222-45e9-9b93-50dc00d9a6bb.jsonl"

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    new_lines = ['[\n']
    for line in lines:
        if line == '}\n':
            new_lines.append('},\n')
        else:
            new_lines.append(line)
    new_lines.append(']')

# save new lines
with open(path.replace('jsonl', 'json'), 'w', encoding='utf-8') as f:
    f.writelines(new_lines)