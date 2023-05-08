import statistics
def main():
    while True:
        _DATA_LIST = []
        _END_OF_DATA_LIST = False
        _RERUN_PROGRAM = True
        _INDEX_OF_DATA = 0
        while (_END_OF_DATA_LIST != True):
            _TEMP_IN = input("Enter the index " + str(_INDEX_OF_DATA) + " data [0x=EOL]: ")
            if ("0x" not in _TEMP_IN and _TEMP_IN != ''):
                _DATA_LIST.append(float(_TEMP_IN))
                _INDEX_OF_DATA += 1
            elif (_TEMP_IN == ''):
                continue
            elif ("0x" in _TEMP_IN and _TEMP_IN != "0x"):
                _RERUN_PROGRAM = False
                break
            elif (_TEMP_IN == "0x"):
                _END_OF_DATA_LIST = True
        if _INDEX_OF_DATA != 0:
            print("Variance of Data: " + str(round(statistics.pvariance(_DATA_LIST), 5)))
            print("Standard Deviation: " + str(round(statistics.pstdev(_DATA_LIST), 5)))
            print("Coefficient of Variation: " + str(round((statistics.pstdev(_DATA_LIST)/statistics.mean(_DATA_LIST)), 5)))
        if _RERUN_PROGRAM == False:
            break
        else:
            _END_OF_DATA_LIST = False
main()