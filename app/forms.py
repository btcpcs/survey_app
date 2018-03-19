from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from app.models import Question
from app import db

def getQuestions():
    '''Builds list of strs representing in DB defined questions as WTForm-elements.'''
    questions = Question.query.all()
    qslist = []
    for i, q in enumerate(questions):
        choices = generateChoices(q)
        if q.frontend == "StringField":
            qslist.append(f'q{i} = {q.frontend}("{q.question}", description="{q.category}")')
        elif q.frontend == "RadioField":
            qslist.append(f'q{i} = {q.frontend}("{q.question}", choices={repr(choices)}, description="{q.category}")')
        elif q.frontend == "SelectField":
            qslist.append(f'q{i} = {q.frontend}("{q.question}", choices={repr(choices)}, description="{q.category}")')
        elif q.frontend == "SelectMultipleField" or "MultiCheckboxField":
            qslist.append(f'q{i} = {q.frontend}("{q.question}", choices={repr(choices)}, option_widget=widgets.CheckboxInput(), description="{q.category}")')
    # print(qslist)
    return qslist

def generateChoices(q):
    '''Generates list of tuples from answer choices to a given question.'''
    items = q.__dict__.items()
    l = [(k, v) for k, v in items if k.startswith("ans") and v != '' and v!= None]
    l.sort()
    return l

def getqs03():
    return '''q03 = StringField('Wie schwer sind Sie? (in kg)')'''

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class LoginForm(FlaskForm):
    accessToken = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class QuestionForm(FlaskForm):
    category = SelectField('Kategorie', choices=[
                                                ('Allgemeines', 'Allgemeines'),
                                                ('Ernährung', 'Ernährung'),
                                                ('Freizeitverhalten', 'Freizeitverhalten'),
                                                ('Gesundheit', 'Gesundheit')])
    question = StringField('Frage', validators=[DataRequired()])
    frontend = SelectField('Interfaceelement', choices=[
                                                ('StringField', 'Freitextfeld'),
                                                ('RadioField', 'Radiobuttons'),
                                                ('SelectField', 'Dropdown'),
                                                ('MultiCheckboxField', 'Checkboxen'),
                                                ('SelectMultipleField', 'Dropdown mit Mehrfachauswahl')])
    ans01 = StringField('Antwortmöglichkeit 1')
    ans02 = StringField('Antwortmöglichkeit 2')
    ans03 = StringField('Antwortmöglichkeit 3')
    ans04 = StringField('Antwortmöglichkeit 4')
    ans05 = StringField('Antwortmöglichkeit 5')
    ans06 = StringField('Antwortmöglichkeit 6')
    ans07 = StringField('Antwortmöglichkeit 7')
    ans08 = StringField('Antwortmöglichkeit 8')
    ans09 = StringField('Antwortmöglichkeit 9')
    ans10 = StringField('Antwortmöglichkeit 10')
    ans11 = StringField('Antwortmöglichkeit 11')
    ans12 = StringField('Antwortmöglichkeit 12')
    ans13 = StringField('Antwortmöglichkeit 13')
    ans14 = StringField('Antwortmöglichkeit 14')
    ans15 = StringField('Antwortmöglichkeit 15')
    ans16 = StringField('Antwortmöglichkeit 16')
    ans17 = StringField('Antwortmöglichkeit 17')
    ans18 = StringField('Antwortmöglichkeit 18')
    ans19 = StringField('Antwortmöglichkeit 19')
    ans20 = StringField('Antwortmöglichkeit 20')
    sort = IntegerField('Sortierung')
    submit = SubmitField('Weiter')

# TODO: Add validators to StringFields
class SurveyForm(FlaskForm):
    qslist = getQuestions()
    for qs in qslist:
        exec(qs)
    submit = SubmitField('Abschicken')
