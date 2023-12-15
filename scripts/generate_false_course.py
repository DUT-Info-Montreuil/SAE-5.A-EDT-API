import random
from datetime import datetime, timedelta
import copy

rooms = dict()

rooms['TD'] = ['A2-05', 'A1-01', 'B0-01', 'B0-02']
rooms['cours'] = ['Amphi','Amphi 2']
rooms['TP'] = ['Amphi 2', 'A1-01', 'B1-13', 'B1-14']

s1 = dict()

s1['Initiation au developpement'] = ['j.rety@iut.univ-paris8.fr','m.simonot@iut.univ-paris8.fr','p.bonnot@iut.univ-paris8.fr']
s1['Developpement d interfaces web'] = ['a.bossard@iut.univ-paris8.fr','m.cataldi@iut.univ-paris8.fr']
s1['Introduction a l Architecture des Ordinateurs'] = ['g.delmas@iut.univ-paris8.fr','a.bossard@iut.univ-paris8.fr']
s1['Introduction aux Systemes d exploitation'] = ['g.delmas@iut.univ-paris8.fr','n.nauwynck@iut.univ-paris8.fr']
s1['Introduction aux bases de donnees SQL'] = ['m.lamolle@iut.univ-paris8.fr', 'm.cataldi@iut.univ-paris8.fr']
s1['Mathematiques Discretes'] = ['m.homps@iut.univ-paris8.fr', 'p.bonnot@iut.univ-paris8.fr']
s1['Outils Mathematiques Fondamentaux'] = ['m.homps@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']
s1['Gestion de projet et des organisations'] = ['v.clement-comparot@iut.univ-paris8.fr']
s1['economie durable et numerique'] = ['v.clement-comparot@iut.univ-paris8.fr']
s1['Anglais Technique'] = ['c.ballay_dally@iut.univ-paris8.fr']
s1['Bases de la Communication'] = ['v.clement-comparot@iut.univ-paris8.fr']
s1['Projet professionnel et personnel'] = ['v.clement-comparot@iut.univ-paris8.fr']

s3 = dict()
s3['Developpement Web'] = ['a.bossard@iut.univ-paris8.fr','m.cataldi@iut.univ-paris8.fr']
s3['Developpement efficace et Qualite'] = ['j.rety@iut.univ-paris8.fr','m.simonot@iut.univ-paris8.fr','p.bonnot@iut.univ-paris8.fr']
s3['Programmation Systeme'] = ['g.delmas@iut.univ-paris8.fr','a.bossard@iut.univ-paris8.fr']
s3['Architecture des Reseaux'] = ['g.delmas@iut.univ-paris8.fr']
s3['SQL et Programmation'] = ['m.lamolle@iut.univ-paris8.fr', 'm.cataldi@iut.univ-paris8.fr']
s3['Analyse'] = ['p.bonnot@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']
s3['Probabilites'] = ['p.bonnot@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']
s3['Cryptographie'] = ['m.homps@iut.univ-paris8.fr', 'p.bonnot@iut.univ-paris8.fr']
s3['Management des Systemes d Information'] = ['v.clement-comparot@iut.univ-paris8.fr']
s3['Droits des contrats et du numerique'] = ['v.clement-comparot@iut.univ-paris8.fr']
s3['Anglais'] = ['c.ballay_dally@iut.univ-paris8.fr']
s3['Anglais Apprentis'] = ['c.ballay_dally@iut.univ-paris8.fr']
s3['Communication Professionnelle'] = ['v.clement-comparot@iut.univ-paris8.fr']
s3['PPP'] = ['v.clement-comparot@iut.univ-paris8.fr']
s3['Outils Mathematiques Fondamentaux'] = ['m.homps@iut.univ-paris8.fr', 'p.bonnot@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']


base_date = datetime(2023, 12, 15)
# Generate a random number between 1 and 3 for the number of hours to add
random_hours = random.randint(1, 3)

# Add the random hours to the current time
new_time = base_date + timedelta(hours=random_hours)
import random
from datetime import datetime, timedelta

def remove_last_comma(input_string):
    if input_string and input_string[-1] == ',':
        return input_string[:-1]
    else:
        return input_string
def remove_last_occurrence(input_str, char_to_remove):
    last_occurrence_index = input_str.rfind(char_to_remove)

    if last_occurrence_index != -1:
        result = input_str[:last_occurrence_index] + input_str[last_occurrence_index + 1:]
    else:
        result = input_str

    return result

