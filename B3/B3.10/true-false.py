test_cases = (
    42,
    '',
    [1, 2],
    [],
    {},
    None,
    0
)

result = []
for entry in test_cases:
    print(entry)
    print(bool(entry))
    if entry:
            result.append(1)
    if entry is None:
            result.append(0)