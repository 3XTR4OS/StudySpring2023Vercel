import scripts.TestQuestions
import random
import scripts.colleges_Info

QUESTION_LIST = scripts.TestQuestions.QUESTIONS


def check_answers(participant_answers,
                  extravert_introvert_yes=scripts.TestQuestions.EXTROVERSION_INTROVERSION_YES,
                  extravert_introvert_no=scripts.TestQuestions.EXTROVERSION_INTROVERSION_NO,
                  neuroticism=scripts.TestQuestions.NEUROTICISM_YES,
                  lie_scale_yes=scripts.TestQuestions.LIE_SCALE_YES,
                  lie_scale_no=scripts.TestQuestions.LIE_SCALE_NO):
    extraversion_score = 0
    neuroticism_score = 0
    lie_score = 0

    for question_number, answer in enumerate(participant_answers, start=1):
        if question_number in extravert_introvert_yes and answer == True:
            extraversion_score += 1

        elif question_number in extravert_introvert_no and answer == False:
            extraversion_score += 1

        elif question_number in neuroticism and answer == True:
            neuroticism_score += 1

        elif question_number in lie_scale_yes and answer == True:
            lie_score += 1

        elif question_number in lie_scale_no and answer == False:
            lie_score += 1

    return extraversion_score, neuroticism_score, lie_score


def temperament_calculate(extraversion_score, neuroticism_score, lie_score):
    participant_is_lying = False

    if lie_score > 4:
        participant_is_lying = True

    if 0 <= extraversion_score <= 12 and 12 <= neuroticism_score <= 24:
        return 'меланхолик', participant_is_lying

    elif 0 <= extraversion_score <= 12 and 0 <= neuroticism_score <= 12:
        return 'флегматик', participant_is_lying

    elif 12 <= extraversion_score <= 24 and 0 <= neuroticism_score <= 12:
        return 'сангвиник', participant_is_lying

    elif 12 <= extraversion_score <= 24 and 12 <= neuroticism_score <= 24:
        return 'холерик', participant_is_lying

    # Возвращает текст с теорией о темпераменте участника


def get_temperament_text(temperament, user_lying=False):
    if user_lying:
        return str(scripts.TestQuestions.TEMPERAMENT[temperament]) + scripts.TestQuestions.INSINCERITY_TEXT

    return str(scripts.TestQuestions.TEMPERAMENT[temperament])


def select_colleges_under_temperament(temperament, college_list=scripts.colleges_Info.COLLEGES):
    result = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <style>
       
    .rounded {
    counter-reset: li;
    list-style: unset;
    font: 14px "Trebuchet MS", "Lucida Sans";
    padding: 0;
    text-shadow: 0 1px 0 rgba(255,255,255,.5);
    }

    .rounded a {
    position: relative;
    display: block;
    padding: .4em .4em .4em 3em;
    margin: .2em 0;
    background: #DAD2CA;
    color: #444;
    text-decoration: none;
    border-radius: .3em;
    transition: .3s ease-out;

    }
    .rounded a:hover {background: #E9E4E0;}
    .rounded a:hover:before {transform: rotate(360deg);}
    .rounded a:before {
    content: counter(li);
    counter-increment: li;
    position: absolute;
    left: -0.3em;
    top: 50%;
    margin-top: -1.3em;
    background: #8FD4C1;
    height: 2em;
    width: 2em;
    line-height: 2em;
    border: .3em solid white;
    text-align: center;
    font-weight: bold;
    border-radius: 2em;
    transition: all .3s ease-out;
    }

    </style>
</head>

<body>

    
    """

    for college in college_list:
        matches_found = False
        college_head_exist = False

        for profession in college_list[college].items():
            if temperament in profession[-1]:
                matches_found = True
                # result += """<div>Под ваш темперамент подходит профессия: {}</div>""".format(profession[0])

            # используется для пропуска заголовков без профессий
            if matches_found:
                if not college_head_exist:
                    result += """<ol class="rounded"> {}""".format(college)
                    college_head_exist = True
                else:
                    result += """
                        <li><a href="#">{}</a></li>
                        """.format(profession[0])

    result += """
    </body>

</html>"""
    return result