def generate_timetable(start_date, end_date, s, grps, number='1',timetable = []):
    text = ""
    textParticipate = ""
    coursNb = 0
    # Check if current time is during lunchtime
    current_time = start_date
    while current_time < end_date and current_time.weekday() not in [5, 6]:
        textParticipate += f"\n-- For the date {(current_time.strftime('%Y-%m-%d'))} (YYYY/MM/DD)"
        textParticipate += f"\nINSERT INTO university.participates (course_id, subgroup_id)\nVALUES"
        
        text += f"\n-- For the date {(current_time.strftime('%Y-%m-%d'))} (YYYY/MM/DD)"
        text += f"\nINSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)\nVALUES"
        
        while current_time <=end_date :
            hour = random.choice([1,2])
            lunch_start = current_time.replace(hour=12, minute=0, second=0, microsecond=0)
            lunch_end = current_time.replace(hour=14, minute=00, second=0, microsecond=0)
            if lunch_start <= current_time <= lunch_end:
                current_time = (current_time + timedelta(hours=1))
                end = (current_time + timedelta(hours=1))
            else :
                end = (current_time + timedelta(hours=hour))
            
            course_type = random.choice(list(rooms))
            room = random.choice(rooms[course_type])
            if course_type == 'cours' :
                while True :
                    teaching_key = random.choice(list(s))
                    teaching_personnal = random.choice(s[teaching_key])
                    already_exists = any(existing_entry[5] == teaching_personnal and (existing_entry[0] <= current_time <= existing_entry[1] or existing_entry[0] <= end <= existing_entry[1])  for existing_entry in timetable)
                    if not already_exists : 
                        break
                # Format the data and append to the timetable
                timetable.append([
                    current_time,
                    end,
                    course_type,
                    room,
                    teaching_key,
                    teaching_personnal
                ])
                
                text += f"\n\t('{current_time.strftime('%Y-%m-%d %H:%M:%S')}', '{end.strftime('%Y-%m-%d %H:%M:%S')}', '{course_type}', \n\t\t(SELECT id FROM university.rooms WHERE code = '{room}'),\n\t\t(SELECT id FROM university.teachings WHERE title = '{teaching_key}' and semestre = {number}),\n\t\t(SELECT id FROM university.personals WHERE mail = '{teaching_personnal}')),"
                coursNb+=1
                textParticipate+="\n\t"
                for grp in grps :
                    textParticipate+= f"({coursNb},{grp[0]}),"
                textParticipate+= f" -- {course_type}"
                for grp in grps :
                    textParticipate+= f" for {grp[1]}"
            else : 
                for grp in grps :
                    excepte = copy.deepcopy(s)
                    while True :
                        if not list(excepte) :
                            excepte = copy.deepcopy(s)
                        coursList = list(excepte)
                        teaching_key = random.choice(coursList)
                        personalList = excepte[teaching_key]
                        teaching_personnal = random.choice(personalList)
                        already_exists = any(existing_entry[5] == teaching_personnal and (existing_entry[0] <= current_time <= existing_entry[1] or existing_entry[0] <= end <= existing_entry[1]) for existing_entry in timetable)
                        if not already_exists : 
                            break
                        else:
                            excepte[teaching_key].remove(teaching_personnal)
                            if not excepte[teaching_key] :
                                del excepte[teaching_key]
                        
                    # Format the data and append to the timetable
                    timetable.append([
                        current_time,
                        end,
                        course_type,
                        room,
                        teaching_key,
                        teaching_personnal
                    ])
                    
                    text += f"\n\t('{current_time.strftime('%Y-%m-%d %H:%M:%S')}', '{end.strftime('%Y-%m-%d %H:%M:%S')}', '{course_type}', \n\t\t(SELECT id FROM university.rooms WHERE code = '{room}'),\n\t\t(SELECT id FROM university.teachings WHERE title = '{teaching_key}' and semestre = {number}),\n\t\t(SELECT id FROM university.personals WHERE mail = '{teaching_personnal}')),"
                    coursNb+=1
                    textParticipate+= f"\n\t({coursNb},{grp[0]}),"
                    textParticipate+= f" -- {course_type} for {grp[1]} "
            
        # Move to the next time slot
            if current_time >= current_time.replace(hour=16, minute=30, second=0, microsecond=0) :
                text = remove_last_occurrence(text,',')+"\n;\n"
                textParticipate = remove_last_occurrence(textParticipate,',')+"\n;\n"
                
                current_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
                
                textParticipate += f"\n -- For the course the {(current_time.strftime('%Y-%m-%d'))} (YYYY/MM/DD)"
                textParticipate += f"\nINSERT INTO university.participates (course_id, subgroup_id)\nVALUES"
                
                text += f"\n -- For the date {(current_time.strftime('%Y-%m-%d'))} (YYYY/MM/DD)"
                text += f"\nINSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)\nVALUES"""
            else :
                current_time = (end + timedelta(minutes=5))
            
            with open('script_university_presentation_sample_course.sql', 'a', encoding='utf-8') as file:
                # Write content to the file
                file.write(text)
            text = ""
            
            with open('script_university_presentation_sample_participate.sql', 'a', encoding='utf-8') as file:
                # Write content to the file
                file.write(textParticipate)
            textParticipate = ""
                
    return timetable 

start_date = datetime(2023, 12, 15, 9, 0, 0)
end_date = datetime(2023, 12, 29, 17, 0, 0)

with open('script_university_presentation_sample_course.sql', 'w') as file:
    file.write("")
with open('script_university_presentation_sample_participate.sql', 'w') as file:
    file.write("")
    
with open('script_university_presentation_sample_course.sql', 'a', encoding='utf-8') as file:
    file.write("\n-- S1")
with open('script_university_presentation_sample_participate.sql', 'a', encoding='utf-8') as file:
    file.write("\n-- S1")
timetable = generate_timetable(start_date, end_date,s1,[('1','A1'),('2','A2'),('3','B1'),('4','B2')],'1')
with open('script_university_presentation_sample_course.sql', 'a', encoding='utf-8') as file:
    file.write("\n-- S3")
with open('script_university_presentation_sample_participate.sql', 'a', encoding='utf-8') as file:
    file.write("\n-- S3")
timetable = generate_timetable(start_date, end_date,s3,[('4','A1'),('5','A2'),('6','app-1'),('7','app-2')],'3', timetable)
print("end")