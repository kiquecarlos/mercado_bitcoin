def calc_list_mms(data, pair):
    def calc_avg(initial_list):
        lst = list(map(lambda x: x['close'], initial_list))
        return round(sum(lst) / len(lst), 2)

    def calc_mms(index, number_mms, data):
        if index >= number_mms-1:
            base_date = data[index-number_mms+1:index+1]
            return calc_avg(base_date)

        return None

    result = []

    for index, d in enumerate(data):
        result.append({
            'pair': pair,
            'timestamp': d['timestamp'],
            'mms_20': calc_mms(index, 20, data),
            'mms_50': calc_mms(index, 50, data),
            'mms_200': calc_mms(index, 200, data)
        })

    return result
