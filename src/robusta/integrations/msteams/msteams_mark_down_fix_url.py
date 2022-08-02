
import re
class MsTeamsMarkDownFixUrl:

    @staticmethod
    def fix_text(text: str):

        pattern = r'<http.*\|.*>'

        new_text = text
        for bad_url in re.findall(pattern, new_text):
            good_url = MsTeamsMarkDownFixUrl.__fix_url(bad_url)
            new_text = new_text.replace(bad_url, good_url)

        return new_text

    @staticmethod
    def __fix_url(bad_url : str):
        parts = bad_url.replace('<', '').replace('>','').split('|')
        url = f'({parts[0]})'
        description = f'[{parts[1]}]'

        return description + url



