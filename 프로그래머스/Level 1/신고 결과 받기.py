def solution(id_list, report, k):
    answer = []
    reported = dict()
    for id in report:
        report_id, reported_id = id.split()
        if reported_id in reported:
            if report_id not in reported[reported_id]:
            	reported[reported_id].append(report_id)
        else:
            reported[reported_id] = [report_id]
    
    # 2명 이상 되는
    report_dict = dict()
    for rep in reported:
        if len(reported[rep]) >= k:
            for id in reported[rep]:
                if id in report_dict:
                    report_dict[id] += 1
                else:
                    report_dict[id] = 1
                    
    for id in id_list:
        if id in report_dict:
            answer.append(report_dict[id])
        else:
            answer.append(0)
            
    return answer
