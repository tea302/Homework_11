import json


"""возвращает список всех кандидатов"""
def load_candidates_from_json():
    with open("candidates.json", 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


"""возвращает одного кандидата по его id"""
def get_candidate_id(uid):
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate



"""возвращает кандидатов по имени"""
def get_candidates_by_name(uname):
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if uname in candidate['name'].lower():
            result.append(candidate)
    return result



"""возвращает кандидатов по навыку"""
def get_candidates_by_skill(skill):
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
