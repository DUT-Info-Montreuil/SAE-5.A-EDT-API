from datetime import datetime, timedelta
from itertools import groupby
import random
import copy
import os 



timetable = []

def select_possible_place (current_time, end, rooms, course):
    excepte_course = copy.deepcopy(course)
    excepte_room = copy.deepcopy(rooms)

    while True :
        if not list(excepte_course) :
            excepte_course = copy.deepcopy(course)
        if not list(excepte_room) :
            excepte_room = copy.deepcopy(rooms)
            
        room_use = random.choice(list(excepte_room))
        room_key = random.choice(excepte_room[room_use])
        teaching_key = random.choice(list(excepte_course))
        teaching_personnal = random.choice(excepte_course[teaching_key])
        
        personnal_already_in_class, room_already_use = course_is_possible(teaching_personnal, current_time, room_key, end)
        
        if personnal_already_in_class :
            keys_to_remove = [key for key in excepte_course if teaching_personnal in excepte_course[key]]
            for key in keys_to_remove:
                excepte_course[key].remove(teaching_personnal)
            excepte_course = {key: value for key, value in excepte_course.items() if value}
        if room_already_use:
            keys_to_remove = [key for key in excepte_room if room_key in excepte_room[key]]
            for key in keys_to_remove:
                excepte_room[key].remove(room_key)
            excepte_room = {key: value for key, value in excepte_room.items() if value}
 
        if not personnal_already_in_class and not room_already_use : 
            break
                
    return room_use, room_key, teaching_key, teaching_personnal

def rooms_info_dict() : 
    rooms = dict()
    rooms['TD'] = [ 'A1-01', 'A2-01', 'A2-03', 'A2-04', 'A2-05', 'B0-01', 'B0-02', 'B0-03', 'B1-09', 'B1-10', 'B1-13', 'B1-14', 'D0-02', 'Salle Visio']
    rooms['TP'] = [ 'A1-01', 'A2-01', 'A2-03', 'A2-04', 'A2-05', 'B0-01', 'B0-02', 'B0-03', 'B1-09', 'B1-10', 'B1-13', 'B1-14', 'D0-02', 'D1-10', 'D1-11 (Langues)', 'D1-12', 'F1-02', 'F1-03 (Langues)', 'F2-01', 'F2-02', 'F2-03']
    rooms['cours'] = [ 'A1-01', 'A2-05', 'Amphi', 'Amphi 2', 'C0-01', 'D1-10', 'D1-11 (Langues)', 'D1-12', 'F1-02', 'F1-03 (Langues)', 'F2-01', 'F2-02', 'F2-03', 'Salle Visio' ]
    return rooms

def semester_1_info() :
    semester = dict()
    semester['Initiation au developpement'] = ['j.rety@iut.univ-paris8.fr','m.simonot@iut.univ-paris8.fr','p.bonnot@iut.univ-paris8.fr']
    semester['Developpement d interfaces web'] = ['a.bossard@iut.univ-paris8.fr','m.cataldi@iut.univ-paris8.fr']
    semester['Introduction a l Architecture des Ordinateurs'] = ['g.delmas@iut.univ-paris8.fr','a.bossard@iut.univ-paris8.fr']
    semester['Introduction aux Systemes d exploitation'] = ['g.delmas@iut.univ-paris8.fr','n.nauwynck@iut.univ-paris8.fr']
    semester['Introduction aux bases de donnees SQL'] = ['m.lamolle@iut.univ-paris8.fr', 'm.cataldi@iut.univ-paris8.fr']
    semester['Mathematiques Discretes'] = ['m.homps@iut.univ-paris8.fr', 'p.bonnot@iut.univ-paris8.fr']
    semester['Outils Mathematiques Fondamentaux'] = ['m.homps@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']
    semester['Gestion de projet et des organisations'] = ['v.clement-comparot@iut.univ-paris8.fr']
    semester['economie durable et numerique'] = ['v.clement-comparot@iut.univ-paris8.fr']
    semester['Anglais Technique'] = ['c.ballay_dally@iut.univ-paris8.fr']
    semester['Bases de la Communication'] = ['v.clement-comparot@iut.univ-paris8.fr']
    semester['Projet professionnel et personnel'] = ['v.clement-comparot@iut.univ-paris8.fr']
    return semester, '1', 'INFO'

