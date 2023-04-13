# Student_table



## Endpoints

| Method | Enpoint | Description |
|--------|---------|----------|
| GET | by_students/ | `by_students` |
| POST | add_student/ | `add_student` |
| GET | by_subjects/ | `by_subjects` |
| POST | rating/ | `rating` |
| GET | get_student/ | `get_student` |



## the use of methods

### `add_student`
> Input data
>> {'name':student_name}


### `rating`
> Input data
>> {'name':subject_name, 'students':[{'id':student_id, 'rating':rating}...]}
