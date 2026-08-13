import pandas as pd
from pathlib import Path
from django.conf import settings

RULES_PATH = Path(settings.BASE_DIR) / 'data' / 'Tabel_Sebelum_Reduksi_8640.xlsx'


def load_rules():
    df = pd.read_excel(RULES_PATH, sheet_name='Kombinasi_8640')
    df = df.where(pd.notnull(df), None)

    for col in ['DAYS_PER_WEEK', 'TIME_PER_SESSION']:
        df[col] = df[col].apply(lambda x: str(x).strip() if x is not None else None)

    return df


RULES_DF = load_rules()
print("RULES_PATH:", RULES_PATH)
print("JUMLAH RULE:", len(RULES_DF))
print(RULES_DF.head(3).to_dict(orient="records"))


def normalize_bmi_sub(bmi_cat, bmi_sub):
    if bmi_cat == 'NORMAL':
        return None

    if bmi_sub in ['KURUS_RINGAN', 'OVERWEIGHT_RINGAN']:
        return 'RINGAN'

    if bmi_sub == 'KURUS_BERAT':
        return 'SANGAT'

    if bmi_sub == 'OVERWEIGHT_BERAT':
        return 'OBES'

    return None


def normalize_form_data(data):
    focus_map = {
        'FULL_BODY': 'FULL',
        'ARMS': 'LENGAN',
        'CHEST': 'DADA',
        'LOWER_BODY': 'KAKI',
    }

    days_map = {
        '1': None,
        '2': '2',
        '3': '3',
        '4': '4-5',
        '5': '4-5',
    }

    time_map = {
        '<30': '<=30',
        '30-45': '31-45',
        '45-60': '46-60',
        '>60': None,
    }

    place = data.get('place')
    injury = data.get('injury')

    return {
        'BMI_CAT': data.get('bmi_cat'),
        'BMI_SUB': normalize_bmi_sub(data.get('bmi_cat'), data.get('bmi_sub')),
        'GOAL': data.get('goal'),
        'FOCUS': focus_map.get(data.get('focus'), data.get('focus')),
        'PLACE': place,
        'EQUIP_HOME': data.get('equip_home') if place == 'HOME' else None,
        'LEVEL': data.get('level'),
        'DAYS_PER_WEEK': days_map.get(str(data.get('days_per_week'))),
        'TIME_PER_SESSION': time_map.get(data.get('time_per_session')),
        'INJURY': injury,
        'INJURY_AREA': data.get('injury_area') if injury == 'YA' else None,
    }


def row_matches_user(row, user_data):
    for col, user_val in user_data.items():
        rule_val = row[col]

        # 🔥 FIX UTAMA: tangani NaN dari pandas
        if pd.isna(rule_val):
            continue

        if str(rule_val).strip() != str(user_val).strip():
            return False

    return True


def count_specific_fields(row):
    fields = [
        'BMI_CAT', 'BMI_SUB', 'GOAL', 'FOCUS', 'PLACE', 'EQUIP_HOME',
        'LEVEL', 'DAYS_PER_WEEK', 'TIME_PER_SESSION', 'INJURY', 'INJURY_AREA'
    ]
    return sum(1 for col in fields if not pd.isna(row[col]))


def find_matching_rule(data):
    # WAJIB: define dulu
    normalized = normalize_form_data(data)

    print("NORMALIZED DI MATCHER:", normalized)

    matches = []

    for _, row in RULES_DF.iterrows():
        if row_matches_user(row, normalized):
            row_dict = row.to_dict()
            row_dict['specificity'] = count_specific_fields(row_dict)
            matches.append(row_dict)

    print("JUMLAH MATCH:", len(matches))

    if not matches:
        return None, normalized

    matches = sorted(matches, key=lambda x: x['specificity'], reverse=True)
    best_match = matches[0]

    print("BEST MATCH:", best_match.get("ROW_ID"))

    return best_match, normalized