def semester_3_info() :
    semester = dict()
    semester['Developpement Web'] = ['a.bossard@iut.univ-paris8.fr','m.cataldi@iut.univ-paris8.fr']
    semester['Developpement efficace et Qualite'] = ['j.rety@iut.univ-paris8.fr','m.simonot@iut.univ-paris8.fr','p.bonnot@iut.univ-paris8.fr']
    semester['Programmation Systeme'] = ['g.delmas@iut.univ-paris8.fr','a.bossard@iut.univ-paris8.fr']
    semester['Architecture des Reseaux'] = ['g.delmas@iut.univ-paris8.fr']
    semester['SQL et Programmation'] = ['m.lamolle@iut.univ-paris8.fr', 'm.cataldi@iut.univ-paris8.fr']
    semester['Analyse'] = ['p.bonnot@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']
    semester['Probabilites'] = ['p.bonnot@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']
    semester['Cryptographie'] = ['m.homps@iut.univ-paris8.fr', 'p.bonnot@iut.univ-paris8.fr']
    semester['Management des Systemes d Information'] = ['v.clement-comparot@iut.univ-paris8.fr']
    semester['Droits des contrats et du numerique'] = ['v.clement-comparot@iut.univ-paris8.fr']
    semester['Anglais'] = ['c.ballay_dally@iut.univ-paris8.fr']
    semester['Anglais Apprentis'] = ['c.ballay_dally@iut.univ-paris8.fr']
    semester['Communication Professionnelle'] = ['v.clement-comparot@iut.univ-paris8.fr']
    semester['PPP'] = ['v.clement-comparot@iut.univ-paris8.fr']
    semester['Outils Mathematiques Fondamentaux'] = ['m.homps@iut.univ-paris8.fr', 'p.bonnot@iut.univ-paris8.fr', 'a.ricordeau@iut.univ-paris8.fr']
    return semester, '3', 'INFO'

def insert_file_course(string, char) : 
    folder_path = "scripts/"
    file_path = os.path.join(folder_path, 'script_university_presentation_sample_course.sql')
    with open(file_path, char) as file:
        file.write(string)
        
def insert_file_participate(string, char) : 
    folder_path = "scripts/"
    file_path = os.path.join(folder_path, 'script_university_presentation_sample_participate.sql')
    with open(file_path, char) as file:
        file.write(string)

def end_of_insert_course():
    folder_path = "scripts/"
    file_path = os.path.join(folder_path, 'script_university_presentation_sample_course.sql')
    
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = remove_last_occurrence(content,',')+"\n;\n"
    
    with open(file_path, 'w') as file:
        file.write(modified_content)

def end_of_insert_participate():
    folder_path = "scripts/"
    file_path = os.path.join(folder_path, 'script_university_presentation_sample_participate.sql')
    
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = remove_last_occurrence(content,',')+"\n;\n"
    
    with open(file_path, 'w') as file:
        file.write(modified_content)

def remove_last_occurrence(input_str, char_to_remove):
    last_occurrence_index = input_str.rfind(char_to_remove)

    if last_occurrence_index != -1:
        result = input_str[:last_occurrence_index] + input_str[last_occurrence_index + 1:]
    else:
        result = input_str

    return result

def course_is_possible(teaching_personnal, current_time, room, end) :
    personnal_already_in_class = any(existing_entry[5] == teaching_personnal 
            and (existing_entry[0] < current_time < existing_entry[1] 
            or  existing_entry[0] < end           < existing_entry[1])  
            for existing_entry in timetable)
    
    room_already_use = any(existing_entry[3] == room 
            and (existing_entry[0] < current_time < existing_entry[1] 
            or existing_entry[0] < end < existing_entry[1]) 
            for existing_entry in timetable)
    return personnal_already_in_class, room_already_use

