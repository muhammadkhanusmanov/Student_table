# Student_table



## Endpoints

| Method | Enpoint | Description |
|--------|---------|----------|
| GET | by_students/ | `by_students` |
| POST | add_student/ | `add_student` |
| GET | by_subjects/ | `by_subjects` |
| POST | rating/ | `rating` |
| GET | get_student/<int:id> | `get_student` |



## the use of methods

#### `add_student`
> Input data
>> {'name':student_name}



#### `rating`
> Input data
>> {'name':subject_name, 'students':[{'id':student_id, 'rating':rating}...]}



#### `get_student`
> Output data
>> Returns the subject rank of the student matching the given `id`


#### `by_students`
> Output data
>> Returns all students with their subject scores


#### `by_subjects`
> Output data
>> Returns all subjects by student ranking
