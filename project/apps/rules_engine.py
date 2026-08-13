def forward_chaining(data):
    bmi_cat = data.get('bmi_cat')
    goal = data.get('goal')
    place = data.get('place')
    level = data.get('level')
    injury = data.get('injury')
    injury_area = data.get('injury_area')
    days_per_week = data.get('days_per_week')
    time_per_session = data.get('time_per_session')

    # Rule 1
    if bmi_cat == 'OVERWEIGHT' and goal == 'FATLOSS' and level == 'PEMULA_TOTAL':
        return {
            'rule_id': 'R1',
            'rule_text': f'IF bmi_cat = {bmi_cat} AND goal = {goal} AND place = {place} THEN Program Fat Loss Gym',
            'program_latihan': 'Program Fat Loss Pemula',
            'intensitas': 'Rendah',
            'frekuensi': f'{days_per_week} kali per minggu',
            'durasi': f'{time_per_session} menit per sesi',
            'catatan': 'Fokus pada adaptasi gerakan dasar dan pembakaran kalori.',
            'larangan': 'Hindari latihan terlalu berat di awal.'
        }

    # Rule 2
    if bmi_cat == 'NORMAL' and goal == 'GAIN' and place == 'GYM':
        return {
            'rule_id': 'R2',
            'program_latihan': 'Program Muscle Gain Gym',
            'intensitas': 'Sedang',
            'frekuensi': f'{days_per_week} kali per minggu',
            'durasi': f'{time_per_session} menit per sesi',
            'catatan': 'Fokus pada progressive overload dan latihan compound.',
            'larangan': 'Pastikan teknik gerakan benar.'
        }

    # Rule 3
    if bmi_cat == 'NORMAL' and goal == 'FATLOSS' and place == 'GYM':
        return {
            'rule_id': 'R3',
            'program_latihan': 'Program Fat Loss Gym',
            'intensitas': 'Sedang',
            'frekuensi': f'{days_per_week} kali per minggu',
            'durasi': f'{time_per_session} menit per sesi',
            'catatan': 'Kombinasikan latihan beban dan kardio ringan.',
            'larangan': 'Jangan langsung latihan dengan volume tinggi.'
        }

    # Rule 4 (Cedera Bahu)
    if injury == 'YA' and injury_area == 'BAHU':
        return {
            'rule_id': 'R4',
            'program_latihan': 'Program Aman untuk Cedera Bahu',
            'intensitas': 'Rendah',
            'frekuensi': f'{days_per_week} kali per minggu',
            'durasi': f'{time_per_session} menit per sesi',
            'catatan': 'Prioritaskan latihan aman untuk bahu.',
            'larangan': 'Hindari shoulder press dan gerakan overhead.'
        }

    # Rule 5 (Cedera Lutut)
    if injury == 'YA' and injury_area == 'LUTUT':
        return {
            'rule_id': 'R5',
            'program_latihan': 'Program Aman untuk Cedera Lutut',
            'intensitas': 'Rendah',
            'frekuensi': f'{days_per_week} kali per minggu',
            'durasi': f'{time_per_session} menit per sesi',
            'catatan': 'Fokus pada low impact.',
            'larangan': 'Hindari squat dalam dan jumping.'
        }

    # Default
    return {
        'rule_id': 'DEFAULT',
        'program_latihan': 'Program Umum Pemula',
        'intensitas': 'Ringan - Sedang',
        'frekuensi': f'{days_per_week} kali per minggu',
        'durasi': f'{time_per_session} menit per sesi',
        'catatan': 'Belum ada rule yang cocok.',
        'larangan': 'Sesuaikan dengan kondisi tubuh.'
    }