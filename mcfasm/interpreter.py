import compiler

def create_score(name: str):
    return f"scoreboard objectives add {name} dummy"

def score_operation(lhs: str, rhs: str):
    return f"scoreboard players operation @e[tag=mcfasm_root] {lhs} %= @e[tag=mcfasm_root] {rhs}"

def score_to_storage(score_name: str, storage_name: str, storage_type: str):
    return f"execute store result storage mcfasm {storage_name} {storage_type} 1 run scoreboard players get @e[tag=mcfasm_root] {score_name}"

def storage_to_score(storage_name: str, score_name: str):
    return f"execute store result score @a[tag=mcfasm_root] {score_name} run data get storage mcfasm {storage_name}"

def create_storage(name: str, value: any): # recommended
    return f"data modify storage mcfasm f{name} set value {value}"