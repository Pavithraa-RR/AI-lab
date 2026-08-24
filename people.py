people = [
    {"name" : "alice", "age":25, "city":"new york"},
    {"name" : "bob", "age" : 30, "city":"los angles"},
    {"name" :"charlie", "age" : 35,"city": "chicago"},
    {"name":"david", "age": 40, "city" : "houston"},
    {"name": "eve", "age": 45, "city": "phoenix"}
    ]
def binary_search_people(people,target_name):
    sortec_people = sorted(people, key=lambda x:x["name"])
    left, right = 0, len(sorted_people)-1
    while left <= right:
        mid = (left+righy)//2
        if sorted_people[mid]["name"] == target_name:
            returnsorted_people[mid]
        elif sorted_people[mid]["name"] < target_name:
            left = mid+1
        else:
            right = mid-1
            return none
            target_name = input("enter the name that you want to search:")
            result = binary_search_people(people, target_name)
            if result:
                print(f"found{target_name} : {result}")
            else:
                print(f"{target_name} not found in the list")
