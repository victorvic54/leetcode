'''
We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"] 
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history

'''

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]


def findContiguousHistory(first_user, second_user):
    max_len = float('-inf')
    left = 0
    right = 0
    
    if (len(first_user) > len(second_user)):
        first_user, second_user = second_user, first_user
    
    user1_data = set(first_user)
    user2_data = set(second_user)
    
    for i in range(0, len(first_user)):
        if (first_user[i] not in user2_data):
            continue
            
        for j in range(0, len(second_user)):
            tmp_index_1, tmp_index_2 = i, j
            
            while (tmp_index_1 < len(first_user) and tmp_index_2 < len(second_user) and first_user[tmp_index_1] == second_user[tmp_index_2]):
                tmp_index_1 += 1
                tmp_index_2 += 1

            if (tmp_index_1 - i > max_len):
                left = i
                right = tmp_index_1
                max_len = tmp_index_1 - i
    
    return first_user[left:right]
    
    
print(findContiguousHistory(user0, user1))
print(findContiguousHistory(user0, user0))







counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]

def calculateClicksByDomain(counts):
    click_count = {}
    
    for count in counts:
        num, domain = count.split(",")
        domain_parts = domain.split(".")
        
        num = int(num)
        tmp_domain = ""
        
        # iterate from back to front
        for i in range(len(domain_parts) - 1, -1, -1):
            if (not tmp_domain):
                tmp_domain = domain_parts[i]
            else:            
                tmp_domain = domain_parts[i] + "." + tmp_domain
                
            # update the dictionary based on count on a particular domain
            if (tmp_domain not in click_count):
                click_count[tmp_domain] = num
            else:
                click_count[tmp_domain] += num
        
    return click_count

# print(calculateClicksByDomain(counts))