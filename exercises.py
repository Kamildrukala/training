ad1_ids = {'001', '002', '003'}
ad2_ids = {'002', '003', '007'}

selected_ids = ad1_ids.symmetric_difference(ad2_ids)
print(f'Selected IDs: {selected_ids}')


intersect = ad1_ids.intersection(ad2_ids)
print(intersect)