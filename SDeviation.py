import math

def main():
    while True:
        _DATA_LIST = []
        _END_OF_DATA_LIST = False
        _RERUN_PROGRAM = True
        _INDEX_OF_DATA = 0
        while (_END_OF_DATA_LIST != True):
            _TEMP_IN = input("Enter the index " + str(_INDEX_OF_DATA) + " data [0x0=EOL]: ")
            if ("0x0" not in _TEMP_IN and _TEMP_IN != ''):
                _DATA_LIST.append(float(_TEMP_IN))
                _INDEX_OF_DATA += 1
            elif (_TEMP_IN == ''):
                continue
            elif ("0x0" in _TEMP_IN and _TEMP_IN != "0x0"):
                _RERUN_PROGRAM = False
                break
            elif (_TEMP_IN == "0x0"):
                _END_OF_DATA_LIST = True

        def _mean(_LIST):
            _MEAN_UNDIVIDED = 0
            for _INDEX in range(len(_LIST)):
                _MEAN_UNDIVIDED += _LIST[_INDEX]
            _MEAN = _MEAN_UNDIVIDED / len(_LIST)
            return _MEAN
        
        def _standard_deviation(_LIST_S):
            _NUMERATOR = 0.0
            _MEAN_S = _mean(_LIST_S)
            for _INDEX_S in range(len(_LIST_S)):
                _NUMERATOR += (_LIST_S[_INDEX_S] - _MEAN_S) ** 2
            _STANDARD_DEVIATION = math.sqrt(_NUMERATOR/len(_LIST_S))
            return _STANDARD_DEVIATION
        
        if _INDEX_OF_DATA != 0:
            print("Standard Deviation: " + str(round(_standard_deviation(_DATA_LIST), 5)))
            print("Variance of Data: " + str(round(_standard_deviation(_DATA_LIST)**2, 5)))
            
        if _RERUN_PROGRAM == False:
            break
        else:
            _END_OF_DATA_LIST = False

main()
