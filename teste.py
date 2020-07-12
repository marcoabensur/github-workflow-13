import requests

def main():
    url = "http://127.0.0.1:5000/"

    headers = {'Content-type': 'application/json'}

    resume = {
        "full_name": "Renzo Armando dos Santos Abensur",
        "email": "renzo.abensur@usp.br",
        "mobile_phone": "+55 (11) 976032332",
        "age": 20,
        "home_address": "5 Rua Luis Martins, Alto da Lapa",
        "start_date": 1595203200,
        "opportunity_tag": "dev_intern_200",
        "past_jobs_experience": "I have worked as an assitant professor of math, physics and chemistry in Colégio Objetivo Integrado for a year and a half",
        "degrees": [{
            "institution_name": "Escola Politécnica da Universidade de Sao Paulo - São Paulo",
            "degree_name": "Engenharia Eletrica",
            "begin_date": 1519862400,
            "end_date": 1675209600
        }],
        "programming_skills": ["python", "C", "C++", "HTML", "CSS"],
        "database_skills": ["mysql"],
        "hobbies": ["Watch Series", "Play videogame"],
        "why": "As I look foward to work in relevant and innovative engineering projects, I see SciCrop team as a great oportunity to improve my personal skills and gain professional experience in a tecnological environment.",
        "git_url_repositories": "https://github.com/renzoabensur/jobs"
    }

    post = requests.post(url, json = resume, headers = headers)
    print(post.status_code)

if __name__ == "__main__":
    main()
