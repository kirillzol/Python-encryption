from src.CesarStatisticsDecipher import CesarStatisticsDecipher

def test_CesarStatisticsDecipher():
    cipher_obj = CesarStatisticsDecipher()
    with open('tests/Test2.txt', 'r') as file:
        data = file.read()
    assert 27 == cipher_obj.find_opt_step(data, 'rus')


