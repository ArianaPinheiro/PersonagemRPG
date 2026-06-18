full_dot = '●'
empty_dot = '○'

def create_character(name, forca,inteligencia, carisma):
    if not isinstance(name, str):
        return 'The character name should be a string'

    if name =='':
        return 'The character should have a name'

    if len(name) >10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    if not all(isinstance(stat, int) for stat in(forca,inteligencia, carisma)):
        return 'All stats should be integers'
    if forca <1 or inteligencia <1 or carisma <1:
        return 'All stats should be no less than 1'
    if forca > 4 or inteligencia > 4 or carisma > 4:
        return 'All stats should be no more than 4'
    if forca + inteligencia + carisma != 7:
        return'The character should start with 7 points'
    return(
    f'{name}\n'
    f'STR {full_dot * forca}{empty_dot * (10 - forca)}\n'
    f'INT {full_dot * inteligencia}{empty_dot * (10 - inteligencia)}\n'
    f'CHA {full_dot * carisma}{empty_dot * (10 - carisma)}'
    )

    

    