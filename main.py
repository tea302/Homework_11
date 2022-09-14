from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def page_main():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    candidates = get_candidate_id(uid)
    if not candidates:
        return "Не найдено"
    return render_template("single.html", candidates=candidates)

@app.route('/search/<candidate_name>')
def page_name(candidate_name):
        candidates = get_candidates_by_name(candidate_name)
        return render_template('search.html', candidates=candidates)

@app.route('/skills/<skills_name>')
def page_skill(skills_name):
        candidates = get_candidates_by_skill(skills_name)
        return render_template('skill.html', skills=skills_name, candidates=candidates)


app.run()