import json


"""возвращает список всех кандидатов"""
def load_candidates_from_json():
    with open("candidates.json", 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates