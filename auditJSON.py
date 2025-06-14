import json
import os
from collections import defaultdict

import json
import os

import json
import os

directory = r"C:\Users\Bonolo Masima\JSON-files"
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        conversations = data if isinstance(data, list) else data.get('conversations', [data])
        for item in conversations:
            # Standardize fields
            item['cultural_notes'] = item.get('cultural_notes', item.get('cultural_elements', []))
            item['humour_potential'] = item.get('humour_potential', item.get('humor_potential', 'low'))
            item['social_context'] = item.get('social_context', 'unknown')
            item['customer_profile'] = item.get('customer_profile', 'unknown')
            item['culture'] = item.get('culture', 'unknown')
            item['difficulty'] = item.get('difficulty', 'beginner')
            item['friendship_building_factor'] = item.get('friendship_building_factor', 'none')
            item['friendship_progression'] = item.get('friendship_progression', 'none')
            item['resident_profile'] = item.get('resident_profile', 'none')
            item['housing_type'] = item.get('housing_type', 'none')
            item['primary_speaker_profile'] = item.get('primary_speaker_profile', 'none')
            item['party_type'] = item.get('party_type', 'none')
            item['communication_challenge'] = item.get('communication_challenge', 'none')
            item['cultural_focus'] = item.get('cultural_focus', 'none')
            item['prompt_used'] = item.get('prompt_used', 'none')
            item['potential_mistakes'] = item.get('potential_mistakes', 'none')
            item['dating_stage'] = item.get('dating_stage', 'none')
            item['interaction_type'] = item.get('interaction_type', 'none')
            item['communication_mode'] = item.get('communication_mode', 'none')
            item['challenge_focus'] = item.get('challenge_focus', 'none')
            item['candidate_profile'] = item.get('candidate_profile', 'none')
            item['interview_type_category'] = item.get('interview_type_category', 'none')
            item['social_dynamic'] = item.get('social_dynamic', 'none')
            item['traveler_profile'] = item.get('traveler_profile', 'none')
            item['transportation_type'] = item.get('transportation_type', 'none')
            item['student_profile'] = item.get('student_profile', 'none')
            item['transportation_type'] = item.get('transportation_type', 'unknown')
            item['student_profile'] = item.get('student_profile', 'unknown')
            item['success_rating'] = item.get('success_rating', None)
            item['naturalness_rating'] = item.get('naturalness_rating', None)
            item['temperature'] = item.get('temperature', 'unknown')
            # Remove old fields
            for old_field in ['cultural_elements', 'humor_potential']:
                if old_field in item:
                    del item[old_field]
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

directory = r"C:\Users\Bonolo Masima\JSON-files"
field_counts = defaultdict(int)
total_files = 0
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        total_files += 1
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Handle top-level list or dictionary
            conversations = data if isinstance(data, list) else data.get('conversations', [data])
            for item in conversations:
                for key in item.keys():
                    field_counts[key] += 1
for field, count in field_counts.items():
    print(f"Field: {field}, Appears in: {count} objects across {total_files} files")

