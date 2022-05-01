import json


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)

data = load_candidates_from_json("candidates.json")

def get_candidates_by_id(candidate_id):
    for candidate in data:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"]
            }
    return {"not_found": "Такого человека нет"}

def get_candidates_by_name(candidate_name):
    return [candidate for candidate in data if candidate_name.lower() in candidate["name"].lower()]


def get_candidates_by_skill(skill_name):
    candidates = []

    for candidate in data:
        skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates
