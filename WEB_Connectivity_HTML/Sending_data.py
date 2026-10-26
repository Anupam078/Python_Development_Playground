import urllib.response
import urllib.parse

query_list={
    "category" : "books",
    "sort" : "price"
}

parsed_query=urllib.parse.urlencode(query_list)

print(parsed_query)