def generate_timetable(start_date, end_date, course, grps, rooms, number):
    text = ""
    textParticipate = ""
    # Check if current time is during lunchtime
    current_time = start_date
    while start_date <= current_time and current_time <= end_date and current_time.weekday() not in [5, 6]:
        insert_file_participate(f"\n-- For the date {(current_time.strftime('%Y-%m-%d %H:%M:%S'))} (YYYY/MM/DD %H:%M)", 'a')
        insert_file_participate(f"\nINSERT INTO university.participates (course_id, subgroup_id)\nVALUES", 'a')
        
        insert_file_course(f"\n-- For the date {(current_time.strftime('%Y-%m-%d %H:%M:%S'))} (YYYY/MM/DD %H:%M)", 'a')
        insert_file_course(f"\nINSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)\nVALUES", 'a')
        
        if 12 <= current_time.hour <= 14:
            current_time = current_time + timedelta(hours=1)
            end = current_time + timedelta(hours=1, minutes=random.choice([0, 0, 5, 15, 30]))
        else :
            end = current_time + timedelta(hours=random.choice([1, 2]), minutes=random.choice([0, 0, 5, 15, 30]))
        
        room_use, room_key, teaching_key, teaching_personnal = select_possible_place(current_time, end, rooms, course)
        
        if room_use  == 'cours' :
            timetable.append([
                current_time,
                end,
                room_use,
                room_key,
                teaching_key,
                teaching_personnal
            ])
            print("course and participate added")
            
            insert_file_course(f"\n\t('{current_time.strftime('%Y-%m-%d %H:%M:%S')}', '{end.strftime('%Y-%m-%d %H:%M:%S')}', '{room_use}', \n\t\t(SELECT id FROM university.rooms WHERE code = '{room_key}'),\n\t\t(SELECT id FROM university.teachings WHERE title = '{teaching_key}' and semestre = {number}),\n\t\t(SELECT id FROM university.personals WHERE mail = '{teaching_personnal}')),", 'a')
            insert = ""
            comment = ""
            for grp in grps :
                insert  += f"({len(timetable)},{grp[0]}), "
                comment += f" {grp[1]} /"
            insert_file_participate("\n\t"+insert + f" -- {room_use} for : /"+ comment , 'a')
        else : 
            except_cours = copy.deepcopy(rooms)
            del except_cours['cours']
            for grp in grps :
                room_use, room_key, teaching_key, teaching_personnal = select_possible_place(current_time, end, except_cours, course)
                timetable.append([
                    current_time,
                    end,
                    room_use,
                    room_key,
                    teaching_key,
                    teaching_personnal
                ])
                print(f"course and participate added : {len(timetable)}")
                insert_file_course(f"\n\t('{current_time.strftime('%Y-%m-%d %H:%M:%S')}', '{end.strftime('%Y-%m-%d %H:%M:%S')}', '{room_use}', \n\t\t(SELECT id FROM university.rooms WHERE code = '{room_key}'),\n\t\t(SELECT id FROM university.teachings WHERE title = '{teaching_key}' and semestre = {number}),\n\t\t(SELECT id FROM university.personals WHERE mail = '{teaching_personnal}')),", 'a')
                insert_file_participate(f"\n\t({len(timetable)},{grp[0]}),  -- {room_use} for {grp[1]} ", 'a')
        
        if current_time >= current_time.replace(hour=17, minute=30, second=0, microsecond=0) :
            current_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
        else :
            current_time = current_time + timedelta(hours=1)
        end_of_insert_course()
        end_of_insert_participate()

cours_and_prof, semester_number, departement,  = semester_1_info()
start_date = datetime(2023, 12, 15, 9, 0, 0)
end_date = datetime(2023, 12, 29, 17, 30, 0)
rooms = rooms_info_dict()

insert_file_course(f"", 'w')
insert_file_participate(f"", 'w')

insert_file_course("\n--INFO Course for promotion 1 ", 'a')
insert_file_participate("\n--INFO Participate for promotion 1 ", 'a')
subgroup_info_id_and_title = [('1','A1'),('2','A2'),('3','B1'),('4','B2')]

generate_timetable(start_date, end_date, cours_and_prof, subgroup_info_id_and_title, rooms, semester_number)

cours_and_prof, semester_number, departement,  = semester_3_info()
insert_file_course("\n-- INFO Course for promotion 3 ", 'a')
insert_file_participate("\n--INFO Participate for promotion 3 ", 'a')
subgroup_info_id_and_title = [('4','A1'),('5','A2'),('6','app-1'),('7','app-2')]

generate_timetable(start_date, end_date, cours_and_prof, subgroup_info_id_and_title, rooms, semester_number)

print("end Insert")