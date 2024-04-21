philosophy = """
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
"""


philosophy_uppercase = philosophy.upper()

philosophy_modified = philosophy_uppercase.replace("I", "&")

count_better = philosophy_uppercase.count("BETTER")
count_never = philosophy_uppercase.count("NEVER")
count_is = philosophy_uppercase.count("IS")

print("Modified Philosophy:")
print(philosophy_modified)

print("\nOccurrences:")
print("Better:", count_better)
print("Never:", count_never)
print("Is:", count_is)