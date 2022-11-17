import re

# uppercase_only_pattern = '[A-Z]*[^a-z]'
case_insensitive_pattern = r'[a-zA-Z0-9]*'
except_new_line_pattern = r'[a-zA-Z0-9]*\S'
digit_non_digit_pair_pattern = r'\d{4}\D{4}'
any_alpha_white_non_white = r'[a-zA-Z]{2}\s[a-zA-Z]{2}\s\S*'
starts_with_three_digit = r'^\d{3}\s*[a-zA-Z0-9]*'
vowel_match = r'[aeiouAEIOU]*'
any_four_digit_num = r'\d{4}'
six_to_ten_digits = r'\d{6,9}'
lowercase_only_pattern = r'[a-z]*[^A-Z]'
zero_or_more_occur_string_pattern = r'[a-zA-Z0-9]*'
ends_with_specific_special_character_pattern = r'[a-zA-Z0-9]*(!$|\?$|\.$)'
negative_string_pattern = r'(not|no)'
three_digit_number = r'\d{3}'

s1 = 'absolute'
s2 = 'I 9L'
s3 = '9999ffff'
s4 = '999ffff'
s5 = '9999fff'
s6 = 'aa bb neknekfeken'
s7 = 'aabb neknekfeken'
s8 = 'aa bbneknekfeken'
s9 = 'aa bb ne knekfeken'
s10 = '123s4ncskcsckj'
s11 = '13ssncskcsckj'
s12 = '1 23ssncskcsckj'
s13 = 'oa'
s14 = 'ioL'
s15 = '9876'
s16 = '98789'
s17 = '987'
s18 = '123456'
s19 = '123456789'
s20 = '12345678910'
s21 = '12345'
s22 = 'ksnksndknk'
s23 = 'ksnkNDKCNDCJKknk'
s24 = 'jghuytyuttiGJFJHF8766969'
s25 = ''
s26 = 'abcDEF567!'
s27 = 'abcDEF567?'
s28 = 'abcDEF567.'
s29 = 'abcDEF567'
s30 = 'not Matched9'
s31 = 'noMatched9'
s32 = 'nMatched0n9ot'
s33 = '123 dnvkdncdkj 112 t4t4 3r45 544 5565'


def is_pattern_matched(pattern_, str_):
    matched = re.fullmatch(pattern_, str_)
    if matched:
        print('\nMatched', matched, end='\n\n')
    else:
        print('\nNot Matched.', matched, end='\n\n')


def is_any_item_matched(pattern_, str_):
    matched = re.match(pattern_, str_)
    if matched:
        print('\nMatched', matched, end='\n\n')
    else:
        print('\nNot Matched.', matched, end='\n\n')


def is_keyword_found(pattern_, str_):
    matched = re.search(pattern_, str_)
    if matched:
        print('\nMatched', matched, end='\n\n')
    else:
        print('\nNot Matched.', matched, end='\n\n')


def get_matched_results(pattern_, sentence):
    result = re.findall(pattern_, sentence)
    if result:
        return result


is_pattern_matched(case_insensitive_pattern, s1)
is_pattern_matched(except_new_line_pattern, s2)
is_pattern_matched(digit_non_digit_pair_pattern, s3)
is_pattern_matched(digit_non_digit_pair_pattern, s4)
is_pattern_matched(digit_non_digit_pair_pattern, s5)
is_pattern_matched(any_alpha_white_non_white, s6)
is_pattern_matched(any_alpha_white_non_white, s7)
is_pattern_matched(any_alpha_white_non_white, s8)
is_pattern_matched(any_alpha_white_non_white, s9)
is_pattern_matched(starts_with_three_digit, s10)
is_pattern_matched(starts_with_three_digit, s11)
is_pattern_matched(starts_with_three_digit, s12)
is_pattern_matched(vowel_match, s13)
is_pattern_matched(vowel_match, s14)
is_pattern_matched(any_four_digit_num, s15)
is_pattern_matched(any_four_digit_num, s16)
is_pattern_matched(any_four_digit_num, s17)
is_pattern_matched(six_to_ten_digits, s18)
is_pattern_matched(six_to_ten_digits, s19)
is_pattern_matched(six_to_ten_digits, s20)
is_pattern_matched(six_to_ten_digits, s21)
is_pattern_matched(lowercase_only_pattern, s22)
is_pattern_matched(lowercase_only_pattern, s23)
is_pattern_matched(zero_or_more_occur_string_pattern, s24)
is_pattern_matched(zero_or_more_occur_string_pattern, s25)
is_pattern_matched(ends_with_specific_special_character_pattern, s26)
is_pattern_matched(ends_with_specific_special_character_pattern, s27)
is_pattern_matched(ends_with_specific_special_character_pattern, s28)
is_pattern_matched(ends_with_specific_special_character_pattern, s29)
is_keyword_found(negative_string_pattern, s30)
is_keyword_found(negative_string_pattern, s31)
is_keyword_found(negative_string_pattern, s32)
print(f'\n12.Extracted values of pattern-->  {three_digit_number}  from--> \n{s33}\n is-->\n,', get_matched_results(three_digit_number, s33))
