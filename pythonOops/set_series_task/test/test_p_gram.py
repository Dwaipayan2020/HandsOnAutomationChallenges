import pytest

from xtest import check_p_gram


class Test:

    @pytest.mark.parametrize(('length', 'breadth'),
                             ((5, 4), (4, 4), (5, 3), (0, 5), (5, 0), (-1, 8), (-1, -2), (0, 0)), )
    def test_if_square_or_rect(self, length, breadth):
        print(length, breadth, end='\n')
        result = check_p_gram(length, breadth)

        assert result, 'Neither rect or sqr'
        # if result is False:
        #     assert False, 'Neither rectangle or neither square.'
        # else:
        #     assert True
