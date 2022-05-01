import http.client
import json
import csv


connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': '7bb329a7cc2847c5b7441cc8ad6b2451'}
connection.request(
    'GET', '/v2/competitions/PL/matches', None, headers)
response = json.loads(connection.getresponse().read().decode())

# print(response)


# print(type(response))

# my_res1 = {
#     "startDate" : response["matches"][0]["season"]["startDate"],
#     "endDate" : response["matches"][0]["season"]["endDate"],
#     "homeTeam" : response["matches"][0]["homeTeam"]["name"],
#     "awayTeam" : response["matches"][0]["awayTeam"]["name"],
#     "status" : response["matches"][0]["status"],
#     "homeTeamScore" : response["matches"][0]["score"]["fullTime"]["homeTeam"],
#     "awayTeamScore" : response["matches"][0]["score"]["fullTime"]["awayTeam"],
#     "result" : response["matches"][0]["score"]["winner"]
# }


# print(my_res1)

for key, value in response.items():
    print(key)

for key, value in response.items():
    if(key == "matches"):
        print(type(value))
        match_list = value

# print(match_list)

# print(match_list[0])
# print(type(match_list[0]))

# print(len(match_list))


final_list = []
for i in range(len(match_list)):
    dict_for_eachMatch = {
        "startDate": match_list[i]["season"]["startDate"],
        "endDate": match_list[i]["season"]["endDate"],
        "homeTeam": match_list[i]["homeTeam"]["name"],
        "awayTeam": match_list[i]["awayTeam"]["name"],
        "status": match_list[i]["status"],
        "homeTeamScore": match_list[i]["score"]["fullTime"]["homeTeam"],
        "awayTeamScore": match_list[i]["score"]["fullTime"]["awayTeam"],
        "result": match_list[i]["score"]["winner"]

    }
    final_list.append(dict_for_eachMatch)


# print(final_list)

keys = final_list[0].keys()

with open('match_data.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(final_list)
