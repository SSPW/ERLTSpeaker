Message Format

text surrounded by {n} will be replaced

N		Replacement
---------------------------
1 	position
2	pilot_name
3	pilot_transponder_token
4	pilot_quad
5	pilot_team
6	last_lap_num
7	last_lap_time
8	fastest_lap_num
9	fastest_lap_time
10	avg_lap_time
11	best_time_phrase or nothing

examples
lap {6}, time {7}, {11}
{2}, place {1}, lap {6}, time {7}, {11}