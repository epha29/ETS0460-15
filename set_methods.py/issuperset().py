old_testament_law = {
    "do not murder", "do not commit adultery", "do not steal", "honor your father and your mother", "have no other GODS before me"
}
ten_commandments = {
    "have no other GODS before me", "do not steal", "do not commit adultery"
}

new_set = old_testament_law.issuperset(ten_commandments)
print(new_